import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "tarefas.json"


# ---------- Persistência ----------

def carregar_tarefas():
    """Lê as tarefas do arquivo JSON. Retorna lista vazia se não existir."""
    if not ARQUIVO.exists():
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Não foi possível ler o arquivo de tarefas. Começando com lista vazia.")
        return []


def salvar_tarefas(tarefas):
    """Grava as tarefas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)


# ---------- Funcionalidades ----------

def adicionar_tarefa(tarefas, descricao):
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['descricao']}")


def pedir_numero_tarefa(tarefas, mensagem):
    """Pede o número de uma tarefa e devolve o índice (começando em 0).
    Retorna None se a entrada for inválida."""
    try:
        numero = int(input(mensagem))
    except ValueError:
        print("Digite apenas números.")
        return None

    if numero < 1 or numero > len(tarefas):
        print("Tarefa não encontrada.")
        return None
    return numero - 1


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    listar_tarefas(tarefas)
    indice = pedir_numero_tarefa(tarefas, "Número da tarefa a concluir: ")
    if indice is None:
        return
    tarefas[indice]["concluida"] = True
    salvar_tarefas(tarefas)
    print("Tarefa concluída!")


def remover_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    listar_tarefas(tarefas)
    indice = pedir_numero_tarefa(tarefas, "Número da tarefa a remover: ")
    if indice is None:
        return
    removida = tarefas.pop(indice)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{removida['descricao']}' removida.")


# ---------- Menu ----------

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()

        try:
            opcao = int(input("Digite a opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if opcao == 1:
            descricao = input("Tarefa: ").strip()
            if descricao:
                adicionar_tarefa(tarefas, descricao)
                print("Tarefa adicionada!")
            else:
                print("A tarefa não pode ser vazia.")
        elif opcao == 2:
            listar_tarefas(tarefas)
        elif opcao == 3:
            concluir_tarefa(tarefas)
        elif opcao == 4:
            remover_tarefa(tarefas)
        elif opcao == 5:
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()