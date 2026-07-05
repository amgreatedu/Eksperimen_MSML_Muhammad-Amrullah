import requests
import time
import random

URL = "http://localhost:8000/predict"

print("Memulai simulasi traffic ke server...")
while True:
    try:
        # Mengirim data dummy
        payload = {"feature1": random.random(), "feature2": random.random()}
        response = requests.post(URL, json=payload)
        print(f"Status: {response.status_code}, Response: {response.json()}")
        
        # Jeda acak antar request (0.5 - 2 detik)
        time.sleep(random.uniform(0.5, 2.0))
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)