"""13 - Um senhor esquelético saiu pela cidade em busca de amigos que pudessem ajudar a
abrir uma porta que estava presa. No percurso, passou pelo zoológico que era gerenciado
por um senhor corcunda e muito peludo. Explicou o problema e o mesmo aceitou ajudar.
Seguiram juntos até um ortodontista e lá encontraram um homem de um braço só e que
utilizava aparelho nos dentes. Esse homem, também resolveu ajudar. O trio caminhava em
direção a porta quando apareceu uma mulher de maiô roxo e a mesma disse que gostaria de
ajudar. Disse que era vidente e que conseguia visualizar que todos juntos irão abrir a porta.
Quando chegaram no lugar, viram que era uma porta grande construída a muito tempo

utilizando madeira de carvalho. Com uma corda, começaram a puxar à porta. O que o grupo
não sabia, era que do outro lado morava uma senhora vestida com fantasia de carnaval. Ela
ficou com medo de ser roubada e pediu ajuda a um amigo praticante de musculação. Os dois
segurando a porta para impedindo de abrir. Agora é com você. A porta abriu ou não abriu?
Neste programa, será necessário saber o nível de força de cada membro. Para isso, utilize a
medida F. Exemplo: Uma pessoa normal tem 20F de força. Já um atleta pode chegar a 50F
de força. Pessoas especiais podem ter um nível maior de força.
OBS: A porta abre quando puxada por força superior a 120F."""
import random
forca_esqueletico = random.randint(1, 100)
forca_corcunda = random.randint(1, 100)
forca_aparelho = random.randint(1, 100)
forca_vidente = random.randint(1, 100)

forca_senhora= random.randint(1, 100)
forca_musculacao = random.randint(1, 200)

forca_abrir=forca_esqueletico+forca_corcunda+forca_aparelho+forca_vidente
forca_fechada=forca_senhora+forca_musculacao

print("Força do esquelético: ",forca_esqueletico)
print("Força do corcunda: ",forca_corcunda)
print("Força do homem de aparelho: ",forca_aparelho)
print("Força da vidente: ",forca_vidente)
print("Força da senhora: ",forca_senhora)
print("Força do musculoso: ",forca_musculacao)
print("Força para abrir a porta: ",forca_abrir)
print("Força para fechar a porta: ",forca_fechada)

if forca_abrir>forca_fechada:
    print("A porta abriu.")
else:
    print("A porta não abriu.")