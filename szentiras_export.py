import requests
import re
import json
import os

# Direkt elérési út a references.json fájlhoz
REFERENCES_FILE_PATH = r"C:\Users\birom\Documents\Szentiras_export\references.json"

# Bibliai versek hivatkozásainak betöltése a JSON fájlból
def load_verse_references():
    try:
        if not os.path.exists(REFERENCES_FILE_PATH):
            print(f"HIBA: A {REFERENCES_FILE_PATH} fájl nem található.")
            return []

        with open(REFERENCES_FILE_PATH, 'r', encoding='utf-8') as file:
            references = json.load(file)
            if not isinstance(references, list):
                print(f"HIBA: A {REFERENCES_FILE_PATH} fájl tartalma nem lista formátumú.")
                return []

            if not references:
                print(f"FIGYELMEZTETÉS: A {REFERENCES_FILE_PATH} fájl nem tartalmaz hivatkozásokat.")

            return references

    except json.JSONDecodeError as e:
        print(f"HIBA: JSON dekódolási hiba a {REFERENCES_FILE_PATH} fájlban: {str(e)}")
    except Exception as e:
        print(f"HIBA: Ismeretlen hiba történt a {REFERENCES_FILE_PATH} fájl olvasásakor: {str(e)}")
        return []

def clean_html(text):
    text = re.sub('<br\s*/?>', '\n', text)
    text = re.sub('<[^>]+>', '', text)
    return text.strip()

def get_verse(reference, translation='SZIT'):
    url = f"https://szentiras.hu/api/idezet/{reference}/{translation}"
    print(f"Lekérés: {url}") #  URL kiírása a konzolra

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        verses = data['valasz']['versek']
        if not verses:
            print(f"HIBA: Nem található vers a(z) {reference} hivatkozásra.  Státuszkód: {response.status_code}")
            print(f"Válasz: {response.text}")  # Válasz kiírása hibakereséshez
            return None

        full_text = '\n'.join(clean_html(verse['szoveg']) for verse in verses)
        reference = verses[0]['hely']['szep']
        translation_info = data['valasz']['forditas']

        return {
            "text": full_text,
            "reference": reference,
            "translation": translation_info['nev']
        }

    except requests.RequestException as e:
        print(f"HIBA: Nem sikerült lekérni a verset ({reference}): {e}")
        return None
    except KeyError as e:
        print(f"HIBA: Hibás formátumú válasz a(z) {reference} hivatkozásra: {e}")
        print(f"Válasz: {response.text}") # Válasz kiírása hibakereséshez
        return None

def export_all_verses():
    verse_references = load_verse_references()
    if not verse_references:
        print("Nincsenek hivatkozások a references.json fájlban.")
        return

    with open("verse_export.txt", "w", encoding="utf-8") as file:
        for reference in verse_references:
            verse = get_verse(reference)
            if verse:
                file.write(f"{verse['text']}\n{verse['reference']} - {verse['translation']}\n\n")
            else:
                file.write(f"HIBA: Nem sikerült lekérni a következő hivatkozást: {reference}\n\n")

    print("Az összes idézet exportálása befejeződött a verse_export.txt fájlba.")

# Az összes idézet exportálása egyszeri futtatással
if __name__ == '__main__':
    export_all_verses()