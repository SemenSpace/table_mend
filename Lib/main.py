import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QTextEdit
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon


class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect("data.db")
        self.cur = self.db.cursor()
        self.mend = 'mend_img.png'
        self.fon = 'background.jpg'
        self.icon = 'icon_img.jpg'
        self.vivod = QTextEdit(self)
        self.back_fon = QPixmap(self.fon)
        self.image = QLabel(self)
        self.photo_mend = QPixmap(self.mend)
        self.image2 = QLabel(self)
        self.name = ''
        self.num = ''
        self.group = ''
        self.per = ''
        self.mas = ''
        self.metal = ''
        self.konf = ''
        self.da = ''
        self.who = ''
        self.inf = ''
        self.element_from_data = ''
        self.inf_mend = '''Менделеев Дмитрий Иванович (1834— 1907), химик, создатель периодической системы химических элементов. Родился 8 февраля 1834 г. в Тобольске в семье директора гимназии. Учился в этой гимназии, затем был принят на отделение естественных наук физико-математического факультета Главного педагогического института в Петербурге. Курс окончил с золотой медалью, однако за годы напряжённых занятий подорвал здоровье. В 1855 г. уехал в Одессу, где преподавал в гимназии при Ришельевском лицее. Благодатный южный климат позволил Менделееву уже в следующем году вернуться в Петербург. Он защитил магистерскую диссертацию и приступил к чтению лекций по органической химии в Петербургском университете. В 1859—1861 гг. посетил Германию «для усовершенствования в науках», а по возвращении на родину издал первый в России учебник по органической химии, который был удостоен Демидовской премии. В 1865 г. Менделеев защитил докторскую диссертацию, заложившую основы учения о растворах. В 1869 г. учёный совершил одно из величайших открытий в истории химии — вывел периодический закон химических элементов. В 1871 г. вышел его классический труд «Основы химии», где обобщались представления о любимой науке. Дмитрий Иванович отдавал много сил преподавательской деятельности — был профессором Петербургского университета, вёл курсы в других учебных заведениях. На склоне лет он отмечал: «Из тысяч моих учеников много теперь повсюду видных деятелей, профессоров, администраторов, и, встречая их, всегда слышал, что доброе в них семя полагал, а не простую отбывал повинность». В 1890 г. Менделеев покинул университет в знак протеста против притеснения студенчества. Несколько лет учёный был консультантом научно-технической лаборатории Морского министерства; в 1892 г. он организовал производство изобретённого им бездымного пороха. С 1892 г. и до конца своей жизни Дмитрий Иванович возглавлял Главную палату мер и весов. Скончался 2 февраля 1907 г. в Петербурге.
        Wiki: https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%BD%D0%B4%D0%B5%D0%BB%D0%B5%D0%B5%D0%B2,_%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B9_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87'''
        self.el1 = QPushButton('H', self)
        self.el2 = QPushButton('Li', self)
        self.el3 = QPushButton('Na', self)
        self.el4 = QPushButton('K', self)
        self.el5 = QPushButton('Rb', self)
        self.el6 = QPushButton('Cs', self)
        self.el7 = QPushButton('Fr', self)
        self.el8 = QPushButton('Be', self)
        self.el9 = QPushButton('Mg', self)
        self.el10 = QPushButton('Ca', self)
        self.el11 = QPushButton('Sr', self)
        self.el12 = QPushButton('Ba', self)
        self.el13 = QPushButton('Ra', self)
        self.el14 = QPushButton('Sc', self)
        self.el15 = QPushButton('Ti', self)
        self.el16 = QPushButton('Y', self)
        self.el17 = QPushButton('Zr', self)
        self.el18 = QPushButton('V', self)
        self.el19 = QPushButton('Nb', self)
        self.el20 = QPushButton('Ta', self)
        self.el21 = QPushButton('Db', self)
        self.el22 = QPushButton('Hf', self)
        self.el23 = QPushButton('Rf', self)
        self.el24 = QPushButton('Cr', self)
        self.el25 = QPushButton('Mo', self)
        self.el26 = QPushButton('W', self)
        self.el27 = QPushButton('Sg', self)
        self.el28 = QPushButton('Mn', self)
        self.el29 = QPushButton('Fe', self)
        self.el30 = QPushButton('Co', self)
        self.el31 = QPushButton('Ni', self)
        self.el32 = QPushButton('Cu', self)
        self.el33 = QPushButton('Zn', self)
        self.el35 = QPushButton('Tc', self)
        self.el36 = QPushButton('Re', self)
        self.el37 = QPushButton('Bh', self)
        self.el38 = QPushButton('Ru', self)
        self.el39 = QPushButton('Os', self)
        self.el40 = QPushButton('Hs', self)
        self.el41 = QPushButton('Rh', self)
        self.el42 = QPushButton('Ir', self)
        self.el43 = QPushButton('Mt', self)
        self.el44 = QPushButton('Pd', self)
        self.el45 = QPushButton('Pt', self)
        self.el46 = QPushButton('Ds', self)
        self.el47 = QPushButton('Ag', self)
        self.el48 = QPushButton('Cd', self)
        self.el50 = QPushButton('Au', self)
        self.el51 = QPushButton('Hg', self)
        self.el53 = QPushButton('Rg', self)
        self.el54 = QPushButton('Cn', self)
        self.el56 = QPushButton('Ga', self)
        self.el57 = QPushButton('Al', self)
        self.el58 = QPushButton('B', self)
        self.el59 = QPushButton('C', self)
        self.el60 = QPushButton('N', self)
        self.el61 = QPushButton('O', self)
        self.el62 = QPushButton('F', self)
        self.el63 = QPushButton('Ne', self)
        self.el64 = QPushButton('He', self)
        self.el65 = QPushButton('Ar', self)
        self.el66 = QPushButton('Cl', self)
        self.el67 = QPushButton('S', self)
        self.el68 = QPushButton('P', self)
        self.el69 = QPushButton('Si', self)
        self.el70 = QPushButton('Ge', self)
        self.el71 = QPushButton('As', self)
        self.el72 = QPushButton('Se', self)
        self.el73 = QPushButton('Br', self)
        self.el74 = QPushButton('Kr', self)
        self.el75 = QPushButton('Xe', self)
        self.el76 = QPushButton('I', self)
        self.el77 = QPushButton('Te', self)
        self.el78 = QPushButton('Sb', self)
        self.el79 = QPushButton('Sn', self)
        self.el80 = QPushButton('In', self)
        self.el81 = QPushButton('Ti', self)
        self.el82 = QPushButton('Nh', self)
        self.el83 = QPushButton('Pb', self)
        self.el84 = QPushButton('Bi', self)
        self.el85 = QPushButton('Po', self)
        self.el86 = QPushButton('At', self)
        self.el87 = QPushButton('Rn', self)
        self.el88 = QPushButton('Og', self)
        self.el89 = QPushButton('Ts', self)
        self.el90 = QPushButton('Lv', self)
        self.el91 = QPushButton('Mc', self)
        self.el92 = QPushButton('Fl', self)
        self.el93 = QPushButton('La', self)
        self.el94 = QPushButton('Ce', self)
        self.el95 = QPushButton('Pr', self)
        self.el96 = QPushButton('Nd', self)
        self.el97 = QPushButton('Pm', self)
        self.el98 = QPushButton('Sm', self)
        self.el99 = QPushButton('Eu', self)
        self.el100 = QPushButton('Gd', self)
        self.el101 = QPushButton('Tb', self)
        self.el102 = QPushButton('Dy', self)
        self.el103 = QPushButton('Ho', self)
        self.el104 = QPushButton('Er', self)
        self.el105 = QPushButton('Tm', self)
        self.el106 = QPushButton('Yb', self)
        self.el107 = QPushButton('Lu', self)
        self.el109 = QPushButton('Ac', self)
        self.el110 = QPushButton('Th', self)
        self.el111 = QPushButton('Pa', self)
        self.el112 = QPushButton('U', self)
        self.el113 = QPushButton('Np', self)
        self.el114 = QPushButton('Pu', self)
        self.el115 = QPushButton('Am', self)
        self.el116 = QPushButton('Cm', self)
        self.el117 = QPushButton('Bk', self)
        self.el118 = QPushButton('Cf', self)
        self.el119 = QPushButton('Es', self)
        self.el120 = QPushButton('Fm', self)
        self.el121 = QPushButton('Md', self)
        self.el122 = QPushButton('No', self)
        self.el123 = QPushButton('Lr', self)
        self.mendeleev = QPushButton('Д.И.Менделеев', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(1430, 630)
        self.setWindowTitle('Периодическая система химических элементов')
        self.setWindowIcon(QIcon(self.icon))

        self.vivod.setGeometry(1170, 30, 250, 411)
        self.vivod.setDisabled(True)

        self.image2.move(400, 7)
        self.image2.setPixmap(self.photo_mend)

        self.el1.setGeometry(20, 30, 51, 51)
        self.el1.setStyleSheet('QPushButton {background-color: #276124; color: white;}')
        self.el1.clicked.connect(self.run)

        self.el2.setGeometry(20, 90, 51, 51)
        self.el2.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el2.clicked.connect(self.run)

        self.el3.setGeometry(20, 150, 51, 51)
        self.el3.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el3.clicked.connect(self.run)

        self.el4.setGeometry(20, 210, 51, 51)
        self.el4.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el4.clicked.connect(self.run)

        self.el5.setGeometry(20, 270, 51, 51)
        self.el5.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el1.clicked.connect(self.run)

        self.el6.setGeometry(20, 330, 51, 51)
        self.el6.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el1.clicked.connect(self.run)

        self.el7.setGeometry(20, 390, 51, 51)
        self.el7.setStyleSheet('QPushButton {background-color: #b53a3a; color: white;}')
        self.el1.clicked.connect(self.run)

        self.el8.setGeometry(80, 90, 51, 51)
        self.el8.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el8.clicked.connect(self.run)

        self.el9.setGeometry(80, 150, 51, 51)
        self.el9.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el9.clicked.connect(self.run)

        self.el10.setGeometry(80, 210, 51, 51)
        self.el10.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el10.clicked.connect(self.run)

        self.el11.setGeometry(80, 270, 51, 51)
        self.el11.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el11.clicked.connect(self.run)

        self.el12.setGeometry(80, 330, 51, 51)
        self.el12.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el12.clicked.connect(self.run)

        self.el13.setGeometry(80, 390, 51, 51)
        self.el13.setStyleSheet('QPushButton {background-color: #e8c289; color: white;}')
        self.el13.clicked.connect(self.run)

        self.el14.setGeometry(140, 210, 51, 51)
        self.el14.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el14.clicked.connect(self.run)

        self.el15.setGeometry(200, 210, 51, 51)
        self.el15.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el15.clicked.connect(self.run)

        self.el16.setGeometry(140, 270, 51, 51)
        self.el16.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el16.clicked.connect(self.run)

        self.el17.setGeometry(200, 270, 51, 51)
        self.el17.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el17.clicked.connect(self.run)

        self.el18.setGeometry(260, 210, 51, 51)
        self.el18.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el18.clicked.connect(self.run)

        self.el19.setGeometry(260, 270, 51, 51)
        self.el19.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el19.clicked.connect(self.run)

        self.el20.setGeometry(260, 330, 51, 51)
        self.el20.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el20.clicked.connect(self.run)

        self.el21.setGeometry(260, 390, 51, 51)
        self.el21.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el21.clicked.connect(self.run)

        self.el22.setGeometry(200, 330, 51, 51)
        self.el22.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el22.clicked.connect(self.run)

        self.el23.setGeometry(200, 390, 51, 51)
        self.el23.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el23.clicked.connect(self.run)

        self.el24.setGeometry(320, 210, 51, 51)
        self.el24.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el24.clicked.connect(self.run)

        self.el25.setGeometry(320, 270, 51, 51)
        self.el25.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el25.clicked.connect(self.run)

        self.el26.setGeometry(320, 330, 51, 51)
        self.el26.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el26.clicked.connect(self.run)

        self.el27.setGeometry(320, 390, 51, 51)
        self.el27.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el27.clicked.connect(self.run)

        self.el28.setGeometry(380, 210, 51, 51)
        self.el28.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el28.clicked.connect(self.run)

        self.el29.setGeometry(440, 210, 51, 51)
        self.el29.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el29.clicked.connect(self.run)

        self.el30.setGeometry(500, 210, 51, 51)
        self.el30.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el30.clicked.connect(self.run)

        self.el31.setGeometry(560, 210, 51, 51)
        self.el31.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el31.clicked.connect(self.run)

        self.el32.setGeometry(620, 210, 51, 51)
        self.el32.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el32.clicked.connect(self.run)

        self.el33.setGeometry(680, 210, 51, 51)
        self.el33.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el33.clicked.connect(self.run)

        self.el35.setGeometry(380, 270, 51, 51)
        self.el35.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el35.clicked.connect(self.run)

        self.el36.setGeometry(380, 330, 51, 51)
        self.el36.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el36.clicked.connect(self.run)

        self.el37.setGeometry(380, 390, 51, 51)
        self.el37.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el37.clicked.connect(self.run)

        self.el38.setGeometry(440, 270, 51, 51)
        self.el38.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el38.clicked.connect(self.run)

        self.el39.setGeometry(440, 330, 51, 51)
        self.el39.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el39.clicked.connect(self.run)

        self.el40.setGeometry(440, 390, 51, 51)
        self.el40.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el40.clicked.connect(self.run)

        self.el41.setGeometry(500, 270, 51, 51)
        self.el41.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el41.clicked.connect(self.run)

        self.el42.setGeometry(500, 330, 51, 51)
        self.el42.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el42.clicked.connect(self.run)

        self.el43.setGeometry(500, 390, 51, 51)
        self.el43.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el43.clicked.connect(self.run)

        self.el44.setGeometry(560, 270, 51, 51)
        self.el44.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el44.clicked.connect(self.run)

        self.el45.setGeometry(560, 330, 51, 51)
        self.el45.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el45.clicked.connect(self.run)

        self.el46.setGeometry(560, 390, 51, 51)
        self.el46.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el46.clicked.connect(self.run)

        self.el47.setGeometry(620, 270, 51, 51)
        self.el47.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el47.clicked.connect(self.run)

        self.el48.setGeometry(680, 270, 51, 51)
        self.el48.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el48.clicked.connect(self.run)

        self.el50.setGeometry(620, 330, 51, 51)
        self.el50.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el50.clicked.connect(self.run)

        self.el51.setGeometry(680, 330, 51, 51)
        self.el51.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el51.clicked.connect(self.run)

        self.el53.setGeometry(620, 390, 51, 51)
        self.el53.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el53.clicked.connect(self.run)

        self.el54.setGeometry(680, 390, 51, 51)
        self.el54.setStyleSheet('QPushButton {background-color: #bd7a73; color: white;}')
        self.el54.clicked.connect(self.run)

        self.el56.setGeometry(800, 210, 51, 51)
        self.el56.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el56.clicked.connect(self.run)

        self.el57.setGeometry(800, 150, 51, 51)
        self.el57.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el57.clicked.connect(self.run)

        self.el58.setGeometry(800, 90, 51, 51)
        self.el58.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el58.clicked.connect(self.run)

        self.el59.setGeometry(860, 90, 51, 51)
        self.el59.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el59.clicked.connect(self.run)

        self.el60.setGeometry(920, 90, 51, 51)
        self.el60.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el60.clicked.connect(self.run)

        self.el61.setGeometry(980, 90, 51, 51)
        self.el61.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el61.clicked.connect(self.run)

        self.el62.setGeometry(1040, 90, 51, 51)
        self.el62.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el62.clicked.connect(self.run)

        self.el63.setGeometry(1100, 90, 51, 51)
        self.el63.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el63.clicked.connect(self.run)

        self.el64.setGeometry(1100, 30, 51, 51)
        self.el64.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el64.clicked.connect(self.run)

        self.el65.setGeometry(1100, 150, 51, 51)
        self.el65.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el65.clicked.connect(self.run)

        self.el66.setGeometry(1040, 150, 51, 51)
        self.el66.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el66.clicked.connect(self.run)

        self.el67.setGeometry(980, 150, 51, 51)
        self.el67.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el67.clicked.connect(self.run)

        self.el68.setGeometry(920, 150, 51, 51)
        self.el68.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el68.clicked.connect(self.run)

        self.el69.setGeometry(860, 150, 51, 51)
        self.el69.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el69.clicked.connect(self.run)

        self.el70.setGeometry(860, 210, 51, 51)
        self.el70.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el70.clicked.connect(self.run)

        self.el71.setGeometry(920, 210, 51, 51)
        self.el71.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el71.clicked.connect(self.run)

        self.el72.setGeometry(980, 210, 51, 51)
        self.el72.setStyleSheet('QPushButton {background-color: #83b07d; color: white;}')
        self.el72.clicked.connect(self.run)

        self.el73.setGeometry(1040, 210, 51, 51)
        self.el73.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el73.clicked.connect(self.run)

        self.el74.setGeometry(1100, 210, 51, 51)
        self.el74.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el74.clicked.connect(self.run)

        self.el75.setGeometry(1100, 270, 51, 51)
        self.el75.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el75.clicked.connect(self.run)

        self.el76.setGeometry(1040, 270, 51, 51)
        self.el76.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el76.clicked.connect(self.run)

        self.el77.setGeometry(980, 270, 51, 51)
        self.el77.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el77.clicked.connect(self.run)

        self.el78.setGeometry(920, 270, 51, 51)
        self.el78.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el78.clicked.connect(self.run)

        self.el79.setGeometry(860, 270, 51, 51)
        self.el79.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el79.clicked.connect(self.run)

        self.el80.setGeometry(800, 270, 51, 51)
        self.el80.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el80.clicked.connect(self.run)

        self.el81.setGeometry(800, 330, 51, 51)
        self.el81.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el81.clicked.connect(self.run)

        self.el82.setGeometry(800, 390, 51, 51)
        self.el82.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el82.clicked.connect(self.run)

        self.el83.setGeometry(860, 330, 51, 51)
        self.el83.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el83.clicked.connect(self.run)

        self.el84.setGeometry(920, 330, 51, 51)
        self.el84.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el84.clicked.connect(self.run)

        self.el85.setGeometry(980, 330, 51, 51)
        self.el85.setStyleSheet('QPushButton {background-color: #607a5d; color: white;}')
        self.el85.clicked.connect(self.run)

        self.el86.setGeometry(1040, 330, 51, 51)
        self.el86.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el86.clicked.connect(self.run)

        self.el87.setGeometry(1100, 330, 51, 51)
        self.el87.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el87.clicked.connect(self.run)

        self.el88.setGeometry(1100, 390, 51, 51)
        self.el88.setStyleSheet('QPushButton {background-color: #b2edd3; color: gray;}')
        self.el88.clicked.connect(self.run)

        self.el89.setGeometry(1040, 390, 51, 51)
        self.el89.setStyleSheet('QPushButton {background-color: #d9c471; color: white;}')
        self.el89.clicked.connect(self.run)

        self.el90.setGeometry(980, 390, 51, 51)
        self.el90.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el90.clicked.connect(self.run)

        self.el91.setGeometry(920, 390, 51, 51)
        self.el91.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el91.clicked.connect(self.run)

        self.el92.setGeometry(860, 390, 51, 51)
        self.el92.setStyleSheet('QPushButton {background-color: #999999; color: white;}')
        self.el92.clicked.connect(self.run)

        self.el93.setGeometry(200, 470, 51, 51)
        self.el93.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el93.clicked.connect(self.run)

        self.el94.setGeometry(260, 470, 51, 51)
        self.el94.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el94.clicked.connect(self.run)

        self.el95.setGeometry(320, 470, 51, 51)
        self.el95.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el95.clicked.connect(self.run)

        self.el96.setGeometry(380, 470, 51, 51)
        self.el96.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el96.clicked.connect(self.run)

        self.el97.setGeometry(440, 470, 51, 51)
        self.el97.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el97.clicked.connect(self.run)

        self.el98.setGeometry(500, 470, 51, 51)
        self.el98.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el98.clicked.connect(self.run)

        self.el99.setGeometry(560, 470, 51, 51)
        self.el99.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el99.clicked.connect(self.run)

        self.el100.setGeometry(620, 470, 51, 51)
        self.el100.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el100.clicked.connect(self.run)

        self.el101.setGeometry(680, 470, 51, 51)
        self.el101.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el101.clicked.connect(self.run)

        self.el102.setGeometry(740, 470, 51, 51)
        self.el102.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el102.clicked.connect(self.run)

        self.el103.setGeometry(800, 470, 51, 51)
        self.el103.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el103.clicked.connect(self.run)

        self.el104.setGeometry(860, 470, 51, 51)
        self.el104.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el104.clicked.connect(self.run)

        self.el105.setGeometry(920, 470, 51, 51)
        self.el105.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el105.clicked.connect(self.run)

        self.el106.setGeometry(980, 470, 51, 51)
        self.el106.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el106.clicked.connect(self.run)

        self.el107.setGeometry(1040, 470, 51, 51)
        self.el107.setStyleSheet('QPushButton {background-color: #d6a1d3; color: white;}')
        self.el107.clicked.connect(self.run)

        self.el109.setGeometry(200, 530, 51, 51)
        self.el109.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el109.clicked.connect(self.run)

        self.el110.setGeometry(260, 530, 51, 51)
        self.el110.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el110.clicked.connect(self.run)

        self.el111.setGeometry(320, 530, 51, 51)
        self.el111.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el111.clicked.connect(self.run)

        self.el112.setGeometry(380, 530, 51, 51)
        self.el112.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el112.clicked.connect(self.run)

        self.el113.setGeometry(440, 530, 51, 51)
        self.el113.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el113.clicked.connect(self.run)

        self.el114.setGeometry(500, 530, 51, 51)
        self.el114.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el114.clicked.connect(self.run)

        self.el115.setGeometry(560, 530, 51, 51)
        self.el115.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el115.clicked.connect(self.run)

        self.el116.setGeometry(620, 530, 51, 51)
        self.el116.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el116.clicked.connect(self.run)

        self.el117.setGeometry(680, 530, 51, 51)
        self.el117.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el117.clicked.connect(self.run)

        self.el118.setGeometry(740, 530, 51, 51)
        self.el118.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el118.clicked.connect(self.run)

        self.el119.setGeometry(800, 530, 51, 51)
        self.el119.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el119.clicked.connect(self.run)

        self.el120.setGeometry(860, 530, 51, 51)
        self.el120.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el120.clicked.connect(self.run)

        self.el121.setGeometry(920, 530, 51, 51)
        self.el121.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el121.clicked.connect(self.run)

        self.el122.setGeometry(980, 530, 51, 51)
        self.el122.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el122.clicked.connect(self.run)

        self.el123.setGeometry(1040, 530, 51, 51)
        self.el123.setStyleSheet('QPushButton {background-color: #9e659a; color: white;}')
        self.el123.clicked.connect(self.run)

        self.mendeleev.setGeometry(50, 480, 80, 80)
        self.mendeleev.setStyleSheet('QPushButton {background-color: #525252; color: white;}')
        self.mendeleev.clicked.connect(self.med)

    def med(self):
        self.vivod.setText(self.inf_mend)

    def run(self):
        self.name = "Название: " + str((self.cur.execute("""SELECT name FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.num = "Порядковый номер: " + str((self.cur.execute("""SELECT num FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.group = "Группа: " + str((self.cur.execute("""SELECT gr FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.per = "Период: " + str((self.cur.execute("""SELECT per FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.mas = "Атомная масса: " + str((self.cur.execute("""SELECT mas FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.metal = "Металл/Неметалл: " + str((self.cur.execute("""SELECT metal FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.konf = "Электронная конфигурация: " + str((self.cur.execute("""SELECT konf FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.da = "Год открытия: " + str((self.cur.execute("""SELECT date FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.who = "Первооткрыватель: " + str((self.cur.execute("""SELECT who FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.inf = "Wiki: " + str((self.cur.execute("""SELECT inf FROM elem WHERE id = ?""", (self.sender().text(),)).fetchone())[0]) + ""
        self.element_from_data = '' + self.name + '\n' + self.num + '\n' + self.per + '\n' + self.group + '\n' + self.mas + '\n' + self.metal + '\n' + self.konf + '\n' + self.da + '\n' + self.who + '\n' + self.inf + '\n'
        self.vivod.setText(self.element_from_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())
