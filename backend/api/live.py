from fastapi import APIRouter, WebSocket
import json

router = APIRouter()

@router.websocket("/ws/live")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = {
            "time": time.time(),
            "gyro": [random.uniform(-100, 100) for _ in 3],
            "voltage": 16.8 - random.random(),
            "rssi": 85 + random.randint(-10, 0)
        }
        await websocket.send_text(json.dumps(data))
        await asyncio.sleep(0.05)  # 20 Гц