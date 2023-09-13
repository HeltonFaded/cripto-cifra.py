chave = int(input('digite uma chave para sua criptografia '))
mensagem = input('oque deve ser criptografado: ')
mensagem = mensagem.replace(' ', '')
mensagem = mensagem.lower()
cripto_letra = ''
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = len(alfabeto)
for letra in mensagem:
    indice = alfabeto.index(letra)
    nova_letra = alfabeto[(indice + chave) % n]
    cripto_letra = cripto_letra + nova_letra


print(mensagem)
print(cripto_letra)