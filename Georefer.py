import pandas as pd
def locator(ref:str):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="Georefer")
    location = geolocator.reverse('6.337403, -75.514541')
    print(location.address)
    print(location.raw)

articulo = pd.read_excel(r'C:\Users\Santiago\PycharmProjects\pythonProject\Alcaldia\Formatos\Articulos.xlsx')
art = pd.DataFrame(articulo)
print(art.values)