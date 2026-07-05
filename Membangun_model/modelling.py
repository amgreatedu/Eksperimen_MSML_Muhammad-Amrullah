import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Setup Autolog
mlflow.autolog()

# Load Data
df = pd.read_csv('data_processed.csv')
X = df.drop('Creditworthiness', axis=1)
y = df['Creditworthiness']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start MLflow run
with mlflow.start_run(run_name="Basic_Autolog_Model"):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model Basic berhasil dilatih dengan autolog!")