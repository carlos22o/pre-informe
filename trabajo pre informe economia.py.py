
import matplotlib.pyplot as plt

# dibujar la curva de la frontera de posibilidades de producción
plt.figure(figsize=(8, 6))
plt.plot([0, 8258], [65588, 0], 'b-', linewidth=2)

# etiquetas para los ejes x e y
plt.xlabel('Cantidad Bovino producido (ton)')
plt.ylabel('Cantidad Aves Broyler(ton)')


plt.title("FPP entre produccion de Bovino y Aves Broyler")
# mostrar el gráfico
plt.show()


"----------------------------------------------------------------------------"
import matplotlib.pyplot as plt

# dibujar la curva de la frontera de posibilidades de producción
plt.figure(figsize=(8, 6))
plt.plot([0, 1.84], [0.459, 0], 'b-', linewidth=2)

# etiquetas para los ejes x e y
plt.xlabel('Cantidad de trabajadores para una ton de bovino (ton)')
plt.ylabel('Cantidad de trabajadores para una ton de Avez Broyler(ton)')
plt.title("FPP entre cantidad de trabajadores por una toneladas producidas")


# mostrar el gráfico
plt.show()
