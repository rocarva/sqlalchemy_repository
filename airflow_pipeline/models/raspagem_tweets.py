import sqlalchemy as sa 
from datetime import datetime
from models.model_base import ModelBase

class RaspagemTweets(ModelBase):
    __tablename__:str = 'raspagem_tweets'
    id: int = sa.Column(sa.BigInteger,primary_key =True , autoincrement=True)     
       
    nome:str = sa.Column(sa.String(100), unique=False, nullable=False)  
    texto:str = sa.Column(sa.String(280), unique=False, nullable=False)
    data_extracao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    def __repr__(self) -> str:
        return f'<Tweets  : {self.nome}>'