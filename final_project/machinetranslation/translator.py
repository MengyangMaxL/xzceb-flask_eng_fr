"""This module allows you:

translate English to French and French to English by using Waston Translator Services.
Apikey and url are obtained from Waston API.
Please use test.py to run below code."""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    """This function is used to translate English to French"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url(url)
    french_temp=language_translator.translate(text=englishText,model_id='en-fr').get_result()

    def get_all_values(french_temp):
        """This function is used to extract the translated words from dictionary"""
        if isinstance(french_temp, dict):
            for vector_new in french_temp.values():
                yield from get_all_values(vector_new)
        elif isinstance(french_temp, list):
            for vector_new in french_temp:
                yield from get_all_values(vector_new)
        else:
            yield french_temp
    frenchText=(list(get_all_values(french_temp))[0])
    return frenchText

def frenchToEnglish(frenchText):
    """This function is used to translate French to English"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url(url)
    english_temp=language_translator.translate(text=frenchText,model_id='fr-en').get_result()

    def get_all_values(english_temp):
        """This function is used to extract the translated words from dictionary"""
        if isinstance(english_temp, dict):
            for vector_new in english_temp.values():
                yield from get_all_values(vector_new)
        elif isinstance(english_temp, list):
            for vector_new in english_temp:
                yield from get_all_values(vector_new)
        else:
            yield english_temp
    englishText=(list(get_all_values(english_temp))[0])
    return englishText
