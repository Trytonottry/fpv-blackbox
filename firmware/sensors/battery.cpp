#include "battery.h"
#include "config.h"

namespace Battery {
  float readVoltage() {
    int raw = analogRead(BATTERY_PIN);
    return raw * (3.3 / 4095.0) * VBAT_SCALE;  // Для STM32 (12-bit ADC)
  }
}