#Importando biblioteca Tkinter
from tkinter import *

#Criando a janela e aplicando um título
janela = Tk() 
janela.title('Desafio - Prova Diagnóstica')

#Definindo posicionamento da janela
janela.geometry(newGeometry='500x250+400+200')
janela.resizable(width=True, height=True)

#Definindo tamanho mínimo e máximo da janela
janela.minsize(width=500, height=250)
janela.maxsize(width=1000, height=500)

#Definindo uma cor de fundo
janela['bg'] = '#2b2b2b'

#Criando segunda janela
segunda_janela = Tk()
segunda_janela.title('Desafio - Prova Diagnóstica')

segunda_janela.geometry(newGeometry='500x250+400+550')
segunda_janela.resizable(width=True, height=True)

segunda_janela.minsize(width=500, height=250)
segunda_janela.maxsize(width=1000, height=500)
    
segunda_janela['bg'] = '#2b2b2b'

#Criando variáveis
texto_n = ''
texto_a = ''

#Definindo função para enviar as mensagens
def enviar():
    texto_n = texto_nome.get()
    texto_dois_pontos = f'{texto_n} disse:'
    resultado_nome.config(text=texto_dois_pontos)

    texto_a = texto_algo.get()
    texto_aspas = f'"{texto_a}"'
    resultado_algo.config(text=texto_aspas)

#Criando botão
botão = Button(janela, text="Enviar", command=lambda:enviar(), font=('Verdana 13'), bg='#2f4d59', overrelief=SUNKEN,fg='white')
botão.place(x=218.5,y=185)

#Criando labels da janela
label_1 = Label(janela, text='Carlos Gabriel Abreu Rocha', font='Ivy 12 bold', bg='#2b2b2b', fg='#0d6080')
label_1.place(x=35,y=10)

label_2 = Label(janela, text='Nome:', font='Ivy 9', bg='#2b2b2b', fg='white')
label_2.place(x=35,y=40)

label_3 = Label(janela, text='Diga algo:', font='Ivy 9', bg='#2b2b2b', fg='white')
label_3.place(x=35,y=100)

#Criando labels da segunda janela
label_s1 = Label(segunda_janela, text='Não foi tão difícil!', font='Ivy 16', bg='#2b2b2b', fg='#0d6080')
label_s1.place(x=165, y=10)

resultado_nome = Label(segunda_janela, text='', font='Ivy 12', bg='#2b2b2b', fg='white')
resultado_nome.place(x=50,y=100)

resultado_algo = Label(segunda_janela, text='', font='Ivy 12', bg='#2b2b2b', fg='white')
resultado_algo.place(x=70,y=140)

#Campo de digitação
texto_nome = Entry(janela, width=70, bd=2, relief='solid')
texto_nome.place(x=38,y=67)

texto_algo = Entry(janela, width=70, bd=2, relief='solid')
texto_algo.place(x=38,y=127)

#Loop para a interface ficar aberta
janela.mainloop()