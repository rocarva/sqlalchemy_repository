import sqlalchemy as sa 
from datetime import datetime
from models.model_base import ModelBase

class Vendas(ModelBase):
    __tablename__:str = 'vendas'
    id: int = sa.Column(sa.BigInteger,primary_key =True , autoincrement=False )    
    marca:str = sa.Column(sa.String(100), unique=False, nullable=False)  
    id_linha: int = sa.Column(sa.Integer, unique= False, nullable = False)
    linha:str = sa.Column(sa.String(100), unique=False, nullable=False)  
    data_venda: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    qtd_venda: int = sa.Column(sa.Integer, unique= False, nullable = False)
    
    def __repr__(self) -> str:
        return f'<Vendas : {self.nome}>'