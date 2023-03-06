import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('E8zpRr2n7ayHhGg5bG7p2rqZArPDLrnEVlo7Nir0EyJU')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def englishToFrench(englishText):

    language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

    frenchtext = language_translator.translate(
        text = englishText ,
        model_id = 'en-fr').get_result()
    print(json.dumps(frenchtext, indent=2, ensure_ascii=False))

    return frenchtext


def frenchToEnglish(frenchText):

    language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

    englishText = language_translator.translate(
        text = frenchText ,
        model_id = 'en-fr').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))

    return englishText