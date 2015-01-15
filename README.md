Eventmanager (Server)
=====================

Diese Datei enthält im wesentlichen den Code, der mithilfe
eines Apache Webservers den Server für das Projekt "Eventmanager"
darstellt.

Setup des Servers
-----------------
Der Server besteht im wesentlichen aus einem Webserver, der mittels des
Python Web-Frameworks Flask, den in diesem Repository befindlichen Code
ausführt. Die Daten, die während der Beantwortung von Anfragen benötigt
werden, werden von einer MySQL-Datenbank abgerufen. Der Server der zu
Testzwecken aufgesetzt wurde, basiert hierbei auf einem Linux (Ubuntu)
Betriebssystem, welches innerhalb einer virtuellen Maschine betrieben wird.
Der Server der tatsälich von den Clients angesprochen wird
(http://eventmanager.pythonanywhere.com), wird allerdings
im Rechenzentrum des Anbieters Pythonanywhere gehostet.

Organisation des Source Code
----------------------------
Der Code des Servers teilt sich hauptsächlich in folgende Bereiche auf:
api.py, server.py, den einzelnen .py Dateien für die Datenbankobjekte
sowie einer Klasse, die einfachen Zugriff auf die Datenbank liefert. Das api.py
Skript dient hierbei hauptsächlich als Verbindungsstück zu Flask und
übernimmt als solches auch Aufgaben bzgl. des Parsing der URL-Parameter.
In der Datei server.py sind alle Funktionen implementiert, wie sie im
Dokument doc/API.txt spezifiziert wurden. Grosser Unterschied zu api.py
ist hierbei die Tatsache, dass hier keine Flask eigenen bzw.
HTTP(S)-Handling Funktionen mehr aufgerufen werden - dadurch kann im Falle eines
Falles schneller das Web-Framework gewechselt werden.
