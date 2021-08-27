import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn import tree
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

depth = []

clf = tree.DecisionTreeClassifier(max_depth=4, random_state=1)
clf = clf.fit(X,y)
cv_score = cross_val_score(clf, X, y, cv=10)
depth.append(cv_score.mean())

print(depth)
plt.figure(figsize=(9,6))
tree.plot_tree(clf, filled=True, fontsize=5)
plt.show()
