from httpx import Client

client = Client()
API_URL_ENDPOINT = "https://node.mysalak.com/raspi"

node_id = 10
temp = 30
hum = 40
light = 50
tip = 6

response = client.post(
    url=API_URL_ENDPOINT,
    json={
        "node_id": node_id,
        "temperature": temp,
        "humidity": hum,
        "lux": light,
        "tips": tip,
    },
)

print(response.status_code)
print(response.text)
