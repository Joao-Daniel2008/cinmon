import imagens
import pygame
import variaveis

#posição inicial do player
posx = variaveis.variavel_posição_inicial_player[0]
posy = variaveis.variavel_posição_inicial_player[1]

casa4 = imagens.casa.get_rect()
casa4.x = 128
casa4.y = 0

porta4 = imagens.porta.get_rect()
porta4.x = 192
porta4.y = 200

cama4 = imagens.cama.get_rect()
cama4.x = 704
cama4.y = 192

tv4 = imagens.tv.get_rect()
tv4.x = 384
tv4.y = 128

lab4 = imagens.lab.get_rect()
lab4.x = 476
lab4.y = 64

porta2_4 = imagens.porta.get_rect()
porta2_4.x = 704
porta2_4.y = 264

#Posições dos objetos no interior do laborátorio 

#posição do Professor Iyoda 
ioda4 = imagens.ioda.get_rect()
ioda4.x = variaveis.variavel_posição_iyoda[0]
ioda4.y = variaveis.variavel_posição_iyoda[1]

#posição da mesa 
mesa4 = imagens.mesa.get_rect()
mesa4.x = variaveis.variavel_posição_mesa_laboratório[0]
mesa4.y = variaveis.variavel_posição_mesa_laboratório[1] 

#posição dos crachábolas
Cinmon_inicial_1 = imagens.crachabol.get_rect()
Cinmon_inicial_1.x = variaveis.variavel_posição_Cinmon_inicial_1[0]
Cinmon_inicial_1.y = variaveis.variavel_posição_Cinmon_inicial_1[1]
Cinmon_inicial_2 = imagens.crachabol.get_rect()
Cinmon_inicial_2.x = variaveis.variavel_posição_Cinmon_inicial_2[0]
Cinmon_inicial_2.y = variaveis.variavel_posição_Cinmon_inicial_2[1]
Cinmon_inicial_3 = imagens.crachabol.get_rect()
Cinmon_inicial_3.x = variaveis.variavel_posição_Cinmon_inicial_1[0]
Cinmon_inicial_3.y = variaveis.variavel_posição_Cinmon_inicial_3[1]


centrocin1_4 = imagens.centrocin1.get_rect()
centrocin1_4.x = 704
centrocin1_4.y = 64

porta3_4 = imagens.porta.get_rect()
porta3_4.x = 832
porta3_4.y = 256

cerca_cen3 = imagens.cerca.get_rect()
cerca_cen3.x = 0
cerca_cen3.y = 0  

loja1_4 = imagens.centrocin1.get_rect()
loja1_4.x = 64
loja1_4.y = 64

porta4_4 = imagens.porta.get_rect()
porta4_4.x = 192
porta4_4.y = 256 

mesa2_4 = pygame.transform.scale(imagens.porta, (1024, 192)).get_rect()
mesa2_4.x = 0
mesa2_4.y = 0

jailson4 = imagens.jailson.get_rect()
jailson4.x = 448
jailson4.y = 72

player4 = imagens.player.get_rect()
player4.x = posx
player4.y = posy

imagenst = {
    'treinador1' : imagens.imagenst['treinador1'].get_rect(),
    'treinador2' : imagens.imagenst['treinador2'].get_rect(),
    'treinador3' : imagens.imagenst['treinador3'].get_rect(),
    'treinador4' : imagens.imagenst['treinador4'].get_rect()
}
imagenst['treinador1'].x = 576
imagenst['treinador1'].y = 192

imagenst['treinador2'].x = 640
imagenst['treinador2'].y = 0

imagenst['treinador3'].x = 384
imagenst['treinador3'].y = 0

imagenst['treinador4'].x = 512
imagenst['treinador4'].y = 0

#listas dos rects de cada objeto dos cenários
listaobj1 = (casa4, porta4, player4)
listaobj2 = (cama4, tv4, player4)
listaobj3 = (lab4, porta2_4, cerca_cen3, player4)
listaobj4 = (ioda4, mesa4, Cinmon_inicial_1, Cinmon_inicial_2, Cinmon_inicial_3, player4)
listaobj5 = (imagenst['treinador1'], imagenst['treinador2'], player4)
listaobj6 = (centrocin1_4, porta3_4, loja1_4, porta4_4, player4)
listaobj7 = (mesa2_4, jailson4, player4)
listaobj8 = (mesa2_4, jailson4, player4)
listaobj9 = (imagenst['treinador3'], imagenst['treinador4'], player4)
listaobjatual = listaobj4

#listas de objetos de cada cenário
lista1 =(imagens.casa, imagens.porta, imagens.player)
lista2 =(imagens.cama, imagens.tv, imagens.player)
lista3 =(imagens.lab, imagens.porta, imagens.cerca, imagens.player)
lista4 =(imagens.ioda, imagens.mesa, imagens.crachabol, imagens.crachabol, imagens.crachabol, imagens.player)
lista5 =(imagens.imagenst['treinador1'], imagens.imagenst['treinador2'], imagens.player)
lista6 =(imagens.centrocin1, imagens.porta, imagens.centrocin1, imagens.porta, imagens.player)
lista7 = (imagens.porta, imagens.jailson, imagens.player)
lista8 = (imagens.porta, imagens.jailson, imagens.player)
lista9 = (imagens.imagenst['treinador1'], imagens.imagenst['treinador1'],imagens.player)
listatual = lista4

#posições de objeto de cada cenário
posobj1 = ((128, 0), (192, 200))
posobj2 = ((704, 192), (384, 128))
posobj3 = ((476, 64), (704, 264), (0, 0))
posobj4 = (variaveis.variavel_posição_iyoda, variaveis.variavel_posição_mesa_laboratório, variaveis.variavel_posição_Cinmon_inicial_1, variaveis.variavel_posição_Cinmon_inicial_2, variaveis.variavel_posição_Cinmon_inicial_3)
posobj5 = ((576, 192), (640, 0))
posobj6 = ((704, 64), (832, 256), (64, 64), (192, 256))
posobj7 = ((192, 128), (448, 72))
posobj8 = ((192, 128), (448, 71))
posobj9 = ((384, 0), (512, 0))
posobjatual = posobj4

#posições dos cinmons em batalha
posx1 = 192
posy1 = 224
posx2 = 688
posy2 = 72

#Dimensões da tela 
largura = 1024  
altura = 512

#Dimensões do player
largurap = variaveis.variavel_dimensão_player[0]
alturap = variaveis.variavel_dimensão_player[1]

xb = 8
yb = 80

velocidade = 16

gramas1 = tuple(imagens.grama for n in range(4))
gramasatual = ()
gramasx1 = (704, 704, 832, 832)
gramasy1 = (64, 192, 64, 128)
gramasxatual = ()
gramasyatual = ()
gramas4_atual = []


gramasx5 = (64, 128, 192, 320, 384, 448, 512, 320, 384, 448, 512)
gramasy5 = (64, 64, 64, 256, 256, 256, 256, 192, 192, 192, 192)
gramas5 = tuple(imagens.grama for n in range (len(gramasx5)))
gramas5_4 = tuple(n.get_rect() for n in gramas5)

gramas9 = tuple(imagens.grama for n in range(32))
gramasx9 = tuple(n * 64 for n in range(16)) + tuple (n * 64 for n in range(16))

gramasy9 = tuple(256 for _ in range(16)) + tuple(320 for _ in range(16))
gramas9_4 = tuple(n.get_rect() for n in gramas9)

padraoL = 160           #dimensão de largura dos cinmon
padraoA = 160              #dimensão de altura dos cimon
