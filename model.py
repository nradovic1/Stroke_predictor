
import pandas as pd
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from imblearn.combine import SMOTEENN

#from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv('Resources/model_clean_data.csv')
df = df.sample(frac=1)

y = df['stroke']
X = df.drop(['stroke'], axis = 1)

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.85, random_state=12)

smoteenn = SMOTEENN(random_state=12)
X_smoteenn, y_smoteenn = smoteenn.fit_resample(X, y)

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
model = knn.fit(X_smoteenn, y_smoteenn)






pickle.dump(model, open('model.pkl','wb'))
print('Model Pickled')