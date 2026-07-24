import pandas as pd

data = pd.read_csv("career_readiness.csv")
print("SMART CAREER READINESS ANALYTICS SYSTEM")
print("="*50)

#check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

#handle missing values
data=data.fillna(data.mean(numeric_only=True))

#check again
print("\nMISSING VALUES AFTER CLEANING")
print(data.isnull().sum())

#check duplicate records
print("\nDUPLICATE RECORDS")
print(data.duplicated().sum())

#remove duplicate records
data = data.drop_duplicates()

#check again
print("\nDUPLICATES AFTER REMOVAL")
print(data.duplicated().sum())

#check data types
print("\nDATA TYPES BEFORE CORRECTION")
print(data.dtypes)

#correct data types
data["CGPA"] = data["CGPA"].astype(float)
data["Projects"] = data["Projects"].astype(int)
data["Certifications"] = data["Certifications"].astype(int)
data["Internships"] = data["Internships"].astype(int)

#verfiy data types
print("\nDATA TYPES AFTER CORRECTION")
print(data.dtypes)

data.to_csv("career_readiness_cleaned.csv",index=False)
print("\nCleaned dataset saved successfully.")