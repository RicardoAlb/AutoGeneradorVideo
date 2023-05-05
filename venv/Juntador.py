from moviepy.editor import *
import main
import edit
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import Pexels
import Claves
import Subtitulos

def generar_video(video_path, audio_path, duracion_video, nombre_video):
    # Cargar la imagen
    imagen = VideoFileClip(video_path)

    # Cargar el audio
    audio = AudioFileClip(audio_path)

    # Ajustar la duración del audio al tiempo deseado del video
    audio = audio.set_duration(duracion_video)

    # Combinar la imagen y el audio en un video
    video = imagen.set_audio(audio)

    # Definir los parámetros del video resultante
    fps = 30
    video = video.set_duration(duracion_video).set_fps(fps)

    # Guardar el video resultante
    video.write_videofile(nombre_video, codec='libx264', audio_codec="aac", fps=fps)

Pexels.descargar_video(Claves.api_key_pexels, query="libertad financiera")
#main.generate_image("misterious, scary and dark demon, H.P. Lovecraf style")

texto="Imagina una vida llena de abundancia y prosperidad. El dinero fluye hacia ti en cantidades ilimitadas. Pero recuerda, la motivación es la clave para alcanzar el éxito financiero. Sin esfuerzo y dedicación, el dinero se escapa de nuestras manos."
edit.convertir_texto_audio(texto, "salida.mp3")

# Ejemplo de uso
video_path = r"D:\autoYoutube\venv\video_descargado.mp4"
audio_path = r"D:\autoYoutube\venv\salida_modificado.mp3"
duracion_video = 10  # Duración en segundos
nombre_video = 'video_generado.mp4'

generar_video(video_path, audio_path, duracion_video, nombre_video)
Subtitulos.agregar_subtitulos(r"D:\autoYoutube\venv\video_generado.mp4", r"D:\autoYoutube\venv\video_generado.mp4", texto, duracion_video)
