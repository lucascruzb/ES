from pickle import TRUE
import tabula as tb
import pandas as pd
import PyPDF2
import math
import pprint
from pymongo import MongoClient
from PyQt6 import QtCore, QtGui, QtWidgets
from p import *
global cont , porcen , cursoM

class pri(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.arquivo = None
        self.ui = Ui_p()
        self.ui.setupUi(self)
        self.seg = seg()
        self.form = forma()
        self.apre = apre()
        self.ui.pushButton_3.clicked.connect(self.mudajanela)
        self.ui.pushButton.clicked.connect(self.abrir_integralizacao)
        
    def abrir_integralizacao(self):
        arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.arquivo = arquivo

    def mudajanela(self):
            analisar(self.arquivo)
            self.seg.show()

            global porcen
            self.seg.ui.label.setText("porcentagem de avanço: " + str(porcen) + "%")
            self.hide()

class seg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_s()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.apresentarCurso)
        self.ui.pushButton_2.clicked.connect(self.apresentarAvanco)
        self.ui.pushButton_3.clicked.connect(self.voltar)

    
    def apresentarCurso(self):

        global primeira
        primeira.form.show()
        primeira.apre.metodo(1)
        self.hide()

    def apresentarAvanco(self):
        
        global primeira
        primeira.apre.metodo(2)
        primeira.form.show()
        self.hide()

    def voltar(self):
        
        global primeira
        primeira.show()
        self.hide()

class forma(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_F()
        self.ui.setupUi(self)
        self.ui.pushButton_12.clicked.connect(self.voltar)
        self.ui.pushButton.clicked.connect(self.apre)
        self.ui.pushButton_2.clicked.connect(self.apre)
        self.ui.pushButton_3.clicked.connect(self.apre)
        self.ui.pushButton_4.clicked.connect(self.apre)
        self.ui.pushButton_5.clicked.connect(self.apre)
        self.ui.pushButton_6.clicked.connect(self.apre)
        self.ui.pushButton_7.clicked.connect(self.apre)
        self.ui.pushButton_8.clicked.connect(self.apre)
        self.ui.pushButton_9.clicked.connect(self.apre)
        self.ui.pushButton_10.clicked.connect(self.apre)
        self.ui.pushButton_11.clicked.connect(self.apre)

    def apre(self):

        global primeira
        if self.sender().objectName() == "pushButton":
            primeira.apre.apresentar(0)
        elif self.sender().objectName() == "pushButton_2":
            primeira.apre.apresentar(1)
        elif self.sender().objectName() == "pushButton_3":
            primeira.apre.apresentar(2)
        elif self.sender().objectName() == "pushButton_4":
            primeira.apre.apresentar(3)
        elif self.sender().objectName() == "pushButton_5":
            primeira.apre.apresentar(4)
        elif self.sender().objectName() == "pushButton_6":
            primeira.apre.apresentar(5)
        elif self.sender().objectName() == "pushButton_7":
            primeira.apre.apresentar(6)
        elif self.sender().objectName() == "pushButton_8":
            primeira.apre.apresentar(7)
        elif self.sender().objectName() == "pushButton_9":
            primeira.apre.apresentar(8)
        elif self.sender().objectName() == "pushButton_10":
            primeira.apre.apresentar(9)
        elif self.sender().objectName() == "pushButton_11":
            primeira.apre.apresentar(0)
        primeira.apre.show()
        self.hide()

    def voltar(self):
        
        global primeira
        primeira.seg.show()
        self.hide()

class apre(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Apre()
        self.ui.setupUi(self)
        self.tipo = None
        self.ui.pushButton_2.setVisible(False)
        self.ui.pushButton.clicked.connect(self.voltar)

    def metodo(self,tipo):
        self.tipo = tipo


    def apresentar(self, botao):
            if(botao == 0):
                self.Completo()
            elif(botao == 1):
                self.PriSemestre()
            elif(botao == 2):
                self.SegSemestre()
            elif(botao == 3):
                self.TerSemestre()
            elif(botao == 4):
                self.QuaSemestre()
            elif(botao == 5):
                self.QuiSemestre()
            elif(botao == 6):
                self.SexSemestre()
            elif(botao == 7):
                self.SetSemestre()
            elif(botao == 8):
                self.OitSemestre()
            elif(botao == 9):
                self.NonSemestre()
            elif(botao == 10):
                self.DecSemestre()

    def Completo(self):
        self.ui.pushButton_2.setVisible(True)
        self.PriSemestre()

    def ajustarI(self,semestre):

            global cont
            self.ui.label.setText(cont[semestre][0]['Disciplina'])
            self.ui.label_3.setText((str)(cont[semestre][0]['C.H.']))
            self.ui.label_5.setText((str)(cont[semestre][0]['Cred.']))
            self.ui.label_7.setText(cont[semestre][0]['Situacao'])
            if len(cont[semestre]) > 1:
                self.ui.label_8.setText(cont[semestre][1]['Disciplina'])
                self.ui.label_10.setText((str)(cont[semestre][1]['C.H.']))
                self.ui.label_12.setText((str)(cont[semestre][1]['Cred.']))
                self.ui.label_14.setText(cont[semestre][1]['Situacao'])
            if len(cont[semestre]) > 2:
                self.ui.label_15.setText(cont[semestre][2]['Disciplina'])
                self.ui.label_17.setText((str)(cont[semestre][2]['C.H.']))
                self.ui.label_19.setText((str)(cont[semestre][2]['Cred.']))
                self.ui.label_21.setText(cont[semestre][2]['Situacao'])
            if len(cont[semestre]) > 3:
                self.ui.label_22.setText(cont[semestre][3]['Disciplina'])
                self.ui.label_24.setText((str)(cont[semestre][3]['C.H.']))
                self.ui.label_26.setText((str)(cont[semestre][3]['Cred.']))
                self.ui.label_28.setText(cont[semestre][3]['Situacao'])
            if len(cont[semestre]) > 4:
                self.ui.label_29.setText(cont[semestre][4]['Disciplina'])
                self.ui.label_31.setText((str)(cont[semestre][4]['C.H.']))
                self.ui.label_33.setText((str)(cont[semestre][4]['Cred.']))
                self.ui.label_35.setText(cont[semestre][4]['Situacao'])
            if len(cont[semestre]) > 5:
                self.ui.label_36.setText(cont[semestre][5]['Disciplina'])
                self.ui.label_38.setText((str)(cont[semestre][5]['C.H.']))
                self.ui.label_40.setText((str)(cont[semestre][5]['Cred.']))
                self.ui.label_42.setText(cont[semestre][5]['Situacao'])
                

    def ajustarM(self, semestre):

            global cursoM
            #cadeira 1
            self.ui.label.setText(cursoM['cadeiras']['semestre'][semestre][0]['Disciplina'])
            self.ui.label_3.setText((str)(cursoM['cadeiras']['semestre'][semestre][0]['C.H.']))
            self.ui.label_5.setText((str)(cursoM['cadeiras']['semestre'][semestre][0]['Cred.']))
            self.ui.label_7.setText(cursoM['cadeiras']['semestre'][semestre][0]['Situacao'])
            if len(cursoM['cadeiras']['semestre'][semestre]) >1 :
            #cadeira 2
                self.ui.label_8.setText(cursoM['cadeiras']['semestre'][semestre][1]['Disciplina'])
                self.ui.label_10.setText((str)(cursoM['cadeiras']['semestre'][semestre][1]['C.H.']))
                self.ui.label_12.setText((str)(cursoM['cadeiras']['semestre'][semestre][1]['Cred.']))
                self.ui.label_14.setText(cursoM['cadeiras']['semestre'][semestre][1]['Situacao'])
            #cadeira 3
            if len(cursoM['cadeiras']['semestre'][semestre]) >2 :
                self.ui.label_15.setText(cursoM['cadeiras']['semestre'][semestre][2]['Disciplina'])
                self.ui.label_17.setText((str)(cursoM['cadeiras']['semestre'][semestre][2]['C.H.']))
                self.ui.label_19.setText((str)(cursoM['cadeiras']['semestre'][semestre][2]['Cred.']))
                self.ui.label_21.setText(cursoM['cadeiras']['semestre'][semestre][2]['Situacao'])
            #cadeira 4
            if len(cursoM['cadeiras']['semestre'][semestre]) >3 :
                self.ui.label_22.setText(cursoM['cadeiras']['semestre'][semestre][3]['Disciplina'])
                self.ui.label_24.setText((str)(cursoM['cadeiras']['semestre'][semestre][3]['C.H.']))
                self.ui.label_26.setText((str)(cursoM['cadeiras']['semestre'][semestre][3]['Cred.']))
                self.ui.label_28.setText(cursoM['cadeiras']['semestre'][semestre][3]['Situacao'])
            #cadeira 5
            if len(cursoM['cadeiras']['semestre'][semestre]) >4 :
                self.ui.label_29.setText(cursoM['cadeiras']['semestre'][semestre][4]['Disciplina'])
                self.ui.label_31.setText((str)(cursoM['cadeiras']['semestre'][semestre][4]['C.H.']))
                self.ui.label_33.setText((str)(cursoM['cadeiras']['semestre'][semestre][4]['Cred.']))
                self.ui.label_35.setText(cursoM['cadeiras']['semestre'][semestre][4]['Situacao'])
            if len(cursoM['cadeiras']['semestre'][semestre]) >5 :
            #cadeira 6
                self.ui.label_36.setText(cursoM['cadeiras']['semestre'][semestre][5]['Disciplina'])
                self.ui.label_38.setText((str)(cursoM['cadeiras']['semestre'][semestre][5]['C.H.']))
                self.ui.label_40.setText((str)(cursoM['cadeiras']['semestre'][semestre][5]['Cred.']))
                self.ui.label_42.setText(cursoM['cadeiras']['semestre'][semestre][5]['Situacao'])

    def PriSemestre(self):
        self.ui.frame_2.setVisible(True)
        self.ui.frame_3.setVisible(True)
        self.ui.frame_4.setVisible(True)
        self.ui.frame_5.setVisible(True)
        self.ui.frame_6.setVisible(False)
        self.ui.pushButton_3.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.SegSemestre)

        if(self.tipo == 1):
            self.ajustarM(0)
        elif(self.tipo == 2):
            self.ajustarI(0)

    def SegSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.TerSemestre)
        self.ui.pushButton_3.setVisible(True)
        self.ui.pushButton_3.clicked.connect(self.PriSemestre)
        self.ui.frame_6.setVisible(True)
        
        if(self.tipo == 1):
            self.ajustarM(1)

        elif(self.tipo == 2):
            self.ajustarI(1)

    def TerSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.QuaSemestre)
        self.ui.pushButton_3.clicked.connect(self.SegSemestre)
         
        if(self.tipo == 1):
            self.ajustarM(2)

        elif(self.tipo == 2):
            self.ajustarI(2)

    def QuaSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.QuiSemestre)
        self.ui.pushButton_3.clicked.connect(self.TerSemestre)
         
        if(self.tipo == 1):
            self.ajustarM(3)

        elif(self.tipo == 2):
            self.ajustarI(3)


    def QuiSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.SexSemestre)
        self.ui.pushButton_3.clicked.connect(self.QuaSemestre)

        if(self.tipo == 1):
            self.ajustarM(4)

        elif(self.tipo == 2):
            self.ajustarI(4)


    def SexSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.SetSemestre)
        self.ui.pushButton_3.clicked.connect(self.QuiSemestre)
         
        if(self.tipo == 1):
            self.ajustarM(5)

        elif(self.tipo == 2):
            self.ajustarI(5)


    def SetSemestre(self):
        self.ui.frame_6.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.OitSemestre)
        self.ui.pushButton_3.clicked.connect(self.SexSemestre)
         
        if(self.tipo == 1):
            self.ajustarM(6)

        elif(self.tipo == 2):
            self.ajustarI(6)


    def OitSemestre(self):
        self.ui.frame_5.setVisible(False)
        self.ui.pushButton_2.clicked.connect(self.NonSemestre)
        self.ui.pushButton_3.clicked.connect(self.SetSemestre)
         
        if(self.tipo == 1):
            self.ajustarM(7)

        elif(self.tipo == 2):
            self.ajustarI(7)


    def NonSemestre(self):
        self.ui.pushButton_2.clicked.connect(self.DecSemestre)
        self.ui.pushButton_3.clicked.connect(self.OitSemestre)
        self.ui.pushButton_2.setVisible(True)
         
        if(self.tipo == 1):
            self.ajustarM(8)

        elif(self.tipo == 2):
            self.ajustarI(8)


    def DecSemestre(self):
        self.ui.frame_2.setVisible(False)
        self.ui.frame_3.setVisible(False)
        self.ui.frame_4.setVisible(False)
        self.ui.pushButton_2.setVisible(False)
        self.ui.pushButton_3.clicked.connect(self.NonSemestre)
         
        if(self.tipo == 1):
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_2.clicked.connect(self.EneSemestre)
            
            self.ajustarM(9)

        elif(self.tipo == 2):
            self.ajustarI(9)
            

    def EneSemestre(self):

        if(self.tipo == 2):
            self.ajustarI(10)
        

    def voltar(self):

        global primeira
        primeira.form.show()
        self.hide()

def analisar(pdf):
    file = pdf
    cluster = "mongodb+srv://lucasd:lucasd@basededados.fau4o.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(cluster) 
    db = client.app
    collection = db.cursos
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader (pdfFileObj)
    pt = pdfReader.numPages
    nomecurso = tb.read_pdf(file, area = (130, 80, 150, 300) ,columns =[], pages = '1',pandas_options={'header': None}, stream=True)[0]
    #print(nomecurso)
    #nome = tb.read_pdf(file, area = (110, 80, 130, 300) ,columns =[], pages = '1',pandas_options={'header': None}, stream=True)[0]
    #print(nome)
    for i in range(1, pt+1):
        if i > 1 :
            df = pd.concat([df, tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [80, 300, 330, 360, 410, 500], pandas_options={'header': None}, stream=True)[0]], ignore_index=True, axis=0)
        else :
            df = tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [80, 300, 330, 360, 410, 500], pandas_options={'header': None}, stream=True)[0]
    #print(df)
    df.rename(columns={ 0: 'Código', 1: 'Disciplina', 2: 'C.H.', 3: 'Cred.', 4: 'Situacao', 5: 'Periodo/Ano', 6: 'Periodo Ideal'}, inplace = True)
    curso = []
    semestre = []
    horasc = []
    hsemestres = []
    for index, row in df.iterrows():
        if type(row['Disciplina']) != str :
            a1 = row['Código']
            a2 = row['C.H.']
            a3 = row['Cred.']
            a4 = row['Situacao']
            a5 = row['Periodo Ideal']
        if type(row['Situacao']) != str and type(row['Código']) == float:
            row['Código'] = a1
            row['C.H.'] = a2
            row['Cred.'] = a3
            row['Situacao'] = a4
            row['Periodo Ideal'] = a5
        if row['Código'].count("ACG") == 1 :
            horasc.append(row)
        else :
            if row['Código'].count("BA") == 0  :
                if row['Código'].count("Autentica") == 0 and row['Código'].count("Estrutura") == 0:
                    if math.isnan(float(row[5])) == False : 
                        if row['Código'].count("ATIVIDADES") == 1 or row['Código'].count("COMPONENTE") == 1 :
                            chs = {
                            'semestre' : row[0] + row[1],
                            'che' : int(row[5]),
                            'chv' : int(row[6])}
                        else :
                            chs = {
                                'semestre' : row[0],
                                'che' : int(row[5]),
                                'chv' : int(row[6])}
                        hsemestres.append(chs)
                if len(semestre) != 0 :
                    #pprint.pprint(semestre)
                    curso.append(semestre.copy())
                    semestre.clear()
            else:
                if type(row['Disciplina']) == str :
                    semestre.append(row)
                    if index+1 == len(df.index) :
                        curso.append(semestre.copy())
                        semestre.clear()
    cur = {
        'nome' : nomecurso[0].to_string(index=False),
        'cadeiras' : {
            'semestre' : [[]]  
        },
        'horas' : []
    }
    def myFunc(e):
        return float(e[0]['Periodo Ideal'])
    curso.sort(key=myFunc)
    for i in curso:
        b = 0
        for j in i :
            doc = {
                'Código' : j['Código'],
                'Disciplina' : j['Disciplina'],
                'C.H.' : j['C.H.'],
                'Cred.' : j['Cred.'],
                'Situacao' : j['Situacao'],
                'Periodo/Ano' : j['Periodo/Ano'],
                'Periodo Ideal' : j['Periodo Ideal']
            }
            if math.isnan(float(j['Periodo Ideal'])) == False :
                a = int(j['Periodo Ideal']) - 1
            else :
                a = 10
            if a > b:
                cur['cadeiras']['semestre'].append([])
            cur['cadeiras']['semestre'][a].append(doc)
            b = a
    for i in horasc:
        doc = {
            'Código' : i['Código'],
            'Disciplina' : i['Disciplina'],
            'C.H.' : i['C.H.'],
            'Situacao' : i['Situacao'],
            'Periodo/Ano' : i['Periodo/Ano']
        }
        cur['horas'].append(doc)

    tc = 0
    t = 0
    for i in hsemestres : 
            t = t + i['che']
            tc = tc + i['chv']
    
    avanco = (tc*100)/t

    global porcen

    porcen = avanco

    global cont, cursoM

    cont = curso
    #print(avanco)
    #collection.insert_one(cur)
    cursoM = collection.find_one({"nome":nomecurso[0].to_string(index=False)})

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    primeira = pri()
    primeira.show()
    sys.exit(app.exec())