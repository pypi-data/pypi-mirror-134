#! /usr/bin/env python

import requests as req

class pylingva:
    
    def __init__(self):
        url = "https://lingva.ml"
        try:
            check_url = req.get(url)
            check_url.raise_for_status()
            self.url = url + "/api/v1/"
        except req.exceptions.RequestException as er:
            print(er)
            exit()
        except req.exceptions.ConnectionError as er:
            print(er)
            exit()
        except req.exceptions.Timeout as er:
            print(er)
            exit()

    def languages(self):
        url = self.url + "languages"
        all_languages = req.get(url)
        all_languages = all_languages.json()
        lang = {}
        for x in range(0, len(all_languages['languages'])):
            list_code = all_languages['languages'][x]['code']
            list_name = all_languages['languages'][x]['name']
            lang.update({list_name: list_code})
        return lang

    def translate(self, source, target, text):
        url = f"{self.url}/{source}/{target}/{text}"
        url = url.replace("?", "%3F")
        r = req.get(url)
        r = r.json()
        result = r['translation']
        return result
