import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Marks": [30, 40, 50, 60, 70, 80, 90],
    "StudyHours": [5, 6, 7, 8, 9, 10, 11]
}

df = pd.DataFrame(data)

X = df[["Marks"]]
y = df["StudyHours"]

model = LinearRegression()
model.fit(X, y)

# User input
marks = int(input("Enter your previous exam marks: "))

predicted_hours = model.predict([[marks]])

print(f"Suggested study hours per day: {round(predicted_hours[0], 1)} hours")
