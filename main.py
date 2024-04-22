import pandas as pd

# Aufgabe 1
df = pd.read_csv('adult 2.csv')

# Aufgabe 2.1
# Zeige die ersten 5 Zeilen des DataFrames an
print("Die ersten 5 Zeilen des DataFrames:")
print(df.head())

# Zeige die letzten 5 Zeilen des DataFrames an
print("\nDie letzten 5 Zeilen des DataFrames:")
print(df.tail())

# Zusammenfassung des DataFrames
print("\nZusammenfassung des DataFrames:")
print(df.info())

# Aufgabe 2.2

# Spalten auswählen
selected_columns = ['age', 'occupation', 'income']
selected_data = df[selected_columns].head(10)
print("\nAusgewählte Spalten und die ersten 10 Zeilen:")
print(selected_data)

# Bedingte Auswahl (Filtern nach 'income' >50K)
high_income_data = df[df['income'] == '>50K']
print("\nZeilen, bei denen das Einkommen '>50K' ist:")
print(high_income_data.head())

# Mehrere Bedingungen (age > 30 und education 'Bachelors')
filtered_data = df[(df['age'] > 30) & (df['education'] == 'Bachelors')]
print("\nZeilen, bei denen das Alter größer als 30 ist und die Bildung 'Bachelors' ist:")
print(filtered_data.head())

# Aufgabe 3

# Neue Spalte hinzufügen (Alter in Jahrzehnten)
df['age_decade'] = df['age'] / 10

# Werte ändern (income-Spalte)
df['income'] = df['income'].replace({'>50K': 'high', '<=50K': 'low'})

# Zeilen löschen (occupation 'Unknown')
df = df[df['occupation'] != 'Unknown']

# Ergebnisse anzeigen
print("\nDataFrame mit neuer Spalte 'age_decade' und geänderten 'income'-Werten:")
print(df.head())

# Aufgabe 4

# Deskriptive Statistiken für die 'age'-Spalte
age_statistics = df['age'].describe()[['min', 'max']]
print("\nDeskriptive Statistiken für die 'age'-Spalte:")
print(age_statistics)

# Gruppieren und Aggregieren (Durchschnitt von 'age' nach 'income')
average_age_by_income = df.groupby('income')['age'].mean()
print("\nDurchschnittliches Alter nach Einkommen:")
print(average_age_by_income)

# Einzigartige Werte in der 'education'-Spalte
unique_education_values = df['education'].unique()
print("\nEinzigartige Werte in der 'education'-Spalte:")
print(unique_education_values)
