import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Hello, World")

# No VS Code (.py), precisamos do print() para ver o resultado do type
print(type(2))
print(type(2.5))
print(type("world"))

altura = [1.60, 1.75, 1.82, 2]
print("\nAlturas:")
print(altura)

print("\nEstatísticas da lista 'altura':")
print(f"Média: {np.mean(altura)}")
print(f"Mediana: {np.median(altura)}")
print(f"Desvio padrão: {np.std(altura)}")
print(f"Variância: {np.var(altura)}")

turma_a = [1.75, 1.77, 1.82, 2, 1.6]
turma_b = [1.55, 1.60, 1.64, 2, 1.7]

# Boxplot comparando Turma A e Turma B (Horizontal, sem outliers)
plt.figure(figsize=(10, 5)) 
plt.boxplot([turma_a, turma_b], tick_labels=['Turma A', 'Turma B'], patch_artist=True, medianprops={'color': 'black'}, vert=False, showfliers=False)
plt.title('Comparação de Altura entre Turma A e Turma B (Boxplot Horizontal, sem Outliers)')
plt.xlabel('Altura') 
plt.ylabel('Turmas') 
plt.grid(False)

# O plt.show() vai abrir uma janela separada no seu computador com o gráfico!
plt.show()

print(f'\nA turma A tem média {np.mean(turma_a):.2f} com desvio padrão de {np.std(turma_a):.2f}')
print(f'A turma B tem média {np.mean(turma_b):.2f} com desvio padrão de {np.std(turma_b):.2f}')