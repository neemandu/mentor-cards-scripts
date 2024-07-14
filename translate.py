import json
import os
import logging
from deep_translator import GoogleTranslator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the path to the folder containing the JSON files
json_folder_path = 'C:\\Users\\neema\\Downloads\\jsons'

# List of target languages
target_languages = {
    'es': 'spanish',
    'ar': 'arabic',
    'en': 'english',
    'ru': 'russian'
}

# Function to check if a string is likely a URL
def is_url(text):
    return text.startswith('http://') or text.startswith('https://')

# Function to recursively translate text in the JSON data
def translate_json(data, translator, lang_code):
    if isinstance(data, dict):
        translated_dict = {}
        for key, value in data.items():
            if key == "language":
                translated_dict[key] = lang_code
            elif key == "__typename":
                translated_dict[key] = value
            else:
                translated_dict[key] = translate_json(value, translator, lang_code)
        return translated_dict
    elif isinstance(data, list):
        return [translate_json(item, translator, lang_code) for item in data]
    elif isinstance(data, str):
        if not is_url(data):  # Only process non-URL strings
            try:
                translated_text = translator.translate(data)
                return translated_text
            except Exception as e:
                # If translation fails, return the original text
                logging.error(f"Error translating text: {data}. Exception: {e}")
                return data
        return data
    else:
        return data

# Iterate over all JSON files in the specified folder
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(json_folder_path, filename)
        logging.info(f"Processing file: {file_path}")
        
        try:
            # Load the original JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            continue
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON file: {file_path}")
            continue

        # Translate the JSON data to each target language
        for lang_code, lang_name in target_languages.items():
            logging.info(f"Translating to {lang_name} ({lang_code})")
            translator = GoogleTranslator(source='auto', target=lang_code)
            try:
                translated_data = translate_json(data, translator, lang_code)
            except Exception as e:
                logging.error(f"Error during translation to {lang_name}: {e}")
                continue

            # Save the translated JSON data to a new file
            translated_file_path = os.path.join(json_folder_path, f'translated_{filename}_{lang_code}.json')
            try:
                with open(translated_file_path, 'w', encoding='utf-8') as file:
                    json.dump(translated_data, file, ensure_ascii=False, indent=2)
                logging.info(f"Translated file saved to {translated_file_path}")
            except Exception as e:
                logging.error(f"Error saving the translated file for {lang_name}: {e}")
