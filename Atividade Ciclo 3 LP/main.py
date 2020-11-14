# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



Calculator = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Cálculo do IMC - Índice de Massa Corporal')
layout = QVBoxLayout()
button1 = QPushButton('Calcular')
button2 = QPushButton('Reniciar')
button3 = QPushButton('Sair')
nome = QLineEdit()
endereço = QLineEdit()
altura = QLineEdit()
peso = QLineEdit()
label1 = QLabel('Nome do Paciente:')
label2 = QLabel('Endereço Completo:')
label3 = QLabel('Altura(Cm):')
label4 = QLabel('Peso(Kg):')
imc = QLineEdit()

window.setMinimumSize(450, 300)

layout.addWidget(label1)
layout.addWidget(nome)
layout.addWidget(label2)
layout.addWidget(endereço)
layout.addWidget(label3)
layout.addWidget(altura)
layout.addWidget(label4)
layout.addWidget(peso)
layout.addWidget(QLabel('Resultado'))
layout.addWidget(imc)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

def CalcularIMC():
    h=float(altura.text())
    p=float(peso.text())
    r=(p/(h*h))
    f= str(r)
    imc.setText(f)

def Reniciar():
    nome.clear()
    endereço.clear()
    altura.clear()
    peso.clear()
    imc.clear()

def Sair():
    sys.exit(Calculator.exec_())


button1.clicked.connect(CalcularIMC)
button2.clicked.connect(Reniciar)
button3.clicked.connect(Sair)


window.setLayout(layout)
window.show()
Calculator.exec()