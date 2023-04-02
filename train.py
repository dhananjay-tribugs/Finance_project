
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("./MF_Model_base.csv")

data.rename(columns={'Txn. Type':'redeem'}, inplace=True)

X = data.drop("redeem", axis=1)
y = data["redeem"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

new_customer = pd.DataFrame([[0.5, 0.3, 0.2, 0.8, 0.4]], columns=X.columns)
prediction = model.predict(new_customer)
print("Prediction:", prediction)
