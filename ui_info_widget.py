from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect, QSize, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(663, 300)
        Form.setStyleSheet(u"QWidget {\n"
                           "background-color: #ECECEC\n"
                           "}")
        Form.setFixedSize(663, 300)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 641, 271))

        self.layout = QVBoxLayout(self.widget)
        self.layout.setObjectName(u"layout")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        pixmap = QPixmap(":/db.png")
        self.label.setPixmap(pixmap)

        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)

        self.layout.addWidget(self.label)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))


    def show_info_widget(self):
        self.info_widget = QWidget()
        self.ui_info_widget = Ui_Form()
        self.ui_info_widget.setupUi(self.info_widget)
        self.info_widget.show()

