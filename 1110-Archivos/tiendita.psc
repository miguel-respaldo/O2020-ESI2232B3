SubAlgoritmo opcion <- menu ()
	Definir opcion Como Entero;
	Escribir "Menu de productos";
	Escribir "";
	Escribir "1. Imprimir productos";
	Escribir "2. Comparar algun producto";
	Escribir "3. Surtir producto";
	Escribir "4. Agregar producto";
	Escribir "5. Quitar  producto";
	Escribir "";
	Escribir "6. Salir";
	Escribir "";
	Escribir "Opción: ";
	Leer opcion;	
FinSubAlgoritmo

SubAlgoritmo de_python <- funcion_python (nombre_funcion)
	Definir de_python Como Caracter;
	de_python <- nombre_funcion;
FinSubAlgoritmo

SubAlgoritmo  abrir ()
	Definir archivo Como Caracter;
	Definir lector Como Caracter;
	archivo <- funcion_python("open");
	lector <- funcion_python("csv.reader");
FinSubAlgoritmo

Algoritmo tiendita
	Definir opcion Como Entero;
	
	opcion <- 0;
	abrir();
	
	Mientras  opcion <> 6 Hacer
		opcion <- menu();
		Segun opcion Hacer
			1:
				Escribir "imprimir productos";
			2:
				Escribir "comparar";
			3:
				Escribir "surtir";
			4:
				Escribir "agregar";
			5:
				Escribir "quitar";
			De Otro Modo:
				Escribir "Opción Invalida";
				Escribir "";
		FinSegun
	FinMientras
	
FinAlgoritmo
