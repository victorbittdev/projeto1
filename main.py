import datetime
import json

ARQUIVO = 'partidas.json'


def encontrar_partida(lista_partidas, nome_procurado):
    for part in lista_partidas:
        if part['nome'] == nome_procurado:
            return part
    return None


def perguntar_status(mensagem):
    while True:
        resposta = input(mensagem).upper()
        if resposta == 'S':
            return True
        if resposta == 'N':
            return False
        print('ERRO: Digite S ou N')


def adicionar_partida(lista_partidas):
    try:
        quantidade = int(input('Quantas partidas gostaria de cadastrar? '))
    except ValueError:
        print('ERRO: Valor não reconhecido. Digite um número inteiro')
        return
    if quantidade < 1:
        print('ERRO: A quantidade precisa ser maior que zero.')
        return
    for i in range(quantidade):
        partida = input(f'Digite a partida {i + 1}: ').strip().title()
        if partida == '':
            print('ERRO: O nome não pode ficar vazio')
            continue
        if encontrar_partida(lista_partidas, partida):
            print('ERRO: Essa partida já está cadastrada')
            continue
        status_partida = perguntar_status('A partida já foi finalizada? (S/N): ')
        dicionario = {
            'nome': partida,
            'concluido': status_partida,
            'historico': []
        }
        lista_partidas.append(dicionario)
        print(f'SUCESSO: Partida {partida} adicionada')


def sobre():
    print('Bem vindo ao Soccer Matches Victor Bittencourt')


def listar_partidas(lista_partidas):
    if not lista_partidas:
        print('Não há nenhuma partida a ser listada no momento')
    else:
        for i, part in enumerate(lista_partidas):
            status = 'Concluída' if part['concluido'] else 'Em aberto'
            historico = part['historico'] if part['historico'] else 'sem atualizações'
            print(f'{i + 1}. {part["nome"]} - {status}')
            print(f'Histórico: {historico}')
            print()


def atualizar_partida(lista_partidas):
    partida_para_modificar = input('Qual partida deseja modificar? ').strip().title()
    partida = encontrar_partida(lista_partidas, partida_para_modificar)
    if partida is None:
        print('Partida não encontrada')
    else:
        novo_nome = input('Digite o novo nome da partida: ').strip().title()
        if novo_nome == '':
            print('ERRO: O nome não pode ficar vazio')
            return
        outra = encontrar_partida(lista_partidas, novo_nome)
        if outra is not None and outra is not partida:
            print('ERRO: Já existe uma partida com esse nome')
            return
        partida['nome'] = novo_nome
        partida['concluido'] = perguntar_status('Finalizada? (S/N): ')
        data = str(datetime.datetime.now())
        partida['historico'].append((data, partida['concluido'], partida['nome']))
        print('SUCESSO: Partida atualizada')


def deletar_partida(lista_partidas):
    nome_partida_para_remover = input('Qual partida deseja remover? ').strip().title()
    partida = encontrar_partida(lista_partidas, nome_partida_para_remover)
    if partida is None:
        print('Partida não encontrada')
    else:
        lista_partidas.remove(partida)
        print(f"Partida {partida['nome']} removida com sucesso.")


def carregar_dados():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print('Nenhum arquivo salvo ainda.')
        return []
    except json.JSONDecodeError:
        print('Arquivo vazio ou corrompido')
        return []


def salvar_dados(lista_partidas):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_partidas, arquivo, indent=4, ensure_ascii=False)


def exibir_estatisticas(lista_partidas):
    concluidas = 0
    em_andamento = 0
    for partida in lista_partidas:
        if partida['concluido']:
            concluidas += 1
        else:
            em_andamento += 1
    print('ESTATÍSTICAS:')
    print(f'Partidas concluídas: {concluidas}')
    print(f'Partidas em andamento: {em_andamento}')


def main():
    lista = carregar_dados()

    while True:
        comando = input('Digite um comando (ABOUT/QUIT/ADD/LIST/UPDATE/DELETE/STATS): ').upper()

        if comando == 'ABOUT':
            sobre()
        elif comando == 'QUIT':
            salvar_dados(lista)
            print('SAINDO')
            break
        elif comando == 'ADD':
            adicionar_partida(lista)
            salvar_dados(lista)
        elif comando == 'LIST':
            listar_partidas(lista)
        elif comando == 'UPDATE':
            atualizar_partida(lista)
            salvar_dados(lista)
        elif comando == 'DELETE':
            deletar_partida(lista)
            salvar_dados(lista)
        elif comando == 'STATS':
            exibir_estatisticas(lista)
        else:
            print('ERRO: Comando não reconhecido')

    print('Até logo!')


if __name__ == '__main__':
    main()