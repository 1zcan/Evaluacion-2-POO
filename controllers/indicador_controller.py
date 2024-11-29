import requests
from datetime import datetime
from models.indicadores import IndicadorEconomico

def consultar_por_fecha(indicador: str, fecha: str, idEmpleado: int) -> IndicadorEconomico:
    try:
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(fecha, "%d-%m-%Y")

        # Consultamos el valor del indicador en la fecha especificada desde la API
        url = f"https://www.mindicador.cl/api/{indicador}/{fecha.strftime('%d-%m-%Y')}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Revisamos si hay datos disponibles para la fecha consultada
        if not data.get('serie'):
            print("No hay datos disponibles para la fecha especificada.")
            return None

        # Extraemos el valor del indicador de la respuesta
        valor_indicador = data['serie'][0]['valor']

        return IndicadorEconomico(
            tipoIndicador=indicador,
            valorIndicador=valor_indicador,
            fechaIndicador=fecha.strftime("%d-%m-%Y"),
            idEmpleado=idEmpleado,
            sitioWeb="https://www.mindicador.cl"
        )
    except requests.exceptions.RequestException as error:
        print(f"Error en la consulta de la API: {error}")
        return None
    except Exception as error:
        print(f"Error al consultar la fecha: {error}")
        return None

def consultar_por_periodo( indicador: str, año: int, fecha_inicio: str, fecha_fin: str, idEmpleado: int) -> list:
        try:
            # Convertimos las fechas de inicio y fin a objetos datetime
            fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
            fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y")

            # Consultamos el año completo desde la API basado en el año especificado por el usuario
            url = f"https://www.mindicador.cl/api/{indicador}/{año}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Revisamos si hay datos disponibles en el año consultado
            if not data.get('serie'):
                print("No hay datos disponibles para el año especificado.")
                return []

            resultados = []
            valores_unicos = set()

            # Filtramos los datos dentro del rango de fecha solicitado
            for item in data['serie']:
                # Intentamos convertir la fecha en el formato de la API a "%Y-%m-%dT%H:%M:%S.%fZ"
                try:
                    fecha_indicador = datetime.strptime(item['fecha'], "%Y-%m-%dT%H:%M:%S.%fZ")
                except ValueError:
                    # Si ya está en el formato "%d-%m-%Y", saltamos la conversión
                    fecha_indicador = datetime.strptime(item['fecha'], "%d-%m-%Y")

                valor_indicador = item['valor']

                # Si la fecha está dentro del rango y el valor no se ha agregado, lo incluimos
                if fecha_inicio <= fecha_indicador <= fecha_fin:
                    par_fecha_valor = (fecha_indicador.date(), valor_indicador)
                    if par_fecha_valor not in valores_unicos:
                        valores_unicos.add(par_fecha_valor)
                        resultados.append(
                            IndicadorEconomico(
                                tipoIndicador=indicador,
                                valorIndicador=valor_indicador,
                                fechaIndicador=fecha_indicador.strftime("%d-%m-%Y"),
                                idEmpleado=idEmpleado,
                                sitioWeb="https://www.mindicador.cl"
                            )
                        )

            return resultados
        except requests.exceptions.RequestException as error:
            print(f"Error en la consulta de la API: {error}")
            return []
        except Exception as error:
            print(f"Error al consultar el periodo: {error}")
            return []

def guardar_indicadores(self, indicadores: list) -> bool:

    cursor = self.conexion.cursor()
    query = ("INSERT INTO IndicadoresEconomicos "
                "(tipoIndicador, valorIndicador, fechaIndicador, idEmpleado, sitioWeb) "
                "VALUES (%s, %s, %s, %s, %s)")
    
    parametros = [(indicador.tipoIndicador, indicador.valorIndicador, indicador.fechaIndicador, indicador.idEmpleado, indicador.sitioWeb)
                    for indicador in indicadores]
    
    cursor.executemany(query, parametros)
    self.conexion.commit()
    cursor.close()
    return True