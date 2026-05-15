import customtkinter as ctk
ctk.set_appearance_mode("dark")


#Função
def calcular():
    nota1 = float(unidade1.get())
    nota2 = float(unidade2.get())
    nota3 = float(unidade3.get())
    
    media = (nota1 + nota2 + nota3) / 3
    
    if media < 5:
        status = 'Reprovado'
    else:
        status = 'Aprovado'
    
    resultado.configure(text=f'Sua média é: {media:.2f} - {status}')


# Janela

janela= ctk.CTk()
janela.geometry('600x400')
janela.title('Sistema escolar Senai 2026')


#Corpo do aplicativo
titulo = ctk.CTkLabel(janela, text='Bem-vindo ao sistema escolar Senai 2026', font=('Arial', 30), text_color='white')


titulo.pack(pady=20)

unidade1 = ctk.CTkEntry(janela, width=300, height=35, placeholder_text='Digite sua nota da 1º unidade', border_color='purple', border_width=2, corner_radius=10)

unidade1.pack(pady=10)

unidade2 = ctk.CTkEntry(janela, width=300, height=35, placeholder_text='Digite sua nota da 2º unidade', border_color='purple', border_width=2, corner_radius=10)

unidade2.pack(pady=10)

unidade3 = ctk.CTkEntry(janela, width=300, height=35, placeholder_text='Digite sua nota da 3º unidade', border_color='purple', border_width=2, fg_color='purple', corner_radius=10, text_color='white')

unidade3.pack(pady=10)


botao = ctk.CTkButton(janela, text='Calcular média', width=200, height=40, border_color='purple', border_width=2, corner_radius=10, command=calcular)

botao.pack(pady=20)

resultado = ctk.CTkLabel(janela, text='', font=('Arial', 20), text_color='white')

resultado.pack(pady=10)

janela.mainloop()