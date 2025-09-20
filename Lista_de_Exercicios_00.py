import math
import random
from mat import impar,area_circulo,ano_bissexto,dias_mes,nome_mes,mdc,mmc

def quest1():
    A = int(input("Digite o valor de A:"))
    B = int(input("Digite o valor de B:"))
    C = int(input("Digite o valor de C:"))
    delta = B**2 -4*A*C
    if delta<0:
        print("A equação não possui raizes reais")
    elif delta==0:
        raiz1=(-B + math.sqrt(delta))/(2*A)
        print(raiz1)
    else:
        raiz1=(-B + math.sqrt(delta))/(2*A)
        raiz2=(-B - math.sqrt(delta))/(2*A)
        print(raiz1,raiz2)
        
def quest2():
    N=int(input("Digite o ano:"))
    if (N%400)==0:
        print("O ano é bissexto")
    elif (N%4)==0 and (N%100)!=0:
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")

def quest3():
    for i in range(1,10):
        print(i," ",end="")
    print()
    for i in range(9,0,-1):
        print(i," ",end="")
    print()

def quest4():
    notas = [0]*10
    soma = 0
    for i in range(10):
        nota1 = float(input(f"Digite a primeira nota do aluno {i+1}:"))
        nota2 = float(input(f"Digite a segunda nota do aluno {i+1}:"))
        nota3 = float(input(f"Digite a terceira nota do aluno {i+1}:"))
        notas[i] = ((nota1*0.3)+(nota2*0.3)+(nota3*0.4))
    
    for i in range(10):
        if notas[i] >= 60:
            print("O aluno",i+1," foi aprovado!")
        else:
            print("O aluno",i+1," foi reprovado!")
        soma += notas[i]
    media = soma/10
    print("A media final é {m:.2f}".format(m=media))

def quest5():
    numeros=[]
    while True:
        numeros.append(int(input("Digite um numero inteiro:")))
        repet = int(input("Digite 1 para continuar ou 0 para parar:"))
        if repet==0:
            break
    print("O maior e menor numero são respectivamente:",max(numeros),min(numeros))

def quest6():
    n=int(input("Qual o valor de n?"))
    def fatorial(n):
        if n==0:
            return 1
        if n==1:
            return 1
        return n*fatorial(n-1)
    print("O fatorial de",n,"=",fatorial(n))

def quest7():
    num1=int(input("Primeiro numero:"))
    num2=int(input("Segundo numero:"))
    MDC=0
    def euclides(A,B):
        resto = A%B
        if resto == 0:
            return B
        else:
            return euclides(B,resto)
    print("O MDC de",num1,"e",num2,"é",euclides(num1,num2))

def quest8():
    num1=int(input("Primeiro numero:"))
    num2=int(input("Segundo numero:"))
    MDC=0
    def euclides(A,B):
        resto = A%B
        if resto == 0:
            return B
        else:
            return euclides(B,resto)
    mmc = (num1*num2)/euclides(num1,num2)
    print("O MMC de",num1,"e",num2,"é",mmc)

def quest9():
    sair=0
    while sair != 6:
        print("Escolha a operação desejada:\n1-soma\n2-multiplicação\n3-divisão\n4-subtração\n5-potência\n6-sair")
        operacao=int(input("opção:"))
        match operacao:
            case 1:
                num1=int(input("Digite o primeiro numero:"))
                num2=int(input("Digite o segundo numero:"))
                print("A soma é:",num1+num2)
            case 2:
                num1=int(input("Digite o primeiro numero:"))
                num2=int(input("Digite o segundo numero:"))
                print("A multiplicação é:",num1*num2)
            case 3:
                num1=int(input("Digite o primeiro numero:"))
                num2=int(input("Digite o segundo numero:"))
                print("A divisão é:",num1/num2)
            case 4:
                num1=int(input("Digite o primeiro numero:"))
                num2=int(input("Digite o segundo numero:"))
                print("A subtração é:",num1-num2)
            case 5:
                num1=int(input("Digite o primeiro numero:"))
                num2=int(input("Digite o segundo numero:"))
                print("A potência é:",num1**num2)
            case 6:
                sair = 6
            
def quest10():
    n=int(input("Quantos elementos tem A:"))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print("[",i+1,j+1,k+1,"]")
    
def quest11():
    n=int(input("Quantos elementos tem A:"))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    print("[",i+1,j+1,k+1,"]")

def quest12():
    n=int(input("Quantos elementos tem a lista:"))
    q=int(input("Quantos deseja sortear:"))
    lista=list(range(1,n+1))
    random.shuffle(lista)
    print(lista[0:q])

def quest13():
    lista=[0]*100
    lista2=[0]*10
    for i in range(100):
        lista[i]=random.randint(1,10)
        lista2[lista[i]-1]+=1
    print(lista)
    for i in range(10):
        print("Quantidade de numeros",i+1,":",lista2[i])

def quest14():
    n=int(input("Quantos trechos tem a viagem:"))
    d=[0]*n
    v=[0]*n
    num=0
    den=0
    for i in range(n):
        d[i]=int(input(f"Digite a distancia do trecho {i+1}:"))
        v[i]=int(input(f"Digite a velocidade do trecho {i+1}:"))
        num+=(d[i]*v[i])
        den+=d[i]
    vmed=num/den
    for i in range(n):
        if v[i]>vmed:
            print(f"O trecho {i+1} teve velocidade acima da media.")

def quest15():
    n=int(input("Quantas posições tem:"))
    vet=[0]*n
    for i in range(n):
        vet[i]=str(input(f"Valor da posição {i+1}:"))
    print(vet)
    for i in range(n):
        for j in range(n-i-1):
            if vet[j+1] < vet[j]:
                aux=vet[j+1]
                vet[j+1]=vet[j]
                vet[j]=aux
                print(vet)

def quest16():
    n=int(input("Quantos numeros deseja colocar:"))
    vet1=[0]*n
    vet2=[]
    for i in range(n):
        vet1[i]=int(input(f"Digite o {i+1} numero:"))
        if vet1[i] not in vet2:
            vet2.append(vet1[i])
    print(vet1)
    print(vet2)

def quest17():
    def input_int(mensagem):
        while True:
            try:
                valor=int(input(mensagem))
                return valor
            except:
                print("numero invalido,digite um inteiro valido.")
    def input_float(mensagem):
        while True:
            try:
                valor=float(input(mensagem))
                return valor
            except:
                print("numero invalido,digite um decimal valido.")
    num1=input_int("Digite um numero inteiro:")
    num2=input_float("Digite um numero decimal:")
    print("Inteiro digitado:",num1)
    print("Decimal digitado:",num2)

def quest18():
    n1=int(input("Digite um numero para validar se ele e impar:"))
    print(impar(n1))
    n2=int(input("Digite o raio para calcular a area do circulo:"))
    print(area_circulo(n2))

def quest19():
    mes=int(input("Digite um mês:"))
    ano=int(input("Digite um ano:"))
    print("É bissexto?",ano_bissexto(ano))
    print(f"Tem {dias_mes(ano,mes)} dias.")
    print(f"O mês é {nome_mes(mes)}.")

def quest20():
    n=int(input("Quantos números deseja colocar:"))
    lista=[0]*n
    for i in range(n):
        lista[i]=int(input(f"Digite o {i+1} número:"))
    


num = int(input("Digite o número da questão:"))
repet = True
match num:
    case 1:
        quest1()
    case 2:
        quest2()
    case 3:
        quest3()
    case 4:
        quest4()
    case 5:
        quest5()
    case 6:
        quest6()
    case 7:
        quest7()
    case 8:
        quest8()
    case 9:
        quest9()
    case 10:
        quest10()
    case 11:
        quest11()
    case 12:
        quest12()
    case 13:
        quest13()
    case 14:
        quest14()
    case 15:
        quest15()
    case 16:
        quest16()
    case 17:
        quest17()
    case 18:
        quest18()
    case 19:
        quest19()
    case 20:
        quest20()

