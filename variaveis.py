import pygame
import imagens
import objetos

largura = 1024  #largura e altura da tela
altura = 512
largurap = 64   #largura e altura do jogador
alturap = 64

xb = 8
yb = 80

posx = 576  #posicao dos jogadores
posy = 64
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

#Posições dos objetos no laborátorio 

#posição do Professro Iyoda 
ioda4 = imagens.ioda.get_rect()
ioda4.x = 448
ioda4.y = 64

#posição da mesa 
mesa4 = imagens.mesa.get_rect()
mesa4.x = 576
mesa4.y = 0

#posição dos crachábolas
crachabol1_4 = imagens.crachabol.get_rect()
crachabol1_4.x = 587
crachabol1_4.y = 20
crachabol2_4 = imagens.crachabol.get_rect()
crachabol2_4.x = 715
crachabol2_4.y = 20
crachabol3_4 = imagens.crachabol.get_rect()
crachabol3_4.x = 843
crachabol3_4.y = 20




#posições de objeto de cada cenário
posobj1 = ((128, 0), (192, 200))
posobj2 = ((704, 192), (384, 128))
posobj3 = ((476, 64), (704, 264), (0, 0))
posobj4 = ((448, 64), (576, 0), (587, 20), (715, 20), (843, 20))
posobj5 = ((576, 192), (640, 0))
posobj6 = ((704, 64), (832, 256), (64, 64), (192, 256))
posobj7 = ((192, 128), (448, 72))
posobj8 = ((192, 128), (448, 71))
posobj9 = ((384, 0), (512, 0))
posobjatual = posobj4



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

#listas dos rects de cada objeto dos cenários
listaobj1 = (objetos.casa4, objetos.porta4, objetos.player4)
listaobj2 = (objetos.cama4, objetos.tv4, objetos.player4)
listaobj3 = (objetos.lab4, objetos.porta2_4, objetos.cerca_cen3, objetos.player4)
listaobj4 = (ioda4, mesa4, crachabol1_4, crachabol2_4, crachabol3_4, objetos.player4)
listaobj5 = (objetos.imagenst['treinador1'], objetos.imagenst['treinador2'], objetos.player4)
listaobj6 = (objetos.centrocin1_4, objetos.porta3_4, objetos.loja1_4, objetos.porta4_4, objetos.player4)
listaobj7 = (objetos.mesa2_4, objetos.jailson4, objetos.player4)
listaobj8 = (objetos.mesa2_4, objetos.jailson4, objetos.player4)
listaobj9 = (objetos.imagenst['treinador3'], objetos.imagenst['treinador4'], objetos.player4)
listaobjatual = listaobj4

padraoL = 160           #dimensão de largura dos cinmon
padraoA = 160              #dimensão de altura dos cimon

#posições dos cinmons em batalha
posx1 = 192
posy1 = 224
posx2 = 688
posy2 = 72



