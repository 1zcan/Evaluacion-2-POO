import requests

class IndicadorEconomico:
    def __init__(self, tipoIndicador: str, valorIndicador: float, fechaIndicador: str, idEmpleado: int, sitioWeb: str):
        self.tipoIndicador = tipoIndicador
        self.valorIndicador = valorIndicador
        self.fechaIndicador = fechaIndicador
        self.idEmpleado = idEmpleado
        self.sitioWeb = sitioWeb

class IndicadorEconomicoModelo(): 
    def consultar_por_fecha(self, indicador: str, fecha: str, idEmpleado: int) -> IndicadorEconomico:

        try:
            url = f"https://www.mindicador.cl/api/{indicador}/{fecha}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            valor = data['serie'][0]['valor'] if data.get('serie') else None
            fecha1 = data['serie'][0]['fecha'] if data.get('serie') else None
        
            if valor is None:
                print("No hay datos disponibles para la fecha especificada.")
                return None
            
            indicador_obj = IndicadorEconomico(tipoIndicador=indicador, valorIndicador=valor, fechaIndicador=fecha1, idEmpleado=idEmpleado, sitioWeb="https://www.mindicador.cl")
            return indicador_obj
        except requests.exceptions.RequestException as error:
            print(f"Error en la consulta de la API: {error}")
            return None