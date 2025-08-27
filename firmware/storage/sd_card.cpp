#include <SD.h>
#include "sd_card.h"
#include "config.h"

namespace SDCard {
  bool init() {
    return SD.begin(SD_CS_PIN);
  }
}