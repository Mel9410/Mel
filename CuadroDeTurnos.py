from numpy import NaN
import pandas as pd

# Leer excel
file = pd.read_excel('CUADRO.xlsx', header=None)

#convertirlo en DataFrame
df =pd.DataFrame(file)

# Remover 2 columnas iniciales
df = df.drop(columns=[0,1])

# Remover últimas 7 columnas
df = df.iloc[: , :-8]

# Remover últimas 8 filas
df = df.drop(df.tail(8).index)

# Remover primeras 3 filas
cuadro = df.drop(df.head(3).index)

print(cuadro)

# Información profesionales
class Profesional:
    def __init__(self, n, c, mm, s1, s2, s3, ts, noc, cor, ft, t, l):
        self.nombre = n
        self.contrato = c
        self.min_mes = mm
        self.score1 = s1
        self.score2 = s2
        self.score3 = s3
        self.total_score = ts
        self.noches = noc
        self.corridos = cor
        self.fast_track = ft
        self.tardes = t
        self.libres = l
    
    def mostrar_info_profesional(self):
        print('Nombre: ', self.nombre)
        print('Horas contrato: ', self.contrato)
        print('Horas mínimas de trabajo: ', self.min_mes)
        print('Score1: ', self.score1)
        print('Score2: ', self.score2)
        print('Score3: ', self.score3)
        print('Total score: ', self.total_score)
        print('Noches: ', self.noches)
        print('Corridos: ', self.corridos)
        print('Fast track: ', self.fast_track)
        print('Tardes: ', self.tardes)
        print('Libres: ', self.libres)
        print('')
        
profesionales = []

for i in range (3, len(cuadro)+3):
    nombre = file[0][i]
    contrato = file[1][i]
    min_mes = file.iat[i,-7]
    noches = file.iat[i,-5]
    corridos = file.iat[i,-4]
    tardes = file.iat[i,-3]
    fast_track = file.iat[i,-2]
    libres = file.iat[i,-1]
    score1 = 0
    score2 = 0
    score3 = 0
    total_score = 0
    i = Profesional(nombre, contrato, min_mes, score1, score2, score3, total_score, noches, corridos, fast_track, tardes, libres)
    profesionales.append(i.nombre)
    #i.mostrar_info_profesional()

#for Profesional in profesionales:
#    print(Profesional)
    
#print(file)

# Scores
dias_disp = 0
dias_laborales = int(file[36][1])
dias_rest = []
dias_mes = int(file[35][2])

for i in range (dias_mes):
    dias_rest[i] = dias_mes - i
    if cuadro[:,i].empty:
        dias_disp[i] = 1 + dias_disp
    
    
print(dias_disp)
print(dias_rest)  

    
#Score1 = dias_disp/dias_rest