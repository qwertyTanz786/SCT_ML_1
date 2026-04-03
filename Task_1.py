import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
df = pd.read_csv(r"C:\Users\panch\Downloads\Training model_OWN\streamlit_github\Housing.csv")
df = df.drop(["id", "date"], axis=1)
X = df.drop("price", axis=1)
Y = df["price"]
Y = np.log1p(Y)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, Y_train)
pred = model.predict(X_test)
mse = mean_squared_error(Y_test, pred)
r2 = r2_score(Y_test, pred)
print(f"MSE (log scale): {mse}")
print(f"R2 Score (log scale): {r2}")