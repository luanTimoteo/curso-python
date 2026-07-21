email = " EMAIL_FALSO@gmail.com "


email = email.lower() #coloca em letra minúscula
email = email.strip() #ajustar espaços vazios
print (email)

#tamanho
print(len(email)) #len = lenght. Mostra quantos caracteres tem

#posicao

posicao = email.find("@") #mostra a posição
print (posicao)

#pedaços do texto
servidor = (email[posicao:])
print (servidor)

#trocar um pedaço do texto
novo_email = email.replace("gmail.com", "terra.com.br")
print(novo_email)

nome ="luan timoteo"
nome = nome.capitalize()
print (nome)
nome = nome.title()
print (nome)
nome = nome.upper()
print (nome)

# formatação numérica
faturamento = 1_000
custo = 600

lucro = faturamento - custo
margem = lucro / faturamento
#texto = "o lucro foi de" + str(lucro) + "e o faturamento foi de" + str(faturamento)
texto = f"o lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem:.0%}"
print (texto)

#ex
nome = "biro binas"
email = "birobinasviado@terra.com.br"

#descobir o servidor do email

#descobrir o 1 nome do usuario

#enviar mensagem de cadastro: usuario x foi cadastrado com sucesso no email x