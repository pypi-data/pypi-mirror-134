# -*- coding: utf-8 -*-
# Author: Benjamin Vial
# License: MIT


__all__ = ["database", "Material","random"]

"""
Get refractive index from a database
====================================

Retrieve the refractive index of a material at a given wavelength
from the refractiveindex.info_ database.
Inspired from from this repository_: github.com/cinek810/refractiveindex.info.

 .. _refractiveindex.info:
     https://refractiveindex.info/
 .. _repository:
     https://github.com/cinek810/refractiveindex.info
"""


from parse import *
import yaml
from yaml.reader import Reader
import numpy as np
import os
import numpy as np
import functools
import random as rdm

path = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(path, "database", "data")


def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    materials_path = []
    materials_list = []
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        _ = []
        for f in files:
            if f.endswith(".yml") and f != "library.yml":
                _.append(f[:-4])
                frel = os.path.join(os.path.relpath(path, database_path), f)
                # print(frel)
                materials_path.append(frel[:-4])
                materials_list.append(frel[:-4].split("/"))
        files = _
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir["data"], materials_path, materials_list


def fix_yml_file(yamlFile):
    if not yamlFile.endswith(".yml"):
        yamlFile += ".yml"
    return yamlFile

# 
# def strip_invalid(s):
#     res = ""
#     for x in s:
#         if Reader.NON_PRINTABLE.match(x):
#             # res += '\\x{:x}'.format(ord(x))
#             continue
#         res += x
#     return res
# 

def yaml_extract(yamlFile):
    yamlFile = fix_yml_file(yamlFile)
    filename = os.path.join(database_path, yamlFile)
    with open(filename) as yamlStream:
        c = yamlStream.read()
        # allData = yaml.safe_load(strip_invalid(c))
        allData = yaml.safe_load(c)
    materialData = allData["DATA"][0]
    return allData, materialData


def get_tabulated_data(materialData, lamb, datatype):
    assert materialData["type"] == "tabulated {}".format(datatype)

    matLambda = []
    matN = []
    matK = []
    # in this type of material read data line by line
    for line in materialData["data"].split("\n"):
        
        line=line.rstrip()
        line=line.replace(" ."," 0.")

        try:
            if datatype == "n":
                parsed = parse("{l:g} {n:g}", line)
                n = parsed["n"]
                matN.append(n)
                matK.append(0)
            elif datatype == "k":
                parsed = parse("{l:g} {k:g}", line)
                k = parsed["k"]
                matN.append(0)
                matK.append(k)
            else:
                parsed = parse("{l:g} {n:g} {k:g}", line)
                n = parsed["n"]
                k = parsed["k"]
                matN.append(n)
                matK.append(k)
            matLambda.append(parsed["l"])
        except TypeError:
            pass

    matLambda = np.array(matLambda)
    matN = np.array(matN)
    matK = np.array(matK)
    if len(matLambda) == 1:
        return matN + 1j * matK
    else:
        interN = np.interp(lamb, matLambda, matN)
        interK = np.interp(lamb, matLambda, matK)
        return interN + 1j * interK


def get_tabulated_range(materialData, datatype):
    assert materialData["type"] == "tabulated {}".format(datatype)
    # in this type of material read data line by line
    matLambda = []
    for line in materialData["data"].split("\n"):
        line=line.rstrip()
        line=line.replace(" ."," 0.")
        try:
            if datatype == "n":
                parsed = parse("{l:g} {n:g}", line)
            elif datatype == "k":
                parsed = parse("{l:g} {k:g}", line)
            else:
                parsed = parse("{l:g} {n:g} {k:g}", line)
            matLambda.append(parsed["l"])
        except TypeError:
            pass
    
    return (np.min(matLambda), np.max(matLambda))


def formula(lamb, coeff, formula_number):
    if formula_number == 1:
        epsi = 0
        for i in reversed(list(range(1, np.size(coeff), 2))):
            epsi += (coeff[i] * lamb ** 2) / (lamb ** 2 - coeff[i + 1] ** 2)
        epsi += coeff[0] + 1
        n = [np.sqrt(ep) for ep in epsi]
    elif formula_number == 2:
        epsi = 0
        for i in reversed(list(range(1, np.size(coeff), 2))):
            epsi += (coeff[i] * lamb ** 2) / (lamb ** 2 - coeff[i + 1])
        epsi += coeff[0] + 1
        n = [np.sqrt(ep) for ep in epsi]
    elif formula_number == 3:
        epsi = coeff[0]
        for i in range(1, np.size(coeff), 2):
            epsi += coeff[i] * lamb ** coeff[i + 1]
        n = [np.sqrt(ep) for ep in epsi]
    elif formula_number == 4:
        coeff_ = np.zeros(17)
        for i, val in enumerate(coeff):
            coeff_[i] = val
        coeff = coeff_
        epsi = coeff[0]
        epsi += coeff[1] * lamb ** coeff[2] / (lamb ** 2 - coeff[3] ** coeff[4])
        epsi += coeff[5] * lamb ** coeff[6] / (lamb ** 2 - coeff[7] ** coeff[8])
        epsi += coeff[9] * lamb ** coeff[10]
        epsi += coeff[11] * lamb ** coeff[12]
        epsi += coeff[13] * lamb ** coeff[14]
        epsi += coeff[15] * lamb ** coeff[16]
        n = [np.sqrt(ep) for ep in epsi]
    elif formula_number == 5:
        n = coeff[0]
        for i in reversed(list(range(1, np.size(coeff), 2))):
            n += coeff[i] * lamb ** coeff[i + 1]
    elif formula_number == 6:
        n = coeff[0] + 1
        for i in reversed(list(range(1, np.size(coeff), 2))):
            n += coeff[i] / (coeff[i + 1] - lamb ** (-2))
    elif formula_number == 7:
        n = coeff[0]
        n += coeff[1] / (lamb ** 2 - 0.028)
        n += coeff[2] / (lamb ** 2 - 0.028) ** 2
        for i in range(3, np.size(coeff)):
            n += coeff[i] * lamb ** (2 * (i - 2))
    elif formula_number == 8:
        A = coeff[0]
        A += coeff[1] * lamb ** 2 / (lamb ** 2 - coeff[2])
        A += coeff[3] * lamb ** 2
        n = ((1 + 2 * A) / (1 - A)) ** 0.5
    elif formula_number == 9:
        epsi = coeff[0]
        epsi += coeff[1] / (lamb ** 2 - coeff[2])
        epsi += coeff[3] * (lamb - coeff[4]) / ((lamb - coeff[4]) ** 2 * +coeff[5])
        n = epsi ** 0.5
    return n


def get_formula_data(materialData, lamb, formula_number):
    assert materialData["type"] == "formula {}".format(formula_number)
    
    try:
        dataRange = np.array(list(map(float, materialData["range"].split())))
    except:
        dataRange = -np.inf,np.inf
    coeff = np.array(list(map(float, materialData["coefficients"].split())))
    return formula(lamb, coeff, formula_number)



def check_bounds(lamb, dataRange):
    if dataRange is None:
        return True
    else:
        return np.min(lamb) >= dataRange[0] and np.max(lamb) <= dataRange[1]




# this is general function to check data type, and run appropriate actions


def get_data(materialData, lamb):
    mtype = materialData["type"]
    if mtype.split()[0] == "tabulated":
        return get_tabulated_data(materialData, lamb, mtype.split()[1])
    elif mtype.split()[0] == "formula":
        return get_formula_data(materialData, lamb, int(mtype.split()[1]))
    else:
        return np.zeros_like(lamb)


def get_wl_range(materialData):

    mtype = materialData["type"]

    if mtype.split()[0] == "tabulated":
        return get_tabulated_range(materialData, mtype.split()[1])
    else:
        try:
            dataRange = np.array(list(map(float, materialData["range"].split())))
        except:
            dataRange = None
        return dataRange


def get_complex_index(lambdas, materialData):
    lambdas = np.array([lambdas],dtype=float).ravel()
    ncomplex = get_data(materialData, lambdas)
    return np.asarray(np.conj(ncomplex))


class Material:
    """Material class"""

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Material " + ("/").join(self.id)

    @property
    def _alldata(self):
        return yaml_extract(self._path)

    
    @property
    def _data(self):
        return self._alldata[0]
        
        
    @property
    def _material_data(self):
        return self._alldata[1]
        
    @property
    def _path(self):
        return os.path.join(*self.id)

    @property
    def _references(self):
        return self._data["REFERENCES"]

    @property
    def _comments(self):
        try:
            comments = self._data["COMMENTS"]
        except:
            comments = None
        return comments

    @property
    def info(self):
        return dict(comments=self._comments, references=self._references)

    

    @property
    def wavelength_range(self):
        return get_wl_range(self._material_data)


    def get_index(self, lambdas):
        wrange = self.wavelength_range
        if not check_bounds(lambdas, wrange):
            raise ValueError(
                f"No data for this material {self.id}. Wavelength must be between {wrange[0]} and {wrange[1]} microns.",
            )
        return get_complex_index(lambdas, self._material_data)


database, _, _ = get_directory_structure(database_path)

for a in list(database):
    for b in list(database[a]):
        for c in list(database[a][b]):
            
            if database[a][b][c] == None:
                id = [a, b, c]
                database[a][b][c] = Material(id)
                    
            else:

                for d in list(database[a][b][c]):
                    id = [a, b, c,d]
                    database[a][b][c][d] = Material(id)

def random():
    mat = database
    while isinstance(mat, dict):
        mat = rdm.choice(list(mat.values()))
    return mat
