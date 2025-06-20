import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Estilo azul para las gráficas
sns.set_palette("Blues")
plt.style.use('default')

# Cargar el dataset
df = pd.read_csv('cards_data.csv')
print("Primeras 5 filas del dataset:")
print(df.head())

# Información básica del dataset
print("\nInformación general:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

# Limpieza básica

# Renombrar columnas (minúsculas y sin espacios)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Eliminar duplicados
df = df.drop_duplicates()

# Llenar nulos en columnas de texto con 'Desconocido'
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna('Desconocido')


# Convertir 'date_added' a tipo fecha
df['expires'] = pd.to_datetime(df['expires'], errors='coerce')

# Extraer año de la fecha agregada
df['year_expires'] = df['expires'].dt.year

df['year_expires']

# Convertir 'date_added' a tipo fecha
df['acct_open_date'] = pd.to_datetime(df['acct_open_date'], errors='coerce')

# Extraer año de la fecha agregada
df['open_year'] = df['acct_open_date'].dt.year

df['open_year']

# Quedarse solo con las 10 categorías más comunes
top_10 = df['open_year'].value_counts().head(10).index
df_top = df[df['open_year'].isin(top_10)]


conteo = df_top['open_year'].value_counts()

conteo.plot(kind='bar', figsize=(8, 4))
plt.title('Cantidad de Tarjetas Abiertas por Año')
plt.xlabel('Año de apertura')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


suma = df.groupby('open_year')['id'].count()

suma.plot(kind='bar', figsize=(8, 4))
plt.title('Suma de Tarjetas Abiertas por Año')
plt.xlabel('Año')
plt.ylabel('Suma de Tarjetas Abiertas')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


tendencia = df.groupby('open_year')['id'].count()

tendencia.plot(kind='line', marker='o', figsize=(8, 4))
plt.title('Tendencia por Año')
plt.xlabel('Año')
plt.ylabel('Promedio/Suma')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


