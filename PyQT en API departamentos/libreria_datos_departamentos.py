import requests

class ClienteDepartamentos:

    @staticmethod
    def consultar_departamentos():
        url = "https://api-colombia.com/api/v1/Department/name/departaments"
        response = requests.get(url)
        response_json = response.json()
        listado = ClienteDepartamentos.convertir_respuesta_a_arreglo(response_json)
    
        return listado

    @staticmethod
    def convertir_respuesta_a_arreglo(response_json):
        listado = []
        for item in response_json:
            id = str(item['id']).strip()
            listado.append([id, item['name'], item['description'], item['cityCapitalId'], item['municipalities'], item['surface'], item['population'], item['phonePrefix'], item['countryId']])
                
        return listado
