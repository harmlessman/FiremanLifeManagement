# Copyright 2022 Junyong Lee(@harmlessman)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QDateTime, Qt
from   PyQt5.QtWidgets import *
from   PyQt5.QtGui     import *
from   PyQt5.QtCore    import *
import datetime
import sys
import os
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("untitled.ui")
form_class = uic.loadUiType(form)[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        count = 0
        self.m1 = QMovie("normal_beat.gif")
        self.m1.setScaledSize(QSize(300,80))
        self.l1.setMovie(self.m1)
        self.l1.show()

        self.m2 = QMovie("normal2_beat.gif")
        self.m2.setScaledSize(QSize(300,80))
        self.l2.setMovie(self.m2)
        self.l2.show()

        self.m3 = QMovie("warn_beat.gif")
        self.m3.setScaledSize(QSize(300, 80))
        self.l3.setMovie(self.m3)
        self.l3.show()

        self.m4 = QMovie("normal3_beat.gif")
        self.m4.setScaledSize(QSize(300, 80))
        self.l4.setMovie(self.m4)
        self.l4.show()

        self.m5 = QMovie("normal_beat.gif")
        self.m5.setScaledSize(QSize(300, 80))
        self.l5.setMovie(self.m5)
        self.l5.show()

        self.m6 = QMovie("warn_beat.gif")
        self.m6.setScaledSize(QSize(300, 80))
        self.l6.setMovie(self.m6)
        self.l6.show()

        self.m7 = QMovie("normal2_beat.gif")
        self.m7.setScaledSize(QSize(300, 80))
        self.l7.setMovie(self.m7)
        self.l7.show()

        self.m8 = QMovie("normal3_beat.gif")
        self.m8.setScaledSize(QSize(300, 80))
        self.l8.setMovie(self.m8)
        self.l8.show()
        self.startAnimation()

        self.t1 = QTime(0, 10, 0)
        self.t2 = QTime(0, 15, 20)
        self.t3 = QTime(0, 45, 14)
        self.t4 = QTime(0, 9, 0)
        self.t5 = QTime(0, 20, 0)
        self.t6 = QTime(0, 35, 35)
        self.t7 = QTime(0, 10, 1)
        self.t8 = QTime(0, 20, 12)



        # timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        self.datetime = QDateTime.currentDateTime()
        self.initUI()

        self.t3time = ""

        self.colortimer1 = QTimer(self)
        self.colortimer2 = QTimer(self)
        self.colortimer3 = QTimer(self)
        self.colortimer1.start(1000)
        self.colortimer2.start(1000)
        self.colortimer3.start(1000)
        self.colortimer1.timeout.connect(self.ct1)
        self.colortimer2.timeout.connect(self.ct2)
        self.colortimer3.timeout.connect(self.ct3)

        #self.alram_1.setHtml('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ffff00"></td><td bgcolor="#ffff00"></td></tr></table></body></html>')












        self.pb1.clicked.connect(self.bt1)
        self.pb2.clicked.connect(self.bt2)
        self.pb3.clicked.connect(self.bt3)
        self.pb4.clicked.connect(self.bt4)
        self.pb5.clicked.connect(self.bt5)
        self.pb6.clicked.connect(self.bt6)
        self.pb7.clicked.connect(self.bt7)
        self.pb8.clicked.connect(self.bt8)




        self.emergency.clicked.connect(self.emerbutton)
        self.show()

        # Start Animation


    def startAnimation(self):
        self.m1.start()
        self.m2.start()
        self.m3.start()
        self.m4.start()
        self.m5.start()
        self.m6.start()
        self.m7.start()
        self.m8.start()

    def initUI(self):
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleShortDate)+"      prototype      made by 이준용 ")
        self.setWindowTitle('종합 상황판')
        '''        
        self.time.setText(self.datetime.toString(Qt.DefaultLocaleShortDate))
        self.time.setStyleSheet(' font-size:16pt; font-weight:600; color:white; align=center')
        '''
        #self.setGeometry(500, 500, 300, 200)
        self.show()

    def timeout(self):
        now = datetime.datetime.now()
        self.time.setText(str(now.strftime('%Y-%m-%d %H:%M:%S')))
        self.time.setStyleSheet(' font-size:16pt; font-weight:600; color:white; align:center')
        self.time.setAlignment(Qt.AlignCenter)

    def changecolor(self):
        a = [self.alram_1, self.alram_2]
        now = datetime.datetime.now()
        random.choice(a).setHtml(f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ffff00"></td><td><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{str(now.strftime("%H:%M:%S"))}</p></td></tr></table></body></html>')

    def ct1(self):
        self.t1 = self.t1.addSecs(1)
        self.t4 = self.t4.addSecs(1)
        self.t7 = self.t7.addSecs(1)
        list = [self.alram_1, self.alram_4, self.alram_7]
        abc1 = [self.gg(self.t1.toString("hh:mm:ss")), self.gy(self.t1.toString("hh:mm:ss")), self.yg(self.t1.toString("hh:mm:ss"))]
        abc2 = [self.gg(self.t4.toString("hh:mm:ss")), self.gy(self.t4.toString("hh:mm:ss")), self.yg(self.t4.toString("hh:mm:ss"))]
        abc3 = [self.gg(self.t7.toString("hh:mm:ss")), self.gy(self.t7.toString("hh:mm:ss")), self.yg(self.t7.toString("hh:mm:ss"))]
        #random.choice(list).setHtml(random.choice(abc))

        self.alram_1.setHtml(random.choice(abc1))
        self.alram_4.setHtml(random.choice(abc2))
        self.alram_7.setHtml(random.choice(abc3))

    def ct2(self):
        self.t2 = self.t2.addSecs(1)
        self.t5 = self.t5.addSecs(1)
        self.t8 = self.t8.addSecs(1)
        list=[self.alram_2, self.alram_5, self.alram_8]
        abc1 = [self.gg(self.t2.toString("hh:mm:ss")), self.gy(self.t2.toString("hh:mm:ss")), self.yg(self.t2.toString("hh:mm:ss"))]
        abc2 = [self.gg(self.t5.toString("hh:mm:ss")), self.gy(self.t5.toString("hh:mm:ss")), self.yg(self.t5.toString("hh:mm:ss"))]
        abc3 = [self.gg(self.t8.toString("hh:mm:ss")), self.gy(self.t8.toString("hh:mm:ss")), self.yg(self.t8.toString("hh:mm:ss"))]
        #random.choice(list).setHtml(random.choice(abc))
        self.alram_2.setHtml(random.choice(abc1))
        self.alram_5.setHtml(random.choice(abc2))
        self.alram_8.setHtml(random.choice(abc3))
    def ct3(self):
        self.t3 = self.t3.addSecs(1)
        self.t6 = self.t6.addSecs(1)
        list=[self.alram_3, self.alram_6]
        abc1=[self.rr(self.t3.toString("hh:mm:ss")), self.rg(self.t3.toString("hh:mm:ss")), self.ry(self.t3.toString("hh:mm:ss")), self.yy(self.t3.toString("hh:mm:ss")), self.yr(self.t3.toString("hh:mm:ss")), self.gr(self.t3.toString("hh:mm:ss"))]
        abc2 = [self.rr(self.t6.toString("hh:mm:ss")), self.rg(self.t6.toString("hh:mm:ss")), self.ry(self.t6.toString("hh:mm:ss")), self.yy(self.t6.toString("hh:mm:ss")), self.yr(self.t6.toString("hh:mm:ss")), self.gr(self.t6.toString("hh:mm:ss"))]
        #random.choice(list).setHtml(random.choice(abc))
        self.alram_3.setHtml(random.choice(abc1))
        self.alram_6.setHtml(random.choice(abc2))
        self.t3time=self.t3.toString("hh:mm:ss")


    def active_time_e(self):
        self.atime = self.atime.addSecs(1)
        print(self.atime.toString("hh:mm:ss"))


    def gg(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#008000"></td><td bgcolor="#008000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def gy(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#008000"></td><td bgcolor="#ffff00"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def gr(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#008000"></td><td bgcolor="#ff0000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def yg(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#008000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def yy(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ffff00"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def yr(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ff0000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def rg(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#008000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def ry(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#ffff00"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
    def rr(self, t):
        return f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#ff0000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{t}</p></td></tr></table></body></html>'
















    '''    
    self.gy = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#008000"></td><td bgcolor="#ffff00"></td><td ></td></tr></table></body></html>'
    self.gr = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#008000"></td><td bgcolor="#ff0000"></td><td ></td></tr></table></body></html>'
    self.yg = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#008000"></td><td ></td></tr></table></body></html>'
    self.yy = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ffff00"></td><td ></td></tr></table></body></html>'
    self.yr = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ffff00"></td><td bgcolor="#ff0000"></td><td ></td></tr></table></body></html>'
    self.rg = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#008000"></td><td ></td></tr></table></body></html>'
    self.ry = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#ffff00"></td><td ></td></tr></table></body></html>'
    self.rr = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동량</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#ff0000"></td><td ></td></tr></table></body></html>'
    '''
    #human data open triger(button)
    def bt1(self):
        sw = s1()
        sw.exec_()

    def bt2(self):
        sw = s2()
        sw.exec_()

    def bt3(self):
        sw = s3()
        sw.exec_()

    def bt4(self):
        sw = s4()
        sw.exec_()

    def bt5(self):
        sw = s5()
        sw.exec_()

    def bt6(self):
        sw = s6()
        sw.exec_()

    def bt7(self):
        sw = s7()
        sw.exec_()

    def bt8(self):
        sw = s8()
        sw.exec_()


    def emerbutton(self):
        self.w_3.setText("위험")
        self.w_3.setStyleSheet(' font-size:16pt; font-weight:600; color:white; background:red')
        self.w_3.setAlignment(Qt.AlignCenter)
        sw = emer(self.t3time)
        sw.exec_()

# human data ui
class s1(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("1.ui", self)
        self.show()
class s2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("2.ui", self)
        self.show()
class s3(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("3.ui", self)
        self.show()
class s4(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("4.ui", self)
        self.show()
class s5(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("5.ui", self)
        self.show()
class s6(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("6.ui", self)
        self.show()
class s7(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("7.ui", self)
        self.show()
class s8(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("8.ui", self)
        self.show()






class emer(QDialog):
    def __init__(self, t3time):
        super().__init__()
        self.t3time = t3time
        print(f't3time = > {self.t3time}')
        self.ui = uic.loadUi("emer.ui", self)
        self.initUI()

    def initUI(self):
        self.emerbox = QTextBrowser(self)
        self.emerbox.setHtml(
            f'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li  white-space: pre-wrap; </style></head><body style=" font-family:"Gulim"; font-size:9pt; font-weight:400; font-style:normal;"><table border="1" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;" width="100%" cellspacing="5" cellpadding="0"><tr><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">심박수</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">SpO</span><span style=" font-weight:600; background-color:#ffffff; vertical-align:sub;">2</span></p></td><td bgcolor="#ffffff"><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; background-color:#ffffff;">활동시간</span></p></td></tr><tr><td bgcolor="#ff0000"></td><td bgcolor="#ff0000"></td><td ><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{self.t3time}</p></td></tr></table></body></html>'
            )
        self.setGeometry(600,400,600,300)
        self.emerbox.setGeometry(60,130,230,70)
        self.show()


'''
f = uic.loadUiType("emer.ui")[0]

class sec(QDialog, QWidget, f):
    def __init__(self):
        super(sec, self).__init__()
        self.setupUi(self)
        self.m4 = QMovie("normal3_beat.gif")
        self.m4.setScaledSize(QSize(300, 80))


        self.initUI()

    def initUI(self):
        #self.ui = uic.loadUi("emer.ui", self)

        pass
'''

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()



