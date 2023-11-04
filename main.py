#fatiamento

nome = "Thiago Said"

primeiro_nome = nome[0:7]
print(primeiro_nome)

#passa a variável - entre colchetes escolhe o primeiro index da string ":" até onde quer extrair o texto +1
# o primeiro paramento é inclusivo, e o ultimo exclusivo, não inclui o caractere naquela posição

segundo_nome = nome[7:11]
print(segundo_nome)

#strings são imutáveis, permitindo apenas a manipulação de uma cópia delas em variáveis

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)

#metodo find() para encontrar o separador da url
indice_interrogacao = url.find('?')
print(indice_interrogacao)

#separar a url origem da url parametros
url_origem = url[0:indice_interrogacao]
print(url_origem)

#usando o metodo de fatiamento sem o segundo parametro ele pega até o final da string
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#definir o parâmetro que será buscado/extraído
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

#verificando se há parametros no url parametros antes ou após o & - se for antes é origem depois é destino
indice_e_comercial = url_parametros.find('&', indice_valor) #  o segundo parametro é onde começa
if(indice_e_comercial == -1):
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

