import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalancedRandomForestClassifier
import pickle

df = pd.read_csv('model_clean_data.csv')
df = df.sample(frac=1)

y = df['stroke']
X = df.drop(['stroke'], axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.85, random_state=12)

clf = BalancedRandomForestClassifier(max_depth=2, random_state=12)
clf.fit(X_train, y_train) 

pickle.dump(clf, open('model.pkl','wb'))
