import socket
import threading
import cimons
import json

escolhas_turno = {}
cimons1 = {1: {}, 2: {}}
jogou = 0
outra_decisao = {1: '', 2: ''}

def resolver_turno(idplayer):
    global cimons1, escolhas_turno

    for cimon in cimons.cimons:
        if cimons1[idplayer]['nome'] == cimon.nome:
            cimon1 = cimon.clonar()
            cimon1.xp = sum(n * 10 for n in range(1, cimons1[idplayer]['nivel']))
            cimon1.subir_nivel()
            cimon1.hp = cimons1[idplayer]['hp']
    
    for cimon in cimons.cimons:
        if cimons1[idplayer]['nome'] == cimon.nome:
            cimon2 = cimon.clonar()
            cimon2.xp = sum(n * 10 for n in range(1, cimons1[idplayer]['nivel']))
            cimon2.subir_nivel()
            cimon2.hp = cimons1[idplayer]['hp']

    


def gerenciar_clientes(conexao, endereco, idplayer):
    global cimons, escolhas_turno, jogou, outra_decisao

    print(f'NOVA CONEXAO: {endereco}')

    while True:
        try:
            dados = conexao.recv(2048).decode('utf-8')
            if not dados:
                print(f'CONEXAO PERDIDA COM: {endereco}')
                conexao.close()
                break

            decisao = json.loads(dados)

            outra_decisao[idplayer] = decisao['evento']

            if decisao['evento'] == 'COMECO' or decisao['evento'] == 'TROCA':
                cimons1[idplayer]['nome'] = decisao['nome']
                cimons1[idplayer]['nivel'] = decisao['nivel']
                cimons1[idplayer]['hp'] = decisao['hp']
                jogou += 1
                aguardando = True
                while jogou < 2:
                    if aguardando:
                        aguardando = False
                conexao.sendall(json.dumps(cimons1[2]).encode('utf-8')) if idplayer == 1 else conexao.sendall(json.dumps(cimons1[1]).encode('utf-8'))
            elif decisao['evento'] == 'ESCOLHA_GOLPE':
                escolhas_turno[idplayer] = decisao['golpe']
                aguardando = True
                while len(escolhas_turno) < 2:
                    if aguardando:
                        aguardando = False
                decisao2 = outra_decisao[1] if idplayer == 2 else decisao2 = outra_decisao[2]
                if decisao2 == 'ESOLHA_GOLPE':
                    resolver_turno(idplayer)
                

        

        except:
            print(f'ERROOOOO')
            conexao.close()
            break








HOST='localhost'
PORTA=5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('CRIANDO SERVIDOR...')
try:
    server.bind((HOST, PORTA))
except:
    print('CRIACAO ERRO')


print('ABRINDO PORTAS...')
server.listen()
print('AGURDANDO CLIENTES...')

jogadores = 1

while True:
    conexao, endereco = server.accept()
    thread = threading.Thread(target=(gerenciar_clientes), args=(conexao, endereco, jogadores), daemon=True)
    thread.start()
    jogadores += 1