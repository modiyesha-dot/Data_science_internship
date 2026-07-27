import pandas as pd

data = pd.read_csv("career_readiness_cleaned.csv")
print("SMART CAREER READINESS ANALYTICS SYSTEM")
print("="*50)

print("\nTOTAL VALUES")

print("Total Python Score:",data["Python"].sum())
print("Total SQL Score:",data["SQL"].sum())
print("Total PowerBI Score:",data["PowerBI"].sum())

print("\nAVERAGE VALUES")

print("Average CGPA:",round(data["CGPA"].mean(),2))
print("Average Python Score:",round(data["Python"],2))
print("Average SQL Score:",round(data["SQL"],2))

print("\nMINIMUM VALUES")

print("Minimum CGPA:",data["CGPA"].min())
print("Minimum Python Score:",data["Python"].min())
print("Minimum SQL Score:",data["SQL"].min())

print("\nMAXIMUM VALUES")

print("Maximum CGPA:",data["CGPA"].max())
print("Maximum Python Score:",data["Python"].max())
print("Maximum SQL Score:",data["SQL"].max())

print("\nCOUNT VALUES")

print("Total Students:",data["Student_Name"].count())
print("CGPA Records",data["CGPA"].count())
print("Python Records",data["Python"].count())