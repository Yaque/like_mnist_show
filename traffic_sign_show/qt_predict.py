from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import time

from keras.models import load_model

from predict import predict

"""
    Note:
        in the emit message, can't having ':'.
        
"""


class Predicter(QThread):
    sinOut = pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self, parent=None):
        super(Predicter, self).__init__(parent)
        self.image_path = ""
        self.working = True

        # load the trained convolutional neural network
        # print("[INFO] loading network...")
        # self.model = load_model("ckpt/traffic_sign.model")

        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    # def send_image_path(self, image_path):
    #     self.image_path = image_path

    def run(self):
        self.sinOut.emit("R:正在分析中\n请稍后。。。\n")
        response = predict(self.image_path, True)
        self.sinOut.emit("P:类型\t{}\n当前时间\t{}\n".format(response, time.localtime()))
        self.sinOut.emit("I:image/save.png")
