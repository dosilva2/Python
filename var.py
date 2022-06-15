import adivinhacao as ad
import random

total_tentativas = 0
chute = 0
numero_secreto = random.randrange(1,101)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto