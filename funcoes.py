import csv
import os
from datetime import datetime

DADOS_PATH = "dados/cadastros.csv"
LOG_PATH = "dados/log.txt"

os.makedirs("dados", exist_ok=True)
if not os.path.exists(DADOS_PATH):
    with open(DADOS_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "titulo", "genero", "ano"])
        writer.writeheader()
if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, "w") as f:
        f.write("=== LOG DE EXECUÇÃO ===\n")

def limpar_terminal():
    os.system("cls")

def registrar_log(acao):
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - {acao}\n")

def carregar_dados():
    registros = []
    try:
        with open(DADOS_PATH, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                registros.append(row)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
    return registros

def salvar_dados(registros):
    try:
        with open(DADOS_PATH, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "titulo", "genero", "ano"])
            writer.writeheader()
            writer.writerows(registros)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def cadastrar():
    registros = carregar_dados()
    try:
        novo_id = str(len(registros) + 1)
        titulo = input("Digite o título: ")
        genero = input("Digite o gênero: ")
        ano = input("Digite o ano: ")

        registros.append({"id": novo_id, "titulo": titulo, "genero": genero, "ano": ano})
        salvar_dados(registros)
        registrar_log(f"Cadastro de novo filme: {titulo}")
        print("✅ Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")

def listar():
    registros = carregar_dados()
    if registros:
        print("\n📋 Lista de Filmes:")
        for r in registros:
            print(f"ID: {r['id']} | Título: {r['titulo']} | Gênero: {r['genero']} | Ano: {r['ano']}")
    else:
        print("Nenhum registro encontrado.")
    registrar_log("Listagem de filmes")

def editar():
    registros = carregar_dados()
    if not registros:
        print("Nenhum registro encontrado para editar.")
        return
    listar()
    try:
        edit_id = input("Digite o ID do filme que deseja editar: ")
        for r in registros:
            if r["id"] == edit_id:
                r["titulo"] = input(f"Novo título ({r['titulo']}): ") or r["titulo"]
                r["genero"] = input(f"Novo gênero ({r['genero']}): ") or r["genero"]
                r["ano"] = input(f"Novo ano ({r['ano']}): ") or r["ano"]
                salvar_dados(registros)
                registrar_log(f"Edição de filme ID {edit_id}")
                print("✅ Filme editado com sucesso!")
                return
        print("ID não encontrado.")
    except Exception as e:
        print(f"Erro ao editar: {e}")

def excluir():
    registros = carregar_dados()
    if not registros:
        print("Nunhum registro encontrado para exluir.")
        return
    listar()
    try:
        del_id = input("Digite o ID do filme que deseja excluir: ")
        for r in registros:
            if r["id"] == del_id:
                registros.remove(r)
                salvar_dados(registros)
                registrar_log(f"Exclusão de filme ID {del_id}")
                print("✅ Filme excluído com sucesso!")
                return
        print("ID não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir: {e}")
