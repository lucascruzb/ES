import tabula as tb
import pandas as pd
import PyPDF2
import math
from pymongo import MongoClient
cluster = "mongodb+srv://lucasd:lucasd@basededados.fau4o.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster) 
db = client.app
collection = db.cursos
file = 'bo.pdf'
pdfFileObj = open (file, 'rb')
pdfReader = PyPDF2.PdfFileReader (pdfFileObj)
pt = pdfReader.numPages
n = tb.read_pdf(file, area = (130, 80, 150, 300) ,columns =[], pages = '1',pandas_options={'header': None}, stream=True)[0]
#print(nomecurso)
nomecurso = n[0].to_string(index=False)
ta = tb.read_pdf(file, pages = '1' , area = (230, 0, 260, 595),  columns = [70, 250, 290, 320, 370, 500], pandas_options={'header': None}, stream=True)[0]
#nome = tb.read_pdf(file, area = (110, 80, 130, 300) ,columns =[], pages = '1',pandas_options={'header': None}, stream=True)[0]
#print(nome)
if nomecurso == 'BAEQ - CURSO DE ENGENHARIA QUIMICA' :
    for i in range(1, pt+1):
        if i > 1 :
            df = pd.concat([df, tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [70, 250, 290, 320, 370, 500], pandas_options={'header': None}, stream=True)[0]], ignore_index=True, axis=0)
        else :
            df = tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [70, 250, 290, 320, 370, 500], pandas_options={'header': None}, stream=True)[0]
if nomecurso == 'BAEP - CURSO DE ENGENHARIA DE PRODUÇÃO' :
    for i in range(1, pt+1):
        if i > 1 :
            df = pd.concat([df, tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [75, 300, 340, 360, 420, 500], pandas_options={'header': None}, stream=True)[0]], ignore_index=True, axis=0)
        else :
            df = tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [75, 300, 340, 360, 420, 500], pandas_options={'header': None}, stream=True)[0]
if nomecurso == 'BAEC - CURSO DE ENGENHARIA DE COMPUTAÇÃO':
    for i in range(1, pt+1):
        if i > 1 :
            df = pd.concat([df, tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [80, 300, 330, 360, 410, 500], pandas_options={'header': None}, stream=True)[0]], ignore_index=True, axis=0)
        else :
            df = tb.read_pdf(file, pages = i, area = (250, 0, 820, 595),  columns = [80, 300, 330, 360, 410, 500], pandas_options={'header': None}, stream=True)[0]
#print(df)
df.rename(columns={ 0: 'Código', 1: 'Disciplina', 2: 'C.H.', 3: 'Cred.', 4: 'Situacao', 5: 'Periodo/Ano', 6: 'Periodo Ideal'}, inplace = True)
curso = []
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
            if row['Código'].count("Autentica") == 0 and row['Código'].count("Estrutura") == 0 :
                if math.isnan(float(row[5])) == False : 
                    chs = {
                        'semestre' : row[0] + str(row[1]),
                        'che' : int(row[5]),
                        'chv' : int(row[6])}
                    hsemestres.append(chs)
                if row['Código'] == "Componentes" :
                    chs = {
                        'semestre' : row[0] + row[1],
                        'che' : int(row[4]),
                        'chv' : int(row[6])}
                    hsemestres.append(chs)
        else:
            if type(row['Disciplina']) == str :
                curso.append(row)
cur = {
    'nome' : nomecurso,
    'cadeiras' : {
        'semestre' : [[]]  
    },
    'horas' : []
}
def myFunc(e):
    return float(e['Periodo Ideal'])
curso.sort(key=myFunc)
for i in curso:
    b = 0
    doc = {
        'Código' : i['Código'],
        'Disciplina' : i['Disciplina'],
        'C.H.' : i['C.H.'],
        'Cred.' : i['Cred.'],
        'Situacao' : i['Situacao'],
        'Periodo/Ano' : i['Periodo/Ano'],
        'Periodo Ideal' : i['Periodo Ideal']
        }
    if math.isnan(float(i['Periodo Ideal'])) == False :
        a = int(i['Periodo Ideal']) - 1
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
print(avanco)
#collection.insert_one(cur)
#result = collection.find({})
#for i in result:
#    pprint.pprint(i)
