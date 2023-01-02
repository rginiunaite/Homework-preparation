import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import random

from sklearn.model_selection import KFold, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Function: Copy-pasted from question and modified
def get_num_people_by_age_category(df):
    df["age_group"] = pd.cut(x=df['age'], bins=[0,30,60,100], labels=["young","middle_aged","old"])
    return df


