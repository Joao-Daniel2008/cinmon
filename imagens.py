import sys
import pygame
from pathlib import Path


if getattr(sys, 'frozen', False):
    # Se for um .exe do PyInstaller
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    # Se for o script .py normal
    BASE_DIR = Path(__file__).resolve().parent

largural = 20
altural = 48

largura = 1024  #largura e altura da tela
altura = 512
largurap = 64   #largura e altura do jogador
alturap = 64

padraoL = 160           #dimensão de largura dos cinmon
padraoA = 160              #dimensão de altura dos cimon

caminho_a = BASE_DIR / "assets" / "letras" /"a.png"
caminho_b = BASE_DIR / "assets" / "letras" /"b.png"
caminho_c = BASE_DIR / "assets" / "letras" /"c.png"
caminho_d = BASE_DIR / "assets" / "letras" /"d.png"
caminho_e = BASE_DIR / "assets" / "letras" /"e.png"
caminho_f = BASE_DIR / "assets" / "letras" /"f.png"
caminho_g = BASE_DIR / "assets" / "letras" /"g.png"
caminho_h = BASE_DIR / "assets" / "letras" /"h.png"
caminho_i = BASE_DIR / "assets" / "letras" /"i.png"
caminho_j = BASE_DIR / "assets" / "letras" /"j.png"
caminho_k = BASE_DIR / "assets" / "letras" /"k.png"
caminho_l = BASE_DIR / "assets" / "letras" /"l.png"
caminho_m = BASE_DIR / "assets" / "letras" /"m.png"
caminho_n = BASE_DIR / "assets" / "letras" /"n.png"
caminho_o = BASE_DIR / "assets" / "letras" /"o.png"
caminho_p = BASE_DIR / "assets" / "letras" /"p.png"
caminho_q = BASE_DIR / "assets" / "letras" /"q.png"
caminho_r = BASE_DIR / "assets" / "letras" /"r.png"
caminho_s = BASE_DIR / "assets" / "letras" /"s.png"
caminho_t = BASE_DIR / "assets" / "letras" /"t.png"
caminho_u = BASE_DIR / "assets" / "letras" /"u.png"
caminho_v = BASE_DIR / "assets" / "letras" /"v.png"
caminho_w = BASE_DIR / "assets" / "letras" / "w.png"
caminho_x = BASE_DIR / "assets" / "letras" /"x.png"
caminho_y = BASE_DIR / "assets" / "letras" /"y.png"
caminho_z = BASE_DIR / "assets" / "letras" /"z.png"

a = pygame.image.load(caminho_a)
a = pygame.transform.scale(a, (largural, altural))
b = pygame.image.load(caminho_b)
b = pygame.transform.scale(b, (largural, altural))
c = pygame.image.load(caminho_c)
c = pygame.transform.scale(c, (largural, altural))
d = pygame.image.load(caminho_d)
d = pygame.transform.scale(d, (largural, altural))
e = pygame.image.load(caminho_e)
e = pygame.transform.scale(e, (largural, altural))
f = pygame.image.load(caminho_f)
f = pygame.transform.scale(f, (largural, altural))
g = pygame.image.load(caminho_g)
g = pygame.transform.scale(g, (largural, altural))
h = pygame.image.load(caminho_h)
h = pygame.transform.scale(h, (largural, altural))
i = pygame.image.load(caminho_i)
i = pygame.transform.scale(i, (largural, altural))
j = pygame.image.load(caminho_j)
j = pygame.transform.scale(j, (largural, altural))
k = pygame.image.load(caminho_k)
k = pygame.transform.scale(k, (largural, altural))
l = pygame.image.load(caminho_l)
l = pygame.transform.scale(l, (largural, altural))
m = pygame.image.load(caminho_m)
m = pygame.transform.scale(m, (largural, altural))
n = pygame.image.load(caminho_n)
eni = pygame.transform.scale(n, (largural, altural))
o = pygame.image.load(caminho_o)
o = pygame.transform.scale(o, (largural, altural))
p = pygame.image.load(caminho_p)
p = pygame.transform.scale(p, (largural, altural))
q = pygame.image.load(caminho_q)
q = pygame.transform.scale(q, (largural, altural))
r = pygame.image.load(caminho_r)
r = pygame.transform.scale(r, (largural, altural))
s = pygame.image.load(caminho_s)
s = pygame.transform.scale(s, (largural, altural))
t = pygame.image.load(caminho_t)
t = pygame.transform.scale(t, (largural, altural))
u = pygame.image.load(caminho_u)
u = pygame.transform.scale(u, (largural, altural))
v = pygame.image.load(caminho_v)
v = pygame.transform.scale(v, (largural, altural))
w = pygame.image.load(caminho_w)
w = pygame.transform.scale(w, (largural, altural))
x = pygame.image.load(caminho_x)
x = pygame.transform.scale(x, (largural, altural))
y = pygame.image.load(caminho_y)
y = pygame.transform.scale(y, (largural, altural))
z = pygame.image.load(caminho_z)
z = pygame.transform.scale(z, (largural, altural))

caminho_fundo = BASE_DIR / "assets" / "batalha" /"fundo.png"
fundo = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo, (largura, altura))

#cenarios
caminho_cenario1 = BASE_DIR / "assets" / "cenarios" / "cenario.png"
cenario1 = pygame.image.load(caminho_cenario1)
cenario1 = pygame.transform.scale(cenario1, (largura, altura))

caminho_cenario2 = BASE_DIR / "assets" / "cenarios" / "cenario2.png"
cenario2 = pygame.image.load(caminho_cenario2)
cenario2 = pygame.transform.scale(cenario2, (largura, altura))

caminho_cenario3 = BASE_DIR / "assets" / "cenarios" / "cenario3.png"
cenario3 = pygame.image.load(caminho_cenario3)
cenario3 = pygame.transform.scale(cenario3, (largura, altura))

caminho_cenario4 = BASE_DIR / "assets" / "cenarios" / "cenario4.png"
cenario4 = pygame.image.load(caminho_cenario4)
cenario4 = pygame.transform.scale(cenario4, (largura, altura))

caminho_cenario5 = BASE_DIR / "assets" / "cenarios" / "cenario5.png"
cenario5 = pygame.image.load(caminho_cenario5)
cenario5 = pygame.transform.scale(cenario5, (largura, altura))

caminho_cenario6 = BASE_DIR / "assets" / "cenarios" / "cenario6.png"
cenario6 = pygame.image.load(caminho_cenario6)
cenario6 = pygame.transform.scale(cenario6, (largura, altura))

caminho_cenario9 = BASE_DIR / "assets" / "cenarios" / "cenario.png"
cenario9 = pygame.image.load(caminho_cenario9)
cenario9 = pygame.transform.scale(cenario9, (largura, altura))

caminho_centrocin = BASE_DIR / "assets" / "cenarios" / "centrocin.png"
centrocin = pygame.image.load(caminho_centrocin)
centrocin = pygame.transform.scale(centrocin, (largura, altura))





caminho_balaofala = BASE_DIR / "assets" / "balao.png"
balaofala = pygame.image.load(caminho_balaofala)
balaofala = pygame.transform.scale(balaofala, (896, 128))

caminho_molde = BASE_DIR / "assets" / "batalha" / "molde.png"
molde = pygame.image.load(caminho_molde)    #molde da batalha
molde = pygame.transform.scale(molde, (largura, altura / 4))

caminho_molde2 = BASE_DIR / "assets" / "batalha" / "molde2.png"
molde2 = pygame.image.load(caminho_molde2)
molde2 = pygame.transform.scale(molde2, (largura, altura / 4))

caminho_molde3 = BASE_DIR / "assets" / "batalha" / "molde3.png"
molde3 = pygame.image.load(caminho_molde3)
molde3 = pygame.transform.scale(molde3, (largura, altura / 4))

caminho_menu1 = BASE_DIR / "assets" / "menus" / "menu1.png"
menu1 = pygame.image.load(caminho_menu1)
menu1 = pygame.transform.scale(menu1, (112, 128))  #736, 368

caminho_menuloja = BASE_DIR / "assets" / "menus" / "menuloja.png"
menuloja = pygame.image.load(caminho_menuloja)
menuloja = pygame.transform.scale(menuloja, (210, 300))

#imagens de batalha
caminho_setinha = BASE_DIR / "assets" / "batalha" / "setinha.png"
setinha = pygame.image.load(caminho_setinha)
setinha = pygame.transform.scale(setinha, (32, 40))

caminho_barra = BASE_DIR / "assets" / "batalha" / "barra_hp.png"
barra = pygame.image.load(caminho_barra)
barra = pygame.transform.scale(barra, (307, 94))

caminho_auxhp = BASE_DIR / "assets" / "batalha" / "auxhp.png"
auxhp = pygame.image.load(caminho_auxhp)
auxhp = pygame.transform.scale(auxhp, (10, 10))

caminho_auxxp = BASE_DIR / "assets" / "batalha" / "auxxp.png"
auxxp = pygame.image.load(caminho_auxxp)
auxxp = pygame.transform.scale(auxxp, (6, 6))

#objetos 1
caminho_casa = BASE_DIR / "assets" / "objetos1" / "casa.png"
casa = pygame.image.load(caminho_casa)
casa = pygame.transform.scale(casa, (320, 256))

caminho_porta = BASE_DIR / "assets" / "objetos1" / "porta.png"
porta = pygame.image.load(caminho_porta)
porta = pygame.transform.scale(porta, (64, 56))

caminho_grama = BASE_DIR / "assets" / "grama.png"
grama = pygame.image.load(caminho_grama)
grama = pygame.transform.scale(grama, (largurap, alturap))

#objetos 2
caminho_cama = BASE_DIR / "assets" / "objetos2" / "cama.png"
cama = pygame.image.load(caminho_cama)
cama = pygame.transform.scale(cama, (224, 64))

caminho_tv = BASE_DIR / "assets" / "objetos2" / "tv.png"
tv = pygame.image.load(caminho_tv)
tv = pygame.transform.scale(tv, (128, 128))

#objetos 3
caminho_lab = BASE_DIR / "assets" / "objetos3" / "casa.png"
lab = pygame.image.load(caminho_lab)
lab = pygame.transform.scale(lab, (512, 256))


#objetos 4 
caminho_ioda = BASE_DIR / "assets" / "objetos4" / "ioda.png"
ioda = pygame.image.load(caminho_ioda)
ioda = pygame.transform.scale(ioda, (alturap, largurap))

caminho_mesa = BASE_DIR / "assets" / "objetos4" / "mesa.png"
mesa = pygame.image.load(caminho_mesa)
mesa = pygame.transform.scale(mesa, (384, alturap))

caminho_crachabol = BASE_DIR / "assets" / "objetos4" / "crachabola.png"
crachabol = pygame.image.load(caminho_crachabol)
crachabol = pygame.transform.scale(crachabol, (largurap//1.5, alturap//1.5))

caminho_crachabola = BASE_DIR / "assets" / "mochila" / "crachabola.png"
crachabola = pygame.image.load(caminho_crachabola)
crachabola = pygame.transform.scale(crachabola, (49, 64))


#objetos 6
caminho_centrocin = BASE_DIR / "assets" / "objetos6" / "centropoke.png"
centrocin1 = pygame.image.load(caminho_centrocin)
centrocin1 = pygame.transform.scale(centrocin1, (320, 256))

#objetos centrocin
caminho_jailson = BASE_DIR / "assets" / "objetos7" / "jailson.png"
jailson = pygame.image.load(caminho_jailson)
jailson = pygame.transform.scale(jailson, (alturap, largurap))

#variações do player
caminho_frente = BASE_DIR / "assets" / "player_frente.png"
frente = pygame.image.load(caminho_frente)
frente = pygame.transform.scale(frente, (largurap, alturap))
caminho_esquerda = BASE_DIR / "assets" / "player_esquerda.png"
esquerda = pygame.image.load(caminho_esquerda)
esquerda = pygame.transform.scale(esquerda, (largurap, alturap))
caminho_direita = BASE_DIR / "assets" / "player_direita.png"
direita = pygame.image.load(caminho_direita)
direita = pygame.transform.scale(direita, (largurap, alturap))
caminho_atras = BASE_DIR / "assets" / "player_costas.png"
atras = pygame.image.load(caminho_atras)
atras = pygame.transform.scale(atras, (largurap, alturap))

#variações player 2
caminho_andando_frente1 = BASE_DIR / "assets" / "andando_frente1.png"
andando_frente1 = pygame.image.load(caminho_andando_frente1)
andando_frente1 = pygame.transform.scale(andando_frente1, (largurap, alturap))
caminho_andando_frente2 = BASE_DIR / "assets" / "andando_frente2.png"
andando_frente2 = pygame.image.load(caminho_andando_frente2)
andando_frente2 = pygame.transform.scale(andando_frente2, (largurap, alturap))

caminho_andando_atras1 = BASE_DIR / "assets" / "andando_atras1.png"
andando_atras1 = pygame.image.load(caminho_andando_atras1)
andando_atras1 = pygame.transform.scale(andando_atras1,(largurap, alturap))
caminho_andando_atras2 = BASE_DIR / "assets" / "andando_atras2.png"
andando_atras2 = pygame.image.load(caminho_andando_atras2)
andando_atras2 = pygame.transform.scale(andando_atras2,(largurap, alturap))

caminho_andando_direita1 = BASE_DIR / "assets" / "andando_direita1.png"
andando_direita1 = pygame.image.load(caminho_andando_direita1)
andando_direita1 = pygame.transform.scale(andando_direita1,(largurap, alturap))
caminho_andando_direita2 = BASE_DIR / "assets" / "andando_direita2.png"
andando_direita2 = pygame.image.load(caminho_andando_direita2)
andando_direita2 = pygame.transform.scale(andando_direita2,(largurap, alturap))

caminho_andando_esquerda1 = BASE_DIR / "assets" / "andando_esquerda1.png"
andando_esquerda1 = pygame.image.load(caminho_andando_esquerda1)
andando_esquerda1 = pygame.transform.scale(andando_esquerda1,(largurap, alturap))
caminho_andando_esquerda2 = BASE_DIR / "assets" / "andando_esquerda2.png"
andando_esquerda2 = pygame.image.load(caminho_andando_esquerda2)
andando_esquerda2 = pygame.transform.scale(andando_esquerda2,(largurap, alturap))


caminho_player = BASE_DIR / "assets" / "objetos1" / "porta.png"
player = pygame.image.load(caminho_player)
player = pygame.transform.scale(player, (largurap, alturap))

caminho_treinador1 = BASE_DIR / "assets" / "treinadores" / "minis" / "treinador1.png"
caminho_treinador2 = BASE_DIR / "assets" / "treinadores" / "minis" / "treinador1.png"
imagenst = {
    'treinador1': pygame.image.load(caminho_treinador1),
    'treinador2': pygame.image.load(caminho_treinador2),
    'treinador3': pygame.image.load(caminho_treinador2),
    'treinador4': pygame.image.load(caminho_treinador2)
}
for n in imagenst:
    imagenst[n] = pygame.transform.scale(imagenst[n], (largurap, alturap))

#CINMÓNSSSSS
caminho_lupi = BASE_DIR / "assets" / "batalha" / "lupi.png"
caminho_mewtwo = BASE_DIR / "assets" / "batalha" / "mewtwo.png"
caminho_mclovin = BASE_DIR / "assets" / "batalha" / "mclovin.png"
caminho_rath = BASE_DIR / "assets" / "batalha" / "rath.png"
caminho_gokussj = BASE_DIR / "assets" / "batalha" / "gokussj.png"
caminho_rayquaza = BASE_DIR / "assets" / "batalha" / "rayquaza.png"
caminho_goku = BASE_DIR / "assets" / "batalha" / "goku.png"
caminho_homelander = BASE_DIR / "assets" / "batalha" / "homelander.png"

caminho_lupi2 = BASE_DIR / "assets" / "batalha" / "lupi2.png"
caminho_mewtwo2 = BASE_DIR / "assets" / "batalha" / "mewtwo2.png"
caminho_mclovin2 = BASE_DIR / "assets" / "batalha" / "mclovin2.png"
caminho_rath2 = BASE_DIR / "assets" / "batalha" / "rath2.png"
caminho_gokussj2 = BASE_DIR / "assets" / "batalha" / "gokussj2.png"
caminho_rayquaza2 = BASE_DIR / "assets" / "batalha" / "rayquaza2.png"
caminho_goku2 = BASE_DIR / "assets" / "batalha" / "goku2.png"
caminho_homelander2 = BASE_DIR / "assets" / "batalha" / "homelander2.png"

caminho_lupim = BASE_DIR / "assets" / "minis" / "mini lupi.png"
caminho_mewtwom = BASE_DIR / "assets" / "minis" / "mini mewtwo.png"
caminho_mclovinm = BASE_DIR / "assets" / "minis" / "mini mclovin.png"
caminho_rathm = BASE_DIR / "assets" / "minis" / "mini rath.png"
caminho_gokussjm = BASE_DIR / "assets" / "minis" / "mini gokussj.png"
caminho_rayquazam = BASE_DIR / "assets" / "minis" / "mini rayquaza.png"
caminho_gokum = BASE_DIR / "assets" / "minis" / "mini goku.png"
caminho_homelanderm = BASE_DIR / "assets" / "minis" / "mini homelander.png"

imagens = {
    'lupi': {
        'imagemf': pygame.image.load(caminho_lupi2),
        'imagemc': pygame.image.load(caminho_lupi),
        'mini': pygame.transform.scale(pygame.image.load(caminho_lupim), (20, 20))
    }, 
    'mewtwo': {
        'mini': pygame.image.load(caminho_mewtwom),
        'imagemc': pygame.image.load(caminho_mewtwo),
        'imagemf': pygame.image.load(caminho_mewtwo2)
    },
    'mc lovin': {
        'imagemc': pygame.image.load(caminho_mclovin),
        'imagemf': pygame.image.load(caminho_mclovin2),
        'mini': pygame.image.load(caminho_mclovinm)
    },
    'rath': {
        'imagemc': pygame.image.load(caminho_rath),
        'imagemf': pygame.image.load(caminho_rath2),
        'mini': pygame.image.load(caminho_rathm)
    },
    'teo': {},
    'rayquaza': {
        'imagemc': pygame.image.load(caminho_rayquaza),
        'imagemf': pygame.image.load(caminho_rayquaza2),
        'mini' : pygame.image.load(caminho_rayquazam)
    },
    'goku':{
        'imagemc': pygame.image.load(caminho_goku),
        'imagemf': pygame.image.load(caminho_goku2),
        'mini': pygame.image.load(caminho_gokum)
    },
    'gokussj':{
        'imagemc': pygame.image.load(caminho_gokussj),
        'imagemf': pygame.image.load(caminho_gokussj2),
        'mini': pygame.image.load(caminho_gokussjm)
    },
    'homelander':{
        'imagemc': pygame.image.load(caminho_homelander),
        'imagemf': pygame.image.load(caminho_homelander2),
        'mini': pygame.image.load(caminho_homelanderm)
    }
}

for n in imagens:
    if n != 'teo':
        imagens[n]['mini'] = pygame.transform.scale(imagens[n]['mini'], (64, 64))

caminho_crachabola = BASE_DIR / "assets" / "mochila" / "crachabola.png"

imagensc = {
    'crachabola': pygame.transform.scale(pygame.image.load(caminho_crachabola), (49, 64))
}


for n in imagens:
    if n != 'teo':    #################
        imagens[n]['imagemf'] = pygame.transform.scale(imagens[n]['imagemf'], (padraoL * 1.5, padraoA * 1.5))
        imagens[n]['imagemc'] = pygame.transform.scale(imagens[n]['imagemc'], (padraoL * 1.5, padraoA * 1.5))


#numeros

caminho_1 = BASE_DIR / "assets" / "numeros" / "1.png"
caminho_2 = BASE_DIR / "assets" / "numeros" / "2.png"
caminho_3 = BASE_DIR / "assets" / "numeros" / "3.png"
caminho_4 = BASE_DIR / "assets" / "numeros" / "4.png"
caminho_5 = BASE_DIR / "assets" / "numeros" / "5.png"
caminho_6 = BASE_DIR / "assets" / "numeros" / "6.png"
caminho_7 = BASE_DIR / "assets" / "numeros" / "7.png"
caminho_8 = BASE_DIR / "assets" / "numeros" / "8.png"
caminho_9 = BASE_DIR / "assets" / "numeros" / "9.png"
caminho_0 = BASE_DIR / "assets" / "numeros" / "0.png"
zero = pygame.image.load(caminho_0)
zero = pygame.transform.scale(zero, (largural, altural))
um = pygame.image.load(caminho_1)
um = pygame.transform.scale(um, (largural, altural))
dois = pygame.image.load(caminho_2)
dois = pygame.transform.scale(dois, (largural, altural))
tres = pygame.image.load(caminho_3)
tres = pygame.transform.scale(tres, (largural, altural))
quatro = pygame.image.load(caminho_4)
quatro = pygame.transform.scale(quatro, (largural, altural))
cinco = pygame.image.load(caminho_5)
cinco = pygame.transform.scale(cinco, (largural, altural))
seis = pygame.image.load(caminho_6)
seis = pygame.transform.scale(seis, (largural, altural))
sete = pygame.image.load(caminho_7)
sete = pygame.transform.scale(sete, (largural, altural))
oito = pygame.image.load(caminho_8)
oito = pygame.transform.scale(oito, (largural, altural))
nove = pygame.image.load(caminho_9)
nove = pygame.transform.scale(nove, (largural, altural))




##MUSICASSSSS
caminho_batalha_tema = BASE_DIR / "assets" / "musicas" / "battleThemeA.mp3"
caminho_musicaPrincipal = BASE_DIR / "assets" / "musicas" / "TownTheme.mp3"




#SOOOOOOOOONS
caminho_atk = BASE_DIR / "assets" / "sons" / "atk.wav"
caminho_nivel = BASE_DIR / "assets" / "sons" / "subiunivel.ogg"
