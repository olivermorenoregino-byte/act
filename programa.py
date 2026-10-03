
import tkinter as tk
from PIL import Image, ImageTk


# =========================
# CLASE DEL NODO
# =========================

class EventoUniversidad:
    def __init__(self, dia, nombre, asistencia, foto_inicio, foto_final):
        self.dia = dia
        self.nombre = nombre
        self.asistencia = asistencia
        self.foto_inicio = foto_inicio
        self.foto_final = foto_final
        self.siguiente = None
        self.anterior = None


# =========================
# CREACIÓN DE EVENTOS
# =========================

lunes = EventoUniversidad(
    "Lunes",
    "Apertura de la Semana Uniremington",
    "Obligatoria",
    "lunes_inicio.jpg",
    "lunes_final.jpg"
)

martes = EventoUniversidad(
    "Martes",
    "talentos uniremington",
    "Obligatoria",
    "martes_inicio.jpg",
    "martes_final.jpg"
)

miercoles = EventoUniversidad(
    "Miércoles",
    "juegos cultura general",
    "Voluntaria",
    "miercoles_inicio.jpg",
    "miercoles_final.jpg"
)

jueves = EventoUniversidad(
    "Jueves",
    "declamadores invitados",
    "Voluntaria",
    "jueves_inicio.jpg",
    "jueves_final.jpg"
)

viernes = EventoUniversidad(
    "Viernes",
    "entrega de distinciones",
    "Voluntaria",
    "viernes_inicio.jpg",
    "viernes_final.jpg"
)

sabado = EventoUniversidad(
    "Sábado",
    "dia de la familia uniremington",
    "Voluntaria",
    "sabado_inicio.jpg",
    "sabado_final.jpg"
)


# =========================
# LISTA LIGADA
# =========================

lunes.siguiente = martes

martes.anterior = lunes
martes.siguiente = miercoles

miercoles.anterior = martes
miercoles.siguiente = jueves

jueves.anterior = miercoles
jueves.siguiente = viernes

viernes.anterior = jueves
viernes.siguiente = sabado

sabado.anterior = viernes


actual = lunes


# =========================
# VENTANA
# =========================

ventana = tk.Tk()
ventana.title("Semana de Aniversario Uniremington")
ventana.geometry("1200x800")
ventana.configure(bg="#f4f6f9")


# =========================
# FUNCIÓN PARA MOSTRAR
# =========================

def mostrar_informacion():

    titulo_evento.config(text=actual.nombre)

    datos.config(
        text=f"Día: {actual.dia}\nTipo de asistencia: {actual.asistencia}"
    )

    try:
        imagen1 = Image.open(actual.foto_inicio)
        imagen1 = imagen1.resize((350, 250))
        foto1 = ImageTk.PhotoImage(imagen1)

        lbl_imagen1.config(image=foto1)
        lbl_imagen1.image = foto1

    except:
        lbl_imagen1.config(
            image="",
            text="No se encontró la imagen"
        )

    try:
        imagen2 = Image.open(actual.foto_final)
        imagen2 = imagen2.resize((350, 250))
        foto2 = ImageTk.PhotoImage(imagen2)

        lbl_imagen2.config(image=foto2)
        lbl_imagen2.image = foto2

    except:
        lbl_imagen2.config(
            image="",
            text="No se encontró la imagen"
        )


# =========================
# BOTONES
# =========================

def siguiente():
    global actual

    if actual.siguiente:
        actual = actual.siguiente
        mostrar_informacion()


def anterior():
    global actual

    if actual.anterior:
        actual = actual.anterior
        mostrar_informacion()


def inicio():
    global actual

    actual = lunes
    mostrar_informacion()


# =========================
# TÍTULO
# =========================

titulo_principal = tk.Label(
    ventana,
    text="SEMANA DE ANIVERSARIO UNIREMINGTON",
    font=("Arial", 24, "bold"),
    bg="#f4f6f9",
    fg="#003366"
)

titulo_principal.pack(pady=20)


# =========================
# CUADRO DE INFORMACIÓN
# =========================

marco = tk.Frame(
    ventana,
    bg="white",
    bd=3,
    relief="ridge"
)

marco.pack(padx=20, pady=10)

titulo_evento = tk.Label(
    marco,
    text="",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#222222"
)

titulo_evento.pack(pady=10)

datos = tk.Label(
    marco,
    text="",
    font=("Arial", 12),
    bg="white"
)

datos.pack(pady=5)


# =========================
# FOTOS
# =========================

contenedor_fotos = tk.Frame(
    ventana,
    bg="#f4f6f9"
)

contenedor_fotos.pack(pady=20)

tk.Label(
    contenedor_fotos,
    text="Foto Inicial",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9"
).grid(row=0, column=0)

tk.Label(
    contenedor_fotos,
    text="Foto Final",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9"
).grid(row=0, column=1)

lbl_imagen1 = tk.Label(contenedor_fotos)
lbl_imagen1.grid(row=1, column=0, padx=30)

lbl_imagen2 = tk.Label(contenedor_fotos)
lbl_imagen2.grid(row=1, column=1, padx=30)


# =========================
# BOTONES
# =========================

marco_botones = tk.Frame(
    ventana,
    bg="#f4f6f9"
)

marco_botones.pack(pady=20)

btn_anterior = tk.Button(
    marco_botones,
    text="Anterior",
    width=15,
    bg="red",
    fg="white",
    command=anterior
)

btn_anterior.grid(row=0, column=0, padx=10)

btn_inicio = tk.Button(
    marco_botones,
    text="Inicio",
    width=15,
    bg="green",
    fg="white",
    command=inicio
)

btn_inicio.grid(row=0, column=1, padx=10)

btn_siguiente = tk.Button(
    marco_botones,
    text="Siguiente",
    width=15,
    bg="blue",
    fg="white",
    command=siguiente
)

btn_siguiente.grid(row=0, column=2, padx=10)


# =========================
# PIE DE PÁGINA
# =========================

pie = tk.Label(
    ventana,
    text="Proyecto realizado con estructura de datos - Lista Ligada",
    font=("Arial", 10),
    bg="#f4f6f9",
    fg="gray"
)

pie.pack(side="bottom", pady=10)

mostrar_informacion()

ventana.mainloop()
