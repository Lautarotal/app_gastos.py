from tkinter import Tk
import vista_poo4


class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = vista_poo4.VistaPrincipal(self.root_controler)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    try:
        application.objeto_vista.actualizar()
    except:
        print("Aún no existe estructura")
    root_tk.mainloop()
