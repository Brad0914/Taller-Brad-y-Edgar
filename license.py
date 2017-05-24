from tkinter import *
license_view = Tk()

def display_license_view():
    license_view.title("Taller GIT - Licencia") 
    license_view.minsize(500,500) 
    license_view.maxsize(500,500)
     
    license_lbl = Label(license_view, text = "Licencia", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
    license_lbl.place(x = 20, y = 20)

    license_desc = Text(license_view, width= 65, height = 8, bg = "#CCC")
    license_desc.pack()
    license_desc.insert(END, "Copyright (C) 2007 Free Software Foundation, Inc. http://fsf.org/ Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.")
    license_desc.config(state=DISABLED)
    license_desc.place(x = 20, y = 60)
     
    license_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_license_view()
