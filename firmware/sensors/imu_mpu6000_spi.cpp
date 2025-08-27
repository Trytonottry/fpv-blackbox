#include <SPI.h>
#include "imu_mpu6000_spi.h"
#include "config.h"

SPISettings spiSettings(10000000, MSBFIRST, SPI_MODE0);

namespace IMU {
  int16_t ax, ay, az, gx, gy, gz;
  float temperature;

  bool init() {
    pinMode(IMU_CS_PIN, OUTPUT);
    digitalWrite(IMU_CS_PIN, HIGH);
    SPI.begin();

    // Сброс
    writeReg(0x6B, 0x80);  // PWR_MGMT_1 = reset
    delay(100);
    writeReg(0x6B, 0x01);  // Включить датчик
    writeReg(0x19, 0x07);  // Sample rate divider
    writeReg(0x1A, 0x03);  // DLPF_CFG = 44Hz
    writeReg(0x1B, 0x08);  // Gyro ±500 dps
    writeReg(0x1C, 0x10);  // Accel ±8g

    return readReg(0x75) == 0x98;  // WHO_AM_I
  }

  void update() {
    uint8_t buffer[14];
    readRegisters(0x3B, buffer, 14);

    ax = ((buffer[0] << 8) | buffer[1]);
    ay = ((buffer[2] << 8) | buffer[3]);
    az = ((buffer[4] << 8) | buffer[5]);
    temperature = ((buffer[6] << 8) | buffer[7]) / 340.0 + 36.53;
    gx = ((buffer[8] << 8) | buffer[9]);
    gy = ((buffer[10] << 8) | buffer[11]);
    gz = ((buffer[12] << 8) | buffer[13]);
  }

  void writeReg(uint8_t reg, uint8_t value) {
    digitalWrite(IMU_CS_PIN, LOW);
    SPI.transfer(reg & 0x7F);
    SPI.transfer(value);
    digitalWrite(IMU_CS_PIN, HIGH);
  }

  uint8_t readReg(uint8_t reg) {
    digitalWrite(IMU_CS_PIN, LOW);
    SPI.transfer(reg | 0x80);
    uint8_t result = SPI.transfer(0x00);
    digitalWrite(IMU_CS_PIN, HIGH);
    return result;
  }

  void readRegisters(uint8_t reg, uint8_t* buffer, uint8_t count) {
    digitalWrite(IMU_CS_PIN, LOW);
    SPI.transfer(reg | 0x80);
    for (int i = 0; i < count; i++) {
      buffer[i] = SPI.transfer(0x00);
    }
    digitalWrite(IMU_CS_PIN, HIGH);
  }
}