#ex
nome = "biro binas"
email = "birobinasviado@terra.com.br"

#descobir o servidor do email
posicao = email.find("@")
servidor = (email[posicao:])
print (servidor)

#descobrir o 1 nome do usuario

nome = nome.title()
nome_posicao = nome.find(" ")
primeiro_nome = (nome[:nome_posicao])
print (primeiro_nome)

#enviar mensagem de cadastro: usuario x foi cadastrado com sucesso no email x

mensagem = f"o usuario {primeiro_nome} foi cadastrado com sucesso no email {servidor}"
print (mensagem)