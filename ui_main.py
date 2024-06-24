from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(817, 542)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
" background-color: #ECECEC;\n"
"}")
        MainWindow.setFixedSize(817, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.plot_widget = QWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(10, 50, 511, 451))
        self.plot_widget.setStyleSheet(u"QWidget {\n"
"	color: #333;\n"
"    border: 3px solid #555;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"      cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"      radius: 1.35, stop: 0 #f0f0f0, stop: 1 #dddddd\n"
"      );\n"
"   \n"
"    }\n"
"\n"
"")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(560, 390, 101, 41))
        self.start_button.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(560, 460, 101, 41))
        self.save_button.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        self.min_text_browser = QTextBrowser(self.centralwidget)
        self.min_text_browser.setObjectName(u"min_text_browser")
        self.min_text_browser.setGeometry(QRect(630, 50, 161, 41))
        self.min_text_browser.setStyleSheet(u"QTextBrowser{\n"
"	border: 2px solid #555;\n"
"    border-style: outset;\n"
"}")
        self.max_text_browser = QTextBrowser(self.centralwidget)
        self.max_text_browser.setObjectName(u"max_text_browser")
        self.max_text_browser.setGeometry(QRect(630, 130, 161, 41))
        self.max_text_browser.setStyleSheet(u"QTextBrowser{\n"
"	border: 2px solid #555;\n"
"    border-style: outset;\n"
"}")
        self.avg_text_browser = QTextBrowser(self.centralwidget)
        self.avg_text_browser.setObjectName(u"avg_text_browser")
        self.avg_text_browser.setGeometry(QRect(630, 210, 161, 41))
        self.avg_text_browser.setStyleSheet(u"QTextBrowser{\n"
"	border: 2px solid #555;\n"
"    border-style: outset;\n"
"}")
        self.scale_text_browser = QTextBrowser(self.centralwidget)
        self.scale_text_browser.setObjectName(u"scale_text_browser")
        self.scale_text_browser.setGeometry(QRect(630, 290, 161, 41))
        self.scale_text_browser.setStyleSheet(u"QTextBrowser{\n"
"	border: 2px solid #555;\n"
"    border-style: outset;\n"
"}")
        self.clean_button = QPushButton(self.centralwidget)
        self.clean_button.setObjectName(u"clean_button")
        self.clean_button.setGeometry(QRect(690, 390, 101, 41))
        self.clean_button.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        self.info_button = QPushButton(self.centralwidget)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(690, 460, 101, 41))
        self.info_button.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        self.min_label = QLabel(self.centralwidget)
        self.min_label.setObjectName(u"min_label")
        self.min_label.setGeometry(QRect(550, 60, 71, 21))
        self.min_label.setStyleSheet(u"QLabel{\n"
"color: #333;\n"
"font-size: 15px;\n"
"}")
        self.max_label = QLabel(self.centralwidget)
        self.max_label.setObjectName(u"max_label")
        self.max_label.setGeometry(QRect(550, 140, 71, 21))
        self.max_label.setStyleSheet(u"QLabel{\n"
"color: #333;\n"
"font-size: 15px;\n"
"}")
        self.avg_label = QLabel(self.centralwidget)
        self.avg_label.setObjectName(u"avg_label")
        self.avg_label.setGeometry(QRect(550, 220, 61, 21))
        self.avg_label.setStyleSheet(u"QLabel{\n"
"color: #333;\n"
"font-size: 15px;\n"
"}")
        self.scale_label = QLabel(self.centralwidget)
        self.scale_label.setObjectName(u"scale_label")
        self.scale_label.setGeometry(QRect(550, 300, 51, 21))
        self.scale_label.setStyleSheet(u"QLabel{\n"
"font-size: 15px;\n"
"color: #333;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.plot_widget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>QWidget {</p><p>    color: #333;</p><p>    border: 2px solid #555;</p><p>    border-style: outset;</p><p>    }</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.clean_button.setText(QCoreApplication.translate("MainWindow", u"Clean Plot", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.min_label.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.max_label.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.avg_label.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.scale_label.setText(QCoreApplication.translate("MainWindow", u"Scale", None))
    # retranslateUi
