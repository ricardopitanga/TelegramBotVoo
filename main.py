import requests
import time

#Ler as mensagens que estão chegando no boot

while true:

token = ´1013804190:AAGZK5CCIwFackMpWbhEF3cML3YiSGyy9M´ 
url_base = f´https://api.telegram.org/bot{token}/getUpdates´
resultado = requests.get(url_base) 
print(resulta.json())
time.sleep(10)  