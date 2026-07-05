import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(input_path, output_path):
    print(f"Membaca data dari: {input_path}")
    df = pd.read_csv(input_path)
    
    # Menghapus duplikat
    df = df.drop_duplicates()
    
    # Encoding data kategorikal
    le = LabelEncoder()
    cat_cols = ['Gender', 'Education', 'Payment_History', 'Employment_Status', 'Residence_Type', 'Marital_Status']
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])
        
    # Standarisasi fitur numerik
    scaler = StandardScaler()
    num_cols = ['Age', 'Income', 'Debt', 'Credit_Score', 'Loan_Amount', 'Loan_Term', 'Num_Credit_Cards']
    df[num_cols] = scaler.fit_transform(df[num_cols])
    
    # Memastikan folder output ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Menyimpan hasil
    df.to_csv(output_path, index=False)
    print(f"Berhasil! Data bersih disimpan di: {output_path}")

if __name__ == "__main__":
    # Menjalankan fungsi dengan path relatif dari root repository
    preprocess_data('data_raw/data.csv', 'data_processed/data_ready.csv')