import numpy as np

print("\nSMART CAREER READINESS ANALYTICS SYSTEM")
print("="*50)

technical_skills = ["Python", "SQL", "Power BI", "Machine Learning"]
technical_scores = np.array([95, 88, 92, 90])

performance_parameters = ["Projects","Certifications","Communication Skills", "Aptitude"]
performance_scores = np.array([90, 85, 88, 92])

print("\nTECHNICAL SKILLS")
print("-" * 30)
for i in range(len(technical_skills)):
    print(f"{technical_skills[i]} : {technical_scores[i]}")

print("\nPERFORMANCE SCORES")
print("-" * 30)
for i in range(len(performance_parameters)):
    print(f"{performance_parameters[i]} : {performance_scores[i]}")

technical_average = np.mean(technical_scores)
print("\nAverage Technical Score = ",technical_average)
performance_average = np.mean(performance_scores)
print("Average Performance Score =", performance_average)

career_readiness_score = (technical_average + performance_average) / 2
print("\nCareer Readiness Score =", round(career_readiness_score,2))

placement_percentage = career_readiness_score
print("Placement Readiness =", placement_percentage,"%")

highest_skill = np.max(technical_scores)
print("\nHighest Technical Skill Score =", highest_skill)

lowest_skill = np.min(technical_scores)
print("Lowest Technical Skill Score =", lowest_skill)

standard_deviation = np.std(technical_scores)
print("\nStandard Deviation =", round(standard_deviation,2))

if career_readiness_score >= 90:
    level = "Industry Ready"
elif career_readiness_score >= 80:
    level = "Placement Ready"
elif career_readiness_score >= 70:
    level = "Skill Development Required"
else:
    level = "Needs Improvement"

print("\nIndustry Readiness Level =", level)

print("\nRECOMMENDATIONS")
print("- Continue building projects.")
print("- Improve technical skills.")
print("- Participate in internships.")
print("- Strengthen aptitude and communication skills.")
print("- Build an impressive GitHub profile.")