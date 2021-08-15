

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout_4.addWidget(self.pushButton1, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        self.title_input = QtWidgets.QLineEdit(Form)
        self.title_input.setText("")
        self.title_input.setObjectName("title_input")
        self.gridLayout_4.addWidget(self.title_input, 0, 2, 1, 1)
        self.Book_label = QtWidgets.QLabel(Form)
        self.Book_label.setObjectName("Book_label")
        self.gridLayout_4.addWidget(self.Book_label, 0, 0, 1, 2)
        self.price_view = QtWidgets.QLabel(Form)
        self.price_view.setObjectName("price_view") 
        self.gridLayout_4.addWidget(self.price_view, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 2, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setLineWidth(20)
        self.line.setMidLineWidth(30)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.total_view = QtWidgets.QLabel(Form)
        self.total_view.setObjectName("total_view")
        self.gridLayout_5.addWidget(self.total_view, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setObjectName("pushButton2") 
        self.gridLayout_5.addWidget(self.pushButton2, 1, 2, 1, 1)
        self.quantity_input = QtWidgets.QLineEdit(Form)
        
        self.quantity_input.setObjectName("quantity_input")  
        self.gridLayout_5.addWidget(self.quantity_input, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton1.pressed.connect(self.book_cost)
        
        self.pushButton2.pressed.connect(self.total_cost)

        
        self.cost=0
    
    def book_cost(self):
        import sqlite3
        book=sqlite3.connect("m6book.db")
        cur_book=book.cursor()
        text=self.title_input.text()
        if (text):
            sql="select price from book where title = '"+text+"';"
            cur_book.execute(sql)
            result=cur_book.fetchone()
            if (result):
                self.price_view.setText("Rs. "+str(result[0]))
                self.cost=result[0]
             
            else:
                self.price_view.setText("Book not found")
        
                
    def total_cost(self):
        num=self.quantity_input.text()
        if (num):
            num=int(num)
            self.total_view.setText("Rs. "+str(self.cost*num))
        else:
            self.total_view.setText("Rs. 0")
            
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "Find Price"))
        self.Book_label.setText(_translate("Form", "Book Title:     "))
        self.price_view.setText(_translate("Form", "Rs. 0"))
        self.label_2.setText(_translate("Form", "Price:    "))
        self.label_5.setText(_translate("Form", "Total:    "))
        self.total_view.setText(_translate("Form", "Rs. 0"))
        self.label_4.setText(_translate("Form", "Quantity:      "))
        self.pushButton2.setText(_translate("Form", "Find Total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
