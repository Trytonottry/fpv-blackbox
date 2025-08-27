import torch
import torch.nn as nn
import numpy as np

# Симуляция данных: хорошие и плохие полёты
data = np.random.randn(1000, 50, 7)  # 1000 полётов, 50 точек, 7 параметров
labels = np.random.rand(1000) > 0.5  # 0 = плавно, 1 = рывки

X = torch.tensor(data, dtype=torch.float32)
y = torch.tensor(labels, dtype=torch.float32).unsqueeze(1)

model = PilotErrorDetector()
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(100):
    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

torch.save(model.state_dict(), "backend/models/error_detector.pth")