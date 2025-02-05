from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys, os
from PyQt5.QtWidgets import QPushButton

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class IntroductionPage(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(IntroductionPage, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_0 = QtWidgets.QLabel("\n\n\n\n\n\n\n\nВступление\nПрограмма предназначена для оценки защищенности информационной системы Вашей компании \nОтметьте галочками пункты, которые соблюдены в Вашей организации", self)
        self.label_0.setAlignment(Qt.AlignCenter)
        self.label_1 = QtWidgets.QLabel("\n\n\n\n\n\n\n\nCoolProgram, 2021-2024", self)
        self.label_1.setAlignment(Qt.AlignCenter)


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_0)
        self.layout.addWidget(self.label_1)
        self.setLayout(self.layout)

    def nextId(self):
        return Wizard.class1

#Процесс 1
#Подпроцесс 1
class ClassesPage1(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage1, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_2 = QtWidgets.QLabel("ПРОЦЕСС I «Обеспечение защиты информации при управлении доступом» \nПодпроцесс «Управление учетными записями и правами субъектов логического доступа»", self)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_3.setAlignment(Qt.AlignLeft)

        self.checkBox_1 = QtWidgets.QCheckBox('  Осуществление логического доступа пользователями и эксплуатационным персоналом под \n  уникальными и  персонифицированными учетными записями')
        self.checkBox_2 = QtWidgets.QCheckBox('  Документарное определение правил предоставления (отзыва) и блокирования логического доступа')
        self.checkBox_3 = QtWidgets.QCheckBox('  Регистрация событий защиты информации, связанных с действиями, и контроль действий \n  эксплуатационного  персонала, обладающего правами по управлению логическим доступом')
        self.checkBox_4 = QtWidgets.QCheckBox('  Закрепление АРМ пользователей и эксплуатационного персонала за конкретными субъектами \n  логического доступа')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.label_3)
        self.layout.addWidget(self.checkBox_1)
        self.layout.addWidget(self.checkBox_2)
        self.layout.addWidget(self.checkBox_3)
        self.layout.addWidget(self.checkBox_4)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4]

    def performance(self):
        self.checkBox_1.stateChanged.connect(self.check)
        self.checkBox_2.stateChanged.connect(self.check)
        self.checkBox_3.stateChanged.connect(self.check)
        self.checkBox_4.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global pp1
        pp1 = mean

    def nextId(self):
        return Wizard.class4

#Подпроцесс 2
class ClassesPage4(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage4, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_6 = QtWidgets.QLabel("ПРОЦЕСС I «Обеспечение защиты информации при управлении доступом» \nПодпроцесс «Идентификация, аутентификация, авторизация \nпри осуществлении логического доступа»", self)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QtWidgets.QLabel("\nСодержание мер системы защиты информации:", self)
        self.label_7.setAlignment(Qt.AlignBottom)

        self.checkBox_5 = QtWidgets.QCheckBox('  Идентификация и однофакторная аутентификация пользователей')
        self.checkBox_6 = QtWidgets.QCheckBox('  Запрет на использование технологии аутентификации с сохранением аутентификационных \n  данных в открытом виде в СВТ')
        self.checkBox_7 = QtWidgets.QCheckBox('  Авторизация логического доступа к ресурсам доступа, в том числе АС')
        self.checkBox_8 = QtWidgets.QCheckBox('  Регистрация выполнения субъектами логического доступа ряда неуспешных последовательных \n  попыток аутентификации')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_6)
        self.layout.addWidget(self.label_7)
        self.layout.addWidget(self.checkBox_5)
        self.layout.addWidget(self.checkBox_6)
        self.layout.addWidget(self.checkBox_7)
        self.layout.addWidget(self.checkBox_8)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8]

    def performance(self):
        self.checkBox_5.stateChanged.connect(self.check)
        self.checkBox_6.stateChanged.connect(self.check)
        self.checkBox_7.stateChanged.connect(self.check)
        self.checkBox_8.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global pp2
        pp2 = mean

    def nextId(self):
        return Wizard.class8

#Подпроцесс 3
class ClassesPage8(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage8, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_10 = QtWidgets.QLabel("ПРОЦЕСС I «Обеспечение защиты информации при управлении доступом» \nПодпроцесс «Защита информации при осуществлении физического доступа»", self)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_11.setAlignment(Qt.AlignBottom)

        self.checkBox_9 = QtWidgets.QCheckBox('  Документарное определение правил предоставления физического доступа')
        self.checkBox_10 = QtWidgets.QCheckBox('  Регистрация доступа к общедоступным объектам доступа с использованием средств \n  видеонаблюдения')
        self.checkBox_11 = QtWidgets.QCheckBox('  Контроль состояния общедоступных объектов доступа с целью выявлений несанкционированных \n  изменений в их аппаратном обеспечении и/или ПО')
        self.checkBox_12 = QtWidgets.QCheckBox('  Регистрация событий защиты информации, связанных с входом (выходом) в помещения \n  (из помещений), в которых  расположены объекты доступа')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_10)
        self.layout.addWidget(self.label_11)
        self.layout.addWidget(self.checkBox_9)
        self.layout.addWidget(self.checkBox_10)
        self.layout.addWidget(self.checkBox_11)
        self.layout.addWidget(self.checkBox_12)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_9, self.checkBox_10, self.checkBox_11, self.checkBox_12]

    def performance(self):
        self.checkBox_9.stateChanged.connect(self.check)
        self.checkBox_10.stateChanged.connect(self.check)
        self.checkBox_11.stateChanged.connect(self.check)
        self.checkBox_12.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global pp3
        pp3 = mean

    def nextId(self):
        return Wizard.class10

#Подпроцесс 4
class ClassesPage10(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage10, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_14 = QtWidgets.QLabel("ПРОЦЕСС I «Обеспечение защиты информации при управлении доступом» \nПодпроцесс «Идентификация и учет ресурсов и объектов доступа»", self)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_15.setAlignment(Qt.AlignBottom)

        self.checkBox_13 = QtWidgets.QCheckBox('  Учет созданных, используемых и/или эксплуатируемых ресурсов доступа')
        self.checkBox_14 = QtWidgets.QCheckBox('  Учет используемых и/или эксплуатируемых объектов доступа')
        self.checkBox_15 = QtWidgets.QCheckBox('  Учет эксплуатируемых общедоступных объектов доступа (в том числе банкоматов, \n  платежных терминалов)')
        self.checkBox_16 = QtWidgets.QCheckBox('  Регистрация событий защиты информации, связанных с подключением (регистрацией) \n  объектов доступа в вычислительных сетях финансовой организации')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_14)
        self.layout.addWidget(self.label_15)
        self.layout.addWidget(self.checkBox_13)
        self.layout.addWidget(self.checkBox_14)
        self.layout.addWidget(self.checkBox_15)
        self.layout.addWidget(self.checkBox_16)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16]

    def performance(self):
        self.checkBox_13.stateChanged.connect(self.check)
        self.checkBox_14.stateChanged.connect(self.check)
        self.checkBox_15.stateChanged.connect(self.check)
        self.checkBox_16.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global pp4
        pp4 = mean

    def nextId(self):
        global res1
        res1 = (float(pp1) + float(pp2) + float(pp3) + float(pp4)) / 4

        return Wizard.class11

#Процесс 2
#Подпроцесс 1
class ClassesPage11(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage11, self).__init__(*args, **kwargs)
        super(ClassesPage11, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_18 = QtWidgets.QLabel("ПРОЦЕСС II «Обеспечение защиты вычислительных сетей» \nПодроцесс «Сегментация и межсетевое экранирование вычислительных сетей»", self)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_19.setAlignment(Qt.AlignBottom)

        self.checkBox_17 = QtWidgets.QCheckBox('  Межсетевое экранирование вычислительных сетей сегментов контуров безопасности, включая фильтрацию данных на сетевом \n  и прикладном уровнях семиуровневой стандартной модели взаимодействия открытых систем, определенной в\n  ГОСТ Р ИСО/МЭК 7498-1')
        self.checkBox_18 = QtWidgets.QCheckBox('  Реализация запрета сетевого взаимодействия сегмента разработки и тестирования и иных внутренних вычислительных сетей \n  финансовой организации по инициативе сегмента разработки и тестирования')
        self.checkBox_19 = QtWidgets.QCheckBox('  Контроль содержимого информации при ее переносе из сегментов или в сегменты контуров безопасности с использованием \n  переносных (отчуждаемых) носителей информации')
        self.checkBox_20 = QtWidgets.QCheckBox('  Реализация сетевого взаимодействия внутренних вычислительных сетей финансовой организации и сети Интернет через \n  ограниченное количество контролируемых точек доступа')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_18)
        self.layout.addWidget(self.label_19)
        self.layout.addWidget(self.checkBox_17)
        self.layout.addWidget(self.checkBox_18)
        self.layout.addWidget(self.checkBox_19)
        self.layout.addWidget(self.checkBox_20)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_17, self.checkBox_18, self.checkBox_19, self.checkBox_20]

    def performance(self):
        self.checkBox_17.stateChanged.connect(self.check)
        self.checkBox_18.stateChanged.connect(self.check)
        self.checkBox_19.stateChanged.connect(self.check)
        self.checkBox_20.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global p2p1
        p2p1 = mean

    def nextId(self):
        return Wizard.class12

#Подпроцесс 2
class ClassesPage12(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage12, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_22 = QtWidgets.QLabel("ПРОЦЕСС II «Обеспечение защиты вычислительных сетей» \nПодпроцесс «Выявление вторжений и сетевых атак»", self)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_23.setAlignment(Qt.AlignBottom)

        self.checkBox_21 = QtWidgets.QCheckBox('  Контроль отсутствия (выявление) аномальной сетевой активности, связанной с возможным несанкционированным \n  информационным взаимодействием между вычислительными сетями финансовой организации и сетью Интернет')
        self.checkBox_22 = QtWidgets.QCheckBox('  Контроль отсутствия (выявление) аномальной сетевой активности, связанной с возможным несанкционированным \n  удаленным доступом')
        self.checkBox_23 = QtWidgets.QCheckBox('  Блокирование атак типа «отказ в обслуживании» в масштабе времени, близком к реальному')
        self.checkBox_24 = QtWidgets.QCheckBox('  Контроль и обеспечение возможности блокировки нежелательных сообщений электронной почты (SPAM)')
    
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_22)
        self.layout.addWidget(self.label_23)
        self.layout.addWidget(self.checkBox_21)
        self.layout.addWidget(self.checkBox_22)
        self.layout.addWidget(self.checkBox_23)
        self.layout.addWidget(self.checkBox_24)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_21, self.checkBox_22, self.checkBox_23, self.checkBox_24]

    def performance(self):
        self.checkBox_21.stateChanged.connect(self.check)
        self.checkBox_22.stateChanged.connect(self.check)
        self.checkBox_23.stateChanged.connect(self.check)
        self.checkBox_24.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global p2p2
        p2p2 = mean

    def nextId(self):
        return Wizard.class13

#Подпроцесс 3
class ClassesPage13(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage13, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_26 = QtWidgets.QLabel("ПРОЦЕСС II «Обеспечение защиты вычислительных сетей» \nПодпроцесс «Защита информации, передаваемой по вычислительным сетям»", self)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_27.setAlignment(Qt.AlignBottom)

        self.checkBox_25 = QtWidgets.QCheckBox('  Применение сетевых протоколов, обеспечивающих защиту подлинности сетевого соединения, контроль целостности \n  сетевого взаимодействия и реализацию технологии двухсторонней аутентификации при осуществлении логического \n  доступа с использованием телекоммуникационных каналов и/или линий связи, не контролируемых финансовой организацией')
        self.checkBox_26 = QtWidgets.QCheckBox('  Реализация защиты информации от раскрытия и модификации, применение двухсторонней аутентификации при ее \n  передаче с использованием сети Интернет, телекоммуникационных каналов и/или линий связи, не контролируемых \n  финансовой организацией')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_26)
        self.layout.addWidget(self.label_27)
        self.layout.addWidget(self.checkBox_25)
        self.layout.addWidget(self.checkBox_26)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_25, self.checkBox_26]

    def performance(self):
        self.checkBox_25.stateChanged.connect(self.check)
        self.checkBox_26.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 2

        global p2p3
        p2p3 = mean

    def nextId(self):
        return Wizard.class14

# Подпроцесс 4
class ClassesPage14(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage14, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_30 = QtWidgets.QLabel("ПРОЦЕСС II «Обеспечение защиты вычислительных сетей» \nПодпроцесс «Защита беспроводных сетей»", self)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_31.setAlignment(Qt.AlignBottom)

        self.checkBox_27 = QtWidgets.QCheckBox('  Размещение технических средств, реализующих функции беспроводного соединения, в выделенных сегментах \n  вычислительных сетей финансовой организации')
        self.checkBox_28 = QtWidgets.QCheckBox('  Межсетевое экранирование внутренних вычислительных сетей финансовой организации и сегментов вычисленных \n  сетей, включая фильтрацию данных на сетевом и прикладном уровнях семиуровневой стандартной модели \n  взаимодействия открытых систем')
        self.checkBox_29 = QtWidgets.QCheckBox('  Блокирование попыток подключения к беспроводным точкам доступа с незарегистрированных устройств доступа, \n  в том числе из-за пределов зданий и сооружений финансовой организации')
        self.checkBox_30 = QtWidgets.QCheckBox('  Регистрация попыток подключения к беспроводным точкам доступа с незарегистрированных устройств доступа, \n  в том числе из-за пределов финансовой организации')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_30)
        self.layout.addWidget(self.label_31)
        self.layout.addWidget(self.checkBox_27)
        self.layout.addWidget(self.checkBox_28)
        self.layout.addWidget(self.checkBox_29)
        self.layout.addWidget(self.checkBox_30)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_27, self.checkBox_28, self.checkBox_29, self.checkBox_30]

    def performance(self):
        self.checkBox_27.stateChanged.connect(self.check)
        self.checkBox_28.stateChanged.connect(self.check)
        self.checkBox_29.stateChanged.connect(self.check)
        self.checkBox_30.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global p2p4
        p2p4 = mean
        
    def nextId(self):
        global res2
        res2 = (float(p2p1) + float(p2p2) + float(p2p3) + float(p2p4)) / 4
        
        return Wizard.class15

#Процесс 3
class ClassesPage15(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage15, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_34 = QtWidgets.QLabel("ПРОЦЕСС III «Контроль целостности и защищенности информационной инфраструктуры»\n", self)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_35 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_35.setAlignment(Qt.AlignBottom)

        self.checkBox_31 = QtWidgets.QCheckBox('  Контроль отсутствия и обеспечение оперативного устранения известных (описанных) уязвимостей защиты информации,\n  использование которых может позволить осуществить несанкционированное (неконтролируемое) информационное \n  взаимодействие между сегментами контуров безопасности и иными внутренними сетями финансовой организации')
        self.checkBox_32 = QtWidgets.QCheckBox('  Контроль отсутствия и обеспечение оперативного устранения известных (описанных) уязвимостей защиты информации,\n  использование которых может позволить осуществить несанкционированный удаленный доступ')
        self.checkBox_33 = QtWidgets.QCheckBox('  Обеспечение возможности восстановления эталонных копий ПО АС, ПО средств и систем защиты информации, системного\n  ПО в случаях нештатных ситуаций')
        self.checkBox_34 = QtWidgets.QCheckBox('  Контроль состава ПО АРМ пользователей и эксплуатационного персонала, запускаемого при загрузке операционной системы')
        self.checkBox_35 = QtWidgets.QCheckBox('  Регистрация результатов выполнения операций по контролю целостности и достоверности источников получения при\n  распространении и/или обновлении ПО АС, ПО средств и систем защиты информации, системного ПО')
       
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_34)
        self.layout.addWidget(self.label_35)
        self.layout.addWidget(self.checkBox_31)
        self.layout.addWidget(self.checkBox_32)
        self.layout.addWidget(self.checkBox_33)
        self.layout.addWidget(self.checkBox_34)
        self.layout.addWidget(self.checkBox_35)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_31, self.checkBox_32, self.checkBox_33, self.checkBox_34, self.checkBox_35]

    def performance(self):
        self.checkBox_31.stateChanged.connect(self.check)
        self.checkBox_32.stateChanged.connect(self.check)
        self.checkBox_33.stateChanged.connect(self.check)
        self.checkBox_34.stateChanged.connect(self.check)
        self.checkBox_35.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 5

        global res3
        res3 = mean

    def nextId(self):
        return Wizard.class16

#Процесс 4
class ClassesPage16(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage16, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_38 = QtWidgets.QLabel("ПРОЦЕСС IV «Защита от вредоносного кода»\n", self)
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_39 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_39.setAlignment(Qt.AlignBottom)

        self.checkBox_36 = QtWidgets.QCheckBox('  Реализация защиты от вредоносного кода на уровне виртуальной информационной инфраструктуры')
        self.checkBox_37 = QtWidgets.QCheckBox('  Реализация защиты от вредоносного кода на уровне контроля почтового трафика')
        self.checkBox_38 = QtWidgets.QCheckBox('  Контроль отключения и своевременного обновления средств защиты от вредоносного кода')
        self.checkBox_39 = QtWidgets.QCheckBox('  Регистрация операций по проведению проверок на отсутствие вредоносного кода')
        self.checkBox_40 = QtWidgets.QCheckBox('  Регистрация нарушений целостности программных компонентов средств защиты от вредоносного кода')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_38)
        self.layout.addWidget(self.label_39)
        self.layout.addWidget(self.checkBox_36)
        self.layout.addWidget(self.checkBox_37)
        self.layout.addWidget(self.checkBox_38)
        self.layout.addWidget(self.checkBox_39)
        self.layout.addWidget(self.checkBox_40)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_36, self.checkBox_37, self.checkBox_38, self.checkBox_39, self.checkBox_40]

    def performance(self):
        self.checkBox_36.stateChanged.connect(self.check)
        self.checkBox_37.stateChanged.connect(self.check)
        self.checkBox_38.stateChanged.connect(self.check)
        self.checkBox_39.stateChanged.connect(self.check)
        self.checkBox_40.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 5

        global res4
        res4 = mean

    def nextId(self):
        return Wizard.class17

#Процесс 5
class ClassesPage17(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage17, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_42 = QtWidgets.QLabel("ПРОЦЕСС V «Предотвращение утечек информации»\n", self)
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_43 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_43.setAlignment(Qt.AlignBottom)

        self.checkBox_41 = QtWidgets.QCheckBox('  Блокирование неразрешенной и контроль (анализ) разрешенной передачи информации конфиденциального характера\n  на внешние адреса электронной почты')
        self.checkBox_42 = QtWidgets.QCheckBox('  Ведение единого архива электронных сообщений с архивным доступом на срок не менее 6 мес и оперативным доступом\n  на срок не менее 1 мес')
        self.checkBox_43 = QtWidgets.QCheckBox('  Ограничение на размеры файлов данных, передаваемых в качестве вложений в сообщения электронной почты')
        self.checkBox_44 = QtWidgets.QCheckBox('  Шифрование информации конфиденциального характера при ее хранении на МНИ, выносимых за пределы финансовой\n  организации')
        self.checkBox_45 = QtWidgets.QCheckBox('  Регистрация операций, связанных с осуществлением доступа работниками финансовой организации к ресурсам сети Интернет')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_42)
        self.layout.addWidget(self.label_43)
        self.layout.addWidget(self.checkBox_41)
        self.layout.addWidget(self.checkBox_42)
        self.layout.addWidget(self.checkBox_43)
        self.layout.addWidget(self.checkBox_44)
        self.layout.addWidget(self.checkBox_45)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_41, self.checkBox_42, self.checkBox_43, self.checkBox_44, self.checkBox_45]

    def performance(self):
        self.checkBox_41.stateChanged.connect(self.check)
        self.checkBox_42.stateChanged.connect(self.check)
        self.checkBox_43.stateChanged.connect(self.check)
        self.checkBox_44.stateChanged.connect(self.check)
        self.checkBox_45.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 5

        global res5
        res5 = mean

    def nextId(self):
        return Wizard.class18

#Процесс 6
#Подпроцесс 1
class ClassesPage18(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage18, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_46 = QtWidgets.QLabel("ПРОЦЕСС VI «Управление инцидентами защиты информации»\nПодпроцесс «Мониторинг и анализ событий защиты информации»", self)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_47.setAlignment(Qt.AlignBottom)

        self.checkBox_46 = QtWidgets.QCheckBox('  Организация мониторинга данных регистрации о событиях защиты информации, формируемых техническими мерами,\n  входящими в состав системы защиты информации')
        self.checkBox_47 = QtWidgets.QCheckBox('  Резервирование необходимого объема памяти для хранения данных регистрации о событиях защиты информации')
        self.checkBox_48 = QtWidgets.QCheckBox('  Обеспечение возможности определения состава действий и/или операций конкретного субъекта доступа')
        self.checkBox_49 = QtWidgets.QCheckBox('  Регистрация нарушений и сбоев в формировании и сборе данных о событиях защиты информации')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_46)
        self.layout.addWidget(self.label_47)
        self.layout.addWidget(self.checkBox_46)
        self.layout.addWidget(self.checkBox_47)
        self.layout.addWidget(self.checkBox_48)
        self.layout.addWidget(self.checkBox_49)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_46, self.checkBox_47, self.checkBox_48, self.checkBox_49]

    def performance(self):
        self.checkBox_46.stateChanged.connect(self.check)
        self.checkBox_47.stateChanged.connect(self.check)
        self.checkBox_48.stateChanged.connect(self.check)
        self.checkBox_49.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global p6p1
        p6p1 = mean

    def nextId(self):
        return Wizard.class19

#Подпроцесс 2
class ClassesPage19(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage19, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_50 = QtWidgets.QLabel("ПРОЦЕСС VI «Управление инцидентами защиты информации»\nПодпроцесс «Обнаружение инцидентов защиты информации и реагирование на них»", self)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_51 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_51.setAlignment(Qt.AlignBottom)

        self.checkBox_50 = QtWidgets.QCheckBox('  Регистрация информации о событиях защиты информации, потенциально связанных с инцидентами\n  защиты информации, в том числе НСД, выявленными в рамках мониторинга и анализа событий защиты информации')
        self.checkBox_51 = QtWidgets.QCheckBox('  Установление и применение единых правил реагирования на инциденты защиты информации')
        self.checkBox_52 = QtWidgets.QCheckBox('  Реализация защиты информации об инцидентах защиты информации от НСД, обеспечение целостности и доступности\n  указанной информации')
        self.checkBox_53 = QtWidgets.QCheckBox('  Регистрация доступа к информации об инцидентах защиты информации')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_50)
        self.layout.addWidget(self.label_51)
        self.layout.addWidget(self.checkBox_50)
        self.layout.addWidget(self.checkBox_51)
        self.layout.addWidget(self.checkBox_52)
        self.layout.addWidget(self.checkBox_53)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_50, self.checkBox_51, self.checkBox_52, self.checkBox_53]

    def performance(self):
        self.checkBox_50.stateChanged.connect(self.check)
        self.checkBox_51.stateChanged.connect(self.check)
        self.checkBox_52.stateChanged.connect(self.check)
        self.checkBox_53.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global p6p2
        p6p2 = mean
        
    def nextId(self):
        global res6
        res6 = (float(p6p1) + float(p6p2)) / 2

        return Wizard.class20

#Процесс 7
class ClassesPage20(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage20, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_54 = QtWidgets.QLabel("ПРОЦЕСС VII «Защита среды виртуализации»\n", self)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_55 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_55.setAlignment(Qt.AlignBottom)

        self.checkBox_54 = QtWidgets.QCheckBox('  Разграничение и контроль осуществления одновременного доступа к виртуальным машинам с АРМ пользователей и\n  эксплуатационного персонала только в пределах одного контура безопасности')
        self.checkBox_55 = QtWidgets.QCheckBox('  Выделение в вычислительных сетях финансовой организации отдельных сегментов (групп сегментов), в том числе\n  виртуальных, используемых для размещения совокупности виртуальных машин, предназначенных для размещения\n  серверных компонент АС, включенных в разные контуры безопасности')
        self.checkBox_56 = QtWidgets.QCheckBox('  Регламентация и контроль выполнения:\n  - операций в рамках жизненного цикла базовых образов виртуальных машин;\n  - операций по копированию образов виртуальных машин')
        self.checkBox_57 = QtWidgets.QCheckBox('  Регистрация операций, связанных с запуском (остановкой) виртуальных машин')
        self.checkBox_58 = QtWidgets.QCheckBox('  Регистрация операций, связанных с изменением настроек технических мер защиты информации, используемых для\n  обеспечения защиты виртуальных машин')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_54)
        self.layout.addWidget(self.label_55)
        self.layout.addWidget(self.checkBox_54)
        self.layout.addWidget(self.checkBox_55)
        self.layout.addWidget(self.checkBox_56)
        self.layout.addWidget(self.checkBox_57)
        self.layout.addWidget(self.checkBox_58)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_54, self.checkBox_55, self.checkBox_56, self.checkBox_57, self.checkBox_58]

    def performance(self):
        self.checkBox_54.stateChanged.connect(self.check)
        self.checkBox_55.stateChanged.connect(self.check)
        self.checkBox_56.stateChanged.connect(self.check)
        self.checkBox_57.stateChanged.connect(self.check)
        self.checkBox_58.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 5

        global res7
        res7 = mean

    def nextId(self):
        return Wizard.class21

#Процесс 8
class ClassesPage21(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesPage21, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_58 = QtWidgets.QLabel("ПРОЦЕСС VIII «Защита информации при осуществлении удаленного логического доступа\nс использованием мобильных (переносных) устройств»", self)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_59 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_59.setAlignment(Qt.AlignBottom)

        self.checkBox_59 = QtWidgets.QCheckBox('  Определение правил удаленного доступа и перечня ресурсов доступа, к которым предоставляется удаленный доступ')
        self.checkBox_60 = QtWidgets.QCheckBox('  Запрет прямого сетевого взаимодействия мобильных (переносных) устройств доступа и внутренних сетей финансовой\n  организации на уровне выше второго (канальный) по семиуровневой стандартной модели взаимодействия открытых систем,\n  определенной в ГОСТ Р ИСО/МЭК 7498-1')
        self.checkBox_61 = QtWidgets.QCheckBox('  Обеспечение защиты мобильных (переносных) устройств от воздействий вредоносного кода')
        self.checkBox_62 = QtWidgets.QCheckBox('  Контентный анализ информации, передаваемой мобильными (переносными) устройствами в сеть Интернет с использованием\n  информационной инфраструктуры финансовой организации')
        self.checkBox_63 = QtWidgets.QCheckBox('  Реализация и контроль информационного взаимодействия внутренних вычислительных сетей финансовой организации и\n  мобильных (переносных) устройств в соответствии с установленными правилами и протоколами сетевого взаимодействия')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_58)
        self.layout.addWidget(self.label_59)
        self.layout.addWidget(self.checkBox_59)
        self.layout.addWidget(self.checkBox_60)
        self.layout.addWidget(self.checkBox_61)
        self.layout.addWidget(self.checkBox_62)
        self.layout.addWidget(self.checkBox_63)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_59, self.checkBox_60, self.checkBox_61, self.checkBox_62, self.checkBox_63]

    def performance(self):
        self.checkBox_59.stateChanged.connect(self.check)
        self.checkBox_60.stateChanged.connect(self.check)
        self.checkBox_61.stateChanged.connect(self.check)
        self.checkBox_62.stateChanged.connect(self.check)
        self.checkBox_63.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 5

        global res8
        res8 = mean

    def nextId(self):
        return Wizard.classDirection1

#Направление 1
class ClassesDirection1(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesDirection1, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_62 = QtWidgets.QLabel("Оценка по направлениям ЗИ системы организации и управления ЗИ\nНАПРАВЛЕНИЕ I «Планирование процесса системы защиты информации»", self)
        self.label_62.setAlignment(Qt.AlignCenter)
        self.label_63 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_63.setAlignment(Qt.AlignBottom)

        self.checkBox_64 = QtWidgets.QCheckBox('  Документарное определение области применения процесса системы защиты информации для уровней информационной \n  инфраструктуры')
        self.checkBox_65 = QtWidgets.QCheckBox('  Документарное определение состава (с указанием соответствия настоящему стандарту) и содержания организационных \n  мер защиты информации, выбранных финансовой организацией и реализуемых в рамках процесса системы защиты\n  информации')
        self.checkBox_66 = QtWidgets.QCheckBox('  Документарное определение порядка применения организационных мер защиты информации, реализуемых в рамках \n  процесса системы защиты информации')
        self.checkBox_67 = QtWidgets.QCheckBox('  Документарное определение состава (с указанием соответствия настоящему стандарту) и содержания технических мер \n  защиты информации, выбранных финансовой организацией и реализуемых в рамках процесса системы защиты информации')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_62)
        self.layout.addWidget(self.label_63)
        self.layout.addWidget(self.checkBox_64)
        self.layout.addWidget(self.checkBox_65)
        self.layout.addWidget(self.checkBox_66)
        self.layout.addWidget(self.checkBox_67)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_64, self.checkBox_65, self.checkBox_66, self.checkBox_67]

    def performance(self):
        self.checkBox_64.stateChanged.connect(self.check)
        self.checkBox_65.stateChanged.connect(self.check)
        self.checkBox_66.stateChanged.connect(self.check)
        self.checkBox_67.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global n1
        n1 = mean

    def nextId(self):
        return Wizard.classDirection2

#Направление 2
class ClassesDirection2(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesDirection2, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_66 = QtWidgets.QLabel("Оценка по направлениям ЗИ системы организации и управления ЗИ\nНАПРАВЛЕНИЕ II «Реализация процесса системы защиты информации»", self)
        self.label_66.setAlignment(Qt.AlignCenter)
        self.label_67 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_67.setAlignment(Qt.AlignBottom)

        self.checkBox_68 = QtWidgets.QCheckBox('  Размещение и настройка (конфигурирование) технических мер защиты информации в информационной инфраструктуре \n  финансовой организации')
        self.checkBox_69 = QtWidgets.QCheckBox('  Определение лиц, которым разрешены действия по внесению изменений в конфигурацию информационной инфраструктуры')
        self.checkBox_70 = QtWidgets.QCheckBox('  Обеспечение возможности сопровождения технических мер защиты информации в течение всего срока их использования')
        self.checkBox_71 = QtWidgets.QCheckBox('  Применение сертифицированных по требованиям безопасности информации средств защиты информации не ниже 6 класса')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_66)
        self.layout.addWidget(self.label_67)
        self.layout.addWidget(self.checkBox_68)
        self.layout.addWidget(self.checkBox_69)
        self.layout.addWidget(self.checkBox_70)
        self.layout.addWidget(self.checkBox_71)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_68, self.checkBox_69, self.checkBox_70, self.checkBox_71]

    def performance(self):
        self.checkBox_68.stateChanged.connect(self.check)
        self.checkBox_69.stateChanged.connect(self.check)
        self.checkBox_70.stateChanged.connect(self.check)
        self.checkBox_71.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global n2
        n2 = mean

    def nextId(self):
        return Wizard.classDirection3

#Направление 3
class ClassesDirection3(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesDirection3, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_70 = QtWidgets.QLabel("Оценка по направлениям ЗИ системы организации и управления ЗИ\nНАПРАВЛЕНИЕ III «Контроль процесса системы защиты информации»", self)
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_71 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_71.setAlignment(Qt.AlignBottom)

        self.checkBox_72 = QtWidgets.QCheckBox('  Периодический контроль (тестирование) полноты реализации технических мер защиты информации')
        self.checkBox_73 = QtWidgets.QCheckBox('  Проведение проверок знаний работников финансовой организации в части применения мер защиты информации в рамках \n  процесса системы защиты информации')
        self.checkBox_74 = QtWidgets.QCheckBox('  Регистрация операций по установке и/или обновлению ПО технических средств защиты информации')
        self.checkBox_75 = QtWidgets.QCheckBox('  Регистрация сбоев (отказов) технических мер защиты информации')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_70)
        self.layout.addWidget(self.label_71)
        self.layout.addWidget(self.checkBox_72)
        self.layout.addWidget(self.checkBox_73)
        self.layout.addWidget(self.checkBox_74)
        self.layout.addWidget(self.checkBox_75)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_72, self.checkBox_73, self.checkBox_74, self.checkBox_75]

    def performance(self):
        self.checkBox_72.stateChanged.connect(self.check)
        self.checkBox_73.stateChanged.connect(self.check)
        self.checkBox_74.stateChanged.connect(self.check)
        self.checkBox_75.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global n3
        n3 = mean

    def nextId(self):
        return Wizard.classDirection4

#Направление 4
class ClassesDirection4(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesDirection4, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_74 = QtWidgets.QLabel("Оценка по направлениям ЗИ системы организации и управления ЗИ\nНАПРАВЛЕНИЕ IV «Совершенствование процесса системы защиты информации»", self)
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_75 = QtWidgets.QLabel("\n\nСодержание мер системы защиты информации:", self)
        self.label_75.setAlignment(Qt.AlignBottom)

        self.checkBox_76 = QtWidgets.QCheckBox('  Проведение и фиксация результатов (свидетельств) анализа необходимости совершенствования процесса системы защиты \n  информации в случаях: \n  - обнаружения инцидентов защиты информации; \n  - обнаружения недостатков в рамках контроля системы защиты информации')
        self.checkBox_77 = QtWidgets.QCheckBox('  Проведение и фиксация результатов (свидетельств) анализа необходимости совершенствования процесса системы защиты \n  информации в случаях изменения политики финансовой организации в отношении: \n  - области применения процесса системы защиты информации; \n  - основных принципов и приоритетов в реализации процесса системы защиты информации; \n  - целевых показателей величины допустимого остаточного операционного риска (риск-аппетита), связанного с обеспечением \n  безопасности информации')
        self.checkBox_78 = QtWidgets.QCheckBox('  Проведение и фиксация результатов (свидетельств) анализа необходимости совершенствования процесса системы защиты \n  информации в случаях: \n  - изменений требований к защите информации, определенных правилами платежной системы; \n  - изменений, внесенных в законодательство Российской Федерации, в том числе нормативные акты Банка России')
        self.checkBox_79 = QtWidgets.QCheckBox('  Фиксация решений о проведении совершенствования процесса системы защиты информации в виде корректирующих или \n  превентивных действий, например: \n  - пересмотр области применения процесса системы защиты информации; \n  - пересмотр состава и содержания организационных мер защиты информации, применяемых в рамках процесса системы \n  защиты информации; \n  - пересмотр состава технических мер защиты информации, применяемых в рамках процесса системы защиты информации')
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_74)
        self.layout.addWidget(self.label_75)
        self.layout.addWidget(self.checkBox_76)
        self.layout.addWidget(self.checkBox_77)
        self.layout.addWidget(self.checkBox_78)
        self.layout.addWidget(self.checkBox_79)
        self.setLayout(self.layout)

        self.performance()
        self.listCheckBox = [self.checkBox_76, self.checkBox_77, self.checkBox_78, self.checkBox_79]

    def performance(self):
        self.checkBox_76.stateChanged.connect(self.check)
        self.checkBox_77.stateChanged.connect(self.check)
        self.checkBox_78.stateChanged.connect(self.check)
        self.checkBox_79.stateChanged.connect(self.check)

    def check(self):
        a = 0
        for checkBox in self.listCheckBox:
            if checkBox.isChecked():
                a += 1
        mean = a / 4

        global n4
        n4 = mean

    def nextId(self):
        global res9
        res9 = (float(n1) + float(n2) + float(n3) + float(n4)) / 4

        global res10
        res10 = float(res1) + float(res2) + float(res3) + float(res4) + float(res5) + float(
            res6) + float(res7) + float(res8) + float(res9)
        res10 = res10 / 9

        return Wizard.classLastPage2


# итоговые расчеты
class ClassesLastPage2(QtWidgets.QWizardPage):
    def __init__(self, *args, **kwargs):
        super(ClassesLastPage2, self).__init__(*args, **kwargs)

        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        self.setFont(font)

        self.label_74 = QtWidgets.QLabel('Итоговые расчеты оценки\n\n\n', self)
        self.label_74.setAlignment(Qt.AlignCenter)

        self.label_75 = QtWidgets.QLabel('Итоговая оценка защищенности информационной системы:\n', self)
        self.label_75.setAlignment(Qt.AlignBottom)
        self.button = QPushButton('Показать', self)
        self.button.setFixedWidth(130)
        self.button.setFixedHeight(22)
        self.button.setStyleSheet("border: 1px solid gray;")

        self.label_res = QtWidgets.QLabel('\n\n')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label_74)
        self.layout.addWidget(self.label_75)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label_res)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        
        if res10 == 1:
            self.label_res.setText(
                '\n1 — ПЯТЫЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(0, 197, 0)")
        elif res10 == 0:
            self.label_res.setText(
                '\n0 — НУЛЕВОЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(255, 0, 0)")
        elif 0 < res10 <= 0.5:
            self.label_res.setText('\n' + str(
                round(res10, 2)) + ' — ПЕРВЫЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(235, 87, 0)")
        elif 0.5 < res10 <= 0.7:
            self.label_res.setText('\n' + str(
                round(res10, 2)) + ' — ВТОРОЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(255, 128, 0)")
        elif 0.7 < res10 <= 0.85:
            self.label_res.setText('\n' + str(
                round(res10, 2)) + ' — ТРЕТИЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(255, 255, 0)")
        elif 0.85 < res10 <= 0.9:
            self.label_res.setText('\n' + str(
                round(res10, 2)) + ' — ЧЕТВЕРТЫЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(102, 255, 0)")
        elif 0.9 < res10 < 1:
            self.label_res.setText('\n' + str(
                round(res10, 2)) + ' — ПЯТЫЙ УРОВЕНЬ СООТВЕТСТВИЯ')
            self.label_res.setStyleSheet("color: rgb(0, 197, 0)")

    def nextId(self):
        return Wizard.classLastPage2

class Wizard(QtWidgets.QWizard):
    num_of_pages = 27
    (intro, class1, class2, class3, class4, class5, class6, class7, class8, class9, class10, class11, class12, class13,
     class14, class15, class16, class17, class18, class19, class20, class21, classDirection1, classDirection2, classDirection3,
     classDirection4, classLastPage2) = range(num_of_pages)

    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.setPage(self.intro, IntroductionPage(self))
        self.setPage(self.class1, ClassesPage1(self))
        self.setPage(self.class4, ClassesPage4(self))
        self.setPage(self.class8, ClassesPage8(self))
        self.setPage(self.class10, ClassesPage10(self))
        self.setPage(self.class11, ClassesPage11(self))
        self.setPage(self.class12, ClassesPage12(self))
        self.setPage(self.class13, ClassesPage13(self))
        self.setPage(self.class14, ClassesPage14(self))
        self.setPage(self.class15, ClassesPage15(self))
        self.setPage(self.class16, ClassesPage16(self))
        self.setPage(self.class17, ClassesPage17(self))
        self.setPage(self.class18, ClassesPage18(self))
        self.setPage(self.class19, ClassesPage19(self))
        self.setPage(self.class20, ClassesPage20(self))
        self.setPage(self.class21, ClassesPage21(self))
        self.setPage(self.classDirection1, ClassesDirection1(self))
        self.setPage(self.classDirection2, ClassesDirection2(self))
        self.setPage(self.classDirection3, ClassesDirection3(self))
        self.setPage(self.classDirection4, ClassesDirection4(self))
        self.setPage(self.classLastPage2, ClassesLastPage2(self))
        self.setStartId(self.intro)

StyleSheet = '''
QWidget {
    background-color: rgb(0, 0, 30);
}
QWizardPage {
    color: rgb(206, 206, 206);
}
QLineEdit {
    color: rgb(28, 28, 28);
    font-size: 15px;
    border: 1px solid gray;
    background-color: rgb(206, 206, 206);
}
QCheckBox {     
    color: rgb(206, 206, 206);
    font-size: 15px;
}
QLabel{
    color: rgb(206, 206, 206);
}
QCheckBox::indicator {
    width:  14px;
    height: 14px;
}
QPushButton {
    color: rgb(206, 206, 206);
    color: rgb(206, 206, 206);
    background-color: rgb(28, 28, 28);
}
QPushButton {
    font-size: 13px;
}
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    pp1, pp2, pp3, pp4 = 0, 0, 0, 0
    p2p1, p2p2, p2p3, p2p4 = 0, 0, 0, 0
    p6p1, p6p2 = 0, 0
    n1, n2, n3, n4 = 0, 0, 0, 0

    res1, res2, res3, res4, res5, res6, res7, res8, res9, res10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    app.setStyle("Sitka")
    app.setStyleSheet(StyleSheet)
    wizard = Wizard()
    wizard.setMinimumSize(QtCore.QSize(1000, 650))
    wizard.setMaximumSize(QtCore.QSize(1000, 650))
    wizard.setWindowTitle("CoolProgram — расчёт оценки защищенности информационной системы")
    wizard.setWindowIcon(QIcon(resource_path("icon.ico")))
    wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
    wizard.show()
    sys.exit(app.exec_())
