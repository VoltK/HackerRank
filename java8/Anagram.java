import java.util.*;

public class Anagram {

    private static boolean isAnagram(String a, String b) {
        if(a.length() == b.length()){
            Map dictA = makeDict(a);
            Map dictB = makeDict(b);
            return dictA.equals(dictB);
        }
        return false;
    }

    private static Map<Character,Integer> makeDict(String word){
        Map<Character,Integer> letters = new HashMap<>();
        for(int x = 0; x <word.length(); x++){
            char letter = word.charAt(x);
            if (letters.containsKey(letter)){
                letters.replace(letter, letters.get(letter)+1);
            }
            else{
                letters.put(letter,1);
            }

        }
        return letters;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.print("Word 1: ");
        String a = scan.next();
        System.out.print("Word 2: ");
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
