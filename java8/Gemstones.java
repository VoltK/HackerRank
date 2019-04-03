import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the gemstones function below.

    private static final Scanner scanner = new Scanner(System.in);

    public static Set<Character> makeSet(String s){
        Set<Character> set = new HashSet<>();

        for(int x = 0; x < s.length(); x++){
            set.add(s.charAt(x));
        }

        return set;
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        Set<Character> rocks = makeSet(scanner.nextLine());
    

        for (int i = 1; i < n; i++) {
            rocks.retainAll(makeSet(scanner.nextLine()));
        }

        int result = rocks.size();

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
