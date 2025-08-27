#include "config.h"
#include "sensors/imu_mpu6000_spi.h"
#include "sensors/battery.h"
#include "sensors/rssi.h"
#include "storage/sd_card.h"
#include "storage/file_writer.h"
#include "protocols/blackbox_format.h"

void setup() {
  Serial.begin(115200);
  
  // Инициализация
  if (!IMU::init()) {
    Serial.println("IMU failed!");
    while (1);
  }

  if (!SDCard::init()) {
    Serial.println("SD init failed!");
    while (1);
  }

  // Создаём файл
  if (!FileWriter::open("FLIGHT001.BFL")) {
    Serial.println("Cannot create file!");
    while (1);
  }

  // Записываем заголовок
  FileWriter::writeHeader();
}

void loop() {
  static uint32_t lastLog = 0;
  uint32_t now = micros();

  // Цель: 2000 Гц (500 мкс)
  if (now - lastLog >= 500) {
    LogData data = {
      .time = now,
      .ax = IMU::ax,
      .ay = IMU::ay,
      .az = IMU::az,
      .gx = IMU::gx,
      .gy = IMU::gy,
      .gz = IMU::gz,
      .voltage = Battery::readVoltage(),
      .rssi = RSSI::read()
    };

    FileWriter::writeMain(&data);
    lastLog = now;
  }

  IMU::update();  // Обновляем IMU
}