import datetime
import csv
import os
import matplotlib.pyplot as plt

# Codigo FUNCIONAL - falta mejorar porque en dos clicks se puede tumbar el programa.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso normal'
    elif 24.9 <= imc < 29.9:
        return 'Sobrepeso'
    elif imc >= 30:
        return 'Obesidad'
def main():
    opcion = 0
    nombre = None
    peso = None
    altura = None
    imc = None

    print("\n¡HOLA!\n Este es un menú para saber más sobre tu anatomía, y si tu estado físico es correcto.\n Podrás observar que se pueden calcular y guardar información que proporciones. \n ¡Ahí van los primeros pasos!:")
    while opcion != 8:
        print("1. Ingresa tu nombre")
        print("2. Ingresa tu primer apellido")
        print("3. Ingresar tu peso")
        print("4. Ingresar altura")
        print("5. Calcular IMC")
        print("6. Clasificar IMC")
        print("7. Mostrar hora y día")
        print("8. Salir")
    
        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            nombre = str(input("\nIntroduce tu nombre: "))
        elif opcion == 2:
            apellido = str(input("\nIntroduce tu primer apellido: "))
        elif opcion == 3:
            peso = float(input("\nIntroduce tu peso en KG: "))
        elif opcion == 4:
            altura = float(input("\nIntroduce tu altura en metros: "))
        elif opcion == 5:
            if peso is None or altura is None:
                print("Primero debes ingresar peso y altura.")
            else:
                imc = calcular_imc(peso, altura)
                print(f"\nTu IMC es: {imc:.2f}")
        elif opcion == 6:
            if imc is None:
                print("Primero debes calcular el IMC.")
            else:
                clasificacion = clasificar_imc(imc)
                print(f"Tu clasificación de IMC es: {clasificacion}")
        elif opcion == 7:
            hora_dia = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")
            print(f"Hora y día actual: {hora_dia}")
        elif opcion == 8:
            print("Guardando información en el archivo CSV...")
            with open('data_info.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(['Nombre', 'Peso', 'Altura', 'IMC', 'Clasificación de IMC', 'Fecha y Hora'])
                writer.writerow([nombre, peso, altura, imc, clasificar_imc(imc), datetime.datetime.now().strftime("%H:%M %d-%m-%Y")])
            print("¡Hasta luego!")

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 7.")

# def mostrar_grafica():
#     datos_registrados = leer_datos_csv()
#     fechas = [registro[0] for registro in datos_registrados]
#     IMCs = [registro[1] for registro in datos_registrados]
#     plt.plot(fechas, IMCs)
#     plt.title('Registro de IMC a lo largo del año')
#     plt.xlabel('Fecha')
#     plt.ylabel('IMC')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

if __name__ == "__main__":
    main()