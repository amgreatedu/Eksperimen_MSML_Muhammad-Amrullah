import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os
import shutil

# Hapus folder model lama jika CI/CD dijalankan ulang
if os.path.exists("saved_model"):
    shutil.rmtree("saved_model")

# Matikan autolog untuk menghindari error environment di CI
mlflow.sklearn.autolog(disable=True)

print("Memulai proses training model CI/CD...")
df = pd.read_csv('data_processed.csv')
X = df.drop('Creditworthiness', axis=1)
y = df['Creditworthiness']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run() as run:
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Menyimpan model secara statis untuk dibungkus Docker nanti
    mlflow.sklearn.save_model(model, "saved_model")
    print("Model berhasil dilatih dan disimpan di folder 'saved_model'!")