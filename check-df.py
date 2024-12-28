import pandas as pd

users_df = pd.read_csv("users.csv")
content_df = pd.read_csv("content.csv")
engagement_df = pd.read_csv("engagement.csv")

print(users_df.head())
print(content_df.head())
print(engagement_df.head())
