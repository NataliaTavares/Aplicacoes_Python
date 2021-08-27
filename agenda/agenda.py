from tabulate import tabulate


def procura_chaves(dicionario, nome):
    chaves = []
    for chave in dicionario:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves


def imprime_contatos(contatos, chaves):
    table = []
    for chave in chaves:
        table.append([
            contatos[chave]["nome"],
            contatos[chave]["telefone"],
            contatos[chave]["email"]
        ])
    print(tabulate(table))


def imprime_tds_contatos(contatos):
    table = []
    for chave in contatos:
        table.append([
            contatos[chave]["nome"],
            contatos[chave]["telefone"],
            contatos[chave]["email"]
        ])
    print(tabulate(table))


print("-----------------------------------------------")
print("-----------------CONTATOS----------------------")
print("-----------------------------------------------")


contatos = {}
comando = "continue"


while comando != "sair":
    comando = input("Digite o comando: (novo, visualizar, pesquisar, sair): ")

    if comando == "novo":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()

        contatos[nome.lower()] = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
    if comando == "pesquisar":
        nome = input("Nome: ").lower()
        chaves_encontradas = procura_chaves(contatos, nome)
        if len(chaves_encontradas) > 0:
            imprime_contatos(contatos, chaves_encontradas)
        else:
            print("Contato não encontrado")
    if comando == "visualizar":
        if len(contatos) > 0:
            imprime_tds_contatos(contatos)
        else:
            print("Nenhum contato encontrado")
