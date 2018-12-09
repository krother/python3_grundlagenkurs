
# Graphen abschreiten

* implementiere den **ungerichteten, zyklischen Graphen** auf [StackOverflow](https://stackoverflow.com/questions/23924010/find-cheapest-cycle-in-an-undirected-weighted-graph).
* schreibe eine Funktion, die den Graphen vollständig abschreitet und jeden Knowten genau einmal ausgibt.

## Hinweise

Du kannst ähnlich wie bei der *Baumsuche* vorgehen:

* erstelle eine Liste der zu besuchenden Knoten
* erstelle eine Liste mit bereits besuchten Knoten
* besuche einen Knoten und füge seine Nachbarn der Liste zu besuchender Knoten hinzu
* experimentiere, was sich an der Reihenfolge der Ausgabe ändert, wenn Du die Liste als Stack oder als Queue implementierst
