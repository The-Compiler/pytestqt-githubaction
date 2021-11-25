import cv2
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QStyle, QVBoxLayout, QWidget)

def test_QLabel(qtbot):
    label = QLabel()
    label.show()
    qtbot.addWidget(label)
