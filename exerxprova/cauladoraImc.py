import customtkinter as ctk
ctk.set_appearance_mode("system")

def imc_peso():
    peso = float(entrada1.get())
    altura = float(entrada2.get())
    
    altura = altura / 100
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Abaixo do peso ideal (procure um especialista)"
    elif imc < 24.9:
        categoria = "Peso normal (continue hábitos saudáveis)"
    elif imc < 29.9:
        categoria = "Sobrepeso (considere mudar hábitos e praticar exercícios)"
    elif imc < 34.9:
        categoria = "Obesidade Grau 1 (consulte um médico)"
    elif imc < 39.9:
        categoria = "Obesidade Grau 2 (procure um médico com urgência)"
    else:
        categoria = "Obesidade Grau 3 (procure um profissional com urgência)"

    resultado.configure(text=f"IMC: {imc:.2f}\n{categoria}")


#Janela principal

janela = ctk.CTk()
janela.geometry('640x400')
janela.title('Calculadora de IMC')

titulo = ctk.CTkLabel(
    janela,
    text='Seu Cálculo de IMC',
    font=('Verdana', 25)
)
titulo.pack(pady=20)

entrada1 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite seu peso em Kg',
    width=400,
    height=30,
    border_color='blue',
    fg_color='black'
)
entrada1.pack(pady=20)

entrada2 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite sua altura em cm (ex: 187)',
    width=400,
    height=30,
    border_color='blue',
    fg_color='black'
)
entrada2.pack(pady=20)

botao_calcular = ctk.CTkButton(
    janela,
    text='Calcular',
    width=150,
    height=40,
    fg_color='green',
    command=imc_peso
)
botao_calcular.pack(pady=10)

resultado = ctk.CTkLabel(
    janela,
    text='',
    font=('Verdana', 20),
    justify='center'
)
resultado.pack(pady=20)

janela.mainloop()