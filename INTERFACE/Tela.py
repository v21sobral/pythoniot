import customtkinter as ctk
import os
os.system("clear")

ctk.set_appearance_mode('white')

# Começo da janela

window = ctk.CTk()
window.geometry('600x400')
window.resizable(False, False)
window.title('Login Bradesco')
window.iconbitmap('Bradesco.ico')

#elementos da janela

titulo = ctk.CTkLabel(window,
                      text='Acesse sua conta',
                      text_color='black',
                      font=('Verdana', 40))

titulo.pack(pady=25)


login = ctk.CTkEntry(window,
                     width = 400,
                     height=42,
                     placeholder_text='Digite o seu Login',
                     border_color='red')
login.pack()



senha = ctk.CTkEntry(window,
                     width = 400,
                     height=42,
                     placeholder_text='Digite o sua Senha',
                     border_color='red',
                     show= '•')
senha.pack(pady=20)

botao = ctk.CTkButton(window,
                      text='Acessar',
                      width=150,
                      height=50,
                      fg_color='Red',
                      text_color='white',
                      hover_color='pink',
                      font=('Verdana',20))

botao.pack(pady=35)


window.mainloop()