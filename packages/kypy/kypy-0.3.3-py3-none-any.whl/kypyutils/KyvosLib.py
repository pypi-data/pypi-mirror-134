"""
Main module of the Kyvos Python Library.

Because pyodbc isn't the most robust way to deal with data sources, try to restrict calls to
pyodbc to just the execute and connect methods - as a DAL (data access layer). This way,
when I can change to a better access method, the code is restricted to just a few methods.
"""
from datetime import datetime
from operator import index
from pandas.core.frame import DataFrame
import pyodbc   #Try to restrict actually calling pyodbc to just executeKyvosSQL and openConnection.
import math
import numpy as np
import pandas as pd
import os
import random
from abc import ABC
from abc import abstractmethod
from enum import Enum,auto
from enum import IntEnum

import concurrent.futures
from multiprocessing import Value,Array,Lock
from collections import namedtuple
from functools import reduce

import json
from json import JSONEncoder
from typing import TypeVar
from typing import Union


from datetime import datetime

class compOp(Enum):
    GT=0
    LT=1
    EQ=2
    LE=3
    GE=4
    NE=5

compOpDesc={compOp.GT:">",compOp.LT:"<",compOp.EQ:"==",compOp.LE:"<=",compOp.GE:">=",compOp.NE:"<>"}

def compOpSymbol(co:compOp):
    return compOpDesc[co]

class sqlFunc(Enum):
    SUM=0
    MAX=1
    MIN=2

class query_language(IntEnum): #This is to help with serializing.
    KyvosSQL=0,
    SparkSQL=1,
    MDX=2,
    DAX=3

def main():
    print("Kyvos Python Library - Q1 2022")

if __name__=="__main__":
    main()
