```markdown
# Szentiras_export

Ez a Python script bibliai verseket tölt le a szentiras.hu API-ról, és elmenti azokat egy szöveges fájlba. A lekérdezendő versek hivatkozásait a `references.json` fájl tartalmazza.

## Használat

1.  Telepítse a szükséges függőségeket:

```bash
pip install requests
```

2.  Hozzon létre egy `references.json` fájlt a projekt gyökerében, és töltse fel a lekérdezni kívánt bibliai hivatkozásokkal. A fájl formátuma a következő:

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

3. Futtassa a `szentiras_export.py` scriptet:

```bash
python szentiras_export.py
```

A script létrehoz egy `verse_export.txt` fájlt, amely tartalmazza a lekérdezett verseket, azok hivatkozásait és a fordítás nevét.

## Hibakezelés

A script tartalmaz hibakezelést a következő esetekre:

*   Hiányzó `references.json` fájl.
*   Érvénytelen JSON formátum a `references.json` fájlban.
*   Hálózati hibák a szentiras.hu API elérésekor.
*   Hibás formátumú válasz az API-tól.
*   Nem található vers a megadott hivatkozásra.

A hibákról szóló üzenetek a konzolra íródnak, és a `verse_export.txt` fájlban is jelennek meg.


## Észrevételek:

*lorem ipsum
