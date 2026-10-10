import random

numero_correto = random.randint(0,15)

niveis = {
    "1": {"nome": "Fácil", "max": 10, "tentativas": 5},
    "2": {"nome": "Médio", "max": 50, "tentativas": 7},
}

def escolher_nivel():
    print("\n--- NÍVEIS ---")
    for chave, nivel in niveis.items():
        print(f"{chave}. {nivel['nome']} (0 a {nivel['max']}, {nivel['tentativas']} tentativas)")

    while True:
        escolha = input("Escolha o nível: ").strip()
        if escolha in niveis:
            return niveis[escolha]
        print("Nível inválido.")

tentativas = 0
while tentativas <= 5:
    try:
        numero_usuario = int(input("Chute um número entre 0 e 15: "))
    except ValueError:
        print("Digite apenas números")
        continue
    tentativas += 1
    if numero_usuario == numero_correto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif numero_usuario > numero_correto:
        print("Alto demais!")
    else:
        print("Baixo demais!")
    if tentativas == 5:
        print("Ultima tentativa!")
    if tentativas > 5:
        print("Fim das tentativas!")