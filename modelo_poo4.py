import re
import sqlite3
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter import END


class motor:
    def __init__(self,):
        try:
            connection_db = sqlite3.connect("Ahorre_ya.db")
            cursor = connection_db.cursor()
            sql = " CREATE TABLE IF NOT EXISTS gastos(id integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
                lugar text, fecha text, importe real, descripcion text)"
            cursor.execute(sql)
            connection_db.commit()
        except:
            print("Error de conexion")

    def conexion(self,):
        connection_db = sqlite3.connect("Ahorre_ya.db")
        return connection_db

    # Función Actualizar Tabla
    def actualizar_tabla(self, tabla):
        records = tabla.get_children()
        for element in records:
            tabla.delete(element)

        # fuera del bucle for
        sql = "SELECT * FROM gastos ORDER BY id ASC"
        connection_db = self.conexion()
        cursor = connection_db.cursor()
        datos = cursor.execute(sql)
        global resultado
        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            tabla.insert(
                "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
            )

    def cerrar_conexion(self,):
        print("cerrar_conexion")

    # FUNCIONES DE LOS BOTONES

    # Función Alta
    def alta(self, lugar, fecha, importe, descripcion, tabla):
        cadena = lugar
        patron = "^[A-Za-záéíóú,0-9]*$"
        if lugar == "":
            self.alta_error()
        else:
            if re.match(patron, cadena):
                connection_db = self.conexion()
                cursor = connection_db.cursor()
                data = (lugar, fecha, importe, descripcion)
                sql = "INSERT INTO gastos (lugar, fecha, importe, descripcion)\
                      VALUES (?, ?, ?, ?);"
                cursor.execute(sql, data)
                connection_db.commit()
                self.actualizar_tabla(tabla)
                # self.alta_correcta()
            else:
                self.alta_error()

    # Función Borrar
    def borrar(self, tabla):
        valor = tabla.selection()
        item = tabla.item(valor)
        mi_id = item["text"]
        connection_db = self.conexion()
        cursor = connection_db.cursor()
        data = (mi_id,)
        sql = "DELETE from gastos WHERE id = ?;"
        cursor.execute(sql, data)
        connection_db.commit()
        # tabla.delete(valor)
        self.actualizar_tabla(tabla)

    # Función limpiar formulario

    def limpiar(self, lugar, fecha, importe, descripcion):
        lugar.delete(0, END)
        fecha.delete(0, END)
        importe.delete(0, END)
        descripcion.delete(0, END)

    # Funcion modificar
    """def modificar(self, lugar, fecha, importe, descripcion, tabla):
        item_seleccionado = tabla.focus()
        mi_id = tabla.item(item_seleccionado)
        connection_db = self.conexion()

        cursor = connection_db.cursor()
        sql = "UPDATE gastos SET (lugar=?, fecha=?, importe=?, descripcion=? WHERE id=?"
        data = (lugar, fecha, importe, descripcion, mi_id)
        cursor.execute(sql, data)
        connection_db.commit()
        print(sql, data)

        self.actualizar_tabla(tabla)"""

    # ----------------------------------------------------------------------
    # FUNCIONES DE NOTIFICACIONES
    #
    # Función ALTA - ERORR
    def alta_error(self,):
        showerror("Error", "Ha ocurrido un error")

    def alta_correcta(self,):
        showinfo("Éxito", "Se guardó la información")

