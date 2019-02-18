import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the gridChallenge function below.
    static String gridChallenge(String[] grid) {
        char [][] matrix = new char[grid.length][grid.length];
        // convert to char array and sort rows
        for (int x = 0; x < grid.length; x++){
            char [] temp = grid[x].toCharArray();
            Arrays.sort(temp);
            matrix[x] = temp;
        }

        for (int x = 0; x < matrix.length; x++){
            
            for( int j = 0; j < matrix.length-1; j++){
            
                if(matrix[j][x] > matrix[j+1][x]){
                    return "NO";
                }

            }

        }
        return "YES";

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            String[] grid = new String[n];

            for (int i = 0; i < n; i++) {
                String gridItem = scanner.nextLine();
                grid[i] = gridItem;
            }

            String result = gridChallenge(grid);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
