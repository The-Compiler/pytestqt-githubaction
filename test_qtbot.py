import cv2
from PyQt5.QtWidgets import QLabel

def test_QLabel(qtbot):
    label = QLabel()
    label.show()
    qtbot.addWidget(label)
