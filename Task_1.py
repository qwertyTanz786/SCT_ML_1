import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
df = pd.read_csv(r"C:\Users\panch\Downloads\Training model_OWN\streamlit_github\Housing.csv")
df = df.drop(["id", "date"],axis=1)
X = df.drop("price", axis=1)
Y = df["price"]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
cv_rf = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid = {
    'n_estimators':[280],      
    'max_depth':[24],            
    'min_samples_split':[6],     
    'min_samples_leaf':[2]
    }
)
cv_rf.fit(X_train,Y_train)
pred = cv_rf.predict(X_test)
# model=RandomForestRegressor(random_state=42)
# model.fit(X_train, Y_train)
# pred = model.predict(X_test)
mse = mean_squared_error(Y_test, pred)
r2 = r2_score(Y_test, pred)
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")