def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"\nContato: '{nome_contato}'. Adicionado a agenda.")

def ver_contatos(contatos):
    print("\nLista de Contatos:\n")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome = contato['nome']
        telefone = contato['telefone']
        email = contato['email']
        print(f"{indice}. [{status}] {nome}, Tel:{telefone}, E-mail:{email} ")

def editar_contato(contatos, indice_contato, atualizar_nome, atualizar_telefone, atualizar_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]['nome'] = atualizar_nome
        contatos[indice_contato_ajustado]['telefone'] = atualizar_telefone
        contatos[indice_contato_ajustado]['email'] = atualizar_email    
    print(f"\nContato {indice_contato}. Atualizado para: \nNome:{atualizar_nome}\nTelefone:{atualizar_telefone}\nE-mail:{atualizar_email}")

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favorito"] == False:
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"\nContato {indice_contato} marcado como Favorito.")
    elif contatos[indice_contato_ajustado]["favorito"] == True:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"\nContato {indice_contato} desmarcado como Favorito.")
    

def ver_contatos_favoritos(contatos):
    print("\nLista de contatos Favoritos:\n")
    for contato in contatos:
        if contato['favorito'] == True:
            print(f"\nNome:{contato['nome']}, Tel:{contato['telefone']}, E-mail:{contato['email']} ")

def deletar_contato(contatos, indice_excluir):
    indice_excluir = int(indice_excluir) - 1
    if 0 <= indice_excluir < len(contatos):
            contatos.remove(contatos[indice_excluir])
            print(f"\nContato excluído!")  
    else:
        print(f"\"Índice inválido. Nenhum contato foi removido.")        


contatos = []

while True:
    print("=-" * 20)
    print("Menu da Agenda. Escolha sua opção:")
    print("\n1. Adicionar contato.")
    print("2. Ver contatos.")
    print("3. Editar contato.")
    print("4. Mudar status de favorito.")
    print("5. Ver contatos favoritos.")
    print("6. Deletar contato.")
    print("7. Sair.")
    print("=-" * 20)

    escolha = input("\nDigite sua escolha:")

    if escolha == "1":
        nome_contato = input("\nDigite o nome do contato: ")
        telefone_contato = input("\nDigite o telefone do contato: ")
        email_contato = input("\nDigite o e-mail do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    
    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o número do contato que deseja atualizar: ")
        atualizar_nome = input("\nDigite o nome para atualizar: \n")
        atualizar_telefone = input("\nDigite o telefone para atualizar: \n")
        atualizar_email = input("\nDigite o e-mail para atualizar: \n")
        editar_contato(contatos, indice_contato, atualizar_nome, atualizar_telefone, atualizar_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o número do contato que deseja mudar o status: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos_favoritos(contatos)

    elif escolha == "6":
        ver_contatos(contatos)
        excluir_contato = input("\nDigite o número do contato que deseja deletar:\n")
        deletar_contato(contatos, excluir_contato)

    elif escolha == "7":
        break

print("\nAgenda finalizada!")