import sqlalchemy as sa 
from datetime import datetime
from models.model_base import ModelBase

class VendasMarcaLinha(ModelBase):
    __tablename__:str = 'vendas_marca_linha'
    id: int = sa.Column(sa.BigInteger,primary_key=True, autoincrement=True) 
    marca:str = sa.Column(sa.String(100), unique=False, nullable=False)
    linha:str = sa.Column(sa.String(100), unique=False, nullable=False)     
    venda: int = sa.Column(sa.Integer, unique= False, nullable = False)      
    data_extracao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    def __repr__(self) -> str:
        return f'<Vendas Linha : {self.venda}>'