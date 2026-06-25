from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
from orchestrator.engine import dispatch

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenSceneFORCE V7")

        layout = QVBoxLayout()

        btn_safe = QPushButton("Run OBS In Safe Mode")
        btn_safe.clicked.connect(lambda: dispatch("SAFE_MODE"))

        btn_backup = QPushButton("Backup OBS")
        btn_backup.clicked.connect(lambda: dispatch("BACKUP"))

        btn_restore = QPushButton("Restore OBS")
        btn_restore.clicked.connect(lambda: dispatch("RESTORE"))

        btn_update = QPushButton("Update App")
        btn_update.clicked.connect(lambda: dispatch("UPDATE_APP"))

        btn_repair = QPushButton("Repair OBS")
        btn_repair.clicked.connect(lambda: dispatch("REPAIR_OBS"))

        for b in [btn_safe, btn_backup, btn_restore, btn_update, btn_repair]:
            layout.addWidget(b)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

def run_app():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
