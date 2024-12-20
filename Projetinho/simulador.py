import requests
import random
import time

URL = 'http://127.0.0.1:5000/enviar_dados'

def gerar_dados():
    return {
        "CO2": random.randint(300, 2000),
        "PM2.5": random.uniform(10, 100)
    }

while True:
    dados = gerar_dados()
    try:
        resposta = requests.post(URL, json=dados)
        print(f"Enviado: {dados}, Resposta: {resposta.json()}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")
    time.sleep(2)  # Envia dados a cada 2 segundos
