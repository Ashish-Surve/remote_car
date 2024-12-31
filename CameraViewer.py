import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, Qt

class CameraViewer(QWidget):
    def __init__(self, ip_address, port):
        super().__init__()
        self.ip_address = ip_address
        self.port = port
        
        # Create QLabel to display the camera feed
        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)  # Set the size of the label to match the camera feed

        # Create a QVBoxLayout to arrange the label
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Initialize the video capture
        self.video_capture = cv2.VideoCapture()
        self.video_capture.open(f"rtsp://{self.ip_address}:{self.port}/h264.sdp")

        # Set up a timer to update the camera feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 30)  # Update the frame every 30 milliseconds

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the OpenCV frame to a QImage
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            q_img = QPixmap.fromImage(QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888))

            # Set the QImage to the QLabel to display the frame
            self.label.setPixmap(q_img.scaled(self.label.size()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CameraViewer("192.168.1.6", 8080)  # Replace with your camera's IP address and port
    viewer.show()
    sys.exit(app.exec_())
