SNAKE
Author: Konrad Ceglarski

Zalecane jest używanie Windowsa 10, gdyż pod ten system aplikacja była pisana.
Prosta, ale kultowa gra odtworzona przeze mnie przy użyciu języka Python 3 (3.6.8+) oraz modułu pygame (1.9.6+).
Program odpala się poprzez start.bat lub main.py. Program można także odpalić przez konsolę podając nazwę - main.py.
Dzięki takiemu uruchomieniu mamy możliwość na customizację gry, gdyż przyjmuje ona 4 kolejne argumenty:
Wymiar planszy		(10 - 30,			default: 25)
Skalę, czyli rozmiar pól	(20 - 40, 			default: 25)
Ilość klatek na sekundę	(niesprecyzowano zakresu, 	default: 15)
Bariery			(true lub false,		default: false)

Polega ona na zjadaniu jabłek, które zwiększają długość węża.
Sterowanie:
	WASD lub STRZAŁKI	- Ustawianie kierunku poruszania się węża
	SPACJA			- Pauza
	ESCAPE			- Wyjscie z aplikacji
	R			- Restart po przegranej
