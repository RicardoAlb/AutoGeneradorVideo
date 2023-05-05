from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.editor import *
import moviepy.config

moviepy.config.IMAGEMAGICK_BINARY = r"D:\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

def agregar_subtitulos(video_input, video_output, texto_subtitulos, duracion_total):
    video = VideoFileClip(video_input)
    video_clips = [video]

    # Dividir el texto en subtítulos utilizando el carácter de nueva línea como separador
    subtitulos = texto_subtitulos.split('\n')

    # Calcular la duración de cada subtítulo en función de la duración total del video
    num_subtitulos = len(subtitulos)
    duracion_subtitulo = duracion_total / num_subtitulos
    duraciones = [(i * duracion_subtitulo, (i + 1) * duracion_subtitulo) for i in range(num_subtitulos)]

    for i, (subtitulo, duracion) in enumerate(zip(subtitulos, duraciones)):
        texto = TextClip(subtitulo, fontsize=24, color='white', bg_color='black', size=(video.size[0], 40))
        texto = texto.set_position(("center", "bottom")).set_start(duracion[0]).set_end(duracion[1])
        video_clips.append(texto)

    video_final = CompositeVideoClip(video_clips)
    video_final.write_videofile(video_output, codec='libx264', audio_codec="aac")
