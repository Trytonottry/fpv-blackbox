#pragma once
namespace IMU {
  extern int16_t ax, ay, az, gx, gy, gz;
  extern float temperature;

  bool init();
  void update();
  void writeReg(uint8_t reg, uint8_t value);
  uint8_t readReg(uint8_t reg);
  void readRegisters(uint8_t reg, uint8_t* buffer, uint8_t count);
}