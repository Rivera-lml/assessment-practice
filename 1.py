import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_palette("Blues")
plt.style.use('default')

df = pd.read_csv('netflix_titles.csv')
print("Primeras 5 filas del dataset:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

df.columns = df.columns.str.lower().str.replace(' ', '_')

df = df.drop_duplicates()

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('Desconocido')


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


df['año_agregado'] = df['date_added'].dt.year


df['duracion_minutos'] = df['duration'].str.extract('(\d+)').astype(float)


plt.figure(figsize=(8,4))
df['año_agregado'].dropna().astype(int).hist(bins=20)
plt.title('Distribución por Año de Agregado a Netflix')
plt.xlabel('Año')
plt.ylabel('Número de Títulos')
plt.grid(True, alpha=0.3)
plt.show()


plt.figure(figsize=(6,4))
sns.boxplot(data=df[df['type'] == 'Movie'], y='duracion_minutos')
plt.title('Duración de Películas (Boxplot)')
plt.ylabel('Minutos')
plt.xticks(rotation=45, ha='right')  
plt.grid(True, alpha=0.3)
plt.show()


plt.figure(figsize=(6,4))
df['type'].value_counts().plot(kind='bar')
plt.title('Distribución por Tipo de Contenido')
plt.ylabel('Cantidad')
plt.grid(True, alpha=0.3)
plt.show()

print("\nINSIGHTS:")
print("• Títulos agregados por año (últimos años han sido más activos).")
print("• La mayoría del contenido es tipo:", df['type'].value_counts().idxmax())
print("• Duración promedio de películas:", round(df[df['type'] == 'Movie']['duracion_minutos'].mean(), 1), "minutos")
