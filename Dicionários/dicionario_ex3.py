quantidade_vogais={}
vogais=[]

texto=str(input("Qual o texto?: "))
contA=0
contE=0
contI=0
contO=0
contU=0

for letra in texto:
    if letra=='A' in texto or letra=='a' in texto:
        contA+=1
        vogais.append('A')
    if letra=='E' in texto or letra=='e' in texto:
        contE+=1
        vogais.append("E")
    if letra=='I' in texto or letra=='i' in texto:
        contI+=1
        vogais.append('I')
    if letra=='O' in texto or letra=='o' in texto:
        contO+=1
        vogais.append("O")
    if letra=='U' in texto or letra=='u' in texto:
        contU+=1
        vogais.append('U')



quantidade_vogais['A']=(contA)
quantidade_vogais['E']=(contE)
quantidade_vogais['I']=(contI)
quantidade_vogais['O']=(contO)
quantidade_vogais['U']=(contU)
print(quantidade_vogais)
#print(vogais)
