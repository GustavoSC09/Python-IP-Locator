
from requests import get
from requests.exceptions import RequestException

ip = input("Enter the IP address: ").strip()
url = f"https://ipwho.is/{ip}"

try:
    response = get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    if not data.get("success", False):
        print("Erro:", data.get("message", "IP não disponível"))
    else:
        print("\n--- IP Information ---")
        print("IP:", data.get("ip"))
        print("Cidade:", data.get("city"))
        print("Região:", data.get("region"))
        print("País:", data.get("country"))
        print("Continente:", data.get("continent"))
        print("Latitude:", data.get("latitude"))
        print("Longitude:", data.get("longitude"))
        print("Código postal:", data.get("postal"))
        print("Fuso horário:", data.get("timezone", {}).get("id"))

except RequestException as e:
    print("Erro de ligação:", e)
except ValueError:
    print("Erro: a API não devolveu JSON válido.")
