from pytube import YouTube
import moviepy.editor as mp
import re
import os

pasta = input('Digite o diretorio que esta o video para conversão: ')
arquivo = input('Digite o nome do arquivo com .mp4 no final:  ')

print('Convertendo arquivo')
for file in os.listdir(pasta):
    if re.search('mp4', file):
        if file == arquivo:
            mp4_pasta = os.path.join(pasta, file)
            mp3_pasta = os.path.join(pasta, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_pasta)
            new_file.write_audiofile(mp3_pasta)
            os.remove(mp4_pasta)
print('Sucesso')   

