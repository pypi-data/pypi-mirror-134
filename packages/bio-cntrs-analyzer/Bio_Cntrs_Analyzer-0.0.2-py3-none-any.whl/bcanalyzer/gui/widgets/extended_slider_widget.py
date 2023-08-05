from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QSlider, QSpinBox, QLabel
from PyQt5.QtWidgets import QHBoxLayout


class ExtendedSliderWidget(QWidget):
    valueChanged = pyqtSignal(int)

    def __init__(self, text="", parent=None) -> None:
        super().__init__(parent)
        self._text = text
        self.initUI()
        self.initSignals()

    def initUI(self):
        self._root_layout = QHBoxLayout()

        self.caption = QLabel(self._text)

        self.slider = QSlider()
        self.slider.setRange(0, 100)
        self.slider.setOrientation(Qt.Horizontal)

        self.value_spinbox = QSpinBox()
        self.value_spinbox.setRange(0, 100)

        self._root_layout.addWidget(self.caption)
        self._root_layout.addWidget(self.slider)
        self._root_layout.addWidget(self.value_spinbox)

        self.setLayout(self._root_layout)

    def value(self):
        return self.value_spinbox.value()

    def set_range(self, mininum: int, maximum: int):
        self.slider.setRange(mininum, maximum)
        self.value_spinbox.setRange(mininum, maximum)

    def set_value(self, new_value: int):
        self.value_spinbox.setValue(new_value)
        self.slider.setValue(new_value)

    def initSignals(self):
        self.slider.valueChanged.connect(self.slider_change_value_handler)
        self.value_spinbox.valueChanged.connect(self.text_change_value_handler)

    def slider_change_value_handler(self, new_value: int):
        self.value_spinbox.setValue(new_value)
        self.valueChanged.emit(new_value)

    def text_change_value_handler(self, new_value: int):
        self.slider.setValue(new_value)
        self.valueChanged.emit(new_value)
