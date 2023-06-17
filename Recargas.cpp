#include<iostream>
#include<locale.h>
#include<string>//Permite manejar mrtodos referidos al string
#include<cstdlib>//Permite hacer conversion de cadena a entero (atoi)
using namespace std;

//ARREGLOS
int recargas[4][100];//MATRIZ
string Companias[4]={"1.- Telcel", "2.- Movistar", "3.- Unefon", "4.- AT&T"};
string MenuPrincipal[3]={"1.- Recarga","2.- Reporte de recargas", "3.- Salir"};
int Montos[]={10, 20, 50, 100, 150, 200, 500};
int cantidadRecargas [4] = {0,0,0,0};

void mostrar_menu(string arreglo[], int tam){	
	for(int i = 0; i < tam; i++){
		cout<<arreglo[i]<<endl;
	}
}

void mostrar_menu_montos(){
	for(int opcion = 0; opcion < 7; opcion++){
		cout<<Montos[opcion]<<endl;
	}
}

int validar(string menaje){
	bool bandera = true;
	string valor1;
	int valor2;
	while(bandera){
		cin>>valor1;
		//valor1 va ha ser igual a valor2 y despues se convierte de cadena a entero es decir a 0
		valor2 = atoi(valor1.c_str());
		bandera = false;
		if(valor2 != 0){
			
			bandera = false;
		}
		else{
			cout<<"Solo se admiten números"<<endl;
			bandera = true;
		}
	}
	return valor2;
}



bool buscar(int monto){
	bool existe = false;
	for(int i = 0; i < 7; i++){
		if(monto == Montos[i]){
			existe = true;
		}
	}
	return existe;
}


void registrar_recarga(){
	int compania;
	int monto;
	cout<<endl<<"Compañias: "<<endl;
	mostrar_menu(Companias, 4);
	compania = validar("Eliga una opcion del 1 al 4: ");
	if(compania > 0 && compania < 5){
		cout<<"Montos: "<<endl;
		mostrar_menu_montos();
		monto = validar("\nIndique el monto: ");
		if(buscar(monto)==true){
			recargas[compania - 1][cantidadRecargas[compania - 1]] = monto;
			cantidadRecargas[compania - 1]++;
			cout<<"Recarga registrada"<<endl;
		}
		else{
			cout<<"Monto no valido";
		}
	}
}


void mostrar_recargas(){
	cout<<"Recargas realizadas"<<endl;
	int total = 0;
	for(int i = 0; i < 4; i++){
		cout<<endl<<Companias[i]<<endl;
		int total = 0;
		for(int j = 0; j < cantidadRecargas[i]; j++){
			cout<< recargas[i][j]<<endl;
			total = total + recargas[i][j];
		}
		cout<<"Total: "<<total;
	}
}











int suma(int vector){
	int res = 0;
	if(vector == 0){
		return 0;
	}
	else{
		for(int i = 1; i<=4; i++){
			res += i;
		}
	}
}

//void mostrar_menu(string arreglo[]){
//	for(int opcion = 1; opcion <=4; opcion++){
//))		cout<<opcion;
//)	}
//}









int main(){
	setlocale(LC_CTYPE, "Spanish");	
	int eleccion = 1;
	string continuar;
	while(eleccion != 3){
		cout<<endl<<"Centro de recargas Ultra"<<endl;
		mostrar_menu(MenuPrincipal,3);
		eleccion = validar("\nEliga una opcion del 1 al 3: ");
		switch(eleccion){
			case 1:
				registrar_recarga();
			break;
			case 2:
				mostrar_recargas();
			break;
			case 3:
				cout<<endl<<"Hasta luego";
			break;
			default:
				cout<<endl<<"Eliga una opcion del 1 al 3: "<<endl;
			break;
		}
		cout<<endl<<"Presione una letra y ENTER para continuar.....";
		cin>>continuar;
	}
	return 0;
}
