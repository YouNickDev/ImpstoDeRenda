def calcular_base(rendimento, deducoes):
    return max(0, rendimento - deducoes)

def calcular_imposto(base):
    imposto = 0

    # Tabela progressiva IRPF válida desde maio/2023
    faixas = [
        (2112.00, 0.0),
        (2826.65, 0.075),
        (3751.05, 0.15),
        (4664.68, 0.225),
        (float('inf'), 0.275)
    ]
    
    limites = [2112.00, 2826.65, 3751.05, 4664.68]

    acumulado = 0
    anterior = 0

    for i, (limite, aliquota) in enumerate(faixas):
        if base > limite:
            faixa_valor = limite - anterior
        else:
            faixa_valor = base - anterior

        faixa_valor = max(0, faixa_valor)
        imposto += faixa_valor * aliquota
        anterior = limite

        if base <= limite:
            break

    return round(imposto, 2)

def main():
    print("=== Cálculo de Imposto de Renda - Brasil ===\n")
    
    rendimento = float(input("Informe o total de rendimentos tributáveis (anual): R$ "))
    
    print("\nAgora informe as deduções anuais:")
    inss = float(input("Contribuição ao INSS: R$ "))
    dependentes = int(input("Número de dependentes: "))
    deducao_dependentes = dependentes * 2275.08  # por dependente anual
    educacao = float(input("Despesas com educação: R$ "))
    
    deducoes = inss + deducao_dependentes + educacao
    
    base = calcular_base(rendimento, deducoes)
    imposto = calcular_imposto(base)
    
    print("\n=== Resultado ===")
    print(f"Base de cálculo: R$ {base:,.2f}")
    print(f"Imposto devido: R$ {imposto:,.2f}")

if __name__ == "__main__":
    main()