import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

# faz requezição e armazena em variável
resposta = requests.get(url)

# transforma em json
data = resposta.json()

# Função para escolher palavra aleatória
def escolher_palavra():
  valor_secreto = random.choice(data)
  palavra_secreta = valor_secreto['palavra']
  dica_secreta = valor_secreto['dica']
  return palavra_secreta, dica_secreta

# Função para verificar a palavra
def verificar_palavra(palavra_secreta, tentativa):
  if palavra_secreta == tentativa.lower():
    return True
  else:
    return False

# Função para iniciar o jogo
def jogar():
  palavra_secreta, dica_secreta = escolher_palavra()

  print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
  print(f"Dica: {dica_secreta}")

  tentativas_restantes = 6
  while tentativas_restantes > 0:
    tentativa = input("Digite seu palpite: ")

    if verificar_palavra(palavra_secreta, tentativa):
      print("Parabéns! Você acertou a palavra!")
      break
    else:
      tentativas_restantes -= 1
      print(f"Errado! Você ainda tem {tentativas_restantes} tentativas restantes.")

  if tentativas_restantes == 0:
    print("Você perdeu! A palavra secreta era:", palavra_secreta)

# Iniciar o jogo
jogar()
