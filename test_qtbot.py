import cv2
from PyQt5.QtWidgets import QLabel

# In my original project, cv2 was used to read an image as numpy array.
# The array was then converted to pixmap and updated to QLabel.

def test_QLabel(qtbot):
    label = QLabel()
    label.show()
    qtbot.addWidget(label)
