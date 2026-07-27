import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("career_readiness_cleaned.csv")
print("DATASET LOADED SUCCESSFULLY")

avg_scores = {"Python": data["Python"].mean(),
              "SQL": data["SQL"].mean(),
              "PowerBI": data["PowerBI"].mean(),
              "Communication": data["Communication"].mean(),
              "Aptitude": data["Aptitude"].mean()}
plt.figure(figsize=(8,5))
plt.bar(avg_scores.keys(),avg_scores.values())
plt.title("Average Skill Scores")
plt.xlabel("Skills")
plt.ylabel("Average Score")
plt.show()

sorted_data = data.sort_values("CGPA")
plt.figure(figsize=(8,5))
plt.plot(sorted_data.index,sorted_data["CGPA"],marker="o")
plt.title("CGPA Trend")
plt.xlabel("Students")
plt.ylabel("CGPA")
plt.show()

top_skills = {"Python": data["Python"].sum(),
              "SQL": data["SQL"].sum(),
              "PowerBI": data["PowerBI"].sum()}
plt.figure(figsize=(7,7))
plt.pie(top_skills.values(),labels=top_skills.keys(),autopct="%1.1f%%")
plt.title("Skill Contribution")
plt.show()