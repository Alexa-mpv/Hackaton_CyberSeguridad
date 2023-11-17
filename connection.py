import openai
import requests


def conexion(prompt, ai):
    """Función que se encarga de conectar con la API de la IA seleccionada y regresa la respuesta de la IA."""

    if ai == "chatgpt":
        openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        print(completion)
    elif ai == "copilot":
        url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
        headers = {
            "Ocp-Apim-Subscription-Key": "api_key",
        }
        params = {
            "prompt": prompt,
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        print(data)
    else:
        print("No se ha seleccionado ninguna IA")
