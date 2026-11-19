import pandas as pd
import matplotlib.pyplot as plt

## Nahum Flores NC 0065
# 1. Crear diccionario con datos de cursos online
cursos_online = {
    'id_curso': [201, 202, 203, 204, 205, 206],
    'titulo': ['Intro a Python', 'Marketing Digital', 'Diseño UX/UI', 'Finanzas Personales', 'Ingles Intermedio', 'Excel Avanzado'],
    'instructor': ['Carlos', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofia'],
    'duracion_horas': [40, 30, 50, 20, 60, 35],
    'precio': [1500, 1200, 2000, 800, 2500, 1000],
    'estudiantes_inscritos': [150, 200, 80, 300, 120, 180],
    'calificacion_promedio': [4.8, 4.5, 4.9, 4.2, 4.7, 4.6],
    'nivel': ['Principiante', 'Intermedio', 'Intermedio', 'Principiante', 'Intermedio', 'Avanzado'],
    'fecha_inicio': ['2024-02-01', '2024-02-15', '2024-03-01', '2024-02-05', '2024-03-15', '2024-02-20'],
    'plataforma': ['Udemy', 'Coursera', 'Domestika', 'Udemy', 'Coursera', 'LinkedIn']
}

print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis por Nahum Flores NC 0065")
print("Crear el diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(cursos_online)
print("\n--- TABLA ORIGINAL DE CURSOS ONLINE ---")
print(df)
# 3. Exportar los datos a CSV
print("-+-+-+-+-+-Convertir el DataFrame en archivo CSV +-+-+-+-+-")
df.to_csv(
    'cursos_online_0065.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n Archivo CSV creado correctamente")
print("8.-+-+-+-+- leer los datos desde el archivo csv -+-+-+-+-+-")
print('cursos_online_0065.csv')

# 4. Leer el archivo CSV
df = pd.read_csv('cursos_online_0065.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+-+-+-+ 9. Análisis Exploratorio de Datos (EDA)-+-+-+-+-+")

# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head):")
print(df.head(3))  # Muestra los primeros 3
print("\n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+-+-+-+ 6. Dimensiones y estructura-+-+-+-+-+")
print(df)  # mostrar tablas matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

# 7. Estadísticas y limpieza
print("-+-+-+-+-+-  Estadísticas y limpieza -+-+-+--+-+")
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Plataformas únicas:", df['plataforma'].unique())

# 8. Análisis específico
print(df)
print("---------------------------------------------------------------")
print("\n11. CURSOS POR PLATAFORMA:")
print(df['plataforma'].value_counts())

print("\n12. PROMEDIO DE PRECIO: $", df['precio'].mean())
print("13. PRECIO MÁXIMO: $", df['precio'].max())
print("14. PRECIO MÍNIMO: $", df['precio'].min())

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")
print("\n15. CURSOS ORDENADOS POR PRECIO (Mayor a menor):")
print(df.sort_values(by='precio', ascending=False))

print("\n16. CURSOS CON PRECIO MAYOR A $1,500:")
filtro = df[df['precio'] > 1500]
print(filtro)

print("\n17. RESUMEN POR PLATAFORMA:")
resumen = df.groupby('plataforma').agg(
    cursos=('id_curso', 'count'),
    precio_promedio=('precio', 'mean'),
    precio_maximo=('precio', 'max')
)
print(resumen)

# 18. Gráfica de barras: Cursos por plataforma
print(" 18. Gráfica de barras: Cursos por plataforma")
conteo = df['plataforma'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Cursos por plataforma Nahum Flores 0065')
plt.xlabel('Plataforma')
plt.ylabel('Cantidad de cursos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Precios por curso
plt.figure(figsize=(9, 5))
plt.bar(df['titulo'], df['precio'], color='lightgreen')
plt.title('Precio por curso Nahum Flores NC 0065')
plt.xlabel('Curso')
plt.ylabel('Precio en pesos')
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de duración en horas
plt.figure(figsize=(8, 5))
plt.hist(df['duracion_horas'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de duración de cursos Nahum Flores NC 0065')
plt.xlabel('Duración (horas)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Duración vs Precio
plt.figure(figsize=(8, 5))
plt.scatter(df['duracion_horas'], df['precio'], color='red', s=100)
plt.title('Relación entre duración y precio Nahum Flores 0065')
plt.xlabel('Duración (horas)')
plt.ylabel('Precio')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de precios
plt.figure(figsize=(7, 5))
plt.boxplot(df['precio'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de precios (Boxplot) EDA Nahum Flores 0065')
plt.ylabel('Precio')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Nahum Flores 0065')
plt.tight_layout()
plt.show()