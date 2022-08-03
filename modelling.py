import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import joblib
from sklearn.metrics import classification_report

dat = pd.read_csv('data/one_day_pp.csv')
dat.head()
dat = dat.iloc[:, 1:]

Le = preprocessing.LabelEncoder()

for i in range(1, 8):
    dat.iloc[:, i] = Le.fit_transform(dat.iloc[:, i])

train, test = train_test_split(dat, test_size=0.3, random_state=25)

X_train = train.iloc[:, 1:]
y_train = train.iloc[:, 0]

X_test = test.iloc[:, 1:]
y_test = test.iloc[:, 0]
#print(X)
#print(y)

model = RandomForestClassifier()
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=1, random_state=1)

n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]

random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth}

rf_random = RandomizedSearchCV(estimator=model, param_distributions=random_grid, n_iter=100, cv=5, verbose=2,
                               random_state=42, n_jobs=-1)

rf_random.fit(X_train, y_train)
rf_random.best_score_
rf_random.best_estimator_

hold_out = pd.DataFrame(X_test.iloc[0, 0:])
y_pred = rf_random.predict(X_test.iloc[1:, 0:])

print(classification_report(y_test.iloc[1:], y_pred))

hold_out.to_csv('data/hold_out_for_flask.csv')
joblib.dump(rf_random, 'model/rf_track.joblib')