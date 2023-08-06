#!/usr/bin/env python

"""
Some example UGRIDs to test, etc with

"""

from __future__ import (absolute_import, division, print_function)

from pyugrid import ugrid


def two_triangles():
    """
    returns about the simplest triangle grid possible

    4 nodes, two triangles, five edges
    """
    nodes = [(0.1, 0.1),
             (2.1, 0.1),
             (1.1, 2.1),
             (3.1, 2.1)]

    faces = [(0, 1, 2),
             (1, 3, 2), ]

    edges = [(0, 1),
             (1, 3),
             (3, 2),
             (2, 0),
             (1, 2)]

    return ugrid.UGrid(nodes, faces, edges)


def twenty_one_triangles():
    """
    returns a basic triangle grid with 21 triangles, a hole and a "tail"
    """
    nodes = [(5, 1),
             (10, 1),
             (3, 3),
             (7, 3),
             (9, 4),
             (12, 4),
             (5, 5),
             (3, 7),
             (5, 7),
             (7, 7),
             (9, 7),
             (11, 7),
             (5, 9),
             (8, 9),
             (11, 9),
             (9, 11),
             (11, 11),
             (7, 13),
             (9, 13),
             (7, 15), ]

    faces = [(0, 1, 3),
             (0, 6, 2),
             (0, 3, 6),
             (1, 4, 3),
             (1, 5, 4),
             (2, 6, 7),
             (6, 8, 7),
             (7, 8, 12),
             (6, 9, 8),
             (8, 9, 12),
             (9, 13, 12),
             (4, 5, 11),
             (4, 11, 10),
             (9, 10, 13),
             (10, 11, 14),
             (10, 14, 13),
             (13, 14, 15),
             (14, 16, 15),
             (15, 16, 18),
             (15, 18, 17),
             (17, 18, 19), ]

    # We may want to use this later to define just the outer boundary.
    boundaries = [(0, 1),
                  (1, 5),
                  (5, 11),
                  (11, 14),
                  (14, 16),
                  (16, 18),
                  (18, 19),
                  (19, 17),
                  (17, 15),
                  (15, 13),
                  (13, 12),
                  (12, 7),
                  (7, 2),
                  (2, 0),
                  (3, 4),
                  (4, 10),
                  (10, 9),
                  (9, 6),
                  (6, 3), ]

    grid = ugrid.UGrid(nodes, faces, boundaries=boundaries)
    grid.build_edges()
    return grid

if __name__ == "__main__":
    grid = twenty_one_triangles()
    print(grid.edges)
    print(len(grid.edges))
    grid.build_edges()
    print(grid.edges)
    print(len(grid.edges))
