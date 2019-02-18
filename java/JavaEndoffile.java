import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner cmd = new Scanner(System.in);
        int counter = 0;
        while (cmd.hasNext()){
            counter++;

            String line = cmd.nextLine();

            System.out.println(counter + " " + line);


        }

    }
}

