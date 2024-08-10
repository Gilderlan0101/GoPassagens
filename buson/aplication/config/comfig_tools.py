import os

def key_projecto():
    # Caminho para o arquivo da secret_key
    key_file_path = '/home/lan/buson/aplication/config/secret_key.txt'
    
    # Leia a chave do arquivo
    with open(key_file_path, 'r') as key_file:
        return key_file.read().strip()
