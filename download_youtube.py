from pytube import YouTube

link = input('Digite o link do vídeo que deseja baixar: ')
pasta = input('Digite o diretório que deseja salvar o vídeo: ')
YouTube(link)
yt = YouTube(link)

# Detalhes do vídeo
print('Título ', yt.title)
print('Número de views ', yt.views)
print('Tamanho do vídeo: ', yt.length, 'segundo')
print('Avaliação do vídeo: ', yt.rating)

# Para uma melhor resolução
ys = yt.streams.get_highest_resolution()

# Download do vídeo 
print('Baixando...')
ys.download(pasta)
print('Download completo!')


