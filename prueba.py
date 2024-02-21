import requests
from bs4 import BeautifulSoup

url = "https://api.allorigins.win/raw?url=https://canales.online/agenda/"

def scrape_and_modify():
    try:
        # Realizar la solicitud GET a la URL
        response = requests.get(url)
        response.encoding = 'utf-8'  # Establecer la codificación de caracteres

        # Obtener el contenido HTML de la respuesta
        html_content = response.text

        # Crear un objeto BeautifulSoup para manipular el HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Modificar el título de la página
        new_title = "Agenda del día - A puro fútbol"
        soup.title.string = new_title

        # Cambiar el tamaño y la tipografía del texto
        style_tag = soup.new_tag('style')
        style_tag.string = "body { font-size: 15px; font-family: Arial, sans-serif; }"
        soup.head.append(style_tag)

        # Obtener el HTML modificado
        modified_html = str(soup)

        # Guardar el contenido HTML modificado en un archivo HTML llamado "agenda_modificado.html"
        with open(r"C:\Users\dblit\OneDrive\Escritorio\TODO CRYPTO\plantillas\Apurofutbol\bot scrappeo\agenda_modificado.html", 'w', encoding='utf-8') as file:
            file.write(modified_html)

        print("El scraping se ha completado y el contenido modificado se ha guardado en el archivo 'agenda_modificado.html'.")

    except Exception as e:
        print("Ha ocurrido un error durante el scraping y modificación del HTML:")
        print(e)

# Ejecutar el scraping, modificar el contenido y guardar en un archivo HTML
scrape_and_modify()
