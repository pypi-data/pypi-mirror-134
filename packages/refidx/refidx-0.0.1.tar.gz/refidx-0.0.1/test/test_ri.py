#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT

import pytest
import refidx as ri
import numpy as np


def _test_material(mat):
    wr = mat.wavelength_range
    if wr is not None:
        lamb = (wr[1] + wr[0]) / 2
    else:
        lamb = 1.0
    index = mat.get_index(lamb)
    print(mat)
    # print(mat._data)
    print(mat.info)
    print("wavelength range: ", wr)
    print("wavelength", lamb)
    print("refractive index: ", index)

    if wr is not None:

        with pytest.raises(ValueError):
            lamb = mat.wavelength_range[0] / 2
            index = mat.get_index(lamb)

        with pytest.raises(ValueError):
            lamb = mat.wavelength_range[1] * 2
            index = mat.get_index(lamb)


def test_material_main():
    a = "main"
    for b in list(ri.database[a]):
        for c in list(ri.database[a][b]):
            mat = ri.database[a][b][c]
            print("######################################################")
            _test_material(mat)


def test_material_glass():
    a = "glass"
    for b in list(ri.database[a]):
        for c in list(ri.database[a][b]):

            if isinstance(ri.database[a][b][c], dict):
                for d in list(ri.database[a][b][c]):
                    mat = ri.database[a][b][c][d]
                    print("######################################################")
                    _test_material(mat)
            else:
                mat = ri.database[a][b][c]
                print("######################################################")
                _test_material(mat)


def test_material_organic():
    a = "organic"
    for b in list(ri.database[a]):
        for c in list(ri.database[a][b]):
            # b,c="C3H9O3P - dimethyl methylphosphonate","Querry-NIR"
            mat = ri.database[a][b][c]
            print("######################################################")
            _test_material(mat)


def test_material_other():
    a = "other"
    for b in list(ri.database[a]):
        for c in list(ri.database[a][b]):

            if isinstance(ri.database[a][b][c], dict):
                for d in list(ri.database[a][b][c]):
                    mat = ri.database[a][b][c][d]
                    print("######################################################")
                    _test_material(mat)
            else:
                mat = ri.database[a][b][c]
                print("######################################################")
                _test_material(mat)
