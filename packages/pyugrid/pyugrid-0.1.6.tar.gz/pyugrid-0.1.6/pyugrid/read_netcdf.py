#!/usr/bin/env python

"""
code to read the netcdf unstructured grid standard:

https://github.com/ugrid-conventions/ugrid-conventions/

This code is called by the UGrid class to load inot a UGRID object.

"""

from __future__ import (absolute_import, division, print_function)

import numpy as np
import netCDF4

from .data_set import DataSet

def find_mesh_names( nc ):
    """
    find all the meshes in an open netcCDF4.DataSet
    
    :param nc: the netCDF4 Dataset object to look for mesh names in

    NOTE: checks for 2-d topology_dimension
    """
    mesh_names = []
    for varname in nc.variables.keys():
        if is_valid_mesh(nc, varname):
                    mesh_names.append(varname)
    return mesh_names            

def is_valid_mesh(nc, varname):
    """
    determine if the given variable name is a valid mesh definition
    
    :param nc: a netCDF4 Dataset to check

    :param varname: name of the candidate mesh variable
    
    """
    try:
        mesh_var = nc.variables[varname]
    except KeyError:
        return False
    try:
        if  ( mesh_var.cf_role.strip() == 'mesh_topology'  and
              int( mesh_var.topology_dimension ) == 2
              ):
            return True
    except AttributeError:
            # not a valid mesh variable
        return False

## defining properties of various connectivity arrays
##   so that the same code can load all of them.
grid_defs = [{'grid_attr':'faces', # attribute name in UGrid object
              'role': 'face_node_connectivity', # attribute name in mesh variable
              'num_ind': 3, # number of indexes expect (3 for faces, 2 for segments)
              },
             {'grid_attr':'face_face_connectivity', # attribute name in UGrid object
              'role': 'face_face_connectivity', # attribute name in mesh variable
              'num_ind': 3, # number of indexes expect (3 for faces, 2 for segments)
              },
             {'grid_attr':'boundaries', # attribute name in UGrid object
              'role': 'boundary_node_connectivity', # attribute name in mesh variable
              'num_ind': 2, # number of indexes expect (3 for faces, 2 for segments)
              },
             {'grid_attr':'edges', # attribute name in UGrid object
              'role': 'edge_node_connectivity', # attribute name in mesh variable
              'num_ind': 2, # number of indexes expect (3 for faces, 2 for segments)
              },

             ]
# defintions for various coordinate arrays
coord_defs = [ {'grid_attr':'nodes', # attribute name in UGrid object
                'role': 'node_coordinates', # attribute name in mesh variable
                'required': True, # is this required?
               },
               {'grid_attr':'face_coordinates', # attribute name in UGrid object
                'role': 'face_coordinates', # attribute name in mesh variable
                'required': False, # is this required?
               },
               {'grid_attr':'edge_coordinates', # attribute name in UGrid object
                'role': 'edge_coordinates', # attribute name in mesh variable
                'required': False, # is this required?
               },
               {'grid_attr':'boundary_coordinates', # attribute name in UGrid object
                'role': 'boundary_coordinates', # attribute name in mesh variable
                'required': False, # is this required?
               }
             ]

def load_grid_from_nc_dataset(nc, grid, mesh_name=None, load_data=True):
    """
    loads UGrid object from a netCDF4.DataSet object, adding the data
    to the passed-in grid object.

    It will load the mesh specified, or look
    for the first one it finds if none is specified

    :param filename: filename or OpenDAP url of dataset.
    
    :param grid: ther gird object to put the mesh and data into.
    :type grid: UGrid object.

    :param mesh_name=None: name of the mesh to load
    :type mesh_name: string

    :param load_data=False: flag to indicate whether you want to load the associated
                            data or not. The mesh will be loaded in any case. If False,
                            only the mesh will be loaded. If True, then all the data
                            associated with the mesh will be loaded. This could be huge!
    :type load_data: boolean

    NOTE: passing the UGrid object in to avoid circular references,
    while keeping the netcdf reading code in its own file.
    """
    ncvars = nc.variables

    ## get the mesh_name
    if mesh_name is None:
        # find the mesh
        meshes = find_mesh_names( nc )
        if len(meshes) == 0:
            raise ValueError("There are no standard-conforming meshes in %s"%nc.filepath)
        if len(meshes) > 1:
            raise ValueError("There is more than one mesh in the file: %s"%(meshes,) )
        mesh_name = meshes[0]
    else:
        if not is_valid_mesh(nc, mesh_name):
            raise ValueError("Mesh: %s is not in %s"%(mesh_name, nc.filepath))
    
    grid.mesh_name = mesh_name

    mesh_var = ncvars[mesh_name]


    ## Load the coordinate variables
    for defs in coord_defs:
        try:
            coord_names = mesh_var.getncattr(defs['role']).strip().split()
            coord_vars = [nc.variables[name] for name in coord_names]
        except AttributeError:
            if defs['required']:
                raise ValueError("Mesh variable must include %s attribute"%defs['role'])
            continue
        except KeyError:
            raise ValueError("file must include %s variables for %s named in mesh variable"%(coord_names, defs['role']))

        coord_vars = [nc.variables[name] for name in coord_names]
        num_node = len(coord_vars[0])
        nodes = np.empty((num_node, 2), dtype=np.float64)
        for var in coord_vars:
            try:
                standard_name = var.standard_name
            except AttributeError:
                # CF does not require a standard name, so look in units, instead
                try:
                    units = var.units
                except AttributeError:
                    raise ValueError("%s variable doesn't contain units attribute: required by CF"%var)
                if units in ('degrees_east', 'degree_east', 'degree_E', 'degrees_E', 'degreeE', 'degreesE'): # CF accepted units attributes for longitude
                        standard_name = 'longitude'
                elif units in ('degrees_north', 'degree_north', 'degree_N', 'degrees_N', 'degreeN', 'degreesN'): # CF accepted units attributes for longitude
                        standard_name = 'latitude'
                else:
                    raise ValueError("%s variable's units value (%s) doesn't look like latitude or longitude"%(var, units))
            if standard_name == 'latitude':
                nodes[:,1] = var[:]
            elif standard_name == 'longitude':
                nodes[:,0] = var[:]
            else:
                raise ValueError('Node coordinates standard_name is neither "longitude" nor "latitude" ') 
        
        setattr(grid, defs['grid_attr'], nodes)


    ## Load assorted connectivity arrays
    for defs in grid_defs:
        try:
            try:
                var = nc.variables[mesh_var.getncattr(defs['role'])]
            except AttributeError: # this connectivity array isn't there
                continue
            array = var[:,:]
            # fortran order, instead of C order, transpose the array
            # logic below will fail for 3 node or two edge grids
            if array.shape[0] == defs['num_ind']:
                array = array.T
            try:
                start_index = var.start_index
            except AttributeError:
                start_index = 0
            if start_index  >= 1:
                array -= start_index
                # check for flag value
                try:
                    ## fixme: this won't work for more than one flag value
                    flag_value = var.flag_values
                    array[array==flag_value-start_index] = flag_value
                except AttributeError:
                    pass
            setattr(grid, defs['grid_attr'], array)
        except KeyError:
            pass ## OK not to have this...

    ## Load the associated data:

    if load_data:
        ## look for data arrays -- they should have a "location" attribute
        for name, var in nc.variables.items():

            #Data Arrays should have "location" and "mesh" attributes
            try:
                location = var.location
                # the mesh attribute should match the mesh we're loading:
                if var.mesh != mesh_name:
                    continue
            except AttributeError:
                continue

            #get the attributes
            ## fixme: is there a way to get the attributes a dict directly?
            attributes = { n: var.getncattr(n) for n in var.ncattrs() if n not in ('location', 'coordinates', 'mesh')}

            # trick with the name: fixme: is this a good idea?
            name = name.lstrip(mesh_name).lstrip('_')
            ds = DataSet(name, data=var[:], location=location, attributes=attributes)

            grid.add_data(ds)

def load_grid_from_ncfilename(filename, grid, mesh_name=None, load_data=True):
    """
    loads UGrid object from a netcdf file, adding the data
    to the passed-in grid object.

    It will load the mesh specified, or look
    for the first one it finds if none is specified

    :param filename: filename or OpenDAP url of dataset.
    
    :param grid: ther gird object to put the mesh and data into.
    :type grid: UGrid object.

    :param mesh_name=None: name of the mesh to load
    :type mesh_name: string

    :param load_data=False: flag to indicate whether you want to load the associated
                            data or not. The mesh will be loaded in any case. If False,
                            only the mesh will be loaded. If True, then all the data
                            associated with the mesh will be loaded. This could be huge!
    :type load_data: boolean

    NOTE: passing the UGrid object in to avoid circular references,
    while keeping the netcdf reading code in its own file.
    """

    with netCDF4.Dataset(filename, 'r') as nc:
        load_grid_from_nc_dataset(nc, grid, mesh_name, load_data)

