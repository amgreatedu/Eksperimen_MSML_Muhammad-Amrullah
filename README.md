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


## 🛠️ Fitur & Kriteria Proyek

### 1. Eksperimen Model (Model Experimentation)
*   Melakukan pembersihan data, *feature engineering*, dan prapemrosesan dataset *Credit Scoring*.
*   Membangun pipeline pelatihan model yang direproduksi dengan mudah melalui skrip modular.

### 2. Pelacakan & Registrasi Model (Model Tracking - MLflow & DagsHub)
*   Menggunakan **MLflow** untuk melacak parameter, metrik evaluasi (akurasi, presisi, *recall*), dan artefak model.
*   **[Advanced]** Artefak dan riwayat pelatihan diintegrasikan secara terpusat dan *online* menggunakan **DagsHub**, memungkinkan kolaborasi tim yang lebih mulus.

### 3. Otomatisasi CI/CD (Continuous Integration / Continuous Deployment)
*   Menggunakan **GitHub Actions** untuk menjalankan alur kerja otomatis setiap kali ada perubahan kode (*push/pull request*).
*   Pipeline mencakup tahapan: instalasi dependensi, pengujian kode (*linting/testing*), dan penyimpanan model secara otomatis.

### 4. Pemantauan & Peringatan (Monitoring & Logging - Prometheus & Grafana)
*   **Model Serving:** Model disajikan sebagai REST API menggunakan Flask.
*   **Metrik Khusus:** Mengekspos 10+ metrik bisnis dan sistem ke rute `/metrics` (contoh: *Total Requests, CPU Usage, Positive Predictions, Error Rate*).
*   **Prometheus:** Melakukan *scraping* data secara *real-time* dari API model.
*   **Grafana Dashboard:** Visualisasi metrik secara interaktif dengan nama *dashboard* khusus.
*   **[Advanced] Alerting:** Mengonfigurasi 3 aturan peringatan (*Alert Rules*) di Grafana (contoh: *High Traffic, CPU Overload, Memory Leak*) yang akan terpicu jika melampaui *threshold* tertentu.

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

### Prasyarat
Pastikan Anda telah menginstal:
*   Python 3.12.7
*   Prometheus & Grafana (Tersedia secara *native* atau via Docker)

### Langkah-Langkah

**1. Clone Repositori**
```bash
git clone [https://github.com/username-anda/Eksperimen_MSML_Muhammad-Amrullah.git](https://github.com/username-anda/Eksperimen_MSML_Muhammad-Amrullah.git)
cd Eksperimen_MSML_Muhammad-Amrullah

**2. Instalasi Dependensi**

```Bash
cd Membangun_model
pip install -r requirements.txt

**3. Menjalankan MLflow (Opsional untuk melihat hasil eksperimen lokal)**
```Bash
mlflow ui
Akses UI di http://localhost:5000

**4. Menjalankan API Model Serving & Prometheus Exporter**

```Bash
cd "../Monitoring dan Logging"
python 3.prometheus_exporter.py
API akan berjalan di http://localhost:8000. Metrik dapat diakses di http://localhost:8000/metrics.

**5. Simulasi Trafik (Inference)**
Buka terminal baru dan jalankan skrip berikut agar grafik di Grafana bergerak:

```Bash
python 7.inference.py

**6. Menjalankan Prometheus & Grafana**

Jalankan file executable prometheus menggunakan konfigurasi 2.prometheus.yml.

Buka Grafana di http://localhost:3000, tambahkan Data Source Prometheus, dan impor/buat Dashboard pemantauan.

👤 Penulis
**Muhammad Amrullah**
_Data & AI Enthusiast_

Dibuat untuk penugasan akhir sertifikasi MLOps - Dicoding Indonesia.
