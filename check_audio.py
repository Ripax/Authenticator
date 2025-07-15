from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QTimer
from pathlib import Path
import sys

app = QApplication([])

path = Path(__file__).parent / "sound" / "clip02.wav"
print("Exists:", path.exists())

effect = QSoundEffect()
effect.setSource(QUrl.fromLocalFile(str(path)))
effect.setVolume(0.9)
effect.play()

QTimer.singleShot(1500, app.quit)
app.exec_()
# QSoundEffect(qaudio): Error decoding source file:sound/click01.wav


