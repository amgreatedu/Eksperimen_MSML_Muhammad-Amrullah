from flask import Flask, request, jsonify, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
import random
import psutil

app = Flask(__name__)

# --- DEFINISI 10 METRIK PROMETHEUS ---
# 1. Total request
REQUEST_COUNT = Counter('model_request_count_total', 'Total HTTP Requests')
# 2. Latency (waktu respons)
REQUEST_LATENCY = Histogram('model_request_latency_seconds', 'Request latency')
# 3. Total error
ERROR_COUNT = Counter('model_error_count_total', 'Total errors')
# 4. Penggunaan CPU
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Current CPU usage percent')
# 5. Penggunaan Memori
MEMORY_USAGE = Gauge('system_memory_usage_bytes', 'Current memory usage in bytes')
# 6. Prediksi Positif (Creditworthy)
PREDICT_POSITIVE = Counter('model_predict_positive_total', 'Total positive predictions')
# 7. Prediksi Negatif (Not Creditworthy)
PREDICT_NEGATIVE = Counter('model_predict_negative_total', 'Total negative predictions')
# 8. Rata-rata Confidence/Probability (Simulasi)
PREDICT_PROBA = Gauge('model_predict_probability_avg', 'Average prediction probability')
# 9. Jumlah Request Aktif (Sedang diproses)
ACTIVE_REQUESTS = Gauge('model_active_requests', 'Number of active requests')
# 10. Suhu/Kesehatan Sistem (Simulasi metrik custom)
SYSTEM_HEALTH = Gauge('system_health_status', 'System health status (1=Good, 0=Bad)')

@app.route('/predict', methods=['POST'])
def predict():
    ACTIVE_REQUESTS.inc()
    start_time = time.time()
    REQUEST_COUNT.inc()
    
    try:
        # Simulasi pemrosesan (Di tahap ini Anda bisa meload model MLflow Anda)
        data = request.json
        time.sleep(random.uniform(0.1, 0.5)) # Simulasi waktu komputasi
        
        # Simulasi hasil prediksi
        prediction = random.choice([0, 1])
        probability = random.uniform(0.6, 0.99)
        
        if prediction == 1:
            PREDICT_POSITIVE.inc()
        else:
            PREDICT_NEGATIVE.inc()
            
        PREDICT_PROBA.set(probability)
        
        # Update metrik sistem
        CPU_USAGE.set(psutil.cpu_percent())
        MEMORY_USAGE.set(psutil.virtual_memory().used)
        SYSTEM_HEALTH.set(1)
        
        latency = time.time() - start_time
        REQUEST_LATENCY.observe(latency)
        ACTIVE_REQUESTS.dec()
        
        return jsonify({'prediction': prediction, 'probability': probability})

    except Exception as e:
        ERROR_COUNT.inc()
        ACTIVE_REQUESTS.dec()
        return jsonify({'error': str(e)}), 500

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)