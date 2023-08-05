# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dxvk.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_DxvkSettings(object):
    def setupUi(self, DxvkSettings):
        DxvkSettings.setObjectName("DxvkSettings")
        self.dxvk_layout = QtWidgets.QGridLayout(DxvkSettings)
        self.dxvk_layout.setObjectName("dxvk_layout")
        self.gb_dxvk_options = QtWidgets.QGroupBox(DxvkSettings)
        self.gb_dxvk_options.setObjectName("gb_dxvk_options")
        self.layout_dxvk_options = QtWidgets.QGridLayout(self.gb_dxvk_options)
        self.layout_dxvk_options.setObjectName("layout_dxvk_options")
        self.version = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.version.setObjectName("version")
        self.layout_dxvk_options.addWidget(self.version, 0, 2, 1, 1)
        self.fps = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.fps.setObjectName("fps")
        self.layout_dxvk_options.addWidget(self.fps, 1, 0, 1, 1)
        self.memory = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.memory.setObjectName("memory")
        self.layout_dxvk_options.addWidget(self.memory, 0, 1, 1, 1)
        self.devinfo = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.devinfo.setObjectName("devinfo")
        self.layout_dxvk_options.addWidget(self.devinfo, 0, 0, 1, 1)
        self.gpuload = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.gpuload.setObjectName("gpuload")
        self.layout_dxvk_options.addWidget(self.gpuload, 1, 1, 1, 1)
        self.frametime = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.frametime.setObjectName("frametime")
        self.layout_dxvk_options.addWidget(self.frametime, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_dxvk_options.addItem(spacerItem, 0, 3, 3, 1)
        self.api = QtWidgets.QCheckBox(self.gb_dxvk_options)
        self.api.setObjectName("api")
        self.layout_dxvk_options.addWidget(self.api, 1, 2, 1, 1)
        self.dxvk_layout.addWidget(self.gb_dxvk_options, 2, 0, 1, 3)
        self.lbl_show_dxvk = QtWidgets.QLabel(DxvkSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_show_dxvk.sizePolicy().hasHeightForWidth())
        self.lbl_show_dxvk.setSizePolicy(sizePolicy)
        self.lbl_show_dxvk.setObjectName("lbl_show_dxvk")
        self.dxvk_layout.addWidget(self.lbl_show_dxvk, 0, 0, 1, 1)
        self.show_dxvk = QtWidgets.QComboBox(DxvkSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_dxvk.sizePolicy().hasHeightForWidth())
        self.show_dxvk.setSizePolicy(sizePolicy)
        self.show_dxvk.setObjectName("show_dxvk")
        self.show_dxvk.addItem("")
        self.show_dxvk.addItem("")
        self.show_dxvk.addItem("")
        self.show_dxvk.addItem("")
        self.dxvk_layout.addWidget(self.show_dxvk, 0, 1, 1, 2)

        self.retranslateUi(DxvkSettings)
        QtCore.QMetaObject.connectSlotsByName(DxvkSettings)

    def retranslateUi(self, DxvkSettings):
        _translate = QtCore.QCoreApplication.translate
        DxvkSettings.setWindowTitle(_translate("DxvkSettings", "DxvkSettings"))
        DxvkSettings.setTitle(_translate("DxvkSettings", "DXVK Settings"))
        self.gb_dxvk_options.setTitle(_translate("DxvkSettings", "DXVK HUD Options"))
        self.version.setText(_translate("DxvkSettings", "DXVK Version"))
        self.fps.setText(_translate("DxvkSettings", "FPS"))
        self.memory.setText(_translate("DxvkSettings", "Memory Usage"))
        self.devinfo.setText(_translate("DxvkSettings", "Device Info"))
        self.gpuload.setText(_translate("DxvkSettings", "GPU Usage"))
        self.frametime.setText(_translate("DxvkSettings", "Frame Time graph"))
        self.api.setText(_translate("DxvkSettings", "D3D Version"))
        self.lbl_show_dxvk.setText(_translate("DxvkSettings", "Show HUD"))
        self.show_dxvk.setItemText(0, _translate("DxvkSettings", "System Default"))
        self.show_dxvk.setItemText(1, _translate("DxvkSettings", "Hidden"))
        self.show_dxvk.setItemText(2, _translate("DxvkSettings", "Visible"))
        self.show_dxvk.setItemText(3, _translate("DxvkSettings", "Custom Options"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DxvkSettings = QtWidgets.QGroupBox()
    ui = Ui_DxvkSettings()
    ui.setupUi(DxvkSettings)
    DxvkSettings.show()
    sys.exit(app.exec_())
