import sqlalchemy as sa 
from datetime import datetime
from models.model_base import ModelBase

class VendasMes(ModelBase):
    __tablename__:str = 'vendas_por_mes'
    id: int = sa.Column(sa.BigInteger,primary_key=True, autoincrement=True)  
    venda: int = sa.Column(sa.Integer, unique= False, nullable = False)
    ano: int = sa.Column(sa.Integer, unique= False, nullable = False)
    mes: int = sa.Column(sa.Integer, unique= False, nullable = False)
    data_extracao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    def __repr__(self) -> str:
        return f'<Vendas por Mes : {self.venda}>'