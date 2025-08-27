#include <opencv2/objdetect.hpp>
#include "person_detector.h"

namespace AI {
  bool detectPerson(Mat& frame) {
    CascadeClassifier detector;
    detector.load("models/person.xml");
    std::vector<Rect> people;
    detector.detectMultiScale(frame, people, 1.1, 3);
    return !people.empty();
  }

  void followPerson() {
    // Получаем кадр с камеры (через DMA или SPI)
    Mat frame = Camera::capture();

    if (detectPerson(frame)) {
      // Вычисляем центр
      Point center = findCenterOfMass();
      // Отправляем команду на FC
      FC::setYaw(center.x - 320);
      FC::setThrottle(1500 + (480 - center.y)/2);
    }
  }
}