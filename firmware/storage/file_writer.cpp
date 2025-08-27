#include "file_writer.h"
#include "sd_card.h"
#include <SD.h>

File logFile;

namespace FileWriter {
  bool open(const char* filename) {
    logFile = SD.open(filename, FILE_WRITE);
    return logFile;
  }

  void writeHeader() {
    logFile.write("H product:FPV Blackbox Logger v1.0\n");
    logFile.write("H format:1\n");
    logFile.write("H time:0\n");
    logFile.write("F 2000\n");  // 2 кГц
    logFile.write("I 0 0 0 0 0 0 0 0 0\n");  // Initial frame
  }

  void writeMain(LogData* data) {
    uint8_t buffer[29];
    int p = 0;

    // Main frame (type 0)
    buffer[p++] = 0x00;  // Frame start

    // time (varint)
    p += writeVarInt(buffer + p, data->time);

    // gyro & accel
    buffer[p++] = data->gx >> 8; buffer[p++] = data->gx;
    buffer[p++] = data->gy >> 8; buffer[p++] = data->gy;
    buffer[p++] = data->gz >> 8; buffer[p++] = data->gz;
    buffer[p++] = data->ax >> 8; buffer[p++] = data->ax;
    buffer[p++] = data->ay >> 8; buffer[p++] = data->ay;
    buffer[p++] = data->az >> 8; buffer[p++] = data->az;

    // voltage (scaled)
    uint16_t vbat = (uint16_t)(data->voltage * 100);
    buffer[p++] = vbat >> 8; buffer[p++] = vbat;

    // RSSI
    buffer[p++] = data->rssi;

    logFile.write(buffer, p);
  }

  int writeVarInt(uint8_t* buf, uint32_t value) {
    int count = 0;
    do {
      uint8_t byte = value & 0x7F;
      value >>= 7;
      if (value) byte |= 0x80;
      buf[count++] = byte;
    } while (value);
    return count;
  }
}