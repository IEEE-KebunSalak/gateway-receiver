import struct
from typing import Any, Tuple

# 'B' for uint8_t, 'f' for float, 'i' for int, 'I' for uint
STRUCT_FORMAT = "Bfffi"
DISTRESS_STRUCT_FORMAT = "Bdd"


def read_struct(payload: bytes) -> Tuple[int, float, float, float, int]:
    """Read struct from bytes"""
    data = struct.unpack(STRUCT_FORMAT, payload)

    # id, temp, hum, light, tip
    return data[0], data[1], data[2], data[3], data[4]


def read_distress_struct(payload: bytes) -> Tuple[int, float, float]:
    """Read distress struct from bytes"""
    data = struct.unpack(DISTRESS_STRUCT_FORMAT, payload)

    # id, latitude, longitude
    return data[0], data[1], data[2]
