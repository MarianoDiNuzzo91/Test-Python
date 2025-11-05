from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

giocatori = read_csv('giocatori.csv')
x = giocatori.drop(columns=['videogame'])
y = giocatori['videogame']

modello = DecisionTreeClassifier()
modello.fit(x.values, y.values)
previsione = modello.predict([[1,31]])
print(previsione)
