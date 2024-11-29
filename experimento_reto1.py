from colorama import init, Fore, Back, Style
from datetime import datetime
from prettytable import PrettyTable
import statistics


class Experimento:

    def __init__(self, name, date, description, results, media, mediana, moda, desviacion_estandar, rango, varianza):
            self.name = name
            self.date = date
            self.description = description
            self.results = results
            self.media = media
            self.mediana = mediana
            self.moda = moda
            self.desviacion_estandar = desviacion_estandar
            self.rango = rango
            self.varianza = varianza
            
   

# función para agregar un experimento


def agregar_experimento(listExperimento):
    name = input("Ingrese el nombre del experimento: ")
    date_text = input("Ingrese la fecha del experimento (dd/mm/aaaa): ")
    
    try:
        date = datetime.strptime(date_text, "%d/%m/%Y")
    except:
        print("Fecha invalida, ingrese una fecha en el formato dd/mm/aaaa")
        return
    
    description = input("Ingrese una categoría del experimento (ej. biología, física, química, etc.): ")
    results_text = (input("Ingrese los resultados del experimento separados por comas (,): "))
    try:
        #results = [float(x) for x in results_text.split(",")]
        results = list(map(float, results_text.split(",")))
    except:
        print("\033[;31m" +"\nLos resultados deben ser separados por comas\n"+"\033[0;m")
        return

    # cálculo de estadisticas básicas
    # media
    media = statistics.mean(results)
    # mediana
    mediana = statistics.median(results)
    # moda
    moda = None
    # desviación estandar
    desviacion_estandar = None
    # varianza
    varianza = None
    
    try:
        moda = statistics.mode(results)
        desviacion_estandar = statistics.stdev(results)
        varianza = statistics.variance(results)
    except:
        print("\033[;31m" + "\nTen en cuenta que con un solo dato ingresado no es posible calcular la moda, desviación estandar y varianza\n"+"\033[0;m")      
        moda = 0
        desviacion_estandar = 0
        varianza = 0
    
    # rango
    maximo = max(results)
    minimo = min(results)
    rango = maximo - minimo

  
    
    agregarExperimento = Experimento(name, date, description, results, media, mediana, moda, desviacion_estandar, rango, varianza)
    listExperimento.append(agregarExperimento)
    print("Experimento agregado con éxito")
    
    
#Visualizar datos estadísticos


def analisis_resultados(listExperimento):
    
    if not listExperimento:
        print("No hay experimentos para analizar")
        return
    
    table = PrettyTable()
    table.field_names = ["Nombre", "Fecha", "Descripción", 
                         "Resultados","Media","Mediana","Moda",
                         "Desviación estándar","Rango","Varianza"
                         ]
    table.align = "l" # alinear a la izquierda
    for i in listExperimento:
        
        descripcion = i.description
        resultados = i.results 
        media = i.media
        mediana = i.mediana
        moda = i.moda
        desviacionEstandar = i.desviacion_estandar 
        rango = i.rango
        varianza = i.varianza
        
        table.add_row([
            f"{i.name}", 
            f"{i.date.strftime('%d/%m/%Y')}", 
            f"\033[;31m{descripcion}\033[0;m",
            f"\033[;31m{resultados}\033[0;m",
            f"\033[;31m{media:.2f}\033[0;m",
            f"\033[;31m{mediana:.2f}\033[0;m",
            f"\033[;31m{moda:.2f}\033[0;m",
            f"\033[;31m{desviacionEstandar:.2f}\033[0;m",
            f"\033[;31m{rango:.2f}\033[0;m",
            f"\033[;31m{varianza:.2f}\033[0;m"
            ])
        
    print(table)
       
        
def eliminar_experimentos(listExperimento):
    if not listExperimento:
        print("No hay experimentos para eliminar")
    
    #listamos experimentos
    print("Experimentos disponibles: \n")
    for i, nombre in enumerate(listExperimento, start=1):
        print(f"{i}. Experimento {nombre.name}\n")
    
    # eliminar experimentos
    respuesta = input("¿Deseas eliminar un experimento? (si/no)\n")
    if respuesta.lower() == "si":
        while True:
            try:
                eliminar = int(input("Ingrese el número del experimento a eliminar: "))
                if 1 <= eliminar <= len(listExperimento):
                    eliminado = listExperimento.pop(eliminar -1)
                    print(f"el Experimento '{eliminado.name}' fue elimado con éxito")
                    break
                else:
                    print(f"Por favor ingresa un número que esté entre 1 y {len(listExperimento)}\n")
            except:
                print("Error, ingrese un número\n")
    else:
        print("No se eliminaron experimentos\n")

def seleccionar_experimentos(listExperimento):
        
    print("\n**************EXPERIMENTOS DISPONIBLES*****************\n")
    for i, nombre in enumerate(listExperimento, start=1):
        print(f"{i}. {nombre.name}\n")
        
    index = input("Selecciona los experimentos que deseas comparar (separados por comas) o escriba" + "\033[1;31m" + " 'all' " + "\033[0;m" "para comparar todos: \n")

    if index == "all": # si se selecciona todos los experimentos
            return listExperimento
    
    try:
        index = [int(i) - 1 for i in (index.split(","))]
        
        return [listExperimento[i] for i in index]
    except:
        print("Error, ingresa los números de los experimentos separados por comas\n")
        return None
  
def comparación_experimentos(listExperimento):
    if not listExperimento:
        print("No hay experimentos para comparar")
        return
    
    # seleccionar experimentos
    experimentoSeleccionado = seleccionar_experimentos(listExperimento)
    
    # Extraemos los nombres de los experimentos y estadisticos
    
    #nombres
    nombres= [exp.name for exp in experimentoSeleccionado]
    # media
    media = [exp.media for exp in experimentoSeleccionado]
    # comparación de mediana    
    mediana = [exp.media for exp in experimentoSeleccionado]
    # comparación de moda
    moda = [exp.moda for exp in experimentoSeleccionado]
    # comparación de desviación estándar
    desviacion = [exp.desviacion_estandar for exp in experimentoSeleccionado]
    # comparación de rango  
    rango = [exp.rango for exp in experimentoSeleccionado]
    
   
        
    # Crear función auxiliar para imprimir comparaciones
    def imprimir_comparación(titulo, valores, numerosExperimentos):
        print(f"\033[1;36m{titulo}\033[0;m")
        for i, (nombre, valor) in enumerate(zip(nombres, valores), start=1):
            print(f"{i}. {nombre}: {valor:.2f}")
        
        max_valor = max(valores)
        min_valor = min(valores)
        
        
        print(f"El maximo valor es :  {max_valor:.2f}")
        print(f"El minimo valor es :  {min_valor:.2f}")
        
        if len(numerosExperimentos) < 2:
            print("Solo hay un experimento, no se puede comparar\n")
        else:
            if len(set(valores)) == 1:
                print("Todos los experimentos tienen el mismo valor.\n")
            else:
                print("Los experimentos tienen valores diferentes.\n")
        
    # Comparar cada métrica
    imprimir_comparación("Medias", media, experimentoSeleccionado)
    imprimir_comparación("Medianas", mediana, experimentoSeleccionado)
    imprimir_comparación("Modas", moda, experimentoSeleccionado)
    imprimir_comparación("Desviaciones estándar", desviacion,experimentoSeleccionado)
    imprimir_comparación("Rangos", rango,experimentoSeleccionado)  
       

def generacion_informe(listExperimento):
    # generar un informe con los resultados de los experimentos
    if not listExperimento:
        print("No hay experimentos para generar informe")
        return
    
    experimentoSeleccionado = seleccionar_experimentos(listExperimento)
    
    with open("informe.txt", "w") as archivo:
        archivo.write(f"***************INFORME DE EXPERIMENTOS************\n\n")
        
        for i, data in enumerate(experimentoSeleccionado, start=1):

            archivo.write(f"===============Experimento {i}=================\n")
            archivo.write(f"Nombre: {data.name}\n")
            archivo.write(f"Fecha: {data.date.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Descripción: {data.description} \n")
            archivo.write(f"Resultados: {data.results} \n")
            archivo.write(f"Media: {data.media}\n")
            archivo.write(f"Mediana: {data.mediana} \n")
            archivo.write(f"Moda: {data.moda} \n")
            archivo.write(f"Desviación estandar: {data.desviacion_estandar} \n")
            archivo.write(f"Rango: {data.rango} \n")
            archivo.write(f"Varianza: {data.varianza} \n")
            archivo.write("\n")
            archivo.write("============================================")
        
    print("******************DATOS A GENERAR EN EL INFORME*******************")
    analisis_resultados(experimentoSeleccionado)             

    print ("\nInforme generado con exito como 'informe.txt'\n")                      
            
def menu():
    
    listExperimento = []
    
    while True:
        print("========================")
        print("-----Menú principal-----")
        print("========================")
        print("1. Agregar experimento")
        print("2. Analizar resultados")
        print("3. Eliminar experimento")
        print("4. Comparar experimentos")
        print("5. Generar informe")
        print("6. Salir" + "\n")
        
        try:
            
            opcion = int(input("¿Qué deseas hacer? (escribir el número de la opción): " + "\n"))
        
            if 1 <= opcion <= 6:
                if opcion == 1:
                    agregar_experimento(listExperimento)
                elif opcion == 2:
                    analisis_resultados(listExperimento)
                elif opcion == 3:
                    eliminar_experimentos(listExperimento)
                elif opcion == 4:
                    comparación_experimentos(listExperimento)
                elif opcion == 5:
                    generacion_informe(listExperimento)
                elif opcion == 6:
                    print("==============================================")
                    print("\033[4;35;47m"+"******************GRACIAS POR USAR EL PROGRAMA*********************"+'\033[0;m')
                    print("==============================================")
                    break
            else:
                print("Por favor, ingresa un número entre 1 y 6.\n")
        except:
            print("Opcion invalida, por favor, ingresa un número entre 1 y 6.\n")
        
        
if __name__ == "__main__":
    menu()
    






