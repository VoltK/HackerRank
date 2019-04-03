import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner cmd = new Scanner(System.in);
        int n = cmd.nextInt();
        int d;
        cmd.nextLine();
        
        ArrayList<ArrayList<Integer>> arrays = new ArrayList<ArrayList<Integer>>();            
        for (int x = 0; x < n; x++){

             d = cmd.nextInt();
             ArrayList<Integer> temp = new ArrayList<>(d);
             for(int input = 0; input < d; input++){
                temp.add(cmd.nextInt());
             }
             arrays.add(temp);

        }
        int arrayIndex, arrayElement;
        int q = cmd.nextInt();
        for(int x = 0; x < q; x++){
            arrayIndex = cmd.nextInt();
            arrayElement = cmd.nextInt();
            ArrayList<Integer> arr = arrays.get(arrayIndex-1);
            if(arr.size() < arrayElement){
                System.out.println("ERROR!");
            }
            else{
                System.out.println(arr.get(arrayElement-1));
            }

        }
    }
}

