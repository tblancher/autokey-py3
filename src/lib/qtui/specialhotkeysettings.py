#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from specialhotkeysettings.ui on Sun Mar  4 11:39:40 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(531, 397)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.monitorKeyLabel = QtGui.QLabel(self.groupBox)
        self.monitorKeyLabel.setObjectName(_fromUtf8("monitorKeyLabel"))
        self.horizontalLayout_2.addWidget(self.monitorKeyLabel)
        spacerItem = QtGui.QSpacerItem(269, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.setMonitorButton = KPushButton(self.groupBox)
        self.setMonitorButton.setObjectName(_fromUtf8("setMonitorButton"))
        self.horizontalLayout_2.addWidget(self.setMonitorButton)
        self.clearMonitorButton = KPushButton(self.groupBox)
        self.clearMonitorButton.setObjectName(_fromUtf8("clearMonitorButton"))
        self.horizontalLayout_2.addWidget(self.clearMonitorButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.configKeyLabel = QtGui.QLabel(self.groupBox_2)
        self.configKeyLabel.setObjectName(_fromUtf8("configKeyLabel"))
        self.horizontalLayout.addWidget(self.configKeyLabel)
        spacerItem1 = QtGui.QSpacerItem(269, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.setConfigButton = KPushButton(self.groupBox_2)
        self.setConfigButton.setObjectName(_fromUtf8("setConfigButton"))
        self.horizontalLayout.addWidget(self.setConfigButton)
        self.clearConfigButton = KPushButton(self.groupBox_2)
        self.clearConfigButton.setObjectName(_fromUtf8("clearConfigButton"))
        self.horizontalLayout.addWidget(self.clearConfigButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtGui.QSpacerItem(20, 224, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.groupBox.setTitle(kdecore.i18n(_fromUtf8("Toggle monitoring using a hotkey")))
        self.label.setText(kdecore.i18n(_fromUtf8("Hotkey: ")))
        self.monitorKeyLabel.setText(kdecore.i18n(_fromUtf8("$hotkey")))
        self.setMonitorButton.setText(kdecore.i18n(_fromUtf8("Set")))
        self.clearMonitorButton.setText(kdecore.i18n(_fromUtf8("Clear")))
        self.groupBox_2.setTitle(kdecore.i18n(_fromUtf8("Show configuration window using a hotkey")))
        self.label_2.setText(kdecore.i18n(_fromUtf8("Hotkey: ")))
        self.configKeyLabel.setText(kdecore.i18n(_fromUtf8("$hotkey")))
        self.setConfigButton.setText(kdecore.i18n(_fromUtf8("Set")))
        self.clearConfigButton.setText(kdecore.i18n(_fromUtf8("Clear")))

from PyKDE4.kdeui import KPushButton
