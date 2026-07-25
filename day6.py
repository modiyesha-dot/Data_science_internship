import pandas as pd

data = pd.read_csv("career_readiness_cleaned.csv")
print("SMART CAREER READINESS ANALYTICS SYSTEM")
print("="*50)

#Display dataset
print("\nDATASET")
print(data.head())

#Filter students with python score above 90
high_python = data[data["Python"] > 90]
print("\nSTUDENTS WITH PYTHON SCORE ABOVE 90")
print(high_python)

#Filter students with CGPA above 9
top_cgpa = data[data["CGPA"] > 9]
print("\nSTUDENTS WITH CGPA ABOVE 9")
print(top_cgpa)

#Select specific columns
selected_columns = data[["Student_Name","CGPA","Python"]]
print("\nSELECTED COLUMNS")
print(selected_columns)

#Sort by CGPA
sorted_cgpa = data.sort_values(by="CGPA",ascending=False)
print("\nSORTED BY CGPA")
print(sorted_cgpa)

#Sort by python score
sorted_python = data.sort_values(by="Python",ascending=False)
print("\nSORTED BY PYTHON SCORE")
print(sorted_python)

sorted_cgpa.to_csv("career_readiness_sorted.csv",index=False)
print("\nSorted dataset saved successfully.")