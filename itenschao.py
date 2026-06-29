import pygame
import random
import imagens
import time as time_module

som_coleta = None 
mochila_global = None
escolhaioda_global = False
palavra_func = None
itens_cenario_global = []
tempo_por_cenario = {}
TEMPO_RESPAWN = 10  # segundos

def carregar_sons():
    global som_coleta
    from pathlib import Path
    import sys
    if getattr(sys, 'frozen', False):
        BASE_DIR = Path(sys.executable).parent
    else:
        BASE_DIR = Path(__file__).parent
    som_coleta = pygame.mixer.Sound(BASE_DIR / "assets" / "sons" / "som_coleta_item.mp3")
    som_coleta.set_volume(0.5)

class ItemChao:
    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.coletado = False
        self.rect = pygame.Rect(x, y, 32, 32)

        if self.tipo == 'crachabola':
            self.imagem = pygame.transform.scale(imagens.crachabola, (32, 32))
        elif self.tipo == 'potion':
            self.imagem = pygame.transform.scale(imagens.potion, (32, 32))
        elif self.tipo == 'dinheiro':
            self.imagem = pygame.transform.scale(imagens.moeda, (32, 32))

    def desenhar(self, janela):
        if not self.coletado:
            janela.blit(self.imagem, (self.x, self.y))

    def verificar_coleta(self, player_rect):
        if not self.coletado and self.rect.colliderect(player_rect):
            self.coletado = True
            return True
        return False


POSICOES_FIXAS = {
    'cenario1': [(128, 384), (256, 320), (512, 384), (768, 320), (896, 384)],
    'cenario2': [(192, 384), (384, 320), (576, 384), (768, 320), (896, 384)],
    'cenario3': [(128, 384), (320, 320), (512, 384), (704, 320), (896, 384)],
    'cenario5': [(128, 384), (256, 320), (576, 384), (768, 320), (960, 384)],
    'cenario6': [(128, 384), (256, 448), (384, 384), (960, 448), (896, 384)],
    'cenario9': [(128, 384), (256, 320), (512, 384), (704, 320), (896, 384)],
}

def gerar_itens(nome_cenario, quantidade=2):
    itens = []
    tipos = ['crachabola', 'potion', 'dinheiro']
    pesos = [3, 3, 4]

    posicoes = POSICOES_FIXAS.get(nome_cenario, []).copy()
    random.shuffle(posicoes)

    for i in range(min(quantidade, len(posicoes))):
        tipo = random.choices(tipos, weights=pesos)[0]
        x, y = posicoes[i]
        itens.append(ItemChao(tipo, x, y))

    return itens

def verificar_respawn(nome_cenario):
    if nome_cenario in tempo_por_cenario:
        if time_module.time() - tempo_por_cenario[nome_cenario] >= TEMPO_RESPAWN:
            return True
    return False

def atualizar_itens(itens, player_rect, mochila, imagens_ref):
    global som_coleta
    if som_coleta is None:
        carregar_sons()
    valor_dinheiro = random.randint(5, 20)
    for item in itens:
        if item.verificar_coleta(player_rect):
            if som_coleta:
                som_coleta.play()
            if item.tipo == 'crachabola':
                idx = mochila.listaDeles.index(imagens_ref.crachabola)
                mochila.listaDeQtd[idx] += 1
            elif item.tipo == 'potion':
                idx = mochila.listaDeles.index(imagens_ref.potion)
                mochila.listaDeQtd[idx] += 1
            elif item.tipo == 'dinheiro':
                mochila.dinheiro += valor_dinheiro

    itens[:] = [i for i in itens if not i.coletado]