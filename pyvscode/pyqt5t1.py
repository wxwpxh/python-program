import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

def show_message():
    QMessageBox.information(window, "提示", "按钮被点击了！")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 简单示例')
window.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout()

label = QLabel('欢迎使用 PyQt5!')
layout.addWidget(label)

button = QPushButton('点击我')
button.clicked.connect(show_message)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())