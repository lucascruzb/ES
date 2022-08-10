import tabula as tb
import pandas as pd
import pprint
import re
from pymongo import MongoClient
import json
import unidecode 
cluster = "mongodb+srv://lucasd:lucasd@basededados.fau4o.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster) 
db = client.app
collection = db.cursos
file = 'b.pdf'
nomecurso = tb.read_pdf(file, area = (130, 80, 150, 300) ,columns =[], pages = '1',pandas_options={'header': None}, stream=True)[0]
horassemestre = tb.read_pdf(file, area = (600, 0, 730, 595) ,columns =[250,400], pages = '2',pandas_options={'header': None}, stream=True)[0]
tc = 0
t = 0
for index, row in horassemestre.iterrows():
    t = t + row[1]
    tc = tc + row[2]
avanco = (tc*100)/t
print(avanco)
df = tb.read_pdf(file, pages = '1', area = (250, 0, 820, 595), columns = [80, 300, 330, 360, 420, 500], pandas_options={'header': None}, stream=True)[0]
df2 = tb.read_pdf(file, pages = '2', area = (250, 0, 570, 595),  columns = [80, 300, 330, 360, 420, 500], pandas_options={'header': None}, stream=True)[0]
df = pd.concat([df, df2], ignore_index=True, axis=0)
df.rename(columns={ 0: 'Código', 1: 'Disciplina', 2: 'C.H.', 3: 'Cred.', 4: 'Situacao', 5: 'Periodo/Ano', 6: 'Periodo Ideal'}, inplace = True)
curso = []
semestre = []
for index, row in df.iterrows():
    if row['Código'].count("SEMESTR") == 1:
        if row['Código'].count("0") == 1:
            row['Código'] = "10o SEMESTRE"
        if len(semestre) != 0 :
            #pprint.pprint(semestre)
            curso.append(semestre.copy())
            semestre.clear()
    else:
        semestre.append(row)
        if index+1 == len(df.index) :
            curso.append(semestre.copy())
            semestre.clear()
cur = {
    'nome' : nomecurso[0].to_string(index=False),
    'cadeiras' : {
        'semestre' : [[]]  
    },
    'horas' : [[]]
}
def myFunc(e):
    return e[0]['Periodo Ideal']
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
        a = int(j['Periodo Ideal']) - 1
        if a > b:
            cur['cadeiras']['semestre'].append([])
        cur['cadeiras']['semestre'][a].append(doc)
        b = a
    
processo = (tc * 100)/t
print(processo)
collection.insert_one(cur)
#result = collection.find({})
#for i in result:
#    pprint.pprint(i)