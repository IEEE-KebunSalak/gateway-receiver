import struct
from typing import Any, Tuple

# 'B' for uint8_t, 'f' for float, 'i' for int, 'I' for uint
STRUCT_FORMAT = "Bfffi"
DISTRESS_STRUCT_FORMAT = "Bdd"


def decode_data(data: bytes) -> dict[str, any]:
    try:
        # Attempt to parse as GpsPayload
        unpacked_data = struct.unpack(DISTRESS_STRUCT_FORMAT, data)
        _, latitude, longitude = unpacked_data
        # Validate latitude and longitude ranges
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return {
                "type": "GpsPayload",
                "node_id": unpacked_data[0],
                "latitude": latitude,
                "longitude": longitude,
            }
    except struct.error:
        pass

    try:
        # Fallback to parse as Payload
        unpacked_data = struct.unpack(STRUCT_FORMAT, data)
        return {
            "type": "Payload",
            "node_id": unpacked_data[0],
            "temperature": unpacked_data[1],
            "humidity": unpacked_data[2],
            "light": unpacked_data[3],
            "tip": unpacked_data[4],
        }
    except struct.error:
        # Handle or log errors if neither format matches
        raise ValueError("Data does not match either struct format")
