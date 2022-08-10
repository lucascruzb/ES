import tabula as tb
import pandas as pd
import PyPDF2
import math
import pprint
import re
from pymongo import MongoClient
import json
import unidecode 
cluster = "mongodb+srv://lucasd:lucasd@basededados.fau4o.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster) 
db = client.app
collection = db.cursos
file = 'a.pdf'
pdfFileObj = open (file, 'rb')
pdfReader = PyPDF2.PdfFileReader (pdfFileObj)
pt = pdfReader.numPages
for i in range(1, pt+1):
    if i > 1 :
        df = pd.concat([df, tb.read_pdf(file, pages = i, area = (230, 0, 820, 595),  columns = [], pandas_options={'header': None}, stream=True)[0]], ignore_index=True, axis=0)
    else :
        df = tb.read_pdf(file, pages = i, area = (230, 0, 820, 595),  columns = [], pandas_options={'header': None}, stream=True)[0]
print(df)
df.rename(columns={ 0: 'Código', 1: 'Disciplina', 2: 'C.H.', 3: 'Cred.', 4: 'Situacao', 5: 'Periodo/Ano', 6: 'Periodo Ideal'}, inplace = True)