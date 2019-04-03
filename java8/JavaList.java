import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner cmd = new Scanner(System.in);
        int listSize = cmd.nextInt();
        
        List<Integer> numbers = new ArrayList<Integer>();
        for (int x = 0; x < listSize; x++){
            numbers.add(cmd.nextInt());
        }
        
        int index, value;
        int queries = cmd.nextInt();
        for (int x = 0; x < queries; x++){
            cmd.nextLine();
            String command = cmd.nextLine();
            if(command.equals("Insert")){
                index = cmd.nextInt();
                value = cmd.nextInt();
                numbers.add(index, value);
            }
            else{
                index = cmd.nextInt();
                numbers.remove(index);
            }
        }

        for(int num: numbers){
            System.out.print(num + " ");
        }


    }
}

