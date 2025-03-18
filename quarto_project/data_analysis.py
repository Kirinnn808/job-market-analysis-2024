import pandas as pd

df = pd.read_csv("lightcast_job_postings.csv")

print(df.head())
print(df.info())

columns_to_drop = [
    "ID", "URL", "ACTIVE_URLS", "DUPLICATES", "LAST_UPDATED_TIMESTAMP",
    "NAICS2", "NAICS3", "NAICS4", "NAICS5", "NAICS6",
    "SOC_2", "SOC_3", "SOC_5"
]

df.drop(columns=columns_to_drop, inplace=True)

print("Updated DataFrame columns:", df.columns.tolist())

# 计算各列缺失值比例
missing_percent = df.isnull().mean() * 100
missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)

import pandas as pd
import matplotlib.pyplot as plt  # 添加此行
import missingno as msno

df = pd.read_csv("lightcast_job_postings.csv")

msno.heatmap(df)
plt.title("Missing Values Heatmap")
plt.show()

df["SALARY"].fillna(df["SALARY"].median(), inplace=True)
df["CITY_NAME"].fillna("Unknown", inplace=True)
df.dropna(thresh=len(df) * 0.5, axis=1, inplace=True)



# Remove duplicates based on key columns
df = df.drop_duplicates(
    subset=["TITLE", "COMPANY", "LOCATION", "POSTED"],
    keep="first"
)

# Verify remaining rows
print(f"Total entries after deduplication: {len(df)}")

import plotly.express as px

mployment_counts = df['EMPLOYMENT_TYPE_NAME'].value_counts()
fig = px.bar(employment_counts, title="Job Postings by Employment Type")
fig.show()

fig = px.box(df, x="CITY_NAME", y="SALARY", title="Salary() Distribution by city")
fig.show()

fig = px.pie(df, names="REMOTE_TYPE_NAME", title="Remote vs. On-Site Jobs")
fig.show()
