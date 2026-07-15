# Business_Case: Nachhaltigkeit in Krisenzeiten
Dieses Projekt dient zur Veranschaulichung meiner Fähigkeiten als Data Scientist/Analytics Engineer außerhalb wissenschaftlicher Studien. Hier übe ich außerdem Programmiersprachen mit denen ich sonst wenig/nicht in Berührung komme. 

Das Projekt soll folgende Frage beantworten: 

**Welchen monetären Aufpreis sind Kunden unter Normalbedingungen vs. in Krisen bereit zu zahlen, um ein Produkt mit dem Merkmal 'Nachhaltig' statt 'Konventionell' zu erhalten?**

Es ist naheliegend das Kunden einen Unterschied machen was sie bereit sind mehr zu zahlen abhängig von Umweltfaktoren wie wirtschaftliche oder politische Krisen. Unternehmen könnten einen Vorteil darausziehen ihre Preise für nachhaltige oder konventionelle Produkte also an solche Faktoren anzupassen. 

Hypothese: In Krisenzeiten zahlen die Menschen nur für nachhaltige Produkte wenn der Aufpreis gering(er) ausfällt. 

## Data
Ich verwende Open Source Data mit simulierten Daten um die Frage zu beantworten und dabei möglichst breit mein Skillset zu zeigen. 

Daten zu Verkauf und Preisen von Produkten extrahiere ich via API von kaggle.com
- https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning
- Zu diesem Datensatz werden simulierte Kategorien zugespielt die zeigen welche Produkte 'nachhaltig' oder 'konventionell' sind. 
- Krisen vs. Normalbedingungen wird anhand von Globalen Nachrichten gemessen. Hierzu wird der GDELT 2.0 Our global world in realtime verwendet (https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/)

## Inhalt
- `data\raw`
- `scripts\data_collection.`
- `scripts\data_preparation.`
- `visuals`
- `presentation`

## Setup 

