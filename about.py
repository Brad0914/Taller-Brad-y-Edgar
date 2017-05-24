from tkinter import *
about_view = Tk()

def display_about_view():
    about_view.title("Taller GIT - Sobre Nosotros") 
    about_view.minsize(500,500) 
    about_view.maxsize(500,500)
     
    about_lbl = Label(about_view, text = "Sobre este proyecto", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
    about_lbl.place(x = 20, y = 20)

    about_desc = Text(about_view, width= 65, height = 8, bg = "#CCC")
    about_desc.pack()
    about_desc.insert(END, "GitHub es una forja (plataforma de desarrollo colaborativo) para alojar proyectos utilizando el sistema de control de versiones Git. Utiliza el framework Ruby on Rails por GitHub, Inc. (anteriormente conocida como Logical Awesome). Desde enero de 2010, GitHub opera bajo el nombre de GitHub, Inc. El código se almacena de forma pública, aunque también se puede hacer de forma privada, creando una cuenta de pago.")
    about_desc.config(state=DISABLED)
    about_desc.place(x = 20, y = 60)
     
    about_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_about_view()
