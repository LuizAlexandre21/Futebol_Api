# Pacotes
from pymodm.connection import connect 
from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields

# Criando Conexão junto ao banco
connect("mongodb://localhost:27017/Futebol_api", alias="my-api")

# Tabela do Campeonato 
class Campeonato(MongoModel):
    id = fields.IntegerField(primary_key=True)
    nome = fields.CharField()
    edição = fields.IntegerField()
    temporada = fields.IntegerField()
    tipo = fields.CharField()
    rodada = fields.IntegerField()
    região = fields.IntegerField()
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'

class Tabela(MongoModel):
    time_id = fields.IntegerField()
    nome = fields.CharField()
    escudo = fields.CharField()
    sigla = fields.CharField()
    pontos = fields.IntegerField()
    jogos = fields.IntegerField()
    vitorias = fields.IntegerField()
    derrotas = fields.IntegerField()
    empates = fields.IntegerField()
    gols_pro = fields.IntegerField()
    gols_cont = fields.IntegerField()
    saldo_gols = fields.IntegerField()
    aproveitamento = fields.IntegerField()
    ultimos_jogos = fields.CharField()
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'

class Artilharia(MongoModel):
    atleta_id = fields.IntegerField()
    atleta = field.CharField()
    posição = field.CharField()
    time_id = field.IntegerField()
    time = field.CharField()
    escudo = field.CharField()
    gols = field_IntegerField()
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'


class Partida(MongoModel):
    partida_id = fields.IntegerField()
    campeonato_id = fields.IntegerField()
    campeonato = fields.CharField()
    rodada = fields.IntegerField()
    edição = field.IntegerField()
    campeonato = field.IntegerField()
    time_mandante = fields.CharField()
    escudo_mandante = fields.CharField()
    placar_mandante = fields.IntegerField()
    placar_visitante = fields.IntegerField()
    escudo_visitante = fields.CharField()
    time_visitante = fields.CharFiels()
    data = fields.DateField()
    estadio = fields.CharField()
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app' 

class Estatisticas(MongoModel):
    time_id = fields.IntegerField()
    time = fields.CharField()
    escudo = fields.CharField()
    partida_id = fields.IntegerField()
    campeonato_id = fields.Charfield()
    gols = fields.IntegerField()
    posse = fields.IntegerField()
    escanteios = fields.IntegerField()
    faltas = fields.IntegerField()
    passes_totais = fields.IntegerField()
    passes_completos = fields.IntegerField()
    finalização_total = fields.IntegerField()
    finalização_gol = fields.IntegerField()
    finalização_fora = fields.IntegerField()
    finalização_trave = fields.IntegerField()
    finalização_bloqueado = fields.IntegerField()
    chances_disperdicadas = fields.IntegerField()
    cruzamentos_totais = fields.IntegerField()
    cruzamentos_completos = fields.IntegerField()
    bolas_afastadas= fields.IntegerField()
    defesas = fields.IntegerField()
    cortes = fields.IntegerField()
    bloqueios = fields.IntegerField()
    desarmes_totais = fields.IntegerField()
    precisão = fields.IntegerField()
    vitorias_divididas = fields.IntegerField()
    vitorias_jogo_aereo = fields.IntegerField()
    dribles = fields.IntegerField()
    faltas = fields.IntegerField()
    esquema_tatico = fields.CharField()
    tecnico = fields.CharField()
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app' 