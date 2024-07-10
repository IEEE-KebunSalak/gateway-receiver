from pyLoraRFM9x import LoRa  # type: ignore // gabisa di install di win64
from typing import Any
from time import sleep
from struct_helper import read_struct

from httpx import Client
from dotenv import load_dotenv
import os


from config import (
    RFM95_PORT,
    RFM95_CS,
    RFM95_INT,
    RFM95_RST,
    RF95_FREQ,
    RF95_POW,
    CLIENT_ADDRESS,
    ModemConfig,
)

if load_dotenv():
    print("Success loading .env file")
else:
    print("Failed loading .env file")
    exit(-1)

API_URL_ENDPOINT = os.getenv("API_URL_ENDPOINT")

# global objects
lora = LoRa(
    spi_port=RFM95_PORT,
    spi_channel=RFM95_CS,
    interrupt_pin=RFM95_INT,
    my_address=CLIENT_ADDRESS,
    reset_pin=RFM95_RST,
    freq=RF95_FREQ,
    tx_power=RF95_POW,
    modem_config=ModemConfig.Bw125Cr45Sf2048,
    acks=True,
    receive_all=False,
)

client = Client()


def on_recv(payload: Any) -> None:
    """Callback function when data received from the LoRa module"""
    global current_index

    try:
        payload_struct = payload.message
        node_id, temp, hum, light, tip = read_struct(payload_struct)

        print("From:", node_id)
        print("Received:", f"{temp=}, {hum=}, {light=}, {tip=}")
        print(f"RSSI: {payload.rssi}; SNR: {payload.snr}")
        print("---------------------------------------------------")

        try:
            response = client.post(
                url=API_URL_ENDPOINT,
                json={
                    "node_id": node_id,
                    "temperature": temp,
                    "humidity": hum,
                    "light": light,
                    "tip": tip,
                },
            )

            print("[HTTP Response]:", response.status_code)
            print("[HTTP Response]:", response.json())

        except Exception as e:
            print("[Error HTTP]:", e)

    except:
        print("[Error]: Ignoring data since it's unreadable.")


def setup() -> None:
    """Setup function only called once per lifetime"""

    global lora

    print("[setup]: setting up LoRa module")
    lora.set_mode_rx()
    lora.on_recv = on_recv

    print("[setup]: setup done...")


def main() -> None:
    """Main Program Loop"""

    print("[Main]: Running main program loop...")

    try:
        while True:
            sleep(0.5)

    except Exception as e:
        print("[Error]:", e)
        pass

    finally:
        lora.close()
        client.close()


setup()
main()
