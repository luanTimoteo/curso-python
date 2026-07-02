faturamento = 1100
custo = 600
print ("faturamento", faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento # float
print ("imposto", imposto)

lucro = faturamento - custo - imposto
print ("faturamento com novas vendas", faturamento)
print ("custo", custo)
print ("lucro", lucro)

mensagem = "o faturamento foi de 2100" #string
teve_lucro = True #boolean

margem_lucro = lucro / faturamento
print ("margem de lucro", margem_lucro)

# tipos de variaveis
# int = numeros inteiros
# float = numeros casa decimal
# strings = textos
# boolean = booleanos (true false)
 
# operadores especiais

# mod -> %
# resto da divisao de um numero pelo outro
# 10 % 3 = 1

anos = int (310 / 12)
print (anos, "anos")

meses = 310 % 12
print (meses, "meses")

# floor division //

print(310 // 12)
