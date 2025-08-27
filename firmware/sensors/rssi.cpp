#include "rssi.h"
#include "config.h"

namespace RSSI {
  uint8_t read() {
    int raw = analogRead(RSSI_PIN);
    return (uint8_t)(raw * (100.0 / 4095.0));  // 0-100%
  }
}