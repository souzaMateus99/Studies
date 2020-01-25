import pandas as pd
import numpy as np
import numpy.random as random

base = pd.read_csv('Datas/iris.csv')

random.seed(2345)
amostra = random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])


print(len(amostra[amostra == 1]))
print(len(amostra[amostra == 0]))