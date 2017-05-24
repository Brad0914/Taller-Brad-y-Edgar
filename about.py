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
    about_desc.insert(END, "A pesar de que 'Linux' se denomina en la jerga cotidiana al sistema operativo,2 3 este es en realidad solo el Kernel (núcleo) del sistema. La verdadera denominación del sistema operativo es 'GNU/Linux' debido a que el resto del sistema (la parte fundamental de la interacción entre el hardware y el usuario) se maneja con las herramientas del proyecto GNU (www.gnu.org) y con entornos de escritorio (como GNOME), que también forma parte del proyecto GNU aunque tuvo un origen independiente. Como el Proyecto GNU destaca,4 GNU es una distribución, usándose el término sistema operativo en el sentido empleado en el ecosistema Unix, lo que en cualquier caso significa que Linux es solo una pieza más dentro de GNU/Linux. Sin embargo, una parte significativa de la comunidad, así como muchos medios generales y especializados, prefieren utilizar el término Linux para referirse a la unión de ambos proyectos.")
    about_desc.config(state=DISABLED)
    about_desc.place(x = 20, y = 60)
     
    about_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_about_view()
