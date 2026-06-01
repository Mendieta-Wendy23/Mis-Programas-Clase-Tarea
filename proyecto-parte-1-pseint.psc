Algoritmo SistemaVeterinaria
		
		Definir opcion Como Entero
		
		Mientras opcion <> 7 Hacer
			
			Escribir ""
			Escribir "===== SISTEMA DE VACUNACION Y CUIDADO DE MASCOTAS ====="
			Escribir "1. Registrar mascota"
			Escribir "2. Buscar mascota"
			Escribir "3. Aplicar vacuna"
			Escribir "4. Centros de vacunacion"
			Escribir "5. Ver descuentos"
			Escribir "6. Esterilizacion"
			Escribir "7. Salir"
			
			Leer opcion
			
			Segun opcion Hacer
				
				1:
					Definir nombre, especie, tamano, raza Como Cadena
					Definir enfermedad, dueno, telefono Como Cadena
					Definir direccion, ciudad Como Cadena
					Definir edad Como Entero
					Definir peso Como Real
					
					Escribir "Nombre:"
					Leer nombre
					
					Escribir "Especie (Perro/Gato):"
					Leer especie
					
					Escribir "Edad:"
					Leer edad
					
					Escribir "Tamaño:"
					Leer tamano
					
					Escribir "Peso:"
					Leer peso
					
					Escribir "Raza:"
					Leer raza
					
					Escribir "Enfermedad:"
					Leer enfermedad
					
					Escribir "Nombre del dueño:"
					Leer dueno
					
					Escribir "Telefono:"
					Leer telefono
					
					Escribir "Direccion:"
					Leer direccion
					
					Escribir "Ciudad:"
					Leer ciudad
					
					Escribir ""
					Escribir "Mascota registrada correctamente"
					
				2:
					Escribir "Buscar mascota"
					Escribir "Funcion disponible"
					
				3:
					Definir vacuna Como Cadena
					
					Escribir "Nombre de la mascota:"
					Leer nombre
					
					Escribir "Vacuna aplicada:"
					Leer vacuna
					
					Escribir "Vacuna registrada"
					
				4:
					Definir ciudadCentro Como Cadena
					
					Escribir "Ciudad:"
					Leer ciudadCentro
					
					Si ciudadCentro="Apizaco" Entonces
						Escribir "Veterinaria Apizaco Centro"
					SiNo
						Si ciudadCentro="Tlaxcala" Entonces
							Escribir "Patitas Felices"
						SiNo
							Escribir "No hay centros registrados"
						FinSi
					FinSi
					
				5:
					Escribir "20% descuento vacuna antirrabica"
					Escribir "Juguete gratis vacuna triple felina"
					Escribir "Baño gratis segunda vacuna"
					
				6:
					Definir nombreEster Como Cadena
					Definir edadEster Como Entero
					
					Escribir "Nombre de la mascota:"
					Leer nombreEster
					
					Escribir "Edad en meses:"
					Leer edadEster
					
					Si edadEster >= 6 Entonces
						Escribir "La mascota puede ser esterilizada"
					SiNo
						Escribir "Aun no cumple la edad recomendada"
					FinSi
					
				7:
					Escribir "Gracias por usar el sistema"
					
				De Otro Modo:
					Escribir "Opcion no valida"
					
			FinSegun
			
		FinMientras
		
FinAlgoritmo
