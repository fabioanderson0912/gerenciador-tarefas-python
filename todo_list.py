import json
import os

ARQUIVO_DADOS = "tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON se ele existir."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas():
    """Salva a lista atual de tarefas no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

# Carrega as tarefas ao iniciar o programa
tarefas = carregar_tarefas()

def exibir_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar nova tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Nova Tarefa ---")
            titulo = input("Digite o título da tarefa: ")
            tarefa = {
                "titulo": titulo,
                "concluida": False
            }
            tarefas.append(tarefa)
            salvar_tarefas()  # Salva automaticamente no arquivo
            print(f"Tarefa '{titulo}' adicionada e salva com sucesso!")

        elif opcao == "2":
            print("\n=== LISTA DE TAREFAS ===")
            if not tarefas:
                print("Nenhuma tarefa cadastrada ainda.")
            else:
                for index, tarefa in enumerate(tarefas):
                    status = "✅" if tarefa["concluida"] else "⏳"
                    print(f"{index + 1}. [{status}] {tarefa['titulo']}")

        elif opcao == "3":
            print("\n=== CONCLUIR TAREFA ===")
            if not tarefas:
                print("Não há tarefas para concluir.")
            else:
                for index, tarefa in enumerate(tarefas):
                    status = "✅" if tarefa["concluida"] else "⏳"
                    print(f"{index + 1}. [{status}] {tarefa['titulo']}")
                
                try:
                    num = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
                    indice = num - 1
                    
                    if 0 <= indice < len(tarefas):
                        tarefas[indice]["concluida"] = True
                        salvar_tarefas()  # Salva a alteração
                        print(f"Tarefa '{tarefas[indice]['titulo']}' marcada como concluída e salva!")
                    else:
                        print("Erro: Número de tarefa inválido!")
                except ValueError:
                    print("Erro: Digite apenas números inteiros válidos!")

        elif opcao == "4":
            print("\n=== REMOVER TAREFA ===")
            if not tarefas:
                print("Não há tarefas para remover.")
            else:
                for index, tarefa in enumerate(tarefas):
                    status = "✅" if tarefa["concluida"] else "⏳"
                    print(f"{index + 1}. [{status}] {tarefa['titulo']}")
                
                try:
                    num = int(input("Digite o número da tarefa que deseja remover: "))
                    indice = num - 1
                    
                    if 0 <= indice < len(tarefas):
                        tarefa_removida = tarefas.pop(indice)
                        salvar_tarefas()  # Salva a lista atualizada
                        print(f"Tarefa '{tarefa_removida['titulo']}' removida e alteração salva!")
                    else:
                        print("Erro: Número de tarefa inválido!")
                except ValueError:
                    print("Erro: Digite apenas números inteiros válidos!")

        elif opcao == "5":
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()