#pragma once

// === Пины ===
#define SD_CS_PIN       PA4     // SPI CS для SD
#define IMU_CS_PIN      PA3     // CS для MPU6000
#define BATTERY_PIN     A0      // Делитель напряжения
#define RSSI_PIN        A1      // Аналоговый RSSI

// === Настройки ===
#define LOG_RATE_HZ     2000    // Частота логирования
#define VBAT_SCALE      2.0     // Коэффициент делителя (например, 30k/150k)

// === Режимы ===
#define USE_MPU6000_SPI         // Использовать MPU6000 по SPI
// #define USE_MPU6050_I2C       // Или MPU6050 по I2C