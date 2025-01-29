import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# Criar a tabela de tarefas
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    status TEXT DEFAULT 'Pendente'
)
''')
conn.commit()

def adicionar_tarefa(descricao):
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    print("\nTarefas:")
    for tarefa in tarefas:
        print(f"{tarefa[0]} - {tarefa[1]} [{tarefa[2]}]")

def atualizar_tarefa(id_tarefa, status):
    cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (status, id_tarefa))
    conn.commit()
    print("Tarefa atualizada com sucesso!")

def remover_tarefa(id_tarefa):
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    print("Tarefa removida com sucesso!")

while True:
    print("\n1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da tarefa: ")
        adicionar_tarefa(descricao)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        id_tarefa = input("ID da tarefa: ")
        status = input("Novo status (Pendente/Concluído): ")
        atualizar_tarefa(id_tarefa, status)
    elif opcao == "4":
        id_tarefa = input("ID da tarefa a remover: ")
        remover_tarefa(id_tarefa)
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")

conn.close()

