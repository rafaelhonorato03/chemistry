from molmass import Formula
from unicode import unicode

def padronizar_palavra(palavra):
    # remove acentos e converte para minuscula
    palavra_padronizada = unicode(palavra).lower()
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