from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import *
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import LabelFrame
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from modelo_poo4 import motor
from tkinter import W
from tkinter import VERTICAL
from tkinter import NS


class VistaPrincipal(tk.Frame):
    def __init__(self, window):
        super(VistaPrincipal, self).__init__()
        self.objeto = motor()
        self.root = window

        self.root.title("A ver si Ahorra")

        # Títulos
        self.titulo = tk.Label(
            self.root, text="Gastos Realizados", font=("Helvetica", 19)
        )
        self.titulo.grid(row=0, column=0, columnspan=5, padx=10, pady=7)

        # Crear el FRAME de DATA y sus campos (Label, Entry, DateEntry)
        self.data_frame = tk.LabelFrame(self.root)
        self.data_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=7)

        self.lugar = tk.Label(self.data_frame, text="Lugar")
        self.lugar.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        self.importe = tk.Label(self.data_frame, text="Importe")
        self.importe.grid(row=1, column=0, sticky=W, padx=10, pady=10)

        self.fecha = tk.Label(self.data_frame, text="Fecha")
        self.fecha.grid(row=0, column=3, sticky=W, padx=10, pady=10)

        self.descripcion = tk.Label(self.data_frame, text="Descripción")
        self.descripcion.grid(row=1, column=3, sticky=W, padx=10, pady=10)

        # separador estético
        self.separador = ttk.Separator(self.data_frame, orient=VERTICAL)
        self.separador.grid(row=0, column=2, rowspan=3, sticky=NS, padx=10)

        # Definir las Variables del Entorno Gráfico
        self.var_tk_lugar, self.var_tk_fecha, self.var_tk_importe, self.var_tk_descripcion = (
            tk.StringVar(),
            tk.StringVar(),
            tk.DoubleVar(),
            tk.StringVar(),
        )
        w_ancho = 20

        # valores de entrada
        self.lugar = tk.Entry(
            self.data_frame, textvariable=self.var_tk_lugar, width=w_ancho
        )
        self.lugar.grid(row=0, column=1, sticky=W, padx=10)

        self.importe = tk.Entry(
            self.data_frame, textvariable=self.var_tk_importe, width=w_ancho
        )
        self.importe.grid(row=1, column=1, sticky=W, padx=10)

        self.fecha = DateEntry(
            self.data_frame,
            selectmode="day",
            textvariable=self.var_tk_fecha,
            date_pattern="dd-mm-y",
            width=w_ancho,
        )
        self.fecha.grid(row=0, column=4, sticky=W, padx=10)

        self.descripcion = tk.Entry(
            self.data_frame, textvariable=self.var_tk_descripcion, width=w_ancho
        )
        self.descripcion.grid(row=1, column=4, sticky=W, padx=10)

        # Botones
        self.botones_frame = tk.LabelFrame(self.root)
        self.botones_frame.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

        # botón alta
        self.boton_alta = tk.Button(
            self.botones_frame, text="Agregar Registro", command=lambda: self.alta()
        )
        self.boton_alta.grid(row=0, column=0, padx=10, pady=10)

        # botón borrar
        self.boton_borrar = tk.Button(
            self.botones_frame, text="Eliminar Registro", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=0, column=1, padx=10, pady=10)

        # botón limpiar
        self.boton_limpiar = tk.Button(
            self.botones_frame, text="Limpiar Registro", command=lambda: self.limpiar()
        )
        self.boton_limpiar.grid(row=0, column=2, padx=10, pady=10)

        # TREEVIEW
        self.tabla = ttk.Treeview(self.root)
        self.tabla["columns"] = ("col1", "col2", "col3", "col4")
        self.tabla.column("#0", width=50, minwidth=50, anchor=W)
        self.tabla.column("col1", width=100, minwidth=100, anchor=W)
        self.tabla.column("col2", width=100, minwidth=100, anchor=W)
        self.tabla.column("col3", width=100, minwidth=100, anchor=W)
        self.tabla.column("col4", width=100, minwidth=100, anchor=W)

        # Crear los Títulos (Headings)
        self.tabla.heading("#0", text="Id")
        self.tabla.heading("col1", text="Lugar")
        self.tabla.heading("col2", text="Fecha")
        self.tabla.heading("col3", text="Importe")
        self.tabla.heading("col4", text="Descripción")

        self.tabla.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

    def alta(self,):
        self.objeto.alta(
            self.lugar.get(),
            self.fecha.get(),
            self.importe.get(),
            self.descripcion.get(),
            self.tabla,
        )

    def baja(self,):
        self.objeto.borrar(self.tabla)

    def limpiar(self,):
        self.objeto.limpiar(self.lugar, self.fecha, self.importe, self.descripcion)

    def actualizar(self,):
        self.objeto.actualizar_tabla(self.tabla)
