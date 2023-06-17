recargas = [[],[],[],[]]
MenuPrincipal = ["1.- Recarga","2.- Reporte de recargas", "3.- Salir"]
Companias = ["1.- Telcel", "2.- Movistar", "3.- Unefon", "4.- AT&T"]
Montos = [10, 20, 50, 100, 150, 200, 500]

def sum(vector)
	res=0
	if vector==[]
		return 0
	else
		vector.each { |i| res+=i}
		return res
	end
end

def mostrar_menu(menus)
  for opcion in menus
    puts (opcion)
  end
end


def validar(mensaje)
  bandera = true
  while bandera
    begin
      valor = gets.to_i
      bandera = false
    rescue
      puts mensaje
    end
    return valor
  end
end


def registrar_recarga(recargas)
  print "\nCompañias\n"
  mostrar_menu(Companias)
  compania=validar("\nElija una compañia (1 a 4): ")
  if compania > 0 and compania < 5
    print "\nMontos\n"
    mostrar_menu(Montos)
    monto=validar("\nIndique el monto de la recarga: ")
    if monto = 10 or monto = 20 or monto = 50 or monto = 100 or monto = 150 or monto = 200 or monto = 500
      recargas[compania - 1].push(monto)
      puts "Recarga registrada"
    else
      puts "\nEl monto ingresado no esta en la lista"
    end
  else
    puts "\nOpción no válida"
  end
end

def mostrar_recargas(companias, recargas)
	puts "\nRecargas realizadas"
	for compania in (0..3)
		puts "\n#{companias[compania]}"
		for recarga in (0..recargas[compania].length-1)
			puts recargas[compania][recarga]
		end
		puts "Total #{sum(recargas[compania])}"
	end
end

eleccion = 1
while eleccion != 3
  system "cls"
  puts "Centro de recargas Ultra"
  mostrar_menu(MenuPrincipal)
  eleccion=validar("\nElija una opción (1 a 3): ")
  system"cls"
  if eleccion == 1
    registrar_recarga(recargas)
  elsif eleccion == 2
    mostrar_recargas(Companias, recargas)
  elsif eleccion == 3
    puts "\nHasta luego..."
  else
  puts "Elija una entrada válida (1 a 3)"
  end
  puts"\nPresione ENTER para continuar"
	gets
end
