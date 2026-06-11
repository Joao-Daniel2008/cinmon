import pygame
import funcoes_Classes
from imagens import imagens_cinmons as imagens
import pygame
import funcoes_Classes

#ataque

#normal
bater = funcoes_Classes.ataques('bater', 'normal', 'dano', 2, 2, 25, 25)
kamehameha = funcoes_Classes.ataques('kamehameha', 'normal', 'dano', 3, 3, 10, 10)
explosao = funcoes_Classes.ataques('explosao', 'normal', 'dano', 4, 4, 5, 5)
rasengan = funcoes_Classes.ataques('rasengan', 'normal', 'dano', 4, 4, 10, 10)

#escuridao
morder = funcoes_Classes.ataques('morder', 'escuridao', 'dano', 3, 3, 15, 15)
escuridao = funcoes_Classes.ataques('escuridao', 'escuridao', 'dano', 4, 4, 15, 15)

#lutador
investida = funcoes_Classes.ataques('investida', 'lutador', 'dano', 3, 3, 25, 25)

#voador
voadora = funcoes_Classes.ataques('voadora', 'voador', 'dano', 3, 3, 15, 15)
ventania = funcoes_Classes.ataques('ventania', 'voador', 'dano', 4, 4, 5, 5)

#fogo
brasas = funcoes_Classes.ataques('brasas', 'fogo', 'dano', 3, 3, 15, 15)
laser = funcoes_Classes.ataques('laser', 'fogo', 'dano', 4, 4, 10, 10)

#psiquico
estrelas = funcoes_Classes.ataques('estrelas', 'psiquico', 'dano', 3, 3, 10, 10)

#dragao
furia = funcoes_Classes.ataques('furia', 'dragao', 'dano', 4, 4, 5, 5)
dracmeteor = funcoes_Classes.ataques('dracmeteor', 'dragao', 'dano', 5, 5, 20, 20)
enfurecer = funcoes_Classes.ataques('enfurecer', 'dragao', 'selfatk', 0, 0, 15, 15)

ataques = [bater, kamehameha, explosao, rasengan, morder, escuridao,
            investida, voadora, ventania, brasas, laser, estrelas, 
            furia, dracmeteor, enfurecer]

#selfatk
aura = funcoes_Classes.ataques('aura', 'aura', 'selfatk', 0, 0, 15, 15)
carregar = funcoes_Classes.ataques('carregar', 'normal', 'selfatk', 0, 0, 10, 10)
chackra = funcoes_Classes.ataques('chakra', 'lutador', 'selfatk', 0, 0, 15, 15)
superbad = funcoes_Classes.ataques('superbad', 'escuridao', 'selfatk', 0, 0, 5, 5)

lupi = funcoes_Classes.Cimons('lupi', 'normal', imagens['lupi']['imagemc'], imagens['lupi']['imagemf'], imagens['lupi']['mini'], 11, 11, 11, 1, 0, {'ataque1':bater, 'ataque2': morder}, [voadora, 0, aura], [], 1)
rayquaza = funcoes_Classes.Cimons('rayquaza', 'voador', imagens['rayquaza']['imagemc'], imagens['rayquaza']['imagemf'], imagens['rayquaza']['mini'], 14, 14, 14, 1, 0, {'ataque1':morder, 'ataque2':ventania}, [furia, 0, enfurecer], [], 1.25)
gokussj = funcoes_Classes.Cimons('goku ssj', 'lutador', imagens['gokussj']['imagemc'], imagens['gokussj']['imagemf'], imagens['gokussj']['mini'], 14, 14, 14, 1, 0, {'ataque1':investida, 'ataque2':kamehameha, 'ataque3':bater, 'ataque4':carregar}, [], [], 1.2)
goku = funcoes_Classes.Cimons('goku', 'lutador', imagens['goku']['imagemc'], imagens['goku']['imagemf'], imagens['goku']['mini'], 12, 12, 12, 1, 0, {'ataque1':investida, 'ataque2':kamehameha}, [0, carregar, 0, 0, dracmeteor], [gokussj, 6], 1.1)
rath = funcoes_Classes.Cimons('rath', 'escuridao', imagens['rath']['imagemc'], imagens['rath']['imagemf'], imagens['rath']['mini'], 12, 12, 12, 1, 0, {'ataque1':bater, 'ataque2':voadora}, [brasas, 0, escuridao], [], 1)
mewtwo = funcoes_Classes.Cimons('mewtwo', 'psiquico', imagens['mewtwo']['imagemc'], imagens['mewtwo']['imagemf'], imagens['mewtwo']['mini'], 14, 14, 14, 1, 0, {'ataque1':explosao, 'ataque2':estrelas}, [voadora], [], 1.25)
mclovin = funcoes_Classes.Cimons('mc lovin', 'psiquico', imagens['mc lovin']['imagemc'], imagens['mc lovin']['imagemf'], imagens['mc lovin']['mini'], 11, 11, 11, 1, 0, {'ataque1':estrelas, 'ataque2':kamehameha}, [explosao, 0, superbad], [], 1.2)
homelander = funcoes_Classes.Cimons('homelander', 'voador', imagens['homelander']['imagemc'], imagens['homelander']['imagemf'], imagens['homelander']['mini'], 13, 13, 13, 1, 0, {'ataque1':laser, 'ataque2':estrelas}, [0, 0, aura, 0, 0, ventania], [], 1.2)
narutobeast = funcoes_Classes.Cimons('naruto beast', 'lutador', imagens['naruto beast']['imagemc'], imagens['naruto beast']['imagemf'], imagens['naruto beast']['mini'], 15, 15, 15, 1, 0, {'ataque1':investida, 'ataque2':rasengan, 'ataque3':chackra, 'ataque4':furia}, [], [], 1.25)
naruto = funcoes_Classes.Cimons('naruto', 'lutador', imagens['naruto']['imagemc'], imagens['naruto']['imagemf'], imagens['naruto']['mini'], 12, 12, 12, 1, 0, {'ataque1':investida, 'ataque2':rasengan}, [0, 0, chackra, 0, 0, furia], [narutobeast, 7], 1.15)


cimons = [lupi, rayquaza, gokussj, goku, rath, mewtwo, mclovin, homelander, narutobeast, naruto]