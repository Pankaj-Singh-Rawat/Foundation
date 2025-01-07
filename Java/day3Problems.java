import java.util.Scanner;

public class day3Problems {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in) ;       
        
        // find factorial of a number
        System.out.println(factorial(5));

        // check if array is sorted using recursion
        // input = [20, 21, 45, 89, 89, 90]

        int[] array1 = {20, 21, 45, 89, 89, 90};
        // System.out.println(isSorted(array1 , 0));

        
        
        
    }

    private static boolean isSorted(int[] array1 , int index){
        if( index == array1.length - 1){
            return true ;
        }

        if ( array1[index] > array1[index + 1 ]){
            return false ;
        }

        return isSorted(array1, index + 1);
    }

    private static int factorial(int n){
        int ans = 1;
        if (n > 0){
            for (int i = 1; i <= n; i++) {
                ans = ans * i ;
            }
        }

        return ans;
        
    }


}

