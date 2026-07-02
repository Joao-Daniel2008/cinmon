import imagens
import pygame
import variaveis

posx = 576
posy = 64

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

ioda4 = imagens.ioda.get_rect()
ioda4.x = 448
ioda4.y = 0

mesa4 = imagens.mesa.get_rect()
mesa4.x = 576
mesa4.y = 0

crachabol1_4 = imagens.crachabol.get_rect()
crachabol1_4.x = 587
crachabol1_4.y = 20
crachabol2_4 = imagens.crachabol.get_rect()
crachabol2_4.x = 715
crachabol2_4.y = 20
crachabol3_4 = imagens.crachabol.get_rect()
crachabol3_4.x = 843
crachabol3_4.y = 20

centrocin1_4 = imagens.centrocin1.get_rect()
centrocin1_4.x = 704
centrocin1_4.y = 64

ginasio4 = imagens.ginasio.get_rect()
ginasio4.x = 256
ginasio4.y = 64

portagym_4 = imagens.porta.get_rect()
portagym_4.x = 512
portagym_4.y = 320

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
imagenst['treinador3'].y = 64

imagenst['treinador4'].x = 512
imagenst['treinador4'].y = 64