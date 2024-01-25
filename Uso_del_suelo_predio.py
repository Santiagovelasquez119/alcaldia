#coding:utf-8
import datetime


def soil_class(barrio:str):
    import pandas as pd
    clasificacion = pd.read_excel(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Clasificacion_suelos.xlsx')
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
    return {'Principal': principal, 'Complementario': complementario, 'Restringido': restringido,
            'Prohibido': prohibido, 'Articulos': articulos}


def CEDULA_CATASTRAL(cedcatast: str):
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
        resp_1 = {'Municipio': dic['MUNICIPIO'][municipio], 'Sector': dic['SECTOR'][sector],
                  'Corregimiento': corregimiento, 'Barrio': dic['BARRIO'][barrio], 'Manzanda-Vereda': manz_vere,
                  'Predio': predio, 'Edificio': edificio, 'Unidad predial': und_pred}
        return resp_1

    if sector == 2:
        resp_2 = {'Municipio': dic['MUNICIPIO'][municipio], 'Sector': dic['SECTOR'][sector],
                  'Corregimiento': corregimiento, 'Vereda': dic['VEREDA'][manz_vere], 'Manzanda-Vereda': manz_vere,
                  'Predio': predio, 'Edificio': edificio, 'Unidad predial': und_pred}

        return resp_2


def RESUMEN_SOLICITUD(query_type: str, soiltype: dict):

    var_principal = 'NO APROBADO'
    var_complementario = 'NO APROBADO'
    var_restringido = 'NO APROBADO'
    var_prohibido = 'NO APROBADO'

    if (query_type in soiltype['Principal'].split(', ')) or ('Múltiple' in soiltype['Principal'].split(', ')):
        if query_type != 'Industria pesada':
            var_principal = 'APROBADO'
    if (query_type in soiltype['Complementario'].split(', ')) or ('Múltiple' in soiltype['Complementario'].split(', ')):
        if query_type != 'Industria pesada':
            var_complementario = 'APROBADO'
    if (query_type in soiltype['Restringido'].split(', ')) or 'Múltiple' in soiltype['Restringido'].split(', '):
        if query_type != 'Industria pesada':
            var_restringido = 'APROBADO'
    if query_type not in soiltype['Prohibido'].split(', '):
        var_prohibido = 'APROBADO'

    return {'ESTADO PRINCIPAL': var_principal, 'ESTADO COMPLEMENTARIO': var_complementario,
            'ESTADO RESTRINGIDO': var_restringido, 'ESTADO PROHIBIDO': var_prohibido}


def VERIFICAR_SOLICITUD(nombre: str, cedula: int, celular: int, dir_notif: str, correo: str, dirPBOT: str, radicado: str,
                        fecha_rad: datetime.date, cedula_catastral:str, matr_inm: str, query_type: str):
    if query_type != 'Consulta':
        datos_solicitante = {'NOMBRE': nombre,
                             'CEDULA': cedula,
                             'CELULAR': celular,
                             'DIRECCION_NOTIFICACION': dir_notif,
                             'CORREO': correo,
                             'SECTOR_PBOT': dirPBOT,
                             'RADICADO': radicado,
                             'FECHA DE RADICADO': fecha_rad,
                             'MATRICULA INMOBILIARIA': matr_inm}

        print('RESUMEN DE LA SOLICITUD DE USO DE SUELOS:\n')
        print('DATOS DEL SOLICITANTE')
        for e in datos_solicitante.keys():
            print(f"{e}: {datos_solicitante[e]}")

        print('\nINFORMACION PREDIAL')
        for i in CEDULA_CATASTRAL(cedula_catastral).keys():
            print(f'{i}: {CEDULA_CATASTRAL(cedula_catastral)[i]}')

        print(f'\nUSO DE SUELOS PARA EL BARRIO/VEREDA {barrio_PBOT}:')
        for a in soil_class(barrio_PBOT):
            print(f'{a}: {soil_class(barrio_PBOT)[a]}')

        print('\nESTUDIO DE LA SOLICITUD ARROJA LOS SIGUIENTES RESULTADOS:')
        print(F'CLASIFICACION DE LA ACTIVIDAD: {query_type}')
        for b in RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT)).keys():
            print(f'{b}: {RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT))[b]}')

        if RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT))['ESTADO PROHIBIDO'] == 'APROBADO':
            if RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT))['ESTADO PRINCIPAL'] == 'APROBADO':
                return '\nCONCEDIDO SIN RESTRICCIONES'
            elif RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT))['ESTADO COMPLEMENTARIO'] == 'APROBADO':
                return '\nCONCEDIDO CON LIGERAS RESTRICCIONES'
            elif RESUMEN_SOLICITUD(query_type, soil_class(barrio_PBOT))['ESTADO RESTRINGIDO'] == 'APROBADO':
                return '\nCONCEDIDO CON RESTRICCIONES'
            else:
                return '\nNO SE PUEDE EXPEDIR USO DE SUELOS'
        else:
            return '\nNO SE PUEDE EXPEDIR USO DE SUELOS'
    else:
        datos_solicitante = {'NOMBRE': nombre,
                             'CEDULA': cedula,
                             'CELULAR': celular,
                             'DIRECCION_NOTIFICACION': dir_notif,
                             'CORREO': correo,
                             'SECTOR_PBOT': dirPBOT,
                             'RADICADO': radicado,
                             'FECHA DE RADICADO': fecha_rad,
                             'MATRICULA INMOBILIARIA': matr_inm}
        print('RESUMEN DE LA SOLICITUD DE USO DE SUELOS:\n')
        print('DATOS DEL SOLICITANTE')
        for e in datos_solicitante.keys():
            print(f"{e}: {datos_solicitante[e]}")

        print('\nINFORMACION PREDIAL')
        for i in CEDULA_CATASTRAL(cedula_catastral).keys():
            print(f'{i}: {CEDULA_CATASTRAL(cedula_catastral)[i]}')

        print(f'\nUSO DE SUELOS PARA EL BARRIO/VEREDA {barrio_PBOT}:')
        for a in soil_class(barrio_PBOT):
            print(f'{a}: {soil_class(barrio_PBOT)[a]}')
def llenar_formato(nombre: str, cedula: int, celular: int, direccion_notif:str, direccion: str, barrio: str,
                   numrad: int, fecharad: datetime.time, cedcatast: str, matr_inm: int, mail: str):
    from docxtpl import DocxTemplate
    import pandas as pd
    articulo = (
        pd.DataFrame(pd.read_excel(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Articulos.xlsx')))
    formato = DocxTemplate(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Formato_Predio.docx')
    arts = ''
    for i in range(len(soil_class(barrio)['Articulos'])):
        var = soil_class(barrio)['Articulos'][i]
        for j in articulo.values:
            if var == j[0]:
                arts += j[1] + '\n'
                arts += '\n'

    replace = {'fecha_hoy': datetime.date.today(),
               'nombre_usuario': nombre,
               'cedula': cedula,
               'celular': celular,
               'direccion': direccion,
               'direccion_notif': direccion_notif,
               'barrio': barrio,
               'num_rad': numrad,
               'fecha_rad': fecharad,
               'mail': mail,
               'ced_catast': cedcatast,
               'matr_inm': matr_inm,
               'Principal': soil_class(barrio)['Principal'],
               'Complementario': soil_class(barrio)['Complementario'], 'Restringido': soil_class(barrio)['Restringido'],
               'Prohibido': soil_class(barrio)['Prohibido'],
               'Articulos': arts,
               'Clasificacion': CEDULA_CATASTRAL(cedcatast)['Sector']}
    formato.render(replace)

    with open("Registro.csv", "a") as archivo:
        archivo.write(f"{datetime.date.today()};{nombre};{cedula};{celular};{mail};{direccion};{barrio};{numrad};"
                      f"{fecharad};{cedcatast};{matr_inm};{typo}\n")
    formato.save(f'UsoSueloPredio_{nombre}.docx')

nombre = 'ALVARO BERNARDO MARIN VIECO'
cedula = '8287909'
dir_notif = ''
celular = 3108251164
direccion_lote = 'VEREDA EL NORAL (PRADES I)'
correo = 'NOLIGASI@GMAIL.COM'
barrio_PBOT = 'EL NORAL SUBURBANO'
radicado = 710
fecha_rad = datetime.date(2024, 1, 24)
cedcatast = '212-2-001-000-0013-00184-00000-00000'
matr_inm = '012-0021506'
query_type = 'Consulta'
typo = 'UsoSueloPredio'

print(CEDULA_CATASTRAL(cedcatast))
print(VERIFICAR_SOLICITUD(nombre, cedula, celular, dir_notif, correo, barrio_PBOT, radicado, fecha_rad, cedcatast,
                            matr_inm, query_type))

req_cert = str(input('Desea expedir certificado? '))
if req_cert == 'si':
    llenar_formato(nombre, cedula, celular, dir_notif, direccion_lote, barrio_PBOT, radicado, fecha_rad, cedcatast,
                   matr_inm, correo)

