# 🛩️ FPV Blackbox Analyzer
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Trytonottry/fpv-blackbox?style=social)](https://github.com/Trytonottry/fpv-blackbox)
[![GitHub Issues](https://img.shields.io/github/issues/Trytonottry/fpv-blackbox)](https://github.com/Trytonottry/fpv-blackbox/issues)
[![GitHub Forks](https://img.shields.io/github/forks/Trytonottry/fpv-blackbox?style=social)](https://github.com/Trytonottry/fpv-blackbox)

**Open-source система анализа полётов FPV-дронов**  
Загружайте `.bfl`-логи, синхронизируйте с видео, анализируйте траекторию, получайте AI-советы и экспортируйте отчёты.

---

## 🎯 Функции

- ✅ Парсинг `.bfl`, `.tlog`, `.csv`
- ✅ 3D-визуализация траектории (Three.js)
- ✅ Синхронизация видео и телеметрии
- ✅ AI-анализ пилотирования (нейросеть)
- ✅ Экспорт в CSV, GPX, PDF
- ✅ Голосовое управление (Vosk)
- ✅ WebSocket для live telemetry
- ✅ Поддержка Betaflight, iNav, ArduPilot
- ✅ Docker и автономный запуск

---

## 🏁 Быстрый старт

### 1. Запуск через Docker (рекомендуется)

```bash
git clone https://github.com/Trytonottry/fpv-blackbox.git
cd fpv-blackbox
docker-compose up --build -d
```
Откройте:
🌐 http://localhost:3000 

## 🧩 Технологии
Backend - Python, FastAPI, SQLAlchemy, PyTorch
Frontend - Vue 3, Three.js, Chart.js
Firmware - C++ (STM32/Arduino), SPI/I2C
Визуализация - 3D WebGL, OpenCV
Сборка - Docker, Docker Compose
CI/CD - GitHub Actions

## 🙌 Благодарности 

    Betaflight  — за open-source прошивку
    Blackbox Parser  — за парсер
    Three.js  — за 3D
    Vosk  — за офлайн-распознавание речи
     
## 📄 Лицензия 

MIT — см. LICENSE  
