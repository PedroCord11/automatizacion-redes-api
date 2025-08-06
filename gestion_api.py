import requests
import json

BASE_URL = "https://reqres.in/api/users"

def listar_dispositivos():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 2xx
        
        datos = response.json()
        print("--- Dispositivos encontrados ---")
        for dispositivo in datos['data']:
            print(f"ID: {dispositivo['id']}, Nombre: {dispositivo['first_name']}, Email: {dispositivo['email']}")
        
        return datos

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar la respuesta JSON.")
        return None

if __name__ == "__main__":
    listar_dispositivos()
