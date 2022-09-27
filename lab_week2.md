# Todo list & deadlines Labo - Week 2

In deze app vinden we de volgende functionaliteit terug:

1. De gebruiker wordt gevraagd om zijn item in te voeren.
2. Hierna wordt er gevraagd naar de deadline.
3. Dankzij het gebruik van een while-loop krijgen we de optie om
   nogmaals een item en deadline toe te voegen.
4. Als men hier de letter 'n' invult, zal de loop stoppen en
   krijgen we een lijst met dictionaries te zien dat de ingevoerde
   items bevat.

### Definition - **main**.py : main

- Keuzemenu (1. Item toevoegen, 2. Item verwijderen, 3. Quit, X. main()).
- Loopt elke keer terug naar de main, behalve bij quit.

### Definition - todo.py : MakeTodoList

- User input: item_name, item_deadline, loopaction.
- Maakt lijst aan.
- Maakt Dictionaries aan.
- Print Todo lijst af.

### Definition - todo.py : EraseItem

- User input: removeInput.
- Lijst item pop adhv gegeven index input.
- Print Todo lijst af.
