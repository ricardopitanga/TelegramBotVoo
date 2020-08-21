import requests
import time
import json

class TelegramBot:
    def _init_(self):
        token = "1013804190:AAGZK5CCIwFackMpWbhEF3cML3YiSGyy9MY"
        self.url_base = f'https://api.telegram.org/bot{token}/'  
    # Iniciar o bot
    def Iniciar(self):
        update_id = None
        while True:
            atualiacao = self.obter_mensagens(update_id)
            mensagens = atualiacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem ['update_id']
                    chat_id = mensagem ['message']['from']['id']
                    # Criar a resposta
                    resposta = self.criar_resposta()
                    # Responder a pessoa
                    self.responder(resposta,chat_id)

    # Obter mensagens
    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=50'
        if update_id: 
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao) 
        return json.loads(resultado.content)        
    # Criar uma resposta
    def criar_resposta(self):
        return 'Olá Bem vindo!'
    # Responder
    def responder (self,resposta,chat_id):
        # enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()