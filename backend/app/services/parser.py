import numpy as np
from betaflight_parser import Reader

def parse_log_file(file_path: str):
    reader = Reader(file_path)
    data = []

    for frame in reader:
        data.append({
            "time": frame.time,
            "ax": frame.gyroADC[0],
            "ay": frame.gyroADC[1],
            "az": frame.gyroADC[2],
            "gx": frame.accSmooth[0],
            "gy": frame.accSmooth[1],
            "gz": frame.accSmooth[2],
            "voltage": frame.vbat,
            "rpm": frame.rssi or 0
        })

    return data