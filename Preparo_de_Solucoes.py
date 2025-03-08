from molmass import Formula
from unidecode import unidecode
from chemicals.identifiers import search_chemical

def padronizar_palavra(palavra):
    # remove acentos e converte para minuscula
    palavra_padronizada = unidecode(palavra).lower()
    return palavra_padronizada

solucao = input("Deseja preparar uma solução sólida ou líquida? ")
solucao = padronizar_palavra(solucao)

if solucao == "solida":
    soluto = input("Digite a fórmula do soluto: ")
    concentracao = float(input("Digite a concentração da solução em g/L: "))
    volume = float(input("Digite o volume da solução em L: "))

    formula = Formula(soluto)
    soluto_massa = formula.mass
    calculo = soluto_massa * concentracao * volume
    print(f"A massa necessária para preparar a solução é de {calculo:.4f} g.")

elif solucao == "liquida":
    soluto = input("Digite a fórmula do soluto: ")
    concentracao = float(input("Digite a concentração da solução em g/L: "))
    volume = float(input("Digite o volume da solução em L: "))
    pureza = float(input("Digite a pureza do soluto em %: "))
    chemical_info = search_chemical(soluto)
    densidade = chemical_info['Density']

    formula = Formula(soluto)
    soluto_massa = formula.mass
    calculo = soluto_massa * concentracao * volume *(1/densidade)* (100/pureza)
    print(f"O volume necessário para preparar a solução é de {calculo:.4f} mL.")

