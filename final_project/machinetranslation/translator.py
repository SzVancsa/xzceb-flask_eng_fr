''' Translates via Watson between English & French '''

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('E8zpRr2n7ayHhGg5bG7p2rqZArPDLrnEVlo7Nir0EyJU')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):

    ''' English to French translation '''

    language_translator.set_service_url(
        'https://api.eu-de.language-translator.watson.cloud.ibm.com')
    french_text = language_translator.translate(
        text = english_text ,
        model_id = 'en-fr').get_result()
    french = french_text['translations']
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french[0]['translation']


def french_to_english(french_text):

    """ French to English translation """

    language_translator.set_service_url(
        'https://api.eu-de.language-translator.watson.cloud.ibm.com')

    english_text = language_translator.translate(
        text = french_text ,
        model_id = 'fr-en').get_result()
    english = english_text['translations']
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))

    return english[0]['translation']
