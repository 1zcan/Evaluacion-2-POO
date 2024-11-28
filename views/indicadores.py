import datetime

def mostrarMenuIndicador(self):
        while True:
            print("Menu Indicadores Económicos")
            print("1. Consultar indicador por fecha específica")
            print("2. Consultar indicador por periodo")
            print("s. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == '1':
                self.consultar_por_fecha()
            elif opcion == '2':
                self.consultar_por_periodo()
            elif opcion == 's':
                print("Saliendo del menú.")
                self.modelo.cerrar()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

def consultar_por_fecha(self):
        print("Consultar indicador por fecha específica")
        print("Lista de Indicadores")
        print("1. UF - Unidad de Fomento")
        print("2. IVP - Índice de valor Promedio")
        print("3. IPC - Índice de Precio al Consumidor")
        print("4. UTM - Unidad Tributaria Mensual")
        print("5. Dolar")
        print("6. Euro")

        indicador = input("Ingrese el indicador (Siglas segun corresponda): ").strip().lower()
        fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
        idEmpleado = int(input("Ingrese su ID empleado: "))

        resultado = self.modelo.consultar_por_fecha(indicador, fecha, idEmpleado)
        if resultado:
            try:
                fecha_acortada = datetime.strptime(resultado.fechaIndicador, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d-%m-%Y")
            except ValueError:
                fecha_acortada = datetime.strptime(resultado.fechaIndicador, "%d-%m-%Y").strftime("%d-%m-%Y")
            
            if indicador == "ipc":
                print(f"Valor de {resultado.tipoIndicador.upper()} el {fecha_acortada}: {resultado.valorIndicador}%")
            else:
                print(f"Valor de {resultado.tipoIndicador.upper()} el {fecha_acortada}: {resultado.valorIndicador} pesos.")
        
            guardar = input("¿Desea guardar este valor en la base de datos? (s/n): ")
            if guardar.lower() == 's':
                self.modelo.guardar_indicadores([resultado])
                print("Indicador guardado en la base de datos.")

def consultar_por_periodo(self):
    print("Consultar indicador por periodo")
    print("Lista de Indicadores")
    print("1. UF - Unidad de Fomento")
    print("2. IVP - Índice de valor Promedio")
    print("3. IPC - Índice de Precio al Consumidor")
    print("4. UTM - Unidad Tributaria Mensual")
    print("5. Dolar")
    print("6. Euro")

    indicador = input("Ingrese el indicador (Siglas segun corresponda): ").strip().lower()
    año = input("ingrese el año que desea consultar: ")
    fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
    fecha_fin = input("Ingrese la fecha de fin (DD-MM-YYYY): ")
    idEmpleado = int(input("Ingrese su ID empleado: "))

    resultados = self.modelo.consultar_por_periodo(indicador, año, fecha_inicio, fecha_fin, idEmpleado)
    if resultados:
        for resultado in resultados:

            try:
                fecha_acortada = datetime.strptime(resultado.fechaIndicador, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d-%m-%Y")
            except ValueError:
                fecha_acortada = datetime.strptime(resultado.fechaIndicador, "%d-%m-%Y").strftime("%d-%m-%Y")
            if indicador == "ipc":
                print(f"Fecha: {fecha_acortada} Valor de {resultado.tipoIndicador.upper()}: {resultado.valorIndicador}%")
            else:
                print(f"Fecha: {fecha_acortada} Valor de {resultado.tipoIndicador.upper()}: {resultado.valorIndicador} pesos")
            
        guardar = input("¿Desea guardar todos estos valores en la base de datos? (s/n): ")
        if guardar.lower() == 's':
            self.modelo.guardar_indicadores(resultados)
            print("Todos los indicadores han sido guardados en la base de datos.")
    else:
        print("No se encontraron valores en el periodo indicado.")