import torch
import torch.nn as nn

class PilotErrorDetector(nn.Module):
    def __init__(self, input_size=7):
        super().__init__()
        self.lstm = nn.LSTM(input_size, 64, batch_first=True)
        self.fc = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x, _ = self.lstm(x)
        return self.sigmoid(self.fc(x[:, -1]))

# Пример использования
def detect_smoothness_errors(telemetry_data):
    model = PilotErrorDetector()
    model.load_state_dict(torch.load("models/error_detector.pth"))
    model.eval()

    data = np.array([[d["ax"], d["ay"], d["az"], d["gx"], d["gy"], d["gz"], d["voltage"]] for d in telemetry_data])
    data = torch.tensor(data, dtype=torch.float32).unsqueeze(0)

    risk = model(data).item()
    return {"error_risk": risk, "advice": "Smooth inputs" if risk > 0.7 else "Good control"}