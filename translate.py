from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
import os
import re

# Function to translate text using deep-translator
def translate_text_google(text, target_language):
    try:
        # Translate the text
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        print(f"Error translating text '{text}' to {target_language}: {e}")
        return None  # Return None in case of error

# Function to translate HTML content
def translate_html_content(input_file, output_dir, languages):
    # Read the original HTML file
    with open(input_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Loop through each language and create a translated HTML file
    for lang in languages:
        print(f"Translating to {lang}...")
        translated_soup = BeautifulSoup(str(soup), "html.parser")  # Create a fresh copy for each language

        # Regular expression to match template tags like {% if message %}
        template_tag_re = re.compile(r'({%.*?%})')

        # Find all text nodes and translate them
        for element in translated_soup.find_all(string=True):
            # Skip non-visible elements (script, style, meta, etc.) and template tags
            if element.parent.name not in ["script", "style", "meta", "link"] and element.strip():
                original_text = element.strip()

                # Skip content that matches template tags like {% if message %}
                if template_tag_re.search(original_text):
                    continue

                # Translate the text content using deep-translator
                translated_text = translate_text_google(original_text, lang)

                # Debugging step: Print the original and translated text
                if translated_text is None:
                    print(f"Warning: Translation failed for text: '{original_text}'")
                    continue  # Skip replacing if translation failed

                print(f"Original: {original_text}")
                print(f"Translated: {translated_text}")

                # Replace the text in the HTML structure
                element.replace_with(translated_text)

        # Save the translated HTML to a new file
        output_file = os.path.join(output_dir, f"index_{lang}.html")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translated_soup.prettify())
        print(f"Translated HTML saved for language '{lang}' at {output_file}")

# Usagessss
input_html_file = r"C:\Users\zmunga\Downloads\fbdownload\templates\privacypolicy.html"  # Your main English HTML file
output_directory = r"C:\Users\zmunga\Downloads\fbdownload\templates\privacypolicy"  # Directory to save the translated files
os.makedirs(output_directory, exist_ok=True)

# List of language codes for 20 different languages
language_codes = [
    "es", "fr", "de", "zh-cn", "hi", "ar", "ru", "ja", "ko", "it",
    "pt", "tr", "vi", "pl", "nl", "el", "th", "he", "sv", "uk"
]

# Translate the HTML content into different languages
translate_html_content(input_html_file, output_directory, language_codes)
