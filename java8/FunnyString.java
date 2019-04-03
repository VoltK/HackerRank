import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the funnyString function below.
    static String funnyString(String s) {

        int [] ascii = new int[s.length()];

        for (int x = 0; x < s.length(); x++){
            ascii[x] = (int) s.charAt(x);
        }

        for (int x = 0, y = ascii.length-1; x < ascii.length / 2; x++, y--){
            int valX = Math.abs(ascii[x] - ascii[x+1]);
            int valY = Math.abs(ascii[y] - ascii[y-1]);

            if(valX != valY){
                return "Not Funny";
            }

        }

        return "Funny";



    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            String result = funnyString(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
