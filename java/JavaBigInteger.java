import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner cmd = new Scanner(System.in);
        BigInteger A = new BigInteger(cmd.nextLine());
        BigInteger B = new BigInteger(cmd.nextLine());

        System.out.println(A.add(B));
        System.out.println(A.multiply(B));

    }
}

