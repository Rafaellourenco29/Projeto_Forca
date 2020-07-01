'''import necessário para randomizar as palavras do array'''
import random

''' variáveis globais'''
palavras = ['desenvolvedor', 'programador', 'python', 'internet',] 
numeroPartidas = 0
partida = 1
ganhou = perdeu = 0

'''fluxo inicial do jogo, contém: while() para controle da quatidade de partidas, variáveis count - jogos ganhos e perdidos,'''
nomeJogador = input("Nome do jogador: ")
while partida == 1:

  '''variavel de controle'''

  numeroPartidas += 1 
  '''variavel para pegar elemento sorteado'''
  palavra = random.choice(palavras).strip()
  for x in range(100):
      print()
  digitadas = []
  acertos = []
  erros = 0
  while True:
      senha = ""
      for letra in palavra:
          senha += letra if letra in acertos else "."
      print(senha)
      if senha == palavra:
          print("{}, Parabéns!!! você acertou a palavra secreta!" .format(nomeJogador))
          ganhou += 1
          ''' se o jogador quiser jogar novamente. Do contrário, sai do jogo..'''
          partida = int(input("Quer jogar novamente? Sim(1) ou Não(2)"))
          break
      tentativa = input("\nDigite uma letra:").lower().strip()
      if tentativa in digitadas:
          print("Atenção, Você já tentou esta letra!")
          continue
      else:
          digitadas += tentativa
          if tentativa in palavra:
              acertos += tentativa
          else:
              erros += 1
              print("Você errou!")

      '''Criação do boneco '''

      print("X==:==\nX  :   ")
      print("X  O   " if erros >= 1 else "X")
      linha2 = ""
      if erros == 2:
          linha2 = "  |   "
      elif erros == 3:
          linha2 = " /|   "
      elif erros >= 4:
          linha2 = " /|\ "
      print("X%s" % linha2)
      linha3 = ""
      if erros == 5:
          linha3 += " /     "
      elif erros >= 6:
          linha3 += " / \ "
      print("X%s" % linha3)
      print("X\n===========")
      if erros == 6:
          print("{}, Que Pena!! Enforcado(a)" .format(nomeJogador))
          perdeu += 1
          partida = int(input(" Jogar novamente? Digite Sim(1) ou Não(2)"))
          break 
  print("\n Total de partida(as) jogada(as):{} " .format(numeroPartidas))
  print("\n Quantidade que você ganhou:{} partida(as)" .format(ganhou))
  print("\n Quantidade que você Perdeu:{} partida(as)".format(perdeu))








