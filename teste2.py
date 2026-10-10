from datetime import datetime

lista = []

while True:
    comando = input("Digite um comando (ABOUT/QUIT/ADD/LIST/UPDATE/DELETE): ").upper()

    if comando == "ABOUT":
        print("Gestor de Portfólio do Victor Bittencourt.")
    elif comando == "QUIT":
        print("Saindo do Gestor de Portfólio.")
        print("Até logo!")
        break
    elif comando == "ADD":
        proj_cad = int(input("Quantos projetos gostaria de cadastrar? "))
        if proj_cad <= 0:
            print("ERRO: A quantidade deve ser maior que zero.")
        else:
            for i in range(proj_cad):
                dicionario = {}
                nome_projeto = input(f"Digite o nome do projeto {i + 1}: ")
                dicionario["nome"] = nome_projeto
                esta_finalizado = input("O projeto está finalizado? (s/n) ")
                if esta_finalizado == "s":
                    esta_finalizado = True
                else:
                    esta_finalizado = False
                dicionario["concluido"] = esta_finalizado
                dicionario["historico"] = []
                lista.append(dicionario)
                print(f"SUCESSO: Projeto '{nome_projeto}' adicionado.")
    elif comando == "LIST":
        if len(lista) == 0:
            print("Não há nenhum projeto a ser listado no momento.")
        else:
            i = 0
            for proj in lista:
                i += 1
                print(f"{i}. {proj['nome']}")
                print("Concluido:",proj['concluido'])
                print("Histórico:",proj['historico'])
    elif comando == "UPDATE":
        projeto_editar = input("Qual projeto deseja editar? ")
        encontrado = False
        for proj in lista:
            if projeto_editar == proj["nome"]:
                encontrado = True
                novo_nome = input("Novo nome: ")
                novo_status = input("Está finalizado? (s/n) ") == "s"
                proj["nome"] = novo_nome
                proj["concluido"] = novo_status
                proj["historico"].append((datetime.now().strftime("%d/%m/%Y %H:%M"), novo_status, novo_nome))
                print("SUCESSO: Projeto atualizado.")
                break
        if not encontrado:
            print("ERRO: Projeto não encontrado")
    elif comando == "DELETE":
        projeto_remover = input("Qual projeto deseja remover? ")
        encontrado = False
        for proj in lista:
            if projeto_remover == proj["nome"]:
                encontrado = True
                lista.remove(proj)
                print("SUCESSO: Projeto removido")
                break
        if not encontrado:
            print("ERRO: Projeto não encontrado")
    else:
        print("ERRO: Comando não reconhecido.")

