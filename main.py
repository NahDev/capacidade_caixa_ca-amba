def calcular_caixas_restantes(volume_cacamba, volume_existente, volume_caixa):
    # Calcula o espaço restante na caçamba
    espaco_restante = volume_cacamba - volume_existente

    # Calcula quantas caixas cabem no espaço restante
    caixas_restantes = espaco_restante // volume_caixa

    return caixas_restantes


while True:
    volume_cacamba = 734  # Volume da caçamba em litros
    kit_1 = int(input("Caixas do volume 1: "))
    kit_2 = int(input("Caixas do volume 2: "))
    kit_3 = int(input("Caixas do volume 3: "))
    volume_existente = (
        (kit_1 * 4) + (kit_2 * 8) + (kit_3 * 10)
    )  # Volume das caixas já existentes
    volume_caixa_4_litros = 4
    volume_caixa_8_litros = 8
    volume_caixa_10_litros = 10

    caixas_restantes_4_litros = calcular_caixas_restantes(
        volume_cacamba, volume_existente, volume_caixa_4_litros
    )
    caixas_restantes_8_litros = calcular_caixas_restantes(
        volume_cacamba, volume_existente, volume_caixa_8_litros
    )
    caixas_restantes_10_litros = calcular_caixas_restantes(
        volume_cacamba, volume_existente, volume_caixa_10_litros
    )
    print()
    print(
        f"Você ainda pode colocar {caixas_restantes_4_litros} caixas de 4 litros na caçamba."
    )
    print(
        f"Você ainda pode colocar {caixas_restantes_8_litros} caixas de 8 litros na caçamba."
    )
    print(
        f"Você ainda pode colocar {caixas_restantes_10_litros} caixas de 10 litros na caçamba."
    )
    print()

    resposta = input("Deseja calcular novamente? (n para sair): ")
    print()

    if resposta.lower() == "n":
        break
