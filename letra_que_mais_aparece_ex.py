str = "oooooiiiaaa"

qtd_que_mais_aparece = 0
contagem_letra_atual = 0
letra_que_mais_aparece = ""
i = 0

while i < len(str):
    letra_atual = str[i]
    if letra_atual ==" ":
        i = i +1
        continue
    else:
        contagem_letra_atual = str.count(letra_atual)
        if contagem_letra_atual > qtd_que_mais_aparece:
            letra_que_mais_aparece = letra_atual
            qtd_que_mais_aparece = contagem_letra_atual
    i = i+1
print(f"a letra que mais apareceu foi '{letra_que_mais_aparece}' aparecendo {qtd_que_mais_aparece}x")



