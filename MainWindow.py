from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTime
from ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.setup_ui()

    def setup_ui(self):
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.pauseButton.clicked.connect(self.pause)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.volumeSlider.valueChanged.connect(self.set_volume)
        self.ui.seekSlider.sliderMoved.connect(self.set_position)
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)

        self.ui.addToPlaylistButton.clicked.connect(self.add_to_playlist_dialog)
        self.ui.removeFromPlaylistButton.clicked.connect(self.remove_from_playlist)
        self.ui.clearPlaylistButton.clicked.connect(self.clear_playlist)
        self.ui.playPlaylistButton.clicked.connect(self.play_playlist_item)
        
        self.ui.playlistListWidget.itemClicked.connect(self.select_playlist_item)

        self.ui.playlistListWidget.setAcceptDrops(True)
        self.ui.playlistListWidget.setDragEnabled(True)
        self.ui.playlistListWidget.viewport().setAcceptDrops(True)
        self.ui.playlistListWidget.setDropIndicatorShown(True)
        self.ui.playlistListWidget.dragEnterEvent = self.playlist_drag_enter_event
        self.ui.playlistListWidget.dragMoveEvent = self.playlist_drag_move_event
        self.ui.playlistListWidget.dropEvent = self.playlist_drop_event
        self.ui.playlistListWidget.setObjectName("playlistListWidget")
        self.ui.playlistListWidget.setStyleSheet("""
                                                    QListWidget {
                                                        background-color: #F5F5F5;
                                                        border: 1px solid #CCCCCC;
                                                    }
                                                    
                                                    QListWidget::item {
                                                        padding: 5px;
                                                    }
                                                    
                                                    QListWidget::item:selected {
                                                        background-color: #C0C0C0;
                                                        color: #FFFFFF;
                                                    }
                                                """)


    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Song")
        if file_path:
            supported_formats = ["mp3", "wav", "ogg"]  # Add more formats if needed
            file_format = file_path.split(".")[-1]
            if file_format in supported_formats:
                self.player.stop()  # Stop the player before loading a new media
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
                self.ui.songLabel.setText(file_path)
            else:
                QMessageBox.warning(self, "Unsupported Format", "The selected file format is not supported.")


    def play(self):
        self.player.play()
        self.statusBar().showMessage("Playing: " + self.ui.songLabel.text())

    def pause(self):
        self.player.pause()
        self.statusBar().showMessage("Paused")

    def stop(self):
        self.player.stop()
        self.statusBar().clearMessage()

    def set_volume(self, value):
        self.player.setVolume(value)

    def set_position(self, value):
        self.player.setPosition(value)

    def update_position(self, position):
        self.ui.seekSlider.setValue(position)
        elapsed_time = QTime(0, 0).addMSecs(position)
        self.ui.elapsedLabel.setText(elapsed_time.toString("mm:ss"))

    def update_duration(self, duration):
        self.ui.seekSlider.setMaximum(duration)
        total_time = QTime(0, 0).addMSecs(duration)
        self.ui.totalLabel.setText(total_time.toString("mm:ss"))

    def add_to_playlist(self, file_path):
        self.ui.playlistListWidget.addItem(file_path)

    def remove_from_playlist(self):
        selected_item = self.ui.playlistListWidget.currentItem()
        if selected_item is not None:
            self.ui.playlistListWidget.takeItem(self.ui.playlistListWidget.row(selected_item))

    def clear_playlist(self):
        self.ui.playlistListWidget.clear()

    def play_playlist_item(self):
        selected_item = self.ui.playlistListWidget.currentItem()
        if selected_item is not None:
            file_path = selected_item.text()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.ui.songLabel.setText(file_path)
            self.player.play()

    def add_to_playlist_dialog(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Add to Playlist")
        for file_path in file_paths:
            self.add_to_playlist(file_path)
            
    def select_playlist_item(self, item):
        file_path = item.text()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.ui.songLabel.setText(file_path)
        self.player.play()
    def playlist_drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def playlist_drag_move_event(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def playlist_drop_event(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            file_paths = [url.toLocalFile() for url in event.mimeData().urls()]
            for file_path in file_paths:
                self.add_to_playlist(file_path)
        else:
            event.ignore()