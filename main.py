from api_versao_1.app.api.acionador_api import AcionadoresAPI
from config_database import IDENTIFIER_IQ, PASSWORD_IQ

class ConnectAPI:
    def __init__(self, identifier, password):
        self.identifier = identifier
        self.password = password
    
    def connect_api(self):
        conn = AcionadoresAPI.autenticacao_iqoption_api(
            username=self.identifier,
            password=self.password
        )
        if conn[0] == True:
            AcionadoresAPI.conectar_wss(
                ssid=conn[1]["ssid"])
        else:
            print("Erro de conexão com a IQ_Option. Credenciais incorretas.")

def startAPI():
    # identier = str(input("Digite o seu usuário da IQ_Option: "))
    # password = str(input("Digite sua senha da IQ_Option: "))
    ConnectAPI(identifier=IDENTIFIER_IQ, password=PASSWORD_IQ).connect_api()
startAPI()