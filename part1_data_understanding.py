# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 09:44:57 2026

@author: Hong-Cheu Liu
"""

# ===============================
# Project 4 – Part 1
# Data Understanding
# ===============================

import os
import pandas as pd

# --- 1. Show where the script is running from ---
print("Script location:", os.path.dirname(__file__))

# --- 2. Move working directory to PROJECT ROOT ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(PROJECT_ROOT)

print("Current working directory:", os.getcwd())

# --- 3. Load dataset ---
data_path = os.path.join("data", "Alzheimers_Synthetic.csv")
print("Loading data from:", data_path)

df = pd.read_csv(data_path)

# --- 4. Inspect data ---
print("\nFirst 5 rows:")
print(df.head())

print("\nDataFrame info:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

# --- 5. Data types ---
print("\nColumn data types:")
print(df.dtypes)

# --- 6. Missing values ---
print("\nMissing values per column:")
print(df.isnull)



