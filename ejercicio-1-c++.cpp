// EJERCICIO 1 - C++
// Vector de alumnos usando una clase
#include<iostream>
#include<vector>
#include<string>
using namespace std;
class Alumno{
public:
    string nombre;
    float calificacion;
    Alumno(string n, float c){
        nombre = n;
        calificacion = c;
    }

    bool aprobado(){
        return calificacion >= 6;
    }
};

int main(){
    vector<Alumno> alumnos = {
        Alumno("Ana", 9),
        Alumno("Luis", 5),
        Alumno("Sofia", 8)
    };

    for(Alumno alumno : alumnos){
        cout << "Nombre: " << alumno.nombre << endl;
        cout << "Calificacion: " << alumno.calificacion << endl;
        if(alumno.aprobado()){
            cout << "Aprobado" << endl;
        }
        else{
            cout << "Reprobado" << endl;
        }
    } 
    return 0;
}
