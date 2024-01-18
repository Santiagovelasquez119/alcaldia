#coding:utf-8

def soil_class(barrio:str):
    import pandas as pd
    clasificacion = pd.read_excel(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Clasificacion_suelos.xlsx')
    indice = clasificacion[' ']
    dataclasif = pd.DataFrame(clasificacion)
    principal = ''
    complementario = ''
    restringido = ''
    prohibido = ''
    articulos = ''
    for e in dataclasif.values:
        ppal = e[1]
        comp = e[2]
        rest = e[3]
        prohib = e[4]
        art = e[5]
        if barrio == e[0]:
            principal = ppal
            complementario = comp
            restringido = rest
            prohibido = prohib
            articulos = art.split(', ')
    return {'Principal': principal, 'Complementario': complementario, 'Restringido': restringido, 'Prohibido': prohibido, 'Articulos': articulos}

def CEDULA_CATASTRAL(cedcatast:str):
    dic = {'MUNICIPIO': {212: 'COPACABANA'},
           'SECTOR': {1: 'URBANO', 2: 'RURAL'},
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
            'Barrio': dic['BARRIO'][barrio], 'Manzanda-Vereda':manz_vere, 'Predio': predio, 'Edificio':edificio,
            'Unidad predial': und_pred}
        return resp_1
    if sector == 2:
        resp_2 = {'Municipio': dic['MUNICIPIO'][municipio], 'Sector': dic['SECTOR'][sector], 'Corregimiento': corregimiento,
            'Barrio': dic['VEREDA'][manz_vere], 'Manzanda-Vereda':manz_vere, 'Predio': predio, 'Edificio':edificio,
            'Unidad predial': und_pred}
        return resp_2

def VERIFICAR_SOLICITUD(query_type:str, soiltype:dict):
    var_principal = 'NO APROBADO'
    var_complementario = 'NO APROBADO'
    var_restringido = 'NO APROBADO'
    var_prohibido = 'NO APROBADO'
    if (query_type in soiltype['Principal'].split(', ')) or ('Múltiple' in soiltype['Principal'].split(', ')):
        var_principal = 'APROBADO'
    if (query_type in soiltype['Complementario'].split(', ')) or ('Múltiple' in soiltype['Complementario'].split(', ')):
        var_complementario = 'APROBADO'
    if (query_type in soiltype['Restringido'].split(', ')) or 'Múltiple' in soiltype['Restringido'].split(', '):
        var_restringido = 'APROBADO'
    if query_type not in soiltype['Prohibido'].split(', '):
        var_prohibido = 'APROBADO'

    return {'ESTADO_PRINCIPAL': var_principal, 'ESTADO COMPLEMENTARIO':var_complementario,
            'ESTADO RESTRINGIDO': var_restringido, 'ESTADO PROHIBIDO': var_prohibido}



cedcatast = '212-1-001-012-0009-00005-00001-00057'
print(CEDULA_CATASTRAL(cedcatast))
print(VERIFICAR_SOLICITUD('Industrial', soil_class('Simon Bolivar')))

print('Múltiple' in soil_class('Simon Bolivar')['Complementario'].split(', '))
