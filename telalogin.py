from tkinter import ttk
from tkinter import *
from datetime import *
from display2lib import *


def tela():

    display = Tk()
    display.title("Àrea de login")
    display.resizable(width=False, height=False)
    display.config(bg="white")
    display.geometry("650x380")
    display.attributes("-alpha", 0.9)

    #funcao relogio
    def relogio():
        tempo = datetime.now()
        hora = tempo.strftime("%H:%M:%S")
        relogio_interface.config(text=hora)
        relogio_interface.after(120, relogio)

    #funcao cadastro
    def registro():
        user_frame.place(x=-1000, y=0)
        user_input.place(x=-1000, y=0)
        pass_frame.place(x=-1000, y=0)
        pass_input.place(x=-1000, y=0)
        bnt_cadastro.place(x=-1000, y=0)
        bnt_entrar.place(x=-1000, y=0)


        user_frame_registro = Label(frame_direita, text="Usuario:", font="Ivy 20", fg="white", bg="MIDNIGHTBLUE")
        user_frame_registro.place(x=30, y=20)

        user_input_registro = ttk.Entry(frame_direita, width= 21, font=("Ivy",15), justify=LEFT)
        user_input_registro.place(x=140, y=30)

        pass_frame_registro = Label(frame_direita, text="Senha:", font="Ivy 20", fg="white", bg="MIDNIGHTBLUE")
        pass_frame_registro.place(x=30, y=100)

        pass_input_registro = ttk.Entry(frame_direita, width= 21, font=("Ivy",15), justify=LEFT, show="*")
        pass_input_registro.place(x=140 ,y=110)

        email_label = Label(frame_direita, text="E-mail:", font="Ivy 20", fg="white", bg="MIDNIGHTBLUE")
        email_label.place(x=30, y=180)

        email_input = ttk.Entry(frame_direita, width= 21, font=("Ivy",15), justify=LEFT)
        email_input.place(x=140, y=180)

        bnt_cadastrar = Button(frame_direita, width=21, text="CADASTRAR", font="Ivy 15")
        bnt_cadastrar.place(x=120, y=250)

        def voltar():
            user_frame_registro.place(x=-1000, y=0)
            user_input_registro.place(x=-1000, y=0)
            pass_frame_registro.place(x=-1000, y=0)
            pass_input_registro.place(x=-1000, y=0)
            email_label.place(x=-1000, y=0)
            email_input.place(x=-1000, y=0)
            bnt_cadastrar.place(x=-1000, y=0)
            bnt_voltar.place(x=-1000, y=0)

            #recolocando
            user_frame.place(x=30, y=60)
            user_input.place(x=140, y=70)
            pass_frame.place(x=30, y=160)
            pass_input.place(x=133 ,y=170)
            bnt_cadastro.place(x=120, y=300)
            bnt_entrar.place(x=120, y=250)



        bnt_voltar = Button(frame_direita, width=10, text="<=", font="Ivy 15", command=voltar)
        bnt_voltar.place(x=120, y=300)




    #frames
    frame_esquerda = Frame(height=380, width=226, bg="MIDNIGHTBLUE")
    frame_esquerda.pack(side=LEFT)

    frame_direita = Frame(height= 380 ,width=420, bg="MIDNIGHTBLUE")
    frame_direita.pack(side=RIGHT)

    #interface
    user_frame = Label(frame_direita, text="Usuario:", font="Ivy 20", fg="white", bg="MIDNIGHTBLUE")
    user_frame.place(x=30, y=60)

    user_input = ttk.Entry(frame_direita, width= 20, font=("Ivy",15), justify=LEFT)
    user_input.place(x=140, y=70)

    pass_frame = Label(frame_direita, text="Senha:", font="Ivy 20", fg="white", bg="MIDNIGHTBLUE")
    pass_frame.place(x=30, y=160)

    pass_input = ttk.Entry(frame_direita, width= 21, font=("Ivy",15), justify=LEFT, show="*")
    pass_input.place(x=133 ,y=170)


    bnt_entrar = Button(frame_direita, width=21, text="ENTRAR", font="Ivy 15")
    bnt_entrar.place(x=120, y=250)

    bnt_cadastro = Button(frame_direita, width=21, text="CADASTRO", font="Ivy 15", command=registro)
    bnt_cadastro.place(x=120, y=300)

    #relogio interface
    relogio_interface = Label(frame_esquerda, text="", bg="MIDNIGHTBLUE", fg="white", font="Ivy 35")
    relogio_interface.place(x=15, y=10)


    relogio()
    display.mainloop()
    