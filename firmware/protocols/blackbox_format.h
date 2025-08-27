#pragma once
// Основные типы фреймов:
// 0x00 — Main frame (IMU, voltage)
// 0x20 — Slow frame (GPS, baro)
// 0x30 — Event frame
// 0x80 — Intraframe (keyframe)

// Подробнее: https://github.com/betaflight/blackbox/wiki/Blackbox-file-format