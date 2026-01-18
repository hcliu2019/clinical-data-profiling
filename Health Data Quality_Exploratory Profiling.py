# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 16:40:34 2026
Machine Learning in Health
Project 4-Part1- Predicting Alzheimer’s Disease Progression Using Clinical and Biomarker Data

Topic-1: Health Data Quality & Exploratory Profiling 
This work conducted basic data analytics (and with advanced/novel methods) on Alzheimer’s Disease dataset. 

It adapt common machine learning techniques to classify patients with Alzheimer’s disease, predict risk factors for the disease,
and find some insights from the datasets, e.g., what correlations between biomarkers and clinical data could be used for speed up diagnosis?
Data source: from ChatGPT - Alzheimers_Synthetic.csv, 200×15, with CSF and imaging biomarkers

@author: Hong-Cheu Liu
"""
import time
start = time.time()
# Time execution of a Python statement or expression in the cell

import numpy as np
import pandas as pd



# Replace with your dataset path
df = pd.read_csv("Alzheimers_Synthetic.csv")

# Quick check
print(df.head())
print(df.info())
print(df.describe())

from ydata_profiling import ProfileReport

profile = ProfileReport(
    df,
    title="Baseline Data Quality Report – Clinical Dataset",
    explorative=True,
    minimal=False  # Set True for very large datasets
)

# Save to HTML
profile.to_file("clinical_data_profile.html")


import numpy as np

df.loc[df.sample(frac=0.05).index, "CognitiveScore"] = np.nan
