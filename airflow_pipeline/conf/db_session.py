import sqlalchemy as sa 

from sqlalchemy.orm import sessionmaker , Session

from pathlib import Path # Usado no SQLite

from typing import Optional

from sqlalchemy.future.engine import Engine 

from models.model_base import ModelBase

__engine: Optional[Engine] = None

# conexao 
user = "postgres"
password = "changeme"


def create_engine(sqlline : bool = False) -> Engine:
    """_summary_

    Args:
        sqlline (bool, optional): _description_. Defaults to False.

    Returns:
        Engine: _description_ Funcao para criar o banco de dados 
    """
    global __engine 
    
    if __engine:
        return
    
    if sqlline:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url = conn_str, echo=False, connect_args={"check_same_thread":False})
    
    else:
        conn_str = f"postgresql://{user}:{password}@localhost:5432/loja"
        __engine = sa.create_engine(url=conn_str , echo=False)
    
    return __engine

def create_sessio() -> Session:
    """
        Função para criar sessão de conexao ao banco de dados 
        
    """
    global __engine
   
    if not __engine:
        create_engine() #caso queria utilizar sqlite colcoar = True
        
    __session = sessionmaker(__engine, expire_on_commit=False, class_= Session)
    
    session: Session = __session()
    
    return session

def create_tables():
    
    global __engine
    
    if not __engine:
        create_engine()
    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
    