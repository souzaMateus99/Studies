import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('Datas/iris.csv')
type_iris_count = iris['class'].value_counts()

iloc = iris.iloc[:, 0:4]
ilocClass = iris.iloc[:, 4]

X, _, Y, _ = train_test_split(iloc, ilocClass, test_size = 0.5, stratify = ilocClass)


infert = pd.read_csv('Datas/infert.csv')
infertCount = infert['education'].value_counts()


X1, _, Y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6, stratify = infert.iloc[:, 1])


print(Y1.value_counts())