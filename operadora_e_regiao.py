import phonenumbers
from phonenumbers import geocoder, carrier

numero = input('Digite o número de telefone com pais e ddd: ')

fone = phonenumbers.parse('+' + numero)

operadora = carrier.name_for_number(fone, 'pt-br')

regiao = geocoder.description_for_number(fone, 'pt-br')

print('A operadora é: ' + operadora)
print('O estado é: ' + regiao)


