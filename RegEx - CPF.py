import re

cpf = "123.456.789-00"

padrão = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-1]{2}")
busca = padrão.search(cpf)

if(busca):
    cpf = busca.group()
    print(cpf)
