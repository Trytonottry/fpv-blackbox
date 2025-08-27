#pragma once

struct LogData {
  uint32_t time;
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
  float voltage;
  uint8_t rssi;
};

namespace FileWriter {
  bool open(const char* filename);
  void writeHeader();
  void writeMain(LogData* data);
  int writeVarInt(uint8_t* buf, uint32_t value);
}