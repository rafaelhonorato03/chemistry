from molmass import Formula
from unidecode import unidecode

def padronizar_palavra(palavra):
    # remove acentos e converte para minuscula
    palavra_padronizada = unidecode(palavra).lower()
    return palavra_padronizada

def obter_valor_numerico(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")

def preparar_solucao_solida():
    soluto = input("Digite a fórmula do soluto: ")
    concentracao = obter_valor_numerico("Digite a concentração da solução em g/L: ")
    volume = obter_valor_numerico("Digite o volume da solução em L: ")

    formula = Formula(soluto)
    soluto_massa = formula.mass
    calculo = soluto_massa * concentracao * volume
    print(f"A massa necessária para preparar a solução é de {calculo:.4f} g.")

def preparar_solucao_liquida():
    soluto = input("Digite a fórmula do soluto: ")
    concentracao = obter_valor_numerico("Digite a concentração da solução em g/L: ")
    volume = obter_valor_numerico("Digite o volume da solução em L: ")
    pureza = obter_valor_numerico("Digite a pureza do soluto em %: ")
    densidade = obter_valor_numerico("Digite a densidade do soluto em g/mL: ")

    formula = Formula(soluto)
    soluto_massa = formula.mass
    calculo = soluto_massa * concentracao * volume * (1 / densidade) * (100 / pureza)
    print(f"O volume necessário para preparar a solução é de {calculo:.4f} mL.")

def main():
    while True:
        solucao = input("Deseja preparar uma solução sólida ou líquida? ")
        solucao = padronizar_palavra(solucao)
        
        if solucao == "solida":
            preparar_solucao_solida()
            break
        elif solucao == "liquida":
            preparar_solucao_liquida()
            break
        else:
            print("Opção inválida. Digite 'solida' ou 'liquida'.")

if __name__ == "__main__":
    main()