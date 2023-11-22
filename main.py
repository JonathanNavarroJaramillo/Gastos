#Recomendación. Trabajar con Jupyer notebook, PyCharm o google colaboratory
#En caso de trabajarlo de manera local instalar las liberias

import speech_recognition as sr
import openpyxl
from reportlab.pdfgen import canvas
from datetime import datetime
import matplotlib.pyplot as plt

def reconocer_voz():
     recognizer = sr.Recognizer()
     with sr.Microphone() as source:
        print("Hable ahora para registrar el gasto:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

     try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
     except sr.UnknownValueError:
        return None
def registrar_gasto():
    gasto = input("Ingrese el gasto por texto: ")
    return {"Fecha": datetime.now(), "Descripción": gasto}

def exportar_a_excel(datos):
    # ... (código para exportar a excel)

def generar_resumen_pdf(datos):
    # ... (cdigo para generar informe)

def generar_grafico(datos):
    # ... (cdigo para generar informe)


def main():
    registros = []

    while True:
        print("¿Desea registrar un gasto? (Sí/No)")
        respuesta = input().lower()

        if respuesta == "si":
            print("¿Desea ingresar el gasto por voz o por texto? (voz/texto)")
            metodo_ingreso = input().lower()

            if metodo_ingreso == "voz":
                print("Hable ahora para registrar el gasto:")
                descripcion_voz = reconocer_voz()
                if descripcion_voz:
                    print(f"Gasto registrado por voz: {descripcion_voz}")
                    registros.append({"Fecha": datetime.now(), "Descripción": descripcion_voz})
                else:
                    print("No se pudo entender el audio. Intente de nuevo.")
            elif metodo_ingreso == "texto":
                gasto = registrar_gasto()
                registros.append(gasto)
                print("Gasto registrado por texto.")
            else:
                print("Método de ingreso no válido. Intente de nuevo.")

        elif respuesta == "no":
            break
        else:
            print("Respuesta no válida. Intente de nuevo.")

    def mostrar_gui():
        root = Tk()
        root.title("Registro de Gastos")

        # Etiquetas
        Label(root, text="Categoría:").grid(row=0, column=0)


        # Campos de entrada
        categoria_var = StringVar()
        cantidad_var = StringVar()

        Entry(root, textvariable=categoria_var).grid(row=0, column=1)


        # Función para registrar gasto desde la GUI
        def registrar_gasto_gui():
            categoria = categoria_var.get()
            cantidad = cantidad_var.get()
            if categoria and cantidad:
                registros.append({"Fecha": datetime.now(), })
                messagebox.showinfo("Registro Exitoso", "Gasto registrado exitosamente.")
                categoria_var.set("")
                cantidad_var.set("")
            else:
                messagebox.showwarning("Error", "Por favor, complete todos los campos.")

        # Botón para registrar gasto
        Button(root, text="Registrar Gasto", command=registrar_gasto_gui).grid(row=2, column=0, columnspan=2)

        root.mainloop()

    exportar_a_excel(registros)
    generar_resumen_pdf(registros)
    generar_grafico(registros)
    print("Registros guardados en registros_gastos.xlsx, resumen_gastos.pdf y grafico_gastos.png")

if __name__ == "__main__":
    main()
