import pandas as pd

data = pd.read_csv("career_readiness_cleaned.csv")

data.to_csv("career_readiness_final.csv",index=False)
print("Cleaned dataset saved successfully!")