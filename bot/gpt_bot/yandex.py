import requests


class YandexGPT:
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    API_TOKEN = ''
    CATALOG = ''

    def get_answer(self, text, system_text='отвечай как обычно'):

        payload = {
                "modelUri": f"gpt://{self.CATALOG}/yandexgpt",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.4,
                    "maxTokens": 100,
                    "reasoningOptions": {
                        "mode": "DISABLED"
                    }
                },
                "messages": [
                    {
                        "role": "user",
                        "text": text
                    },
                    {
                        "role": "system",
                        "text": system_text
                    }
                ]
            }


        headers = {'Authorization': f"Api-Key {self.API_TOKEN}"}
        res = requests.post(self.url, json=payload, headers=headers)
        res = res.json()
        text = res['result']['alternatives'][0]['message']['text']
        return text
