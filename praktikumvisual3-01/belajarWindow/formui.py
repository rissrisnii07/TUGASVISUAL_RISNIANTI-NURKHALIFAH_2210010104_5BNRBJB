from smtpd import usage

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form): 1 usage
        Form.setObjectName("Form"): 1 usage
        Form.resize(400,300)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form): 1 usage
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(context: "Form", sourceText: "Form"))