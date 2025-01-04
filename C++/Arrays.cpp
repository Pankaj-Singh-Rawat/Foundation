//  declaring and initialising an array 

#include <iostream>
using namespace std;

int main(){

    int arr[5] = {1,2,3,4,5}; // length is already defined as 5 for array 

    int arr1[] = {1,2,3} ; // length of array will now be equal to the elements in the array for this case length is 3

    // initialising array after declaration
    int num = 10 ;
    // int value[] = {};
    for( int i = 0 ; i <= num ; i++){
        // arr[i] = value;
    }
    

    // partial arrays : stores only given numer at the indices and all other numbers are considered 0

    int partialArray[5] = {1,2}; // here at indices 0 and 1 the calues are stored and every other value will remain 0


    // accessing elements in arrays 
    int arr2[] = {1,2,3,4,5};
    int length = sizeof(arr2) / sizeof(arr2[0]);
    for (int i = 0 ; i < length; i++){
        cout << arr[i] << endl ;
    }

    int* ptr = arr2 ; // creating a pointer of array 
    cout << ptr << endl; // a pointer stores address of given variable
    // as the variable is an array the address of 1st location is stored i.e. location of index 0


    cout << *ptr << endl ; // printing the 1st value at the stored loaction using *ptr
    cout << *(ptr + 1) << endl ; // printing the 2nd value using the same pointer in arrays


    cout << endl ; 

    // declaring 2D arrays 


    int arr5[2][3] ; // array with 2 rows and 3 columns

    // initialising the same array using loop 
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            arr5[i][j] = i + j ;
        }
    }

    

    // printing the initialised values
        
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            cout << arr5[i][j] << " ";
        }
        cout << endl ;

    }

    cout << endl ; 


    // declaring 3D arrays 
    int arr6[3][3][3] ; 

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            for (int k = 0; k < 3; k++){
                arr6[i][j][k] = i + j +k ;
            }   
        }
    }

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            for (int k = 0; k < 3; k++){
                cout << arr6[i][j][k] << " " ;
            }  
            cout << endl ;  
        }
        cout << endl ;
    }
    


}