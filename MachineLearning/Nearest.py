import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('/Users/Pedro/Desktop/IA/MachineLearning/Car/car.data', encoding='utf-8', header=None)

le = LabelEncoder()
buying = le.fit_transform(list(data[0]))
maint = le.fit_transform(list(data[1]))
door = le.fit_transform(list(data[2]))
persons = le.fit_transform(list(data[3]))
lug_boot = le.fit_transform(list(data[4]))
safety = le.fit_transform(list(data[5]))
cls = le.fit_transform(list(data[6]))

X = list(zip(buying,maint,door,persons,lug_boot,safety))
y = list(cls)

k_list = [1,3,5,7,9]
k_scores = []

for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_score = cross_val_score(knn, X, y, cv=10)
    k_scores.append(cv_score.mean())

plt.plot(k_list, k_scores)
plt.xlabel('Valor K de KNN')
plt.ylabel('Acuracia 10Fold Cross-Validada')
plt.show()

