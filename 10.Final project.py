import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Titanic-Dataset.csv")


print(df.head())
print(df.info())
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


print("\nSurvival Count:")
print(df["Survived"].value_counts())

print("\nSurvival Rate:")
print(df["Survived"].mean() * 100)

print("\nSurvival by Gender:")
print(df.groupby("Sex")["Survived"].mean() * 100)

print("\nSurvival by Class:")
print(df.groupby("Pclass")["Survived"].mean() * 100)

sns.set_theme(style="whitegrid")


sns.countplot(data=df, x="Survived")
plt.title("Titanic Survival")
plt.show()


sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.show()


sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Class")
plt.show()


sns.histplot(data=df, x="Age", kde=True)
plt.title("Age Distribution")
plt.show()


sns.heatmap(df.select_dtypes("number").corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()