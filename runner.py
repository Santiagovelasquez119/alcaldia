import datetime
def soil_class(barrio:str):
    import pandas as pd
    clasificacion = pd.read_excel(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Clasificacion_suelos.xlsx')
    indice = clasificacion[' ']
    dataclasif = pd.DataFrame(clasificacion)
    principal = ''
    complementario = ''
    restringido = ''
    prohibido = ''
    tipo = ''
    articulos = ''
    for e in dataclasif.values:
        ppal = e[1]
        comp = e[2]
        rest = e[3]
        prohib = e[4]
        clasif = e[5]
        art = e[6]
        if barrio == e[0]:
            principal = ppal
            complementario = comp
            restringido = rest
            prohibido = prohib
            tipo = clasif
            articulos = art.split(', ')
    return {'Principal': principal, 'Complementario': complementario, 'Restringido': restringido, 'Prohibido': prohibido, 'Clasificacion':tipo, 'Articulos': articulos}

def llenar_formato(nombre:str, cedula:int, celular:int, direccion_notif:str, direccion:str, barrio:str, numrad:int, fecharad:datetime.time,
                   cedcatast:str, matr_inm:int, mail:str, tiposol:str, servicio:str, razon_social:str):
    from docxtpl import DocxTemplate
    import pandas as pd
    articulo = (
        pd.DataFrame(pd.read_excel(r'C:\Users\Fernando.Castrillon\PycharmProjects\pythonProject\Alcaldia\Formatos\Articulos.xlsx')))
    formato = DocxTemplate(r'/Alcaldia/Formatos/Formato_Comercial.docx')
    arts = ''
    for i in range(len(soil_class(barrio)['Articulos'])):
        var = soil_class(barrio)['Articulos'][i]
        for j in articulo.values:
            if var == j[0]:
                arts += j[1] + '\n'
                arts += '\n'
    replace = {'fecha_hoy': datetime.date.today(), 'nombre_usuario': nombre, 'cedula':cedula, 'razon_social': razon_social, 'servicio':servicio, 'celular':celular, 'direccion':direccion, 'direccion_notif': direccion_notif, 'barrio': barrio,
               'num_rad':numrad, 'fecha_rad': fecharad, 'mail': mail, 'ced_catast': cedcatast, 'matr_inm': matr_inm, 'Principal': soil_class(barrio)['Principal'],
               'Complementario':soil_class(barrio)['Complementario'], 'Restringido':soil_class(barrio)['Restringido'],
               'Prohibido':soil_class(barrio)['Prohibido'], 'Clasificacion':soil_class(barrio)['Clasificacion'], 'Articulos':arts}
    formato.render(replace)
    with open("Registro.csv", "a") as archivo:
        archivo.write(f"{datetime.date.today()};{nombre};{cedula};{celular};{mail};{direccion};{razon_social};{servicio};{barrio};{numrad};{fecharad};{cedcatast};{matr_inm};{typo}\n")
    formato.save(f'UsoSuelo_{nombre}.docx')

nombre = 'John Dario Gomez Cañas'
cedula = 15509793
celular = 3122795708
direccion_notif = 'Cl 49 #48-26'
direccion = 'Simon Bolivar'
mail = 'juansz3@hotmail.com'
barrio = 'Simon Bolivar'
numrad = '00147'
fecharad = datetime.date(2024, 1, 9)
cedcatast = '212-2-001-000-0011-00025-00000-00000'
matr_inm = '012-31680'
servicio = 'Distribución y comercialización de SLP al por mayor'
razon_social = 'Inversiones SLP S.A.S ESP'
typo = 'UsoSueloComercial'

llenar_formato(nombre, cedula, celular, direccion_notif, direccion, barrio, numrad, fecharad, cedcatast, matr_inm, mail, typo, servicio, razon_social)


