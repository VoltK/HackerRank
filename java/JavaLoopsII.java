import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0; i<t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            String result = "";
            int sum = a;
            
            for(int x = 0; x < n; x++){
                sum += Math.pow(2, x) * b;
                result += sum + " ";
            }
            System.out.println(result);


        }
        in.close();
    }
}

