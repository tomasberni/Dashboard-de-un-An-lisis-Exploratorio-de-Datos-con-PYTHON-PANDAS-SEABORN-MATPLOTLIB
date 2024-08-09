#MADE BY TOMAS BERNI
#SE UTILIZO JUPYTER NOTEBOOK PARA ESTE PROYECTO, SEGURAMENTE NECESITE plt.show() para ejecutar graficos




import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Cargar el dataset diamonds de Seaborn

diamantes = sns.load_dataset("diamonds")


#Realizar un análisis exploratorio preliminar para familiarizarse con los datos

head = diamantes.head()
tail = diamantes.tail()
description = diamantes.describe()

#Crear visualizaciones
#precio vs. peso en quilates
sns.set(style="whitegrid")

g = sns.relplot(data=diamantes, x='carat', y='price', alpha=0.5, height=6, aspect=1.5, hue="color")

g.fig.suptitle('Relación entre el Precio y el Peso en Quilates de los Diamantes',
               va='baseline',
               ha='center')
g.set_axis_labels('Peso en Quilates', 'Precio');


#Distribuciones de variables numéricas (por ejemplo, precio, peso en quilates)
a = sns.displot(data = diamantes, x="price", kind="hist",color="blue", height=4,
                aspect=2, kde=True)
a.fig.suptitle('Distribución del Precio de los Diamantes',
               va='baseline',
               ha='center')
a.set_axis_labels('Precio ($)', 'Frecuencia');



# Creando la visualización de la distribución del peso en quilates
b = sns.displot(data = diamantes, x="carat", kind="hist",color="gold", height=4,
                aspect=3, kde=True)
b.fig.suptitle('Distribución del Peso en Quilates',
               va='baseline',
               ha='center')
b.set_axis_labels('Quilate', 'Frecuencia');


# Comparaciones de variables numéricas agrupadas por categorías (por ejemplo, calidad del corte)

c = sns.catplot(data=diamantes,
                kind="box",
                x="cut",
                y="price",
                height=6,
                aspect=1,
                order=["Fair", "Good", "Very Good", "Premium", "Ideal"],  palette="husl")


c.fig.suptitle('Comparación del Precio de los Diamantes por Calidad del Corte',
               va='baseline',
               ha='center')


c.set_axis_labels("Calidad del Corte",
                  "Precio ($)");



# Utilizando jointplot para visualizar la relación entre 'depth' y 'price' con un gráfico de densidad kernel
d = sns.jointplot(data=diamantes,
                  x="depth",
                  y="price",
                  kind="kde",
                  fill=True,
                  space=0,
                  color="purple")

# Cambiando las etiquetas de los ejes
d.set_axis_labels("Profundidad del Diamante (%)",
                  "Precio ($)")

# Mejorando el título
d.fig.suptitle('Relación entre la Profundidad y el Precio de los Diamantes',
               va='baseline',
               ha='center',
               fontsize=16);

# Creando el pairplot para el dataset diamonds, Seaborn ignorará automáticamente las variables no numéricas
e = sns.pairplot(diamantes,
                corner=True)

# Mejorando el título con plt.subplots_adjust y plt.suptitle para el gráfico generado
e.fig.suptitle('Relaciones entre Variables Numéricas en el Dataset Diamonds',
               va='baseline',
               ha='center',
               fontsize=16);

