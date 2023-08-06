"""
for rolling updates:
    - python setup.py bdist_wheel sdist
    - twine upload dist/*

"""
from welcome_page import *
from variables import *
import pandas as pd 
import numpy as np
import re


def get_column_types(df,col_name,get_type):
    if get_type == "cat":
        allowed_words = re.compile(categorical_words) 
        if bool(forbiddenwords.search(col_name)):
            return col_name
        if df[col_name].nunique() < ( int(df.shape[0] * 0.15) ):
            return col_name


def get_similarity(df,cat_cols = None,numeric_cols = None,other_cols = None):
    cols = list(df.columns)
    if cat_cols == None:
        cat_cols = [get_column_types(df,_,"cat") for _ in df.columns]
        cat_cols = [_ for _ in cat_cols if _ != None]
    if numeric_cols == None:
        num_cols = [get_column_types(df,_,"num") for _ in df.columns]
    