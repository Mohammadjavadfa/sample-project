import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("updated_file.csv")


X = df.iloc[:, 1:4]
y = df.iloc[:, 4]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))




count_0_train = (y_train == 0).sum()
count_1_train = (y_train == 1).sum()
print(f"تعداد 0 در y_train: {count_0_train}")
print(f"تعداد 1 در y_train: {count_1_train}")
count_0_test = (y_test == 0).sum()
count_1_test = (y_test == 1).sum()
print(f"\nتعداد 0 در y_test: {count_0_test}")
print(f"تعداد 1 در y_test: {count_1_test}")



classification_error = 1 - accuracy
print(f"Classification Error: {classification_error:.2f}")


incorrect_index = y_test[y_test != y_pred].index[0]
incorrect_record = df.iloc[incorrect_index]

print("One record with incorrect prediction:")
print(incorrect_record)
