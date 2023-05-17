"""
translator.py

This module provides functions for translating text using IBM Watson Language Translator service.
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):

    """
    Description:
        Translates English text to French.

    Args:
        englishText (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    
    if english_text is None:
        return None

    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):

    """
     Description:
        Translates French text to English.

    Args:
        frenchText (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """

    if french_text is None:
        return None

    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
