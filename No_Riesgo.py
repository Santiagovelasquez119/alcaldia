#coding:utf-8
import datetime

def RIESGO(categoria:int):
    riesgo = {0: 'NO SE ENCUENTRA EN ZONA DE RIESGO',
              1: 'SE ENCUENTRA EN ZONA DE RIESGO BAJO RECUPERABLE',
              2: 'SE ENCUENTRA EN ZONA DE RIESGO MEDIO RECUPERABLE',
              3: 'SE ENCUENTRA EN ZONA DE RIESGO ALTO RECUPERABLE',
              4: 'SE ENCUENTRA EN ZONA DE ALTO RIESGO'}
    return riesgo[categoria]


def CEDULA_CATASTRAL(cedcatast:str):
    dic = {'MUNICIPIO': {212: 'COPACABANA'},
           'SECTOR': {1: 'Urbano', 2: 'Rural'},
           'BARRIO': {1: 'SAN JUAN', 2: 'MARIA', 3: 'TABLAZO-CANOAS', 4: 'MOJON', 5: 'FATIMA', 6: 'LA PEDRERA',
                      7: 'SAN FRANCISCO', 8: 'MIRA FLOREZ', 9: 'CRISTO REY', 10: 'EL RECREO', 11: 'OBRERO',
                      12: 'SIMON BOLIVAR', 13: 'TOBON QUINTERO', 14: 'YARUMITO', 15: 'LAS VEGAS', 16: 'LA ASUNCION',
                      17: 'LA AZULITA', 18: 'CORREDOR MULTIPLE', 19: 'PORVENIR', 20: 'PEDREGAL', 21: 'REMANSO',
                      22: 'MISERICORDIA', 23: 'MACHADO', 24: 'VILLANUEVA'},
           'VEREDA': {1: 'QUEBRADA ARRIBA', 2: 'SABANETA', 3: 'PEÑOLCITO', 4: 'CABUYAL', 5: 'GRANIZAL',
                      6: 'CONVENTO', 7: 'FONTIDUEÑO', 8: 'MONTAÑITA', 9: 'EL SALADO', 10: 'ALVARADO', 11: 'ANCON',
                      12: 'ZARZAL CURAZAO', 13: 'EL NORAL', 14: 'LA VETA', 15: 'ZARZAL LA LUZ'}}
    partes = cedcatast.split('-')
    municipio, sector, corregimiento = int(partes[0]), int(partes[1]), int(partes[2])
    barrio, manz_vere, predio = int(partes[3]), int(partes[4]), int(partes[5])
    edificio, und_pred = int(partes[6]), int(partes[7])

    if sector == 1:
        resp_1 = {'Municipio': dic['MUNICIPIO'][municipio], 'Sector': dic['SECTOR'][sector], 'Corregimiento': corregimiento,
                  'Barrio': dic['BARRIO'][barrio], 'Manzanda-Vereda': manz_vere, 'Predio': predio, 'Edificio':edificio,
                  'Unidad predial': und_pred}
        return resp_1

    if sector == 2:
        resp_2 = {'Municipio': dic['MUNICIPIO'][municipio], 'Sector': dic['SECTOR'][sector],
                  'Corregimiento': corregimiento, 'Vereda': dic['VEREDA'][manz_vere], 'Manzanda-Vereda':manz_vere,
                  'Predio': predio, 'Edificio': edificio, 'Unidad predial': und_pred}

        return resp_2


def llenar_formato(nombre:str, cedula:int, celular:int, numrad:int, fecharad:datetime.time,
                   cedcatast:str, matr_inm:int, mail:str, nivel_riesgo:int):
    from docxtpl import DocxTemplate
    formato = DocxTemplate(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Formato_riesgo.docx')
    if CEDULA_CATASTRAL(cedcatast)['Sector'] == 'Urbano':
        barrio = CEDULA_CATASTRAL(cedcatast)['Barrio']
        replace = {'nombre': nombre,
                   'cedula': cedula,
                   'celular': celular,
                   'vereda': barrio,
                   'radicado': numrad,
                   'fecha_rad': fecharad,
                   'mail': mail,
                   'ced_catast': cedcatast,
                   'matr_inm': matr_inm,
                   'tipo_riesgo': RIESGO(nivel_riesgo)}
        formato.render(replace)
        with open("Registro_riesgo.csv", "a") as archivo:
            archivo.write(
                f"{datetime.date.today()};{nombre};{cedula};{celular};{mail};{barrio};{numrad};{fecharad};{cedcatast};{matr_inm};{RIESGO(nivel_riesgo)}\n")
        formato.save(f'CertificadoNoRiesgo_{nombre}.docx')
        print('OK')
    elif CEDULA_CATASTRAL(cedcatast)['Sector'] == 'Rural':
        vereda = CEDULA_CATASTRAL(cedcatast)['Vereda']
        replace = {'nombre': nombre,
                   'cedula': cedula,
                   'celular': celular,
                   'vereda': vereda,
                   'radicado': numrad,
                   'fecha_rad': fecharad,
                   'mail': mail,
                   'ced_catast': cedcatast,
                   'matr_inm': matr_inm,
                   'tipo_riesgo': RIESGO(nivel_riesgo)}
        formato.render(replace)
        with open("Registro_riesgo.csv", "a") as archivo:
            archivo.write(
                f"{datetime.date.today()};{nombre};{cedula};{celular};{mail};{vereda};{numrad};{fecharad};{cedcatast};{matr_inm};{RIESGO(nivel_riesgo)}\n")
        formato.save(f'CertificadoNoRiesgo_{nombre}.docx')
        print('ok')


nombre = 'RIESGO_A QUIEN PUEDA INTERESAR_OBRERO'
cedula = ''
celular = ''
correo = ''
radicado = ''
fecha_rad = datetime.date(2024, 1, 22)
cedcatast = '212-1-001-011-0017-00075-00000-00000'
matr_inm = '012-60694'

# 0: NO SE ENCUENTRA EN ZONA DE RIESGO
#
#
#
#

nivel_riesgo = 1

print(RIESGO(nivel_riesgo))
#print(CEDULA_CATASTRAL(cedcatast)['VEREDA'])
certificado = input('Desdea generar certificado? ')
if certificado == 'si':
    llenar_formato(nombre, cedula, celular, radicado, fecha_rad, cedcatast, matr_inm, correo, nivel_riesgo)