// traversing means printing elements of array 

#include <iostream>
using namespace std ; 

int main (){

    //using for loop
    int arr[] = {2, -1, 5, 6, 0, -3} ;
    int length = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < length; i++){
        cout << arr[i] << " " ; 
    }

    cout<< endl;
    
    // using for each loop 
    for (int x : arr ){
        cout << x << " " ;
    }

    cout<< endl;

    // using auto keyword in foreach 
    for(auto x : arr ){
        cout << x << " " ; 
    }

    cout << endl;
    

}