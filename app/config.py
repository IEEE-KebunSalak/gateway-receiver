from enum import Enum

# Lora Parameters
RFM95_RST = 25
RFM95_PORT = 0
RFM95_CS = 1
RFM95_INT = 5
RF95_FREQ = 922.0
RF95_POW = 23
CLIENT_ADDRESS = 2
SERVER_ADDRESS = 5


class ModemConfig(Enum):
    Bw125Cr45Sf128 = (
        0x72,
        0x74,
        0x04,
    )  # < Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on. Default medium range
    Bw500Cr45Sf128 = (
        0x92,
        0x74,
        0x04,
    )  # < Bw = 500 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on. Fast+short range
    Bw31_25Cr48Sf512 = (
        0x48,
        0x94,
        0x04,
    )  # < Bw = 31.25 kHz, Cr = 4/8, Sf = 512chips/symbol, CRC on. Slow+long range
    Bw125Cr48Sf4096 = (
        0x78,
        0xC4,
        0x0C,
    )  # /< Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, low data rate, CRC on. Slow+long range
    Bw125Cr45Sf2048 = (
        0x72,
        0xB4,
        0x04,
    )  # < Bw = 125 kHz, Cr = 4/5, Sf = 2048chips/symbol, CRC on. Slow+long range
