
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(570, 500)
        Dialog.setMinimumSize(QtCore.QSize(570, 500))
        Dialog.setMaximumSize(QtCore.QSize(570, 16777215))
        font = QtGui.QFont()
        font.setUnderline(False)
        Dialog.setFont(font)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(-140, -90, 1000, 1041))
        self.widget.setMinimumSize(QtCore.QSize(1000, 1000))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color:#F1F1F1\n"
";  /* cor de fundo da janela */\n"
"}")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(310, 240, 231, 41))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background: transparent;          /* fundo transparente */\n"
"    color: #000000;                   /* cor do texto */\n"
"    border: 2px solid #AAAAAA;        /* cor e espessura da borda */\n"
"    border-radius: 5px;              /* arredondamento */\n"
"    padding-left: 40px;                     /* espaço interno */\n"
"}\n"
"")     
        
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText("Email")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("Email")
        
        
        
   
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 300, 231, 41))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background: transparent;          /* fundo transparente */\n"
"    color:  #000000;                   /* cor do texto */\n"
"    border: 2px solid #AAAAAA;        /* cor e espessura da borda */\n"
"    border-radius: 5px;              /* arredondamento */\n"
"    padding-left: 40px;                     /* espaço interno */\n"
"}\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setPlaceholderText("Digite sua senha")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.botao_login = QtWidgets.QPushButton(self.widget)
        self.botao_login.setGeometry(QtCore.QRect(380, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        self.botao_login.setFont(font)
        self.botao_login.setStyleSheet("QPushButton {\n"
"    background: #504B4B;          /* fundo transparente */\n"
"    color: #FFFFFF;                   /* cor do texto */       \n"
"    border-radius: 5px;              /* arredondamento */\n"
"    paddind: 5px; \n"
"}\n"
"")
        self.botao_login.setObjectName("botao_login")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 250, 21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/pessoa.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 310, 21, 21))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/chave.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.botao_login.raise_()
        self.label.lower()
        self.label_3.lower()
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(380, 470, 100, 50))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        
        self.botao_login.setText(_translate("Dialog", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
