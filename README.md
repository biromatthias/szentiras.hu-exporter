# 📖 Szentiras_export ✨

Ez a Python script bibliai verseket tölt le a szentiras.hu API-ról, és szépen formázva elmenti azokat egy szöveges fájlba.  A lekérdezendő versek hivatkozásait a `references.json` fájl tartalmazza.


## 🚀 Használat

1. **Függőségek telepítése:**

    ```bash
    pip install requests
    ```

2. **Hivatkozások előkészítése:**

    Hozzon létre egy `references.json` fájlt a projekt gyökerében, és töltse fel a lekérdezni kívánt bibliai hivatkozásokkal.  A fájl formátuma a következő:

    ```json
    [
      "1Jn3,18",
      "1Jn4,7",
      "1Jn4,18",
      "1Jn4,19",
      "1Jn4,20"
      // ...
    ]
    ```

3. **Script futtatása:**

    ```bash
    python szentiras_export.py
    ```

    🎉 A script létrehoz egy `verse_export.txt` fájlt, amely tartalmazza a lekérdezett verseket, azok hivatkozásait és a fordítás nevét.



## ⚙️ Fordítás módosítása

A script alapértelmezésben a SZIT fordítást használja.  Ha másik fordítást szeretnél használni, módosítsd a `get_verse` függvényben a `translation` paraméter értékét:

```python
def get_verse(reference, translation='SZIT'): #  <- Itt módosíthatod a fordítást
    url = f"https://szentiras.hu/api/idezet/{reference}/{translation}"
    # ...
```

Valamint a `export_all_verses` függvényben a `get_verse` hívásánál is:

```python
def export_all_verses():
    #...
    verse = get_verse(reference, translation="KG") # <- és itt is
    #...
```

Például a Károli Gáspár fordításhoz használd a `KG` rövidítést.

## ❗❗❗ Fontos

Mivel a program a konkrét szentírási részt nyeri ki a szentiras.hu-ból, ezért vesszőhibák, idézőjelhibák és félbehagyott mondatok keletkezhetnek:

Például: Józsue könyve: [Józsue könyve: 1. fejezet](https://szentiras.hu/SZIT/J%C3%B3zs1) ➡️ [9-es rész](https://szentiras.hu/SZIT/J%C3%B3zs1,9)

Hát nem azt a parancsot adtam neked, `9` hogy légy...

Mivel az 1. fejezet `9` része itt kezdődik, ezért így fog kinézni:

_hogy légy erős és kitartó? Ne félj és ne aggódj tehát, mert az Úr, a te Istened veled lesz mindenütt, ahova csak mész.”_

## 🛡️ Hibakezelés

A script gondosan kezeli a lehetséges hibákat, mint például:

*   `references.json` fájl hiánya 🚫
*   Érvénytelen JSON formátum a `references.json` fájlban  ❌
*   Hálózati hibák  🌐
*   Hibás API válaszok ❗
*   Nem található vers  ❓

A hibákról részletes üzenetek jelennek meg a konzolon, és a `verse_export.txt` fájlban is rögzítésre kerülnek.


## ✨ További fejlesztési lehetőségek

*   **Parancssori argumentumok:**  A fordítás és a kimeneti fájl nevének megadása. 🗣️
*   **Részletesebb naplózás:** Még több információ a script működéséről. 📝
*   **Több fordítás támogatása:**  Egyszerre több fordítás letöltése. 🌍
*   **Progress bar:**  A letöltés folyamatának vizualizálása. ⏳


##  🙏  Közreműködés

Szeretettel várunk minden hozzájárulást!  Küldj pull requestet, ha van ötleted a fejlesztésre! ❤️
