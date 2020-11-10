SubAlgoritmo comprar ()
	Definir lector Como Entero;
	Definir producto Como Caracter;
	Definir producto_num Como Entero;
	funcion_python2("next(lector)");
	Para lector <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir lector,".- producto";
	FinPara
	funcion_python2("archivo.seek(0)");
	Escribir "¿Cual producto quieres comprar?:";
	Leer producto;
	
	Si producto = "numero" Entonces
		producto_num <- 1;
		Si producto_num < 1 | producto_num > 6 Entonces
			Escribir "El producto no existe";
			Escribir "";
			funcion_python2("return");
		FinSi
	FinSi
	
	Si producto = "no en lista" Entonces
		Escribir "El producto no existe";
		Escribir "";
		funcion_python2("return");
	FinSi
	
	Escribir "Cantidad de producto";
	Leer producto_num;
	
	Si producto_num < 1 Entonces
		Escribir "La cantidad es invalida";
		Escribir "";
		funcion_python2("return");
	FinSi
	
	funcion_python2("Crear temporal");
	Para lector <- 1 Hasta 5 Con Paso 1 Hacer
		Si lector = 1 Entonces
			Si producto_num > 5 Entonces
				Escribir "No hay suficiente producto";
			SiNo
				producto_num <- 3;
			FinSi
			funcion_python2("writerow");
		SiNo
			funcion_python2("writerow");
		FinSi
	FinPara
	funcion_python2("close");
	funcion_python2("remove");
	funcion_python2("rename");
	abrir();
FinSubAlgoritmo

SubAlgoritmo imprimir_productos ()
	Definir lector Como Entero;
	Escribir "Producto       Cantidad     Precio";
	Escribir "-----------------------------------";
	funcion_python2("next(lector)");
	Para lector <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir "producto",lector,"  cantidad",lector,"   precio",lector;
	FinPara
	funcion_python2("archivo.seek(0)");
FinSubAlgoritmo

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

SubAlgoritmo funcion_python2 (nombre_funcion)
	
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
				imprimir_productos();
			2:
				comprar();
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
