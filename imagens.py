import sys
import pygame
from pathlib import Path



fundo_menu  = None
botoes_menu = None
caminho_coleta = None
moeda = None
def carregar():
    global fundo_menu, botoes_menu, som_clique,caminho_coleta,moeda


    caminho_moeda = BASE_DIR / "assets" / "imagens" / "moeda_jogo_cinmon.png"
    moeda = pygame.image.load(caminho_moeda)
    moeda = pygame.transform.scale(moeda, (32, 32))




    pygame.mixer.music.load(BASE_DIR / "assets" / "musicas" / "musica menu incial.mp3")
    caminho_coleta = BASE_DIR / "assets" / "sons" / "som_coleta_item.mp3"
    caminho_fundo_menu = BASE_DIR / "assets" / "imagens" / "mncin 1.png"
    fundo_menu  = pygame.image.load(caminho_fundo_menu)
    fundo_menu  = pygame.transform.scale(fundo_menu, (1024, 512))

    caminho_botoes_menu = BASE_DIR / "assets" / "imagens" / "tela_carregamento.png"
    botoes_menu = pygame.image.load(caminho_botoes_menu)
    botoes_menu = pygame.transform.scale(botoes_menu, (300, 150))

    som_clique = pygame.mixer.Sound(BASE_DIR / "assets" / "musicas" / "efeito_inicial.mp3")


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

caminho_a = BASE_DIR / "assets" / "imagens" / "letras" /"a.png"
caminho_b = BASE_DIR / "assets" / "imagens" / "letras" /"b.png"
caminho_c = BASE_DIR / "assets" / "imagens" / "letras" /"c.png"
caminho_d = BASE_DIR / "assets" / "imagens" / "letras" /"d.png"
caminho_e = BASE_DIR / "assets" / "imagens" / "letras" /"e.png"
caminho_f = BASE_DIR / "assets" / "imagens" / "letras" /"f.png"
caminho_g = BASE_DIR / "assets" / "imagens" / "letras" /"g.png"
caminho_h = BASE_DIR / "assets" / "imagens" / "letras" /"h.png"
caminho_i = BASE_DIR / "assets" / "imagens" / "letras" /"i.png"
caminho_j = BASE_DIR / "assets" / "imagens" / "letras" /"j.png"
caminho_k = BASE_DIR / "assets" / "imagens" / "letras" /"k.png"
caminho_l = BASE_DIR / "assets" / "imagens" / "letras" /"l.png"
caminho_m = BASE_DIR / "assets" / "imagens" / "letras" /"m.png"
caminho_n = BASE_DIR / "assets" / "imagens" / "letras" /"n.png"
caminho_o = BASE_DIR / "assets" / "imagens" / "letras" /"o.png"
caminho_p = BASE_DIR / "assets" / "imagens" / "letras" /"p.png"
caminho_q = BASE_DIR / "assets" / "imagens" / "letras" /"q.png"
caminho_r = BASE_DIR / "assets" / "imagens" / "letras" /"r.png"
caminho_s = BASE_DIR / "assets" / "imagens" / "letras" /"s.png"
caminho_t = BASE_DIR / "assets" / "imagens" / "letras" /"t.png"
caminho_u = BASE_DIR / "assets" / "imagens" / "letras" /"u.png"
caminho_v = BASE_DIR / "assets" / "imagens" / "letras" /"v.png"
caminho_w = BASE_DIR / "assets" / "imagens" / "letras" / "w.png"
caminho_x = BASE_DIR / "assets" / "imagens" / "letras" /"x.png"
caminho_y = BASE_DIR / "assets" / "imagens" / "letras" /"y.png"
caminho_z = BASE_DIR / "assets" / "imagens" / "letras" /"z.png"

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

caminho_tela_carregamento = BASE_DIR / "assets" / "imagens" / "tela_carregamento.png"
tela_carregamento = pygame.image.load(caminho_tela_carregamento)
tela_carregamento = pygame.transform.scale(tela_carregamento, (largura, altura))



caminho_fundo = BASE_DIR / "assets" / "imagens" / "batalha" /"fundo.png"
fundo = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo, (largura, altura))

#cenarios
caminho_cenario1 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario.png"
cenario1 = pygame.image.load(caminho_cenario1)
cenario1 = pygame.transform.scale(cenario1, (largura, altura))

caminho_cenario2 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario2.png"
cenario2 = pygame.image.load(caminho_cenario2)
cenario2 = pygame.transform.scale(cenario2, (largura, altura))

caminho_cenario3 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario3.png"
cenario3 = pygame.image.load(caminho_cenario3)
cenario3 = pygame.transform.scale(cenario3, (largura, altura))

caminho_cenario4 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario4.png"
cenario4 = pygame.image.load(caminho_cenario4)
cenario4 = pygame.transform.scale(cenario4, (largura, altura))

caminho_cenario5 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario5.png"
cenario5 = pygame.image.load(caminho_cenario5)
cenario5 = pygame.transform.scale(cenario5, (largura, altura))

caminho_cenario6 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario6.png"
cenario6 = pygame.image.load(caminho_cenario6)
cenario6 = pygame.transform.scale(cenario6, (largura, altura))

caminho_cenario9 = BASE_DIR / "assets" / "imagens" / "cenarios" / "cenario.png"
cenario9 = pygame.image.load(caminho_cenario9)
cenario9 = pygame.transform.scale(cenario9, (largura, altura))

caminho_centrocin = BASE_DIR / "assets" / "imagens" / "cenarios" / "centrocin.png"
centrocin = pygame.image.load(caminho_centrocin)
centrocin = pygame.transform.scale(centrocin, (largura, altura))


caminho_balaofala = BASE_DIR / "assets" / "imagens" / "balao.png"
balaofala = pygame.image.load(caminho_balaofala)
balaofala = pygame.transform.scale(balaofala, (896, 128))

caminho_molde = BASE_DIR / "assets" / "imagens" / "batalha" / "molde.png"
molde = pygame.image.load(caminho_molde)    #molde da batalha
molde = pygame.transform.scale(molde, (largura, altura / 4))

caminho_molde2 = BASE_DIR / "assets" / "imagens" / "batalha" / "molde2.png"
molde2 = pygame.image.load(caminho_molde2)
molde2 = pygame.transform.scale(molde2, (largura, altura / 4))

caminho_molde3 = BASE_DIR / "assets" / "imagens" / "batalha" / "molde3.png"
molde3 = pygame.image.load(caminho_molde3)
molde3 = pygame.transform.scale(molde3, (largura, altura / 4))

caminho_menu1 = BASE_DIR / "assets" / "imagens" / "menus" / "menu1.png"
menu1 = pygame.image.load(caminho_menu1)
menu1 = pygame.transform.scale(menu1, (112, 128))  #736, 368

caminho_menuloja = BASE_DIR / "assets" / "imagens" / "menus" / "menuloja.png"
menuloja = pygame.image.load(caminho_menuloja)
menuloja = pygame.transform.scale(menuloja, (210, 300))

#imagens de batalha
caminho_setinha = BASE_DIR / "assets" / "imagens" / "batalha" / "setinha.png"
setinha = pygame.image.load(caminho_setinha)
setinha = pygame.transform.scale(setinha, (32, 40))

caminho_barra = BASE_DIR / "assets" / "imagens" / "batalha" / "barra_hp.png"
barra = pygame.image.load(caminho_barra)
barra = pygame.transform.scale(barra, (307, 94))

caminho_auxhp = BASE_DIR / "assets" / "imagens" / "batalha" / "auxhp.png"
auxhp = pygame.image.load(caminho_auxhp)
auxhp = pygame.transform.scale(auxhp, (10, 10))

caminho_auxxp = BASE_DIR / "assets" / "imagens" / "batalha" / "auxxp.png"
auxxp = pygame.image.load(caminho_auxxp)
auxxp = pygame.transform.scale(auxxp, (6, 6))

#objetos 1
caminho_casa = BASE_DIR / "assets" / "imagens" / "objetos1" / "casa.png"
casa = pygame.image.load(caminho_casa)
casa = pygame.transform.scale(casa, (320, 256))

caminho_porta = BASE_DIR / "assets" / "imagens" / "objetos1" / "porta.png"
porta = pygame.image.load(caminho_porta)
porta = pygame.transform.scale(porta, (64, 56))

cerca = pygame.image.load(caminho_porta)
cerca = pygame.transform.scale(porta, (320, 320))

caminho_grama = BASE_DIR / "assets" / "imagens" / "grama.png"
grama = pygame.image.load(caminho_grama)
grama = pygame.transform.scale(grama, (largurap, alturap))

#objetos 2
caminho_cama = BASE_DIR / "assets" / "imagens" / "objetos2" / "cama.png"
cama = pygame.image.load(caminho_cama)
cama = pygame.transform.scale(cama, (224, 64))

caminho_tv = BASE_DIR / "assets" / "imagens" / "objetos2" / "tv.png"
tv = pygame.image.load(caminho_tv)
tv = pygame.transform.scale(tv, (128, 128))

#objetos 3
caminho_lab = BASE_DIR / "assets" / "imagens" / "objetos3" / "casa.png"
lab = pygame.image.load(caminho_lab)
lab = pygame.transform.scale(lab, (512, 256))


#objetos 4 
caminho_ioda = BASE_DIR / "assets" / "imagens" / "objetos4" / "ioda.png"
ioda = pygame.image.load(caminho_ioda)
ioda = pygame.transform.scale(ioda, (alturap, largurap))

caminho_mesa = BASE_DIR / "assets" / "imagens" / "objetos4" / "mesa.png"
mesa = pygame.image.load(caminho_mesa)
mesa = pygame.transform.scale(mesa, (384, alturap))

caminho_crachabol = BASE_DIR / "assets" / "imagens" / "objetos4" / "crachabola.png"
crachabol = pygame.image.load(caminho_crachabol)
crachabol = pygame.transform.scale(crachabol, (largurap//1.5, alturap//1.5))

caminho_crachabola = BASE_DIR / "assets" / "imagens" / "mochila" / "crachabola.png"
crachabola = pygame.image.load(caminho_crachabola)
crachabola = pygame.transform.scale(crachabola, (49, 64))

caminho_potion = BASE_DIR / "assets" / "imagens" / "mochila" / "potion.png"
potion = pygame.image.load(caminho_potion)
potion = pygame.transform.scale(potion, (49, 64))


#objetos 6
caminho_centrocin = BASE_DIR / "assets" / "imagens" / "objetos6" / "centropoke.png"
centrocin1 = pygame.image.load(caminho_centrocin)
centrocin1 = pygame.transform.scale(centrocin1, (320, 256))

#objetos centrocin
caminho_jailson = BASE_DIR / "assets" / "imagens" / "objetos7" / "jailson.png"
jailson = pygame.image.load(caminho_jailson)
jailson = pygame.transform.scale(jailson, (alturap, largurap))

#variações do player
caminho_frente = BASE_DIR / "assets" / "imagens" / "player_frente.png"
frente = pygame.image.load(caminho_frente)
frente = pygame.transform.scale(frente, (largurap, alturap))
caminho_esquerda = BASE_DIR / "assets" / "imagens" / "player_esquerda.png"
esquerda = pygame.image.load(caminho_esquerda)
esquerda = pygame.transform.scale(esquerda, (largurap, alturap))
caminho_direita = BASE_DIR / "assets" / "imagens" / "player_direita.png"
direita = pygame.image.load(caminho_direita)
direita = pygame.transform.scale(direita, (largurap, alturap))
caminho_atras = BASE_DIR / "assets" / "imagens" / "player_costas.png"
atras = pygame.image.load(caminho_atras)
atras = pygame.transform.scale(atras, (largurap, alturap))

#variações player 2
caminho_andando_frente1 = BASE_DIR / "assets" / "imagens" / "andando_frente1.png"
andando_frente1 = pygame.image.load(caminho_andando_frente1)
andando_frente1 = pygame.transform.scale(andando_frente1, (largurap, alturap))
caminho_andando_frente2 = BASE_DIR / "assets" / "imagens" / "andando_frente2.png"
andando_frente2 = pygame.image.load(caminho_andando_frente2)
andando_frente2 = pygame.transform.scale(andando_frente2, (largurap, alturap))

caminho_andando_atras1 = BASE_DIR / "assets" / "imagens" / "andando_atras1.png"
andando_atras1 = pygame.image.load(caminho_andando_atras1)
andando_atras1 = pygame.transform.scale(andando_atras1,(largurap, alturap))
caminho_andando_atras2 = BASE_DIR / "assets" / "imagens" / "andando_atras2.png"
andando_atras2 = pygame.image.load(caminho_andando_atras2)
andando_atras2 = pygame.transform.scale(andando_atras2,(largurap, alturap))

caminho_andando_direita1 = BASE_DIR / "assets" / "imagens" / "andando_direita1.png"
andando_direita1 = pygame.image.load(caminho_andando_direita1)
andando_direita1 = pygame.transform.scale(andando_direita1,(largurap, alturap))
caminho_andando_direita2 = BASE_DIR / "assets" / "imagens" / "andando_direita2.png"
andando_direita2 = pygame.image.load(caminho_andando_direita2)
andando_direita2 = pygame.transform.scale(andando_direita2,(largurap, alturap))

caminho_andando_esquerda1 = BASE_DIR / "assets" / "imagens" / "andando_esquerda1.png"
andando_esquerda1 = pygame.image.load(caminho_andando_esquerda1)
andando_esquerda1 = pygame.transform.scale(andando_esquerda1,(largurap, alturap))
caminho_andando_esquerda2 = BASE_DIR / "assets" / "imagens" / "andando_esquerda2.png"
andando_esquerda2 = pygame.image.load(caminho_andando_esquerda2)
andando_esquerda2 = pygame.transform.scale(andando_esquerda2,(largurap, alturap))


caminho_player = BASE_DIR / "assets" / "imagens" / "objetos1" / "porta.png"
player = pygame.image.load(caminho_player)
player = pygame.transform.scale(player, (largurap, alturap))

caminho_treinador1 = BASE_DIR / "assets" / "imagens" / "treinadores" / "minis" / "treinador1.png"
caminho_treinador2 = BASE_DIR / "assets" / "imagens" / "treinadores" / "minis" / "treinador1.png"
imagenst = {
    'treinador1': pygame.image.load(caminho_treinador1),
    'treinador2': pygame.image.load(caminho_treinador2),
    'treinador3': pygame.image.load(caminho_treinador2),
    'treinador4': pygame.image.load(caminho_treinador2),
    'treinador5': pygame.image.load(caminho_treinador2),
    'treinador6': pygame.image.load(caminho_treinador2),
    'treinador7': pygame.image.load(caminho_treinador2)

}
for n in imagenst:
    imagenst[n] = pygame.transform.scale(imagenst[n], (largurap, alturap))

#CINMÓNSSSSS
caminho_lupi = BASE_DIR / "assets" / "imagens" / "batalha" / "lupi.png"
caminho_mewtwo = BASE_DIR / "assets" / "imagens" / "batalha" / "mewtwo.png"
caminho_mclovin = BASE_DIR / "assets" / "imagens" / "batalha" / "mclovin.png"
caminho_rath = BASE_DIR / "assets" / "imagens" / "batalha" / "rath.png"
caminho_gokussj = BASE_DIR / "assets" / "imagens" / "batalha" / "gokussj.png"
caminho_rayquaza = BASE_DIR / "assets" / "imagens" / "batalha" / "rayquaza.png"
caminho_goku = BASE_DIR / "assets" / "imagens" / "batalha" / "goku.png"
caminho_homelander = BASE_DIR / "assets" / "imagens" / "batalha" / "homelander.png"
caminho_naruto = BASE_DIR / "assets" / "imagens" / "batalha" / "naruto.png"
caminho_narutobeast = BASE_DIR / "assets" / "imagens" / "batalha" / "naruto beast.png"
caminho_megarayquaza = BASE_DIR / "assets" / "imagens" / "batalha" / "megarayquazashiny.png"
caminho_arceus = BASE_DIR / "assets" / "imagens" / "batalha" / "arceus.png"
caminho_gengar = BASE_DIR / "assets" / "imagens" / "batalha" / "gengar.png"

caminho_lupi2 = BASE_DIR / "assets" / "imagens" / "batalha" / "lupi2.png"
caminho_mewtwo2 = BASE_DIR / "assets" / "imagens" / "batalha" / "mewtwo2.png"
caminho_mclovin2 = BASE_DIR / "assets" / "imagens" / "batalha" / "mclovin2.png"
caminho_rath2 = BASE_DIR / "assets" / "imagens" / "batalha" / "rath2.png"
caminho_gokussj2 = BASE_DIR / "assets" / "imagens" / "batalha" / "gokussj2.png"
caminho_rayquaza2 = BASE_DIR / "assets" / "imagens" / "batalha" / "rayquaza2.png"
caminho_goku2 = BASE_DIR / "assets" / "imagens" / "batalha" / "goku2.png"
caminho_homelander2 = BASE_DIR / "assets" / "imagens" / "batalha" / "homelander2.png"
caminho_naruto2 = BASE_DIR / "assets" / "imagens" / "batalha" / "naruto2.png"
caminho_narutobeast2 = BASE_DIR / "assets" / "imagens" / "batalha" / "naruto beast2.png"
caminho_megarayquaza2 = BASE_DIR / "assets" / "imagens" / "batalha" / "megarayquazashiny2.png"
caminho_arceus2 = BASE_DIR / "assets" / "imagens" / "batalha" / "arceus2.png"
caminho_gengar2 = BASE_DIR / "assets" / "imagens" / "batalha" / "gengar2.png"

caminho_lupim = BASE_DIR / "assets" / "imagens" / "minis" / "mini lupi.png"
caminho_mewtwom = BASE_DIR / "assets" / "imagens" / "minis" / "mini mewtwo.png"
caminho_mclovinm = BASE_DIR / "assets" / "imagens" / "minis" / "mini mclovin.png"
caminho_rathm = BASE_DIR / "assets" / "imagens" / "minis" / "mini rath.png"
caminho_gokussjm = BASE_DIR / "assets" / "imagens" / "minis" / "mini gokussj.png"
caminho_rayquazam = BASE_DIR / "assets" / "imagens" / "minis" / "mini rayquaza.png"
caminho_gokum = BASE_DIR / "assets" / "imagens" / "minis" / "mini goku.png"
caminho_homelanderm = BASE_DIR / "assets" / "imagens" / "minis" / "mini homelander.png"
caminho_narutom = BASE_DIR / "assets" / "imagens" / "minis" / "mini naruto.png"
caminho_narutobeastm = BASE_DIR / "assets" / "imagens" / "minis" / "mini naruto beast.png"
caminho_megarayquazam = BASE_DIR / "assets" / "imagens" / "minis" / "mini megarayquaza.png"
caminho_arceusm = BASE_DIR / "assets" / "imagens" / "minis" / "mini_arceuss.png"
caminho_gengarm = BASE_DIR / "assets" / "imagens" / "minis" / "mini gengar.png"

imagens_cinmons = {
    'lupi': {
        'imagemf': pygame.image.load(caminho_lupi2),
        'imagemc': pygame.image.load(caminho_lupi),
        'mini': pygame.transform.scale(pygame.image.load(caminho_lupim), (20, 20))
    }, 
    'shiny_mega_rayquaza' : {
        'imagemf': pygame.image.load(caminho_megarayquaza),
        'imagemc': pygame.image.load(caminho_megarayquaza2),
        'mini': pygame.image.load(caminho_megarayquazam)
    },
    'gengar': {
        'imagemf': pygame.image.load(caminho_gengar2),
        'imagemc': pygame.image.load(caminho_gengar),
        'mini': pygame.image.load(caminho_gengarm)
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
    'arceus':{
        'imagemc': pygame.image.load(caminho_arceus),
        'imagemf': pygame.image.load(caminho_arceus2),
        'mini': pygame.image.load(caminho_arceusm)
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
    }, 
    'naruto':{
        'imagemc': pygame.image.load(caminho_naruto),
        'imagemf': pygame.image.load(caminho_naruto2),
        'mini': pygame.image.load(caminho_narutom)
    },
    'naruto beast':{
        'imagemc': pygame.image.load(caminho_narutobeast),
        'imagemf': pygame.image.load(caminho_narutobeast2),
        'mini': pygame.image.load(caminho_narutobeastm)
    }
    
}

for n in imagens_cinmons:
    if n != 'teo':
        imagens_cinmons[n]['mini'] = pygame.transform.scale(imagens_cinmons[n]['mini'], (64, 64))

caminho_crachabola = BASE_DIR / "assets" / "imagens" / "mochila" / "crachabola.png"

imagensc = {
    'crachabola': pygame.transform.scale(pygame.image.load(caminho_crachabola), (49, 64))
}


for n in imagens_cinmons:
    if n != 'teo':    #################
        imagens_cinmons[n]['imagemf'] = pygame.transform.scale(imagens_cinmons[n]['imagemf'], (padraoL * 1.5, padraoA * 1.5))
        imagens_cinmons[n]['imagemc'] = pygame.transform.scale(imagens_cinmons[n]['imagemc'], (padraoL * 1.5, padraoA * 1.5))


#numeros

caminho_1 = BASE_DIR / "assets" / "imagens" / "numeros" / "1.png"
caminho_2 = BASE_DIR / "assets" / "imagens" / "numeros" / "2.png"
caminho_3 = BASE_DIR / "assets" / "imagens" / "numeros" / "3.png"
caminho_4 = BASE_DIR / "assets" / "imagens" / "numeros" / "4.png"
caminho_5 = BASE_DIR / "assets" / "imagens" / "numeros" / "5.png"
caminho_6 = BASE_DIR / "assets" / "imagens" / "numeros" / "6.png"
caminho_7 = BASE_DIR / "assets" / "imagens" / "numeros" / "7.png"
caminho_8 = BASE_DIR / "assets" / "imagens" / "numeros" / "8.png"
caminho_9 = BASE_DIR / "assets" / "imagens" / "numeros" / "9.png"
caminho_0 = BASE_DIR / "assets" / "imagens" / "numeros" / "0.png"
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