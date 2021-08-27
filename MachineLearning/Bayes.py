import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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

scores = []

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7, random_state = 0)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
cv_score = cross_val_score(gnb, X_train, y_train, cv=10, scoring='accuracy')
scores = cv_score.mean()

print(scores)

