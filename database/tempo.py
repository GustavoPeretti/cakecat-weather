from db import db

class Tempo(db.Model):
    cidade = db.Column(db.Text, primary_key=True)
    estado = db.Column(db.Text, primary_key=True)
    data = db.column(db.Date, primary_key=True)
    maxima = db.column(db.Float, nullable=False)
    minima = db.column(db.Float, nullable=False)
    chuva = db.column(db.Float, nullable=False)
    vento = db.column(db.Float, nullable=False)
    umidade = db.column(db.Float, nullable=False)
    arco_iris = db.Column(db.Text, nullable=False)
    inicio_sol = db.Column(db.Time, nullable=False)
    fim_sol = db.Column(db.Time, nullable=False)
    lua = db.Column(db.Text, nullable=False)

    def __init__(self, cidade, estado, data, maxima, minima, chuva, vento, umidade, arco_iris, inicio_sol, fim_sol, lua):
        self.cidade = cidade
        self.estado = estado
        self.data = data,
        self.maxima = maxima,
        self.minima = minima,
        self.chuva = chuva,
        self.vento = vento,
        self.umidade = umidade
        self.arco_iris = arco_iris,
        self.inicio_sol = inicio_sol,
        self.fim_sol = fim_sol
        self.lua = lua
