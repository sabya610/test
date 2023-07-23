import pandas as pd

data = {
    'Name': ['John', 'Emma', 'Sam', 'Olivia', 'Daniel'],
    'Age': [25, 28, 30, 22, 27],
    'City': ['New York', 'London', 'Paris', 'Sydney', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}
df = pd.DataFrame(data)
sel_col=df[['Name','Age']]
print(df.info())
print(df[df['Age'] > 25])
print(df.sort_values('Salary'))
print(df['Salary'].mean())
print(df['Age'].max())
