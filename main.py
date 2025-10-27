from funcoes import cadastrar, listar, editar, excluir, limpar_terminal

def menu():
    while True:
        limpar_terminal()  # ← ESTA É A LINHA NOVA
        print("\n=== MovieBox ===")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Editar Filme")
        print("4 - Excluir Filme")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        
        limpar_terminal()
        print("Opção escolhida:", opcao)

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            excluir()
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Digite novamente.")

if __name__ == "__main__":
    menu()
