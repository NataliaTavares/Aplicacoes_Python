from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input('Digite o link do vídeo que você deseja baixar o mp3 : ')
pasta = input('Digite o diretorio que você deseja salvar o mp3: ')
yt = YouTube(link)

print('Baixando')
ys = yt.streams.filter(only_audio=True).first().download(pasta)
print('Download completo')

print('Convertendo arquivo')
for file in os.listdir(pasta):
    if re.search('mp4', file):
        mp4_pasta = os.path.join(pasta, file)
        mp3_pasta = os.path.join(pasta, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_pasta)
        new_file.write_audiofile(mp3_pasta)
        os.remove(mp4_pasta)
print('Sucesso')    

