import re # importa o RegEx

endereço = "Rua Urubu Amarelo, 56, Lagoa Azul, Capim D'Ouro, PO, 69852-356"

#Qual o padrão do cep?
# 5 digitos, hifén(opcional), 3 digitos

#re.compile - compila a expressão em um objeto RegEx
# ? - informa para o compile que nesse padrão o hifén pode ou não aparecer
padrao = re.compile("[0-9]{5}[-]{0,1}[0123456789]{3}")
busca = padrao.search(endereço) #verifica se dá match no padrão na string endereço
if (busca):
    cep = busca.group()
    print(cep)


