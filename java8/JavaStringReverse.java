import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        String reverse = "";
        for(int x = A.length()-1; x >= 0; x--){
            reverse += A.substring(x, x+1);
        }
        if( A.equals(reverse)){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }


    }
}



