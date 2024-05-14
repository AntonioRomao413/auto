#### Importa Biblioteca
from bcb import sgs 

#### Importa o Dados
dados_brutos = sgs.get(
    codes= { "IPCA": 433, "INPC": 188, "IGP-M": 189, "IGP-DI": 190, "IPC-Br": 191},
    start= "2000-01-01"
)


#### Tratar Dados
dados_tratados = dados_brutos.reset_index()

#### Salvar Dados
dados_tratados.to_csv(path_or_buf = "dados_tratados.csv", index= False)