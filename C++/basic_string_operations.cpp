#include <iostream>
using namespace std ;

int main (){
    // accessing characters by index in a string

    string sentence = "My Name is Pankaj Singh Rawat";
    for (int i = 0; i < sizeof(sentence); i++){
        cout << sentence[i] << " " ;
    }
    cout << endl ; 

    // inserting characters into a string ;
    sentence.insert( 29 , "." );
    cout << sentence << endl ; 

    // CONCATENATING strings : combining multiple string into 1
    string a = "1st" , b = " 2nd" ;

    cout << a + b << endl ;

    // finding size of a string 

    cout << sentence.size() << endl ; 

}