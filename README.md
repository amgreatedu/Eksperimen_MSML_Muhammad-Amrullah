# End-to-End MLOps: Credit Scoring Model 🚀

Proyek ini adalah implementasi *Machine Learning Operations* (MLOps) secara *end-to-end* untuk model **Credit Scoring** (Penilaian Kredit). Repositori ini merangkum seluruh siklus hidup model *machine learning*, mulai dari eksperimen data, pelacakan model, otomatisasi CI/CD, hingga penyajian (*serving*) dan pemantauan (*monitoring*).

Proyek ini disusun untuk memenuhi kriteria kelulusan (Advanced) pada program Dicoding.

## 📁 Struktur Repositori

Proyek ini dibagi menjadi beberapa modul utama sesuai dengan tahapan MLOps:

```text
├── Membangun_model/
│   ├── dataset_preprocessing.py   # Skrip prapemrosesan data
│   ├── modelling.py               # Skrip pelatihan model dasar
│   ├── modelling_tuning.py        # Skrip hyperparameter tuning (Advanced)
│   ├── requirements.txt           # Dependensi library Python
│   └── DagsHub.txt                # Tautan pelacakan artefak online
├── Monitoring dan Logging/
│   ├── 2.prometheus.yml           # Konfigurasi target metrik Prometheus
│   ├── 3.prometheus_exporter.py   # API Flask untuk serving model & export metrik
│   ├── 7.inference.py             # Skrip simulasi request trafik terus-menerus
│   └── (Folder Bukti Screenshoot) # Dokumentasi dashboard dan alerting
├── .github/workflows/
│   └── ci_workflow.yaml           # Konfigurasi GitHub Actions untuk CI/CD
└── README.md                      # Dokumentasi proyek
