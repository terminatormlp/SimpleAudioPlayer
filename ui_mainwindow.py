from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.songLabel = QtWidgets.QLabel(self.centralwidget)
        self.songLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songLabel.setObjectName("songLabel")
        self.verticalLayout.addWidget(self.songLabel)
        self.seekSlider = QtWidgets.QSlider(self.centralwidget)
        self.seekSlider.setOrientation(QtCore.Qt.Horizontal)
        self.seekSlider.setObjectName("seekSlider")
        self.seekSlider.setStyleSheet("""
        QSlider::groove:horizontal {
            background-color: #CCCCCC;
            height: 4px;
        }
        
        QSlider::handle:horizontal {
            background-color: #666666;
            width: 10px;
            margin: -8px 0;
            border-radius: 5px;
        }
    """)
        self.verticalLayout.addWidget(self.seekSlider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.verticalLayout.addWidget(self.volumeSlider)
        self.elapsedLabel = QtWidgets.QLabel(self.centralwidget)
        self.elapsedLabel.setObjectName("elapsedLabel")
        self.verticalLayout.addWidget(self.elapsedLabel)
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout.addWidget(self.totalLabel)
        self.playlistListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.playlistListWidget.setObjectName("playlistListWidget")
        self.verticalLayout.addWidget(self.playlistListWidget)
        self.addToPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToPlaylistButton.setObjectName("addToPlaylistButton")
        self.horizontalLayout.addWidget(self.addToPlaylistButton)
        self.removeFromPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeFromPlaylistButton.setObjectName("removeFromPlaylistButton")
        self.horizontalLayout.addWidget(self.removeFromPlaylistButton)
        self.clearPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearPlaylistButton.setObjectName("clearPlaylistButton")
        self.horizontalLayout.addWidget(self.clearPlaylistButton)
        self.playPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.playPlaylistButton.setObjectName("playPlaylistButton")
        self.horizontalLayout.addWidget(self.playPlaylistButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.apply_stylesheet()

    def apply_stylesheet(self):
        style_sheet = """
            QMainWindow {
                background-color: #F0F0F0;
            }
            
            QLabel {
                color: #333333;
                font-size: 14px;
            }
            
            QSlider {
                background-color: #DDDDDD;
                height: 8px;
            }
            
            QSlider::groove:horizontal {
                background-color: #CCCCCC;
            }
            
            QSlider::handle:horizontal {
                background-color: #666666;
                width: 16px;
                margin: -4px 0;
                border-radius: 8px;
            }
            
            QPushButton {
                background-color: #DDDDDD;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            
            QPushButton:hover {
                background-color: #CCCCCC;
            }
            
            QPushButton:pressed {
                background-color: #AAAAAA;
            }
        """
        self.centralwidget.setStyleSheet(style_sheet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.songLabel.setText(_translate("MainWindow", "No song selected"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.elapsedLabel.setText(_translate("MainWindow", "00:00"))
        self.totalLabel.setText(_translate("MainWindow", "00:00"))
        self.addToPlaylistButton.setText(_translate("MainWindow", "Add to Playlist"))
        self.removeFromPlaylistButton.setText(_translate("MainWindow", "Remove from Playlist"))
        self.clearPlaylistButton.setText(_translate("MainWindow", "Clear Playlist"))
        self.playPlaylistButton.setText(_translate("MainWindow", "Play Playlist"))
