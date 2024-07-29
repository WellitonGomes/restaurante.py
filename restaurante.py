#uma função para obter os valores dos pratos
def obter_pratos():
    while True:
        try:
            pratos = float(input("Por favor, digite a soma total dos valores dos pratos consumidos: "))
            if pratos <= 0:
                print("Os valores dos pratos não pode ser zero")
                continue
            return pratos
        except ValueError:
            print("Por favor, digite apenas os valores dos pratos.")

#uma função para obter a quantidade dos pagantes
def obter_pagantes():
    while True:
        try:
            pagantes = int(input("Por favor digite o total de pagantes:"))
            if pagantes <= 0:
                print("O total de pagantes não pode ser zero")
                continue
            return pagantes
        except ValueError:
            print("Informe apenas o total de pagantes.")


#função somar a porcentagem de trabalho
def somar_pratos(pratos):
    porcentagem = pratos * 0.10
    total_com_porcentagem = pratos + porcentagem
    print("O valor total gasto foi:", total_com_porcentagem)
    return total_com_porcentagem

#função para dividir o valor total entre os pagantes
def obter_valorTotal(total_com_porcentagem, pagantes):
    totalApagar = total_com_porcentagem / pagantes
    print("Este é o total a ser pago por cada pagante:", totalApagar)

total_pratos = obter_pratos()
total_com_porcentagem = somar_pratos(total_pratos)
pagantes = obter_pagantes()
obter_valorTotal(total_com_porcentagem, pagantes)
