# -*- coding: utf-8 -*-

import statsmodels.api as sm
!pip install statsmodels openpyxl

import pandas as pd

file_path = "/content/GPT4 - France - EGA - English reg dataset-everything.xlsx"  #Change as needed
xls = pd.ExcelFile(file_path)
df = xls.parse('Score')  # Load the sheet named 'recoded'
df.head()  # Display first few rows

# Define dependent and independent variables
y = df["Score"]
X = df.drop(columns=["Score"])

# Add constant for intercept
X = sm.add_constant(X)

# Run the regression
model = sm.OLS(y, X).fit()

# Display the summary
print(model.summary())
