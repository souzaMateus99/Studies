import numpy as np
from scipy import stats


salario_jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 30000, 40000, 800000]

## calculando a média de salario dos jogadores
media = np.mean(salario_jogadores)

## calculando a mediana de salario dos jogadores
mediana = np.median(salario_jogadores)

## retornando os quartis
quartis = np.quantile(salario_jogadores, [0, 0.25, 0.5, 0.75, 1])

## desvio padrão
desvio_padrao = np.std(salario_jogadores, ddof = 1)


print(stats.describe(salario_jogadores))