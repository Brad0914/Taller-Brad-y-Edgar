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
    about_desc.insert(END, "GNU/Linux, es el término empleado para referirse a la combinación del sistema operativo GNU, desarrollado por la FSF, y el núcleo(kernel) Linux, desarrollado por Linus Torvalds y la Linux Foundation. Su desarrollo es uno de los ejemplos más prominentes de software libre; todo su código fuente puede ser utilizado, modificado y redistribuido libremente por cualquiera bajo los términos de la GPL (Licencia Pública General de GNU) y otra serie de licencias libres")
    about_desc.config(state=DISABLED)
    about_desc.place(x = 20, y = 60)
     
    about_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_about_view()
