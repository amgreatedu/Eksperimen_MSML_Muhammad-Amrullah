# Eksperimen Data: Credit Scoring Model 📊

Repositori ini berisi tahapan awal dari proyek *Machine Learning Operations* (MLOps) secara *end-to-end* untuk model **Credit Scoring** (Penilaian Kredit). Repositori ini dikhususkan untuk memuat proses eksperimen data, pembersihan data (*data cleaning*), rekayasa fitur (*feature engineering*), dan prapemrosesan (*preprocessing*).

Proyek ini disusun untuk memenuhi **Kriteria 1: Melakukan Eksperimen terhadap Dataset Pelatihan** pada program kelulusan Dicoding Indonesia.

## 📁 Struktur Repositori

Struktur folder pada repositori ini disusun agar bersih dan berfokus pada alur pemrosesan data, sesuai dengan standar Kriteria 1:

```text
Eksperimen_SML_Muhammad-Amrullah
├── data_raw/
│   └── data.csv                            # Dataset mentah original sebelum diproses
├── preprocessing/
│   ├── automate_Muhammad-Amrullah.py       # Skrip Python untuk otomatisasi prapemrosesan (Skilled)
│   ├── data_processed.csv                  # Dataset hasil prapemrosesan yang siap dilatih
│   └── Eksperimen_Muhammad-Amrullah.ipynb  # Jupyter Notebook berisi tahapan riset & eksperimen data
├── .gitignore                              # File untuk mengabaikan file temporary/cache di Git
├── README.md                               # Dokumentasi repositori eksperimen
└── requirements.txt                        # Daftar dependensi library eksperimen