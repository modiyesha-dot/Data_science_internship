import pandas as pd
data = pd.read_csv("career_readiness.csv")

print("\nSMART CAREER READINESS ANALYTICS SYSTEM")
print("="*50)

print("\nDATASET")
print(data)

print("\nFIRST 5 ROWS")
print(data.head())

print("\nLAST 5 ROWS")
print(data.tail())

print("\nDATASET SHAPE")
print(data.shape)

print("\nCOLUMN NAMES")
print(data.columns)

print("\nDATASET INFORMATION")
data.info()

print("\nDATA TYPES")
print(data.dtypes)
