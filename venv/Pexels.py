import Claves
import requests
import shutil

def descargar_video(api_key, query, orientation='portrait', size='hd'):
    url = f'https://api.pexels.com/v1/videos/search?query={query}&orientation={orientation}&per_page=1'

    headers = {
        'Authorization': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        if json_response['total_results'] > 0:
            video_url = json_response['videos'][0]['video_files'][0]['link']
            response = requests.get(video_url, stream=True)
            if response.status_code == 200:
                with open('video_descargado.mp4', 'wb') as file:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, file)
                print("Video descargado con éxito.")
            else:
                print("Error al descargar el video.")
        else:
            print("No se encontraron resultados.")
    else:
        print("Error al realizar la búsqueda.")



