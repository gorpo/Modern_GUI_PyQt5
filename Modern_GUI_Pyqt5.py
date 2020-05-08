# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projeto004.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    #funções que ativam e desativam o menu das configurações
    def menuAtivaConfiguracoes(self):
        self.menus_configuracoes.setGeometry(QtCore.QRect(-10, 420, 261, 450))
        self.btn_configuracoes1.clicked.connect(self.menuDesativaConfiguracoes)
    def menuDesativaConfiguracoes(self):
        self.menus_configuracoes.setGeometry(QtCore.QRect(-10, 680, 261, 50))
        self.btn_configuracoes1.clicked.connect(self.menuAtivaConfiguracoes)

    #funções que ativam e desativam o menu das databases
    def menuAtivaDatabase(self):
        self.menus_databases.setGeometry(QtCore.QRect(-10, 250, 261, 450))
        self.btn_database1.clicked.connect(self.menuDesativaDatabase)
    def menuDesativaDatabase(self):
        self.menus_databases.setGeometry(QtCore.QRect(-10, 250, 261, 50))
        self.btn_database1.clicked.connect(self.menuAtivaDatabase)

    #funções que ativam e desativam o menu dos servidores
    def menuAtivaServidor(self):
        self.menus_servidores.setGeometry(QtCore.QRect(-10, 200, 261, 450))
        self.btn_servidor1.clicked.connect(self.menuDesativaServidor)
    def menuDesativaServidor(self):
        self.menus_servidores.setGeometry(QtCore.QRect(-10, 200, 261, 50))
        self.btn_servidor1.clicked.connect(self.menuAtivaServidor)

    #funçoes que ativam e desativam o menu do telegram
    def menuAtivaTelegram(self):
        self.menus_telegrambots.setGeometry(QtCore.QRect(-10, 150, 261, 450))
        self.btn_telegrambot1.clicked.connect(self.menuDesativaTelegram)
    def menuDesativaTelegram(self):
        self.menus_telegrambots.setGeometry(QtCore.QRect(-10, 150, 261, 50))
        self.btn_telegrambot1.clicked.connect(self.menuAtivaTelegram)

    #funções que ativam e desativam o menu snes
    def menuAtivaSnes(self):
        self.menus_snes.setGeometry(QtCore.QRect(-10, 100, 261, 450))
        self.btn_snes1.clicked.connect(self.menuDesativaSnes)
    def menuDesativaSnes(self):
        self.menus_snes.setGeometry(QtCore.QRect(-10, 100, 261, 50))
        self.btn_snes1.clicked.connect(self.menuAtivaSnes)


    #funções que ativam e desativam o menu camera
    def menuAtivaCamera(self):
        self.menus_camera.setGeometry(QtCore.QRect(-10, 50, 261, 250))
        self.btn_camera1.clicked.connect(self.menuDesativaCamera)
    def menuDesativaCamera(self):
        self.menus_camera.setGeometry(QtCore.QRect(-10, 50, 261, 50))
        self.btn_camera1.clicked.connect(self.menuAtivaCamera)


    #funções que ativam e desativam o menu da esquerda
    def ativaMenu(self):
        self.menu_esquerda.setMaximumSize(QtCore.QSize(250, 16777215))
        self.botao_ativa_menu.clicked.connect(self.desativaMenu)
    def desativaMenu(self):
        self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
        self.botao_ativa_menu.clicked.connect(self.ativaMenu)

    # Funções minimizar maximizar e fechar personalizadas-----------------------
    def fecharPrograma(self):
            sys.exit()
    def minimizar(self):
            janela.showMinimized()
    def maximizar(self):
            self.botao_maximizar.setStyleSheet("QPushButton {\n"
                                               "    \n"
                                               "    background-image: url('imagens/volta_full_screen.png');\n"
                                               "    background-color: transparent;\n"
                                               "    background-repeat: no-repeat;\n"
                                               "    background-position: center;\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
            janela.showMaximized()
            self.botao_maximizar.clicked.connect(self.janela_normal)
    def janela_normal(self):
            self.botao_maximizar.setStyleSheet("QPushButton {\n"
                                           "    \n"
                                           "    background-image: url(:/toggle_mudar_jan/imagens/icons8-toggle-full-screen-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
            janela.showNormal()
            self.botao_maximizar.clicked.connect(self.maximizar)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 768)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 768))
        #remove a barra do sistema operacional--------------->>
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        #inicio do menu do topo -------------------------->>
        self.menu_topo = QtWidgets.QFrame(self.centralwidget)
        self.menu_topo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.menu_topo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.menu_topo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_topo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_topo.setObjectName("menu_topo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menu_topo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #botao que ativa os menus da esquerda------------------------------>>
        self.barra_ativa_menu = QtWidgets.QFrame(self.menu_topo)
        self.barra_ativa_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.barra_ativa_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.barra_ativa_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.barra_ativa_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_ativa_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_ativa_menu.setObjectName("barra_ativa_menu")
        self.botao_ativa_menu = QtWidgets.QPushButton(self.barra_ativa_menu)
        self.botao_ativa_menu.setGeometry(QtCore.QRect(0, -2, 51, 50))
        self.botao_ativa_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_ativa_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/ativa_menu/imagens/menu-4-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_ativa_menu.setText("")
        self.botao_ativa_menu.setObjectName("botao_ativa_menu")
        self.botao_ativa_menu.clicked.connect(self.ativaMenu)

        #barra de informações do topo---------------------------->>
        self.horizontalLayout_2.addWidget(self.barra_ativa_menu)
        self.Barra_informacoes = QtWidgets.QFrame(self.menu_topo)
        self.Barra_informacoes.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Barra_informacoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Barra_informacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Barra_informacoes.setObjectName("Barra_informacoes")
        self.horizontalLayout_2.addWidget(self.Barra_informacoes)
        self.frame_minimizar_janela = QtWidgets.QFrame(self.menu_topo)
        self.frame_minimizar_janela.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_minimizar_janela.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_minimizar_janela.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_minimizar_janela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_minimizar_janela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_minimizar_janela.setObjectName("frame_minimizar_janela")
        self.botao_minimizar = QtWidgets.QPushButton(self.frame_minimizar_janela)
        self.botao_minimizar.setGeometry(QtCore.QRect(-10, -2, 75, 50))
        self.botao_minimizar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/minimizar/imagens/minimize.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_minimizar.setText("")
        self.botao_minimizar.setObjectName("botao_minimizar")
        self.botao_minimizar.clicked.connect(self.minimizar)

        #botao redimensionar janela(subsititiu do windows deu moh mao fz saporra)-------------------------------->>
        self.horizontalLayout_2.addWidget(self.frame_minimizar_janela)
        self.frame_redimensionar_janela = QtWidgets.QFrame(self.menu_topo)
        self.frame_redimensionar_janela.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_redimensionar_janela.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_redimensionar_janela.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_redimensionar_janela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_redimensionar_janela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_redimensionar_janela.setObjectName("frame_redimensionar_janela")
        self.botao_maximizar = QtWidgets.QPushButton(self.frame_redimensionar_janela)
        self.botao_maximizar.setGeometry(QtCore.QRect(-10, -2, 75, 50))
        self.botao_maximizar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/toggle_mudar_jan/imagens/icons8-toggle-full-screen-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_maximizar.setText("")
        self.botao_maximizar.setObjectName("botao_maximizar")
        self.botao_maximizar.clicked.connect(self.maximizar)

        #botao fechar janela (subsititiu do windows deu moh mao fz saporra)----------------------------------------->
        self.horizontalLayout_2.addWidget(self.frame_redimensionar_janela)
        self.frame_fechar_janela = QtWidgets.QFrame(self.menu_topo)
        self.frame_fechar_janela.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_fechar_janela.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_fechar_janela.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(35, 35, 35);\n"
"    \n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.frame_fechar_janela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fechar_janela.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fechar_janela.setObjectName("frame_fechar_janela")
        self.botao_fechar_janela = QtWidgets.QPushButton(self.frame_fechar_janela)
        self.botao_fechar_janela.setGeometry(QtCore.QRect(-10, -2, 75, 50))
        self.botao_fechar_janela.setStyleSheet("QPushButton {\n"
"    background-image: url(:/close_fechar/imagens/icons8-delete-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_fechar_janela.setText("")
        self.botao_fechar_janela.setObjectName("pushButton_3")
        self.botao_fechar_janela.clicked.connect(self.fecharPrograma)

        self.horizontalLayout_2.addWidget(self.frame_fechar_janela)
        self.verticalLayout.addWidget(self.menu_topo)
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.background)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

#=====================================================================================================
#                         INICIO DOS MENUS
#=======================================================================================================

        #menu da esquerda completo-------------------------->>
        self.menu_esquerda = QtWidgets.QFrame(self.background)
        self.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
        self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menu_esquerda.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.menu_esquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_esquerda.setObjectName("menu_esquerda")

        #menu home ----------->>
        self.menus_home = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_home.setGeometry(QtCore.QRect(-10, 0, 261, 50))
        self.menus_home.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.menus_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_home.setObjectName("menus_home")
        self.btn_home = QtWidgets.QPushButton(self.menus_home)
        self.btn_home.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background-image: url(:/home/imagens/home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_home.setText("")
        self.btn_home.setObjectName("btn_home")
        self.texto_btn_home = QtWidgets.QLabel(self.menus_home)
        self.texto_btn_home.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_home.setFont(font)
        self.texto_btn_home.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_home.setObjectName("texto_btn_home")









        #menus de configurações------------------------------------------------->>
        self.menus_configuracoes = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_configuracoes.setGeometry(QtCore.QRect(-10, 680, 261, 50))
        self.menus_configuracoes.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(35, 35, 35);\n"
"}")
        self.menus_configuracoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_configuracoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_configuracoes.setObjectName("menus_configuracoes")
        self.barra_btn_configuracoes1 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_configuracoes1.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1.setObjectName("barra_btn_configuracoes1")
        self.btn_configuracoes1 = QtWidgets.QPushButton(self.barra_btn_configuracoes1)
        self.btn_configuracoes1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_configuracoes1.clicked.connect(self.menuAtivaConfiguracoes)


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1.setFont(font)
        self.btn_configuracoes1.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1.setText("")
        self.btn_configuracoes1.setObjectName("btn_configuracoes1")
        self.texto_btn_configuracoes1 = QtWidgets.QLabel(self.barra_btn_configuracoes1)
        self.texto_btn_configuracoes1.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1.setFont(font)
        self.texto_btn_configuracoes1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1.setObjectName("texto_btn_configuracoes1")
        self.barra_btn_configuracoes1_2 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1_2.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_configuracoes1_2.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1_2.setObjectName("barra_btn_configuracoes1_2")
        self.btn_configuracoes1_2 = QtWidgets.QPushButton(self.barra_btn_configuracoes1_2)
        self.btn_configuracoes1_2.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1_2.setFont(font)
        self.btn_configuracoes1_2.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1_2.setText("")
        self.btn_configuracoes1_2.setObjectName("btn_configuracoes1_2")
        self.texto_btn_configuracoes1_2 = QtWidgets.QLabel(self.barra_btn_configuracoes1_2)
        self.texto_btn_configuracoes1_2.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1_2.setFont(font)
        self.texto_btn_configuracoes1_2.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1_2.setObjectName("texto_btn_configuracoes1_2")
        self.barra_btn_configuracoes1_3 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1_3.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_configuracoes1_3.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1_3.setObjectName("barra_btn_configuracoes1_3")
        self.btn_configuracoes1_3 = QtWidgets.QPushButton(self.barra_btn_configuracoes1_3)
        self.btn_configuracoes1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1_3.setFont(font)
        self.btn_configuracoes1_3.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1_3.setText("")
        self.btn_configuracoes1_3.setObjectName("btn_configuracoes1_3")
        self.texto_btn_configuracoes1_3 = QtWidgets.QLabel(self.barra_btn_configuracoes1_3)
        self.texto_btn_configuracoes1_3.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1_3.setFont(font)
        self.texto_btn_configuracoes1_3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1_3.setObjectName("texto_btn_configuracoes1_3")
        self.barra_btn_configuracoes1_4 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1_4.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_configuracoes1_4.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1_4.setObjectName("barra_btn_configuracoes1_4")
        self.btn_configuracoes1_5 = QtWidgets.QPushButton(self.barra_btn_configuracoes1_4)
        self.btn_configuracoes1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1_5.setFont(font)
        self.btn_configuracoes1_5.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1_5.setText("")
        self.btn_configuracoes1_5.setObjectName("btn_configuracoes1_5")
        self.texto_btn_configuracoes1_5 = QtWidgets.QLabel(self.barra_btn_configuracoes1_4)
        self.texto_btn_configuracoes1_5.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1_5.setFont(font)
        self.texto_btn_configuracoes1_5.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1_5.setObjectName("texto_btn_configuracoes1_5")
        self.barra_btn_configuracoes1_5 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1_5.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_configuracoes1_5.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1_5.setObjectName("barra_btn_configuracoes1_5")
        self.btn_configuracoes1_7 = QtWidgets.QPushButton(self.barra_btn_configuracoes1_5)
        self.btn_configuracoes1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1_7.setFont(font)
        self.btn_configuracoes1_7.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1_7.setText("")
        self.btn_configuracoes1_7.setObjectName("btn_configuracoes1_7")
        self.texto_btn_configuracoes1_7 = QtWidgets.QLabel(self.barra_btn_configuracoes1_5)
        self.texto_btn_configuracoes1_7.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1_7.setFont(font)
        self.texto_btn_configuracoes1_7.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1_7.setObjectName("texto_btn_configuracoes1_7")
        self.barra_btn_configuracoes1_6 = QtWidgets.QFrame(self.menus_configuracoes)
        self.barra_btn_configuracoes1_6.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_configuracoes1_6.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_configuracoes1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_configuracoes1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_configuracoes1_6.setObjectName("barra_btn_configuracoes1_6")
        self.btn_configuracoes1_8 = QtWidgets.QPushButton(self.barra_btn_configuracoes1_6)
        self.btn_configuracoes1_8.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_configuracoes1_8.setFont(font)
        self.btn_configuracoes1_8.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_configuracoes1_8.setText("")
        self.btn_configuracoes1_8.setObjectName("btn_configuracoes1_8")
        self.texto_btn_configuracoes1_8 = QtWidgets.QLabel(self.barra_btn_configuracoes1_6)
        self.texto_btn_configuracoes1_8.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_configuracoes1_8.setFont(font)
        self.texto_btn_configuracoes1_8.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px SegoeUIl, bold;\n"
"}")
        self.texto_btn_configuracoes1_8.setObjectName("texto_btn_configuracoes1_8")
        self.horizontalLayout.addWidget(self.menu_esquerda)



        # menus das databases---------------------------------------------------->>
        self.menus_databases = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_databases.setGeometry(QtCore.QRect(-10, 250, 261, 50))
        self.menus_databases.setStyleSheet("QFrame {\n"
                                           "    \n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QFrame:hover {\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "}\n"
                                           "QFrame:pressed {\n"
                                           "    background-color: rgb(35, 35, 35);\n"
                                           "}")
        self.menus_databases.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_databases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_databases.setObjectName("menus_databases")
        self.barra_btn_database1 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_database1.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_database1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1.setObjectName("barra_btn_database1")
        self.btn_database1 = QtWidgets.QPushButton(self.barra_btn_database1)
        self.btn_database1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_database1.clicked.connect(self.menuAtivaDatabase)


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1.setFont(font)
        self.btn_database1.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_database1.setText("")
        self.btn_database1.setObjectName("btn_database1")
        self.texto_btn_database1 = QtWidgets.QLabel(self.barra_btn_database1)
        self.texto_btn_database1.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1.setFont(font)
        self.texto_btn_database1.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_database1.setObjectName("texto_btn_database1")
        self.barra_btn_database1_2 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_2.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_database1_2.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_2.setObjectName("barra_btn_database1_2")
        self.btn_database1_2 = QtWidgets.QPushButton(self.barra_btn_database1_2)
        self.btn_database1_2.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_2.setFont(font)
        self.btn_database1_2.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_2.setText("")
        self.btn_database1_2.setObjectName("btn_database1_2")
        self.texto_btn_database1_2 = QtWidgets.QLabel(self.barra_btn_database1_2)
        self.texto_btn_database1_2.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_2.setFont(font)
        self.texto_btn_database1_2.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_2.setObjectName("texto_btn_database1_2")
        self.barra_btn_database1_3 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_3.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_database1_3.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_3.setObjectName("barra_btn_database1_3")
        self.btn_database1_3 = QtWidgets.QPushButton(self.barra_btn_database1_3)
        self.btn_database1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_3.setFont(font)
        self.btn_database1_3.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_3.setText("")
        self.btn_database1_3.setObjectName("btn_database1_3")
        self.texto_btn_database1_3 = QtWidgets.QLabel(self.barra_btn_database1_3)
        self.texto_btn_database1_3.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_3.setFont(font)
        self.texto_btn_database1_3.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_3.setObjectName("texto_btn_database1_3")
        self.barra_btn_database1_4 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_4.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_database1_4.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_4.setObjectName("barra_btn_database1_4")
        self.btn_database1_4 = QtWidgets.QPushButton(self.barra_btn_database1_4)
        self.btn_database1_4.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_4.setFont(font)
        self.btn_database1_4.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_4.setText("")
        self.btn_database1_4.setObjectName("btn_database1_4")
        self.texto_btn_database1_4 = QtWidgets.QLabel(self.barra_btn_database1_4)
        self.texto_btn_database1_4.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_4.setFont(font)
        self.texto_btn_database1_4.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_4.setObjectName("texto_btn_database1_4")
        self.barra_btn_database1_5 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_5.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_database1_5.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_5.setObjectName("barra_btn_database1_5")
        self.btn_database1_5 = QtWidgets.QPushButton(self.barra_btn_database1_5)
        self.btn_database1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_5.setFont(font)
        self.btn_database1_5.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_5.setText("")
        self.btn_database1_5.setObjectName("btn_database1_5")
        self.texto_btn_database1_5 = QtWidgets.QLabel(self.barra_btn_database1_5)
        self.texto_btn_database1_5.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_5.setFont(font)
        self.texto_btn_database1_5.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_5.setObjectName("texto_btn_database1_5")
        self.barra_btn_database1_6 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_6.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_database1_6.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_6.setObjectName("barra_btn_database1_6")
        self.btn_database1_6 = QtWidgets.QPushButton(self.barra_btn_database1_6)
        self.btn_database1_6.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_6.setFont(font)
        self.btn_database1_6.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_6.setText("")
        self.btn_database1_6.setObjectName("btn_database1_6")
        self.texto_btn_database1_6 = QtWidgets.QLabel(self.barra_btn_database1_6)
        self.texto_btn_database1_6.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_6.setFont(font)
        self.texto_btn_database1_6.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_6.setObjectName("texto_btn_database1_6")
        self.barra_btn_database1_7 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_7.setGeometry(QtCore.QRect(0, 300, 261, 50))
        self.barra_btn_database1_7.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_7.setObjectName("barra_btn_database1_7")
        self.btn_database1_7 = QtWidgets.QPushButton(self.barra_btn_database1_7)
        self.btn_database1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_7.setFont(font)
        self.btn_database1_7.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_7.setText("")
        self.btn_database1_7.setObjectName("btn_database1_7")
        self.texto_btn_database1_7 = QtWidgets.QLabel(self.barra_btn_database1_7)
        self.texto_btn_database1_7.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_7.setFont(font)
        self.texto_btn_database1_7.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_7.setObjectName("texto_btn_database1_7")
        self.barra_btn_database1_8 = QtWidgets.QFrame(self.menus_databases)
        self.barra_btn_database1_8.setGeometry(QtCore.QRect(0, 350, 261, 50))
        self.barra_btn_database1_8.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_database1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_database1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_database1_8.setObjectName("barra_btn_database1_8")
        self.btn_database1_8 = QtWidgets.QPushButton(self.barra_btn_database1_8)
        self.btn_database1_8.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_database1_8.setFont(font)
        self.btn_database1_8.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_database1_8.setText("")
        self.btn_database1_8.setObjectName("btn_database1_8")
        self.texto_btn_database1_8 = QtWidgets.QLabel(self.barra_btn_database1_8)
        self.texto_btn_database1_8.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_database1_8.setFont(font)
        self.texto_btn_database1_8.setStyleSheet("QLabel{\n"
                                                 "    background-color: transparent;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "font: 20px SegoeUIl, bold;\n"
                                                 "}")
        self.texto_btn_database1_8.setObjectName("texto_btn_database1_8")





        # menus dos servidores----------------------------------------->
        self.menus_servidores = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_servidores.setGeometry(QtCore.QRect(-10, 200, 261, 50))
        self.menus_servidores.setStyleSheet("QFrame {\n"
                                            "    \n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "QFrame:hover {\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "}\n"
                                            "QFrame:pressed {\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "}")
        self.menus_servidores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_servidores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_servidores.setObjectName("menus_servidores")
        self.barra_btn_servidor1 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_servidor1.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_servidor1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1.setObjectName("barra_btn_servidor1")
        self.btn_servidor1 = QtWidgets.QPushButton(self.barra_btn_servidor1)
        self.btn_servidor1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_servidor1.clicked.connect(self.menuAtivaServidor)


        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1.setFont(font)
        self.btn_servidor1.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/server/imagens/server-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_servidor1.setText("")
        self.btn_servidor1.setObjectName("btn_servidor1")
        self.texto_btn_snes1_22 = QtWidgets.QLabel(self.barra_btn_servidor1)
        self.texto_btn_snes1_22.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_22.setFont(font)
        self.texto_btn_snes1_22.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_22.setObjectName("texto_btn_snes1_22")
        self.barra_btn_servidor1_2 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_2.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_servidor1_2.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_2.setObjectName("barra_btn_servidor1_2")
        self.btn_servidor1_3 = QtWidgets.QPushButton(self.barra_btn_servidor1_2)
        self.btn_servidor1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_3.setFont(font)
        self.btn_servidor1_3.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_3.setText("")
        self.btn_servidor1_3.setObjectName("btn_servidor1_3")
        self.texto_btn_snes1_24 = QtWidgets.QLabel(self.barra_btn_servidor1_2)
        self.texto_btn_snes1_24.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_24.setFont(font)
        self.texto_btn_snes1_24.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_24.setObjectName("texto_btn_snes1_24")
        self.barra_btn_servidor1_3 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_3.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_servidor1_3.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_3.setObjectName("barra_btn_servidor1_3")
        self.btn_servidor1_4 = QtWidgets.QPushButton(self.barra_btn_servidor1_3)
        self.btn_servidor1_4.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_4.setFont(font)
        self.btn_servidor1_4.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_4.setText("")
        self.btn_servidor1_4.setObjectName("btn_servidor1_4")
        self.texto_btn_snes1_25 = QtWidgets.QLabel(self.barra_btn_servidor1_3)
        self.texto_btn_snes1_25.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_25.setFont(font)
        self.texto_btn_snes1_25.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_25.setObjectName("texto_btn_snes1_25")
        self.barra_btn_servidor1_5 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_5.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_servidor1_5.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_5.setObjectName("barra_btn_servidor1_5")
        self.btn_servidor1_6 = QtWidgets.QPushButton(self.barra_btn_servidor1_5)
        self.btn_servidor1_6.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_6.setFont(font)
        self.btn_servidor1_6.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_6.setText("")
        self.btn_servidor1_6.setObjectName("btn_servidor1_6")
        self.texto_btn_snes1_27 = QtWidgets.QLabel(self.barra_btn_servidor1_5)
        self.texto_btn_snes1_27.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_27.setFont(font)
        self.texto_btn_snes1_27.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_27.setObjectName("texto_btn_snes1_27")
        self.barra_btn_servidor1_6 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_6.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_servidor1_6.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_6.setObjectName("barra_btn_servidor1_6")
        self.btn_servidor1_7 = QtWidgets.QPushButton(self.barra_btn_servidor1_6)
        self.btn_servidor1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_7.setFont(font)
        self.btn_servidor1_7.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_7.setText("")
        self.btn_servidor1_7.setObjectName("btn_servidor1_7")
        self.texto_btn_snes1_28 = QtWidgets.QLabel(self.barra_btn_servidor1_6)
        self.texto_btn_snes1_28.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_28.setFont(font)
        self.texto_btn_snes1_28.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_28.setObjectName("texto_btn_snes1_28")
        self.barra_btn_servidor1_4 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_4.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_servidor1_4.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_4.setObjectName("barra_btn_servidor1_4")
        self.btn_servidor1_5 = QtWidgets.QPushButton(self.barra_btn_servidor1_4)
        self.btn_servidor1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_5.setFont(font)
        self.btn_servidor1_5.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_5.setText("")
        self.btn_servidor1_5.setObjectName("btn_servidor1_5")
        self.texto_btn_snes1_26 = QtWidgets.QLabel(self.barra_btn_servidor1_4)
        self.texto_btn_snes1_26.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_26.setFont(font)
        self.texto_btn_snes1_26.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_26.setObjectName("texto_btn_snes1_26")
        self.barra_btn_servidor1_7 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_7.setGeometry(QtCore.QRect(0, 300, 261, 50))
        self.barra_btn_servidor1_7.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_7.setObjectName("barra_btn_servidor1_7")
        self.btn_servidor1_8 = QtWidgets.QPushButton(self.barra_btn_servidor1_7)
        self.btn_servidor1_8.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_8.setFont(font)
        self.btn_servidor1_8.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_8.setText("")
        self.btn_servidor1_8.setObjectName("btn_servidor1_8")
        self.texto_btn_snes1_29 = QtWidgets.QLabel(self.barra_btn_servidor1_7)
        self.texto_btn_snes1_29.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_29.setFont(font)
        self.texto_btn_snes1_29.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_29.setObjectName("texto_btn_snes1_29")
        self.barra_btn_servidor1_8 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_8.setGeometry(QtCore.QRect(0, 350, 261, 50))
        self.barra_btn_servidor1_8.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_8.setObjectName("barra_btn_servidor1_8")
        self.btn_servidor1_9 = QtWidgets.QPushButton(self.barra_btn_servidor1_8)
        self.btn_servidor1_9.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_9.setFont(font)
        self.btn_servidor1_9.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/server/imagens/server-24.png);\n"
                                           "    background-color: transparent;\n"
                                           "    background-repeat: no-repeat;\n"
                                           "    background-position: center;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.btn_servidor1_9.setText("")
        self.btn_servidor1_9.setObjectName("btn_servidor1_9")
        self.texto_btn_snes1_30 = QtWidgets.QLabel(self.barra_btn_servidor1_8)
        self.texto_btn_snes1_30.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_30.setFont(font)
        self.texto_btn_snes1_30.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_30.setObjectName("texto_btn_snes1_30")
        self.barra_btn_servidor1_9 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_9.setGeometry(QtCore.QRect(0, 400, 261, 50))
        self.barra_btn_servidor1_9.setStyleSheet("QFrame {\n"
                                                 "    border: none;\n"
                                                 "}\n"
                                                 "QFrame:hover {\n"
                                                 "    background-color: rgb(30,144,255);\n"
                                                 "}\n"
                                                 "QFrame:pressed {\n"
                                                 "    background-color: rgb(1,84,149);\n"
                                                 "}")
        self.barra_btn_servidor1_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_9.setObjectName("barra_btn_servidor1_9")
        self.btn_servidor1_10 = QtWidgets.QPushButton(self.barra_btn_servidor1_9)
        self.btn_servidor1_10.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_10.setFont(font)
        self.btn_servidor1_10.setStyleSheet("QPushButton {\n"
                                            "    background-image: url(:/server/imagens/server-24.png);\n"
                                            "    background-color: transparent;\n"
                                            "    background-repeat: no-repeat;\n"
                                            "    background-position: center;\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(30,144,255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(1,84,149);\n"
                                            "}")
        self.btn_servidor1_10.setText("")
        self.btn_servidor1_10.setObjectName("btn_servidor1_10")
        self.texto_btn_snes1_31 = QtWidgets.QLabel(self.barra_btn_servidor1_9)
        self.texto_btn_snes1_31.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_31.setFont(font)
        self.texto_btn_snes1_31.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_31.setObjectName("texto_btn_snes1_31")
        self.barra_btn_servidor1_10 = QtWidgets.QFrame(self.menus_servidores)
        self.barra_btn_servidor1_10.setGeometry(QtCore.QRect(0, 450, 261, 50))
        self.barra_btn_servidor1_10.setStyleSheet("QFrame {\n"
                                                  "    border: none;\n"
                                                  "}\n"
                                                  "QFrame:hover {\n"
                                                  "    background-color: rgb(30,144,255);\n"
                                                  "}\n"
                                                  "QFrame:pressed {\n"
                                                  "    background-color: rgb(1,84,149);\n"
                                                  "}")
        self.barra_btn_servidor1_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor1_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor1_10.setObjectName("barra_btn_servidor1_10")
        self.btn_servidor1_11 = QtWidgets.QPushButton(self.barra_btn_servidor1_10)
        self.btn_servidor1_11.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor1_11.setFont(font)
        self.btn_servidor1_11.setStyleSheet("QPushButton {\n"
                                            "    background-image: url(:/server/imagens/server-24.png);\n"
                                            "    background-color: transparent;\n"
                                            "    background-repeat: no-repeat;\n"
                                            "    background-position: center;\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(30,144,255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(1,84,149);\n"
                                            "}")
        self.btn_servidor1_11.setText("")
        self.btn_servidor1_11.setObjectName("btn_servidor1_11")
        self.texto_btn_snes1_32 = QtWidgets.QLabel(self.barra_btn_servidor1_10)
        self.texto_btn_snes1_32.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_32.setFont(font)
        self.texto_btn_snes1_32.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_32.setObjectName("texto_btn_snes1_32")




        # menus dos botoes dos bots do telegram-----------------------------
        self.menus_telegrambots = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_telegrambots.setGeometry(QtCore.QRect(-10, 150, 261, 50))
        self.menus_telegrambots.setStyleSheet("QFrame {\n"
                                              "    \n"
                                              "    background-color: rgb(35, 35, 35);\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QFrame:hover {\n"
                                              "    background-color: rgb(35, 35, 35);\n"
                                              "}\n"
                                              "QFrame:pressed {\n"
                                              "    background-color: rgb(35, 35, 35);\n"
                                              "}")
        self.menus_telegrambots.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_telegrambots.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_telegrambots.setObjectName("menus_telegrambots")
        self.barra_btn_telegrambot1 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_telegrambot1.setStyleSheet("QFrame {\n"
                                                  "    border: none;\n"
                                                  "}\n"
                                                  "QFrame:hover {\n"
                                                  "    background-color: rgb(30,144,255);\n"
                                                  "}\n"
                                                  "QFrame:pressed {\n"
                                                  "    background-color: rgb(1,84,149);\n"
                                                  "}")
        self.barra_btn_telegrambot1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1.setObjectName("barra_btn_telegrambot1")
        self.btn_telegrambot1 = QtWidgets.QPushButton(self.barra_btn_telegrambot1)
        self.btn_telegrambot1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_telegrambot1.clicked.connect(self.menuAtivaTelegram)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1.setFont(font)
        self.btn_telegrambot1.setStyleSheet("QPushButton {\n"
                                            "    background-image: url(:/bot/imagens/telegram.png);\n"
                                            "    background-color: transparent;\n"
                                            "    background-repeat: no-repeat;\n"
                                            "    background-position: center;\n"
                                            "    border: none;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(30,144,255);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: rgb(1,84,149);\n"
                                            "}")
        self.btn_telegrambot1.setText("")
        self.btn_telegrambot1.setObjectName("btn_telegrambot1")
        self.texto_btn_snes1_12 = QtWidgets.QLabel(self.barra_btn_telegrambot1)
        self.texto_btn_snes1_12.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_12.setFont(font)
        self.texto_btn_snes1_12.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_12.setObjectName("texto_btn_snes1_12")
        self.barra_btn_telegrambot1_2 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_2.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_telegrambot1_2.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_2.setObjectName("barra_btn_telegrambot1_2")
        self.btn_telegrambot1_2 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_2)
        self.btn_telegrambot1_2.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_2.setFont(font)
        self.btn_telegrambot1_2.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_2.setText("")
        self.btn_telegrambot1_2.setObjectName("btn_telegrambot1_2")
        self.texto_btn_snes1_13 = QtWidgets.QLabel(self.barra_btn_telegrambot1_2)
        self.texto_btn_snes1_13.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_13.setFont(font)
        self.texto_btn_snes1_13.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_13.setObjectName("texto_btn_snes1_13")
        self.barra_btn_telegrambot1_3 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_3.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_telegrambot1_3.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_3.setObjectName("barra_btn_telegrambot1_3")
        self.btn_telegrambot1_3 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_3)
        self.btn_telegrambot1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_3.setFont(font)
        self.btn_telegrambot1_3.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_3.setText("")
        self.btn_telegrambot1_3.setObjectName("btn_telegrambot1_3")
        self.texto_btn_snes1_14 = QtWidgets.QLabel(self.barra_btn_telegrambot1_3)
        self.texto_btn_snes1_14.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_14.setFont(font)
        self.texto_btn_snes1_14.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_14.setObjectName("texto_btn_snes1_14")
        self.barra_btn_telegrambot1_4 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_4.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_telegrambot1_4.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_4.setObjectName("barra_btn_telegrambot1_4")
        self.btn_telegrambot1_4 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_4)
        self.btn_telegrambot1_4.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_4.setFont(font)
        self.btn_telegrambot1_4.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_4.setText("")
        self.btn_telegrambot1_4.setObjectName("btn_telegrambot1_4")
        self.texto_btn_snes1_15 = QtWidgets.QLabel(self.barra_btn_telegrambot1_4)
        self.texto_btn_snes1_15.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_15.setFont(font)
        self.texto_btn_snes1_15.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_15.setObjectName("texto_btn_snes1_15")
        self.barra_btn_telegrambot1_5 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_5.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_telegrambot1_5.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_5.setObjectName("barra_btn_telegrambot1_5")
        self.btn_telegrambot1_5 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_5)
        self.btn_telegrambot1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_5.setFont(font)
        self.btn_telegrambot1_5.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_5.setText("")
        self.btn_telegrambot1_5.setObjectName("btn_telegrambot1_5")
        self.texto_btn_snes1_16 = QtWidgets.QLabel(self.barra_btn_telegrambot1_5)
        self.texto_btn_snes1_16.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_16.setFont(font)
        self.texto_btn_snes1_16.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_16.setObjectName("texto_btn_snes1_16")
        self.barra_btn_telegrambot1_6 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_6.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_telegrambot1_6.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_6.setObjectName("barra_btn_telegrambot1_6")
        self.btn_telegrambot1_6 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_6)
        self.btn_telegrambot1_6.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_6.setFont(font)
        self.btn_telegrambot1_6.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_6.setText("")
        self.btn_telegrambot1_6.setObjectName("btn_telegrambot1_6")
        self.texto_btn_snes1_17 = QtWidgets.QLabel(self.barra_btn_telegrambot1_6)
        self.texto_btn_snes1_17.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_17.setFont(font)
        self.texto_btn_snes1_17.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_17.setObjectName("texto_btn_snes1_17")
        self.barra_btn_telegrambot1_7 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_7.setGeometry(QtCore.QRect(0, 300, 261, 50))
        self.barra_btn_telegrambot1_7.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_7.setObjectName("barra_btn_telegrambot1_7")
        self.btn_telegrambot1_7 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_7)
        self.btn_telegrambot1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_7.setFont(font)
        self.btn_telegrambot1_7.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_7.setText("")
        self.btn_telegrambot1_7.setObjectName("btn_telegrambot1_7")
        self.texto_btn_snes1_18 = QtWidgets.QLabel(self.barra_btn_telegrambot1_7)
        self.texto_btn_snes1_18.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_18.setFont(font)
        self.texto_btn_snes1_18.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_18.setObjectName("texto_btn_snes1_18")
        self.barra_btn_telegrambot1_8 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_8.setGeometry(QtCore.QRect(0, 350, 261, 50))
        self.barra_btn_telegrambot1_8.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_8.setObjectName("barra_btn_telegrambot1_8")
        self.btn_telegrambot1_8 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_8)
        self.btn_telegrambot1_8.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_8.setFont(font)
        self.btn_telegrambot1_8.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_8.setText("")
        self.btn_telegrambot1_8.setObjectName("btn_telegrambot1_8")
        self.texto_btn_snes1_19 = QtWidgets.QLabel(self.barra_btn_telegrambot1_8)
        self.texto_btn_snes1_19.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_19.setFont(font)
        self.texto_btn_snes1_19.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_19.setObjectName("texto_btn_snes1_19")
        self.barra_btn_telegrambot1_9 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_9.setGeometry(QtCore.QRect(0, 400, 261, 50))
        self.barra_btn_telegrambot1_9.setStyleSheet("QFrame {\n"
                                                    "    border: none;\n"
                                                    "}\n"
                                                    "QFrame:hover {\n"
                                                    "    background-color: rgb(30,144,255);\n"
                                                    "}\n"
                                                    "QFrame:pressed {\n"
                                                    "    background-color: rgb(1,84,149);\n"
                                                    "}")
        self.barra_btn_telegrambot1_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_9.setObjectName("barra_btn_telegrambot1_9")
        self.btn_telegrambot1_9 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_9)
        self.btn_telegrambot1_9.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_9.setFont(font)
        self.btn_telegrambot1_9.setStyleSheet("QPushButton {\n"
                                              "    background-image: url(:/bot/imagens/telegram.png);\n"
                                              "    background-color: transparent;\n"
                                              "    background-repeat: no-repeat;\n"
                                              "    background-position: center;\n"
                                              "    border: none;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(30,144,255);\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: rgb(1,84,149);\n"
                                              "}")
        self.btn_telegrambot1_9.setText("")
        self.btn_telegrambot1_9.setObjectName("btn_telegrambot1_9")
        self.texto_btn_snes1_20 = QtWidgets.QLabel(self.barra_btn_telegrambot1_9)
        self.texto_btn_snes1_20.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_20.setFont(font)
        self.texto_btn_snes1_20.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_20.setObjectName("texto_btn_snes1_20")
        self.barra_btn_telegrambot1_10 = QtWidgets.QFrame(self.menus_telegrambots)
        self.barra_btn_telegrambot1_10.setGeometry(QtCore.QRect(0, 450, 261, 50))
        self.barra_btn_telegrambot1_10.setStyleSheet("QFrame {\n"
                                                     "    border: none;\n"
                                                     "}\n"
                                                     "QFrame:hover {\n"
                                                     "    background-color: rgb(30,144,255);\n"
                                                     "}\n"
                                                     "QFrame:pressed {\n"
                                                     "    background-color: rgb(1,84,149);\n"
                                                     "}")
        self.barra_btn_telegrambot1_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_telegrambot1_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_telegrambot1_10.setObjectName("barra_btn_telegrambot1_10")
        self.btn_telegrambot1_10 = QtWidgets.QPushButton(self.barra_btn_telegrambot1_10)
        self.btn_telegrambot1_10.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_telegrambot1_10.setFont(font)
        self.btn_telegrambot1_10.setStyleSheet("QPushButton {\n"
                                               "    background-image: url(:/bot/imagens/telegram.png);\n"
                                               "    background-color: transparent;\n"
                                               "    background-repeat: no-repeat;\n"
                                               "    background-position: center;\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.btn_telegrambot1_10.setText("")
        self.btn_telegrambot1_10.setObjectName("btn_telegrambot1_10")
        self.texto_btn_snes1_21 = QtWidgets.QLabel(self.barra_btn_telegrambot1_10)
        self.texto_btn_snes1_21.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_21.setFont(font)
        self.texto_btn_snes1_21.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_21.setObjectName("texto_btn_snes1_21")



        # menus snes ------------------------------------->>
        self.menus_snes = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_snes.setGeometry(QtCore.QRect(-10, 100, 261, 50))
        self.menus_snes.setStyleSheet("QFrame {\n"
                                      "    \n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "QFrame:hover {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "}\n"
                                      "QFrame:pressed {\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "}")
        self.menus_snes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_snes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_snes.setObjectName("menus_snes")
        self.barra_btn_snes1 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_snes1.setStyleSheet("QFrame {\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "QFrame:hover {\n"
                                           "    background-color: rgb(30,144,255);\n"
                                           "}\n"
                                           "QFrame:pressed {\n"
                                           "    background-color: rgb(1,84,149);\n"
                                           "}")
        self.barra_btn_snes1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1.setObjectName("barra_btn_snes1")
        self.btn_snes1 = QtWidgets.QPushButton(self.barra_btn_snes1)
        self.btn_snes1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_snes1.clicked.connect(self.menuAtivaSnes)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1.setFont(font)
        self.btn_snes1.setStyleSheet("QPushButton {\n"
                                     "    \n"
                                     "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                     "    background-color: transparent;\n"
                                     "    background-repeat: no-repeat;\n"
                                     "    background-position: center;\n"
                                     "    border: none;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(30,144,255);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(1,84,149);\n"
                                     "}")
        self.btn_snes1.setText("")
        self.btn_snes1.setObjectName("btn_snes1")
        self.texto_btn_snes1 = QtWidgets.QLabel(self.barra_btn_snes1)
        self.texto_btn_snes1.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1.setFont(font)
        self.texto_btn_snes1.setStyleSheet("QLabel{\n"
                                           "    background-color: transparent;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "font: 20px SegoeUIl, bold;\n"
                                           "}")
        self.texto_btn_snes1.setObjectName("texto_btn_snes1")
        self.barra_btn_snes1_2 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_2.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_snes1_2.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_2.setObjectName("barra_btn_snes1_2")
        self.btn_snes1_2 = QtWidgets.QPushButton(self.barra_btn_snes1_2)
        self.btn_snes1_2.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_2.setFont(font)
        self.btn_snes1_2.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_2.setText("")
        self.btn_snes1_2.setObjectName("btn_snes1_2")
        self.texto_btn_snes1_2 = QtWidgets.QLabel(self.barra_btn_snes1_2)
        self.texto_btn_snes1_2.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_2.setFont(font)
        self.texto_btn_snes1_2.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_2.setObjectName("texto_btn_snes1_2")
        self.barra_btn_snes1_3 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_3.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_snes1_3.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_3.setObjectName("barra_btn_snes1_3")
        self.btn_snes1_3 = QtWidgets.QPushButton(self.barra_btn_snes1_3)
        self.btn_snes1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_3.setFont(font)
        self.btn_snes1_3.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_3.setText("")
        self.btn_snes1_3.setObjectName("btn_snes1_3")
        self.texto_btn_snes1_3 = QtWidgets.QLabel(self.barra_btn_snes1_3)
        self.texto_btn_snes1_3.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_3.setFont(font)
        self.texto_btn_snes1_3.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_3.setObjectName("texto_btn_snes1_3")
        self.barra_btn_snes1_4 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_4.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_snes1_4.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_4.setObjectName("barra_btn_snes1_4")
        self.btn_snes1_5 = QtWidgets.QPushButton(self.barra_btn_snes1_4)
        self.btn_snes1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_5.setFont(font)
        self.btn_snes1_5.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_5.setText("")
        self.btn_snes1_5.setObjectName("btn_snes1_5")
        self.texto_btn_snes1_5 = QtWidgets.QLabel(self.barra_btn_snes1_4)
        self.texto_btn_snes1_5.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_5.setFont(font)
        self.texto_btn_snes1_5.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_5.setObjectName("texto_btn_snes1_5")
        self.barra_btn_snes1_5 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_5.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_snes1_5.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_5.setObjectName("barra_btn_snes1_5")
        self.btn_snes1_6 = QtWidgets.QPushButton(self.barra_btn_snes1_5)
        self.btn_snes1_6.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_6.setFont(font)
        self.btn_snes1_6.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_6.setText("")
        self.btn_snes1_6.setObjectName("btn_snes1_6")
        self.texto_btn_snes1_6 = QtWidgets.QLabel(self.barra_btn_snes1_5)
        self.texto_btn_snes1_6.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_6.setFont(font)
        self.texto_btn_snes1_6.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_6.setObjectName("texto_btn_snes1_6")
        self.barra_btn_snes1_6 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_6.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_snes1_6.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_6.setObjectName("barra_btn_snes1_6")
        self.btn_snes1_7 = QtWidgets.QPushButton(self.barra_btn_snes1_6)
        self.btn_snes1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_7.setFont(font)
        self.btn_snes1_7.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_7.setText("")
        self.btn_snes1_7.setObjectName("btn_snes1_7")
        self.texto_btn_snes1_7 = QtWidgets.QLabel(self.barra_btn_snes1_6)
        self.texto_btn_snes1_7.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_7.setFont(font)
        self.texto_btn_snes1_7.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_7.setObjectName("texto_btn_snes1_7")
        self.barra_btn_snes1_7 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_7.setGeometry(QtCore.QRect(0, 300, 261, 50))
        self.barra_btn_snes1_7.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_7.setObjectName("barra_btn_snes1_7")
        self.btn_snes1_8 = QtWidgets.QPushButton(self.barra_btn_snes1_7)
        self.btn_snes1_8.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_8.setFont(font)
        self.btn_snes1_8.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_8.setText("")
        self.btn_snes1_8.setObjectName("btn_snes1_8")
        self.texto_btn_snes1_8 = QtWidgets.QLabel(self.barra_btn_snes1_7)
        self.texto_btn_snes1_8.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_8.setFont(font)
        self.texto_btn_snes1_8.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_8.setObjectName("texto_btn_snes1_8")
        self.barra_btn_snes1_8 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_8.setGeometry(QtCore.QRect(0, 350, 261, 50))
        self.barra_btn_snes1_8.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_8.setObjectName("barra_btn_snes1_8")
        self.btn_snes1_9 = QtWidgets.QPushButton(self.barra_btn_snes1_8)
        self.btn_snes1_9.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_9.setFont(font)
        self.btn_snes1_9.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_snes1_9.setText("")
        self.btn_snes1_9.setObjectName("btn_snes1_9")
        self.texto_btn_snes1_9 = QtWidgets.QLabel(self.barra_btn_snes1_8)
        self.texto_btn_snes1_9.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_9.setFont(font)
        self.texto_btn_snes1_9.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_snes1_9.setObjectName("texto_btn_snes1_9")
        self.barra_btn_snes1_9 = QtWidgets.QFrame(self.menus_snes)
        self.barra_btn_snes1_9.setGeometry(QtCore.QRect(0, 400, 261, 50))
        self.barra_btn_snes1_9.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_snes1_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes1_9.setObjectName("barra_btn_snes1_9")
        self.btn_snes1_10 = QtWidgets.QPushButton(self.barra_btn_snes1_9)
        self.btn_snes1_10.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes1_10.setFont(font)
        self.btn_snes1_10.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
                                        "    background-color: transparent;\n"
                                        "    background-repeat: no-repeat;\n"
                                        "    background-position: center;\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(30,144,255);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(1,84,149);\n"
                                        "}")
        self.btn_snes1_10.setText("")
        self.btn_snes1_10.setObjectName("btn_snes1_10")
        self.texto_btn_snes1_10 = QtWidgets.QLabel(self.barra_btn_snes1_9)
        self.texto_btn_snes1_10.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_snes1_10.setFont(font)
        self.texto_btn_snes1_10.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.texto_btn_snes1_10.setObjectName("texto_btn_snes1_10")




        # menus da camera------------------------------------------------------>>>
        self.menus_camera = QtWidgets.QFrame(self.menu_esquerda)
        self.menus_camera.setGeometry(QtCore.QRect(-10, 50, 261, 50))
        self.menus_camera.setStyleSheet("QFrame {\n"
                                        "        \n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "QFrame:hover {\n"
                                        "    \n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "}\n"
                                        "QFrame:pressed {\n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "}")
        self.menus_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menus_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menus_camera.setObjectName("menus_camera")
        self.barra_btn_camera1 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1.setGeometry(QtCore.QRect(0, 0, 261, 50))
        self.barra_btn_camera1.setStyleSheet("QFrame {\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QFrame:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.barra_btn_camera1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1.setObjectName("barra_btn_camera1")
        self.btn_camera1 = QtWidgets.QPushButton(self.barra_btn_camera1)
        self.btn_camera1.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.btn_camera1.clicked.connect(self.menuAtivaCamera)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1.setFont(font)
        self.btn_camera1.setStyleSheet("QPushButton {\n"
                                       "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
        self.btn_camera1.setText("")
        self.btn_camera1.setObjectName("btn_camera1")
        self.texto_btn_camera1 = QtWidgets.QLabel(self.barra_btn_camera1)
        self.texto_btn_camera1.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1.setFont(font)
        self.texto_btn_camera1.setStyleSheet("QLabel{\n"
                                             "    background-color: transparent;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "font: 20px SegoeUIl, bold;\n"
                                             "}")
        self.texto_btn_camera1.setObjectName("texto_btn_camera1")
        self.barra_btn_camera1_2 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_2.setGeometry(QtCore.QRect(0, 50, 261, 50))
        self.barra_btn_camera1_2.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_2.setObjectName("barra_btn_camera1_2")
        self.btn_btn_camera1_2 = QtWidgets.QPushButton(self.barra_btn_camera1_2)
        self.btn_btn_camera1_2.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_btn_camera1_2.setFont(font)
        self.btn_btn_camera1_2.setStyleSheet("QPushButton {\n"
                                             "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                             "    background-color: transparent;\n"
                                             "    background-repeat: no-repeat;\n"
                                             "    background-position: center;\n"
                                             "    border: none;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: rgb(30,144,255);\n"
                                             "}\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: rgb(1,84,149);\n"
                                             "}")
        self.btn_btn_camera1_2.setText("")
        self.btn_btn_camera1_2.setObjectName("btn_btn_camera1_2")
        self.texto_btn_camera1_2 = QtWidgets.QLabel(self.barra_btn_camera1_2)
        self.texto_btn_camera1_2.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1_2.setFont(font)
        self.texto_btn_camera1_2.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_camera1_2.setObjectName("texto_btn_camera1_2")
        self.barra_btn_camera1_3 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_3.setGeometry(QtCore.QRect(0, 100, 261, 50))
        self.barra_btn_camera1_3.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_3.setObjectName("barra_btn_camera1_3")
        self.btn_camera1_3 = QtWidgets.QPushButton(self.barra_btn_camera1_3)
        self.btn_camera1_3.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1_3.setFont(font)
        self.btn_camera1_3.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_camera1_3.setText("")
        self.btn_camera1_3.setObjectName("btn_camera1_3")
        self.textobtn_camera1_3 = QtWidgets.QLabel(self.barra_btn_camera1_3)
        self.textobtn_camera1_3.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textobtn_camera1_3.setFont(font)
        self.textobtn_camera1_3.setStyleSheet("QLabel{\n"
                                              "    background-color: transparent;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "font: 20px SegoeUIl, bold;\n"
                                              "}")
        self.textobtn_camera1_3.setObjectName("textobtn_camera1_3")
        self.barra_btn_camera1_4 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_4.setGeometry(QtCore.QRect(0, 150, 261, 50))
        self.barra_btn_camera1_4.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_4.setObjectName("barra_btn_camera1_4")
        self.btn_camera1_4 = QtWidgets.QPushButton(self.barra_btn_camera1_4)
        self.btn_camera1_4.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1_4.setFont(font)
        self.btn_camera1_4.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_camera1_4.setText("")
        self.btn_camera1_4.setObjectName("btn_camera1_4")
        self.texto_btn_camera1_4 = QtWidgets.QLabel(self.barra_btn_camera1_4)
        self.texto_btn_camera1_4.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1_4.setFont(font)
        self.texto_btn_camera1_4.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_camera1_4.setObjectName("texto_btn_camera1_4")
        self.barra_btn_camera1_5 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_5.setGeometry(QtCore.QRect(0, 200, 261, 50))
        self.barra_btn_camera1_5.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_5.setObjectName("barra_btn_camera1_5")
        self.btn_camera1_5 = QtWidgets.QPushButton(self.barra_btn_camera1_5)
        self.btn_camera1_5.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1_5.setFont(font)
        self.btn_camera1_5.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_camera1_5.setText("")
        self.btn_camera1_5.setObjectName("btn_camera1_5")
        self.texto_btn_camera1_5 = QtWidgets.QLabel(self.barra_btn_camera1_5)
        self.texto_btn_camera1_5.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1_5.setFont(font)
        self.texto_btn_camera1_5.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_camera1_5.setObjectName("texto_btn_camera1_5")
        self.barra_btn_camera1_6 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_6.setGeometry(QtCore.QRect(0, 250, 261, 50))
        self.barra_btn_camera1_6.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_6.setObjectName("barra_btn_camera1_6")
        self.btn_camera1_6 = QtWidgets.QPushButton(self.barra_btn_camera1_6)
        self.btn_camera1_6.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1_6.setFont(font)
        self.btn_camera1_6.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_camera1_6.setText("")
        self.btn_camera1_6.setObjectName("btn_camera1_6")
        self.texto_btn_camera1_6 = QtWidgets.QLabel(self.barra_btn_camera1_6)
        self.texto_btn_camera1_6.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1_6.setFont(font)
        self.texto_btn_camera1_6.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_camera1_6.setObjectName("texto_btn_camera1_6")
        self.barra_btn_camera1_7 = QtWidgets.QFrame(self.menus_camera)
        self.barra_btn_camera1_7.setGeometry(QtCore.QRect(0, 300, 261, 50))
        self.barra_btn_camera1_7.setStyleSheet("QFrame {\n"
                                               "    border: none;\n"
                                               "}\n"
                                               "QFrame:hover {\n"
                                               "    background-color: rgb(30,144,255);\n"
                                               "}\n"
                                               "QFrame:pressed {\n"
                                               "    background-color: rgb(1,84,149);\n"
                                               "}")
        self.barra_btn_camera1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera1_7.setObjectName("barra_btn_camera1_7")
        self.btn_camera1_7 = QtWidgets.QPushButton(self.barra_btn_camera1_7)
        self.btn_camera1_7.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera1_7.setFont(font)
        self.btn_camera1_7.setStyleSheet("QPushButton {\n"
                                         "    background-image: url(:/camera/imagens/screenshot-24.png);\n"
                                         "    background-color: transparent;\n"
                                         "    background-repeat: no-repeat;\n"
                                         "    background-position: center;\n"
                                         "    border: none;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(30,144,255);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(1,84,149);\n"
                                         "}")
        self.btn_camera1_7.setText("")
        self.btn_camera1_7.setObjectName("btn_camera1_7")
        self.texto_btn_camera1_7 = QtWidgets.QLabel(self.barra_btn_camera1_7)
        self.texto_btn_camera1_7.setGeometry(QtCore.QRect(60, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.texto_btn_camera1_7.setFont(font)
        self.texto_btn_camera1_7.setStyleSheet("QLabel{\n"
                                               "    background-color: transparent;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "font: 20px SegoeUIl, bold;\n"
                                               "}")
        self.texto_btn_camera1_7.setObjectName("texto_btn_camera1_7")

























        #area principal do layout------------->
        self.area_principal = QtWidgets.QFrame(self.background)
        self.area_principal.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.area_principal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_principal.setObjectName("area_principal")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.area_principal)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.area_visualizcao = QtWidgets.QFrame(self.area_principal)
        self.area_visualizcao.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.area_visualizcao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.area_visualizcao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_visualizcao.setObjectName("area_visualizcao")
        self.verticalLayout_2.addWidget(self.area_visualizcao)
        self.rodape = QtWidgets.QFrame(self.area_principal)
        self.rodape.setMaximumSize(QtCore.QSize(16777215, 30))
        self.rodape.setStyleSheet("")
        self.rodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape.setLineWidth(1)
        self.rodape.setObjectName("rodape")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.rodape)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_rodape_avisos = QtWidgets.QLabel(self.rodape)
        self.label_rodape_avisos.setMinimumSize(QtCore.QSize(0, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_rodape_avisos.setFont(font)
        self.label_rodape_avisos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_rodape_avisos.setText("")
        self.label_rodape_avisos.setObjectName("label_rodape_avisos")
        self.horizontalLayout_3.addWidget(self.label_rodape_avisos)
        self.label_rodape_creditos = QtWidgets.QLabel(self.rodape)
        self.label_rodape_creditos.setEnabled(True)
        self.label_rodape_creditos.setMinimumSize(QtCore.QSize(0, 16))
        self.label_rodape_creditos.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_rodape_creditos.setFont(font)
        self.label_rodape_creditos.setStyleSheet("Qlabel{\n"
"    align: right;\n"
"}")
        self.label_rodape_creditos.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_rodape_creditos.setObjectName("label_rodape_creditos")
        self.horizontalLayout_3.addWidget(self.label_rodape_creditos)
        self.verticalLayout_2.addWidget(self.rodape)
        self.horizontalLayout.addWidget(self.area_principal)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.texto_btn_home.setText(_translate("MainWindow", "home"))
        self.texto_btn_camera1.setText(_translate("MainWindow", "camera "))
        self.texto_btn_camera1_2.setText(_translate("MainWindow", "activate"))
        self.textobtn_camera1_3.setText(_translate("MainWindow", "deep fake"))
        self.texto_btn_camera1_4.setText(_translate("MainWindow", "recognition"))
        self.texto_btn_camera1_5.setText(_translate("MainWindow", "null"))
        self.texto_btn_camera1_6.setText(_translate("MainWindow", "null"))
        self.texto_btn_camera1_7.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_2.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_3.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_5.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_6.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_7.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_8.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_9.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_10.setText(_translate("MainWindow", "hack\'s snes"))
        self.texto_btn_snes1_12.setText(_translate("MainWindow", "telegram bot\'s"))
        self.texto_btn_snes1_13.setText(_translate("MainWindow", "manicomio bot"))
        self.texto_btn_snes1_14.setText(_translate("MainWindow", "chatterbot bot"))
        self.texto_btn_snes1_15.setText(_translate("MainWindow", "deep fake bot"))
        self.texto_btn_snes1_16.setText(_translate("MainWindow", "super mario bot"))
        self.texto_btn_snes1_17.setText(_translate("MainWindow", "contra3 bot"))
        self.texto_btn_snes1_18.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_19.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_20.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_21.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_22.setText(_translate("MainWindow", "servidores"))
        self.texto_btn_snes1_24.setText(_translate("MainWindow", "hacker flask"))
        self.texto_btn_snes1_25.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_27.setText(_translate("MainWindow", "deep fake flask"))
        self.texto_btn_snes1_28.setText(_translate("MainWindow", "site flask"))
        self.texto_btn_snes1_26.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_29.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_30.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_31.setText(_translate("MainWindow", "null"))
        self.texto_btn_snes1_32.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1.setText(_translate("MainWindow", "databases"))
        self.texto_btn_database1_2.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_3.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_4.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_5.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_6.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_7.setText(_translate("MainWindow", "null"))
        self.texto_btn_database1_8.setText(_translate("MainWindow", "null"))
        self.texto_btn_configuracoes1.setText(_translate("MainWindow", "settings"))
        self.texto_btn_configuracoes1_2.setText(_translate("MainWindow", "null"))
        self.texto_btn_configuracoes1_3.setText(_translate("MainWindow", "null"))
        self.texto_btn_configuracoes1_5.setText(_translate("MainWindow", "null"))
        self.texto_btn_configuracoes1_7.setText(_translate("MainWindow", "null"))
        self.texto_btn_configuracoes1_8.setText(_translate("MainWindow", "null"))
        self.label_rodape_creditos.setText(_translate("MainWindow", "manicomio 2020 | @GorpoOrko developer"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())
