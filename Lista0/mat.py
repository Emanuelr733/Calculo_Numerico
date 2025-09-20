import math
def impar(numero):
    resto=numero%2
    if resto==1:
        return True
    else:
        return False
def area_circulo(raio):
    area=(raio**2)*math.pi
    return area
def ano_bissexto(ano):
    if (ano%400)==0:
        return True
    elif (ano%4)==0 and (ano%100)!=0:
        return True
    else:
        return False
def dias_mes(ano,mes):
    match mes:
        case 1|3|5|7|8|10|12:
            return 31
        case 4|6|9|11:
            return 30
        case 2:
            if ano_bissexto(ano)==True:
                return 29
            else:
                return 28
def nome_mes(mes):
    match mes:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"
def mdc(num1,num2):
    MDC=0
    def euclides(A,B):
        resto = A%B
        if resto == 0:
            return B
        else:
            return euclides(B,resto)
    return euclides(num1,num2)
def mmc(num1,num2):
    mmc = (num1*num2)/mdc(num1,num2)
    return mmc