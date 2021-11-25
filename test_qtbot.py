from PyQt5.QtWidgets import QLabel
import cv2

# In my original project, cv2 was imported to read an image as numpy
# array. The array was then converted to pixmap and updated to QLabel,
# which was tested.

def test_QLabel(qtbot):
    label = QLabel()
    label.show()
    qtbot.addWidget(label)
