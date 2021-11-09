# Pacote 
import requests 
import pymongo
import pandas as pd 
import json 
from database import *

# Importando Parametros 
# Chaves 
headers = {'Authorization':'Bearer live_f149db67d4a0441badafd95bc2bef4'}

# Campeonato 
campeonato = {'campeonato-brasileiro':10}
campeonato_id = campeonato['campeonato-brasileiro']

# Importando dados da API 
# Requisições
# Tabela
Tab = requests.get(f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela',headers=headers)

# Campeonato 
Camp = requests.get(f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}',headers=headers)

# Artilharia 
Art = requests.get(f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/artilharia',headers=headers)


# Exportando os resultados 
# Campeonato 
json= Camp.json()
for i in json:
    Campeonato.objects.create(
        id = i['campeonato_id'],
        nome = i['nome'],
        edição = i['edicao_atual']['edicao_id'],
        temporada = i['edicao_atual']['temporada'],
        tipo = i['fase_atual']['tipo'],
        rodada = i['rodada_atual']['rodada'],
        região = i['região']
    )

# Tabela 
json = Tab.json()
for i in json:
    tabela.objects.create(
    time_id = i['time']['time_id'],
    nome = i['time']['nome_popular'],
    escudo = i['time']['escudo'],
    jogos = i['jogos'],
    vitorias = i['vitorias'],
    empates = i['empates'],
    derrotas = i['derrotas'],
    gols_pro = i['gols_pro'],
    gols_cont = i['gols_contra'],
    saldo_gols = i['saldo_gols'],
    aproveitamento = i['aproveitamento'],
    ultimos_jogos = i['ultimos_jogos']
    )

# Artilharia
json = Art.json()
for i in json:
    Artilharia.objects.create(
    atleta_id = i['atleta_id'],
    atleta = i['nome_popular'],
    posição = i['posicao']['nome'],
    time_id = i['time']['time_id'],
    time = i['time']['nome_popular'],
    escudo = i['time']['escudo'],
    gols = i['gols']
    )

# Rodadas
try:
    for r in range(1,31):
        Rod = requests.get(f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/rodadas/{r}',headers=headers)
        json = Rod.json()
        partidas = json['partidas']
        for j in ['time_mandante','time_visitante']:
            for k in range(0,len(json)):
                match = partidas[k][j]
                if j == 'time_mandante':
                    mandante = 1
                    placar = partidas[k]['placar_mandante']
                    if placar is None:
                        partidas[k]['placar_mandante'],partidas[k]['placar_visitante'] = 0,0 
                        placar =0 
                    if partidas[k]['placar_mandante'] >= partidas[k]['placar_visitante']:
                        resultado = 'Vitoria'
                    elif partidas[k]['placar_mandante'] == partidas[k]['placar_visitante']:
                        resultado = 'Empate'
                    else:
                        resultado = 'Derrota'
                else:
                    mandante = 0 
                    placar = partidas[k]['placar_visitante']
                    if placar is None:
                        partidas[k]['placar_mandante'],partidas[k]['placar_visitante'] = 0,0 
                        placar = 0
                    if partidas[k]['placar_visitante'] >= partidas[k]['placar_mandante']:
                        resultado = 'Vitoria'
                    elif partidas[k]['placar_visitante'] == partidas[k]['placar_mandante']:
                        resultado = 'Empate'
                    else:
                        resultado = 'Derrota'


                clube = match['nome_popular']
                escudo = match['escudo']
                data = partidas[k]['data_realizacao_iso']
                if data is None:
                    data = 0
                estadio = partidas[k]['estadio']['nome_popular']
            
                Rodada.objects.create(
                rodada = json['rodada'],
                status = json['status'],
                clube = clube,
#                mandante = mandante,
                escudo = escudo,
                gols = placar,
                resultado = resultado,
                data = data,
                estadio = estadio
                )
except Exception as e:
    print(e)