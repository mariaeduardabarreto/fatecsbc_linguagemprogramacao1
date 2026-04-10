# Versão 1
texto = input("Digite algo: ").lower()
contador = 0

for letra in texto:
    if letra in "aeiou":
        contador += 1

print("Vogais:", contador)

# Versão 2
def contar_vogais(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador

texto = input("Digite algo: ")
print("Vogais:", contar_vogais(texto))
