# importing necessary librarires
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv("d:\\Python\\numpy\\indian employee\\indian_employee_data_60.csv")
print(df.head())

# checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

df["Salary (INR)"].fillna(
    int(np.isfinite(df["Salary (INR)"]).mean(numeric_only=True)), inplace=True
)

df["Performance Rating"].fillna(
    int(np.isfinite(df["Performance Rating"]).median(numeric_only=True)), inplace=True
)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.mean(numeric_only=True), inplace=True)

# remove duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries
df["Salary (INR)"] = np.where(
    df["Salary (INR)"] < 0,
    df["Salary (INR)"].mean(numeric_only=True),
    df["Salary (INR)"],
)

salary_mean = df["Salary (INR)"].mean(numeric_only=True)
salary_std = df["Salary (INR)"].std(numeric_only=True)
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high or too low

df = df[(df["Salary (INR)"] >= lower_bound) & (df["Salary (INR)"] <= upper_bound)]

df.to_csv(
    "d:\\Python\\numpy\\indian employee\\cleaned_indian_employee_Data.csv", index=False
)

print('Data cleaning completed! Saved as "cleaned_indian_employee_Data.csv"')
