import requests

# URL de la API
url = "http://127.0.0.1:8000/predict"

# Datos de ejemplo
payload = {
    "HP": 100,
    "Attack": 120,
    "Defense": 90,
    "SP_Atk": 110,
    "SP_Def": 85,
    "Speed": 95
}

# Realizar la solicitud POST
response = requests.post(url, json=payload)

# Imprimir la respuesta de la API
print(response.json())
