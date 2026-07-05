import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import os

# --- TAMBAHKAN 2 BARIS INI (Ganti dengan Username dan Token Anda) ---
os.environ["MLFLOW_TRACKING_USERNAME"] = "amgreatedu"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "6cd285adb31393a7d0f0c1faab228a3014b3d186"

# 1. Konfigurasi DagsHub URI
DAGSHUB_URI = "https://dagshub.com/amgreatedu/Eksperimen_MSML_Muhammad-Amrullah.mlflow" # GANTI DENGAN URL ANDA
mlflow.set_tracking_uri(DAGSHUB_URI)

# Memastikan autolog MATI sesuai instruksi (Manual Logging)
mlflow.sklearn.autolog(disable=True)

# 2. Persiapan Data
df = pd.read_csv('data_processed.csv')
X = df.drop('Creditworthiness', axis=1)
y = df['Creditworthiness']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Hyperparameter Tuning dengan GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

print("Memulai Hyperparameter Tuning...")
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# Prediksi menggunakan model terbaik
y_pred = best_model.predict(X_test)

# 4. MLflow Manual Logging
with mlflow.start_run(run_name="Advanced_Tuning_Model"):
    
    # A. Logging Parameters (Parameter terbaik dari GridSearchCV)
    mlflow.log_params(grid_search.best_params_)
    
    # B. Logging Metrics
    mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
    mlflow.log_metric("precision", precision_score(y_test, y_pred))
    mlflow.log_metric("recall", recall_score(y_test, y_pred))
    mlflow.log_metric("f1_score", f1_score(y_test, y_pred))
    
    # C. Logging Model Utama
    mlflow.sklearn.log_model(best_model, "random_forest_best_model")
    
    # D. Membuat dan Menyimpan 2 Artefak Tambahan
    os.makedirs("artifacts", exist_ok=True)
    
    # Artefak 1: Confusion Matrix Plot
    plt.figure(figsize=(6, 4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Best Model")
    cm_path = "artifacts/confusion_matrix.png"
    plt.savefig(cm_path)
    mlflow.log_artifact(cm_path)
    plt.close()
    
    # Artefak 2: Feature Importance Plot
    plt.figure(figsize=(10, 6))
    feat_importances = pd.Series(best_model.feature_importances_, index=X.columns)
    feat_importances.nlargest(10).plot(kind='barh', color='teal')
    plt.title("Top 10 Feature Importances")
    fi_path = "artifacts/feature_importance.png"
    plt.savefig(fi_path)
    mlflow.log_artifact(fi_path)
    plt.close()

    print("Model tuning, metrik, dan 2 artefak berhasil dicatat ke DagsHub!")