import sys
import os
from Crypto.Hash import SHA256
from binascii import unhexlify
from binascii import hexlify

tam_bloco = 1024 #blocos de 1KB

#Video teste do hash
tam_video1 = os.path.getsize("/home/hugo/Área de Trabalho/SHA256-Video/video05.mp4")

#video que precisa calcular o hash
tam_video2 = os.path.getsize("/home/hugo/Área de Trabalho/SHA256-Video/video_03.mp4")

# Descobre o tamanho variável do último bloco dos dois videos.
tUlt_bloco_vid1 = tam_video1 % tam_bloco
tUlt_bloco_vid2 = tam_video2 % tam_bloco

#inicialização das variaveis que vao conter o hash h0 
bloco_hash_vid1 = ''
bloco_hash_vid2 = ''

#variavel que vai conter o tamanho do bloco
bloco_controle = 0

#abertura do arquivo
arq = open("/home/hugo/Área de Trabalho/SHA256-Video/video05.mp4",'rb')
 
#Leitura dos bytes do arquivo de trás para frente para conseguir calcular o hash h0

# flag_termino -> Variavel de controle que vai diminuindo conforme o tamanho do arquivo de video
flag_termino = tam_video1

while flag_termino > 0:
        
    if(flag_termino == tam_video1):
        bloco_controle = tUlt_bloco_vid1
    else:
        bloco_controle = tam_bloco 

# faz a leitura dos dados dos blocos e faz o calculo do hash até chegar o h0
    
    #vai até a posição no arquivo e lê aquele bloco conforme o tamanho. Ultimo bloco com tam variável
    arq.seek(flag_termino - bloco_controle)
    bloco_data = arq.read(tam_bloco)

    
    #Inicializa o objeto relacionado a biblioteca do pycrypto que tem os métodos necessários para calculo do SHA256
    obj_sha = SHA256.new()

    #Faz o update dos hashes das mensagens continuamente pedaço por pedaço dos dados
    obj_sha.update(bloco_data)

    #FAz o update do hash conforme percorre o arquivo 
    if(bloco_hash_vid1):
        obj_sha.update(bloco_hash_vid1)
    
    bloco_hash_vid1 = obj_sha.digest()
    
    #Percorre o arquivo
    flag_termino -= bloco_controle

# Printa H0
print(bytes.decode(hexlify(bloco_hash_vid1)))