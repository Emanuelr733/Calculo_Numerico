import argparse
import csv
import numpy as np

def gera_sistema_linear(num_var, precisao=None):
    """Gerador de sistema lineares aleatórios"""
    # Gera lista de números para compor a matriz
    lista_int = np.asarray(range(-10, 11))
    lista_frac = np.linspace(-9.9, 9.9)
    lista_num = np.concatenate((lista_int, lista_frac))
    
    # Gera matriz com números aleatórios
    mat_a = np.random.choice(lista_num, (num_var, num_var))
    
    # Garante dominância diagonal
    for i in range(num_var):
        mat_a[i, i] = np.sum(np.abs(mat_a[i, :])) + 1
        
    # Gera vetor com a solução do sistema
    vet_x = np.random.choice(lista_num, num_var)
    
    # Calcula vetor de termos independentes
    vet_b = mat_a.dot(vet_x)
    
    # Monta a matriz estendida
    mat = np.append(mat_a, vet_b[:, None], axis=1)
    
    if precisao is not None:
        mat = np.round(mat, precisao)
        
    return mat

def salva_csv(mat, arq_csv):
    """Salva matriz em arquivo CSV"""
    with open(arq_csv, 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        for row in mat:
            writer.writerow(row)

def argumentos():
    """Lê argumentos da linha de comando"""
    parser = argparse.ArgumentParser(description='Gerador de sistemas lineares')
    parser.add_argument('-v', '--variaveis', type=int, help='Número de variáveis')
    parser.add_argument('-a', '--arquivo', help='Arquivo CSV para salvar a matriz')
    parser.add_argument('-p', '--precisao', type=int, help='Precisão em casas decimais')
    parser.add_argument('-s', '--semente', type=int, help='Semente para geração de números aleatórios')
    parser.add_argument('-e', '--exibe', action='store_true', help='Exibe matriz gerada')
    
    return parser.parse_args()

def principal():
    """Função principal"""
    args = argumentos()
    
    # Inicializa semente para geração de números aleatórios
    if args.semente:
        np.random.seed(args.semente)
        
    # Verifica número de variáveis
    if not args.variaveis or args.variaveis < 2:
        args.variaveis = np.random.randint(5, 10)
        
    # Gera matriz do sistema linear
    mat = gera_sistema_linear(args.variaveis, args.precisao)
    
    if args.exibe:
        print(mat)
        
    if args.arquivo:
        salva_csv(mat, args.arquivo)

if __name__ == '__main__':
    principal()