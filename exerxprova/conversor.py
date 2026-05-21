import customtkinter as ctk
ctk.set_appearance_mode("light")




#  Funcao de conversao dolar para real
def dolar_real():
    valor = float(entrada.get())

    conversao = valor * 5.25
    resultado.configure(text=f"R$ {conversao:.2f}")




# Janela principal

janela = ctk.CTk()
janela.geometry('640x400')
janela.title('Conversor de Moedas')


titulo = ctk.CTkLabel(
    janela,
    text='CONVERSOR DE MOEDAS',
    font=('Verdana', 30)
)

titulo.pack(pady=20)


# Entrada de valor
entrada = ctk.CTkEntry(
    janela,
    placeholder_text='Digite o valor a ser convertido',
    width=400,
    height=30,
    border_color='blue',
)

entrada.pack(pady=20)


# Botao de conversao dolar para real
botao_dolar_real = ctk.CTkButton(
    janela,
    text='DÓLAR',
    width=150,
    height=40,
    fg_color='blue',
    command=dolar_real
)

botao_dolar_real.pack(pady=10)


# Botao de conversao real para dolar
botao_real_dolar = ctk.CTkButton(
    janela,
    text='REAL',
    width=150,
    height=40,
    fg_color='blue',
    command=real_dolar
)

botao_real_dolar.pack(pady=10)


# Label de resultado
resultado = ctk.CTkLabel(
    janela,
    text='',
    font=('Verdana', 25)
)

resultado.pack(pady=20)


# Rodar a janela
janela.mainloop()