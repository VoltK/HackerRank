

    static boolean isAnagram(String a, String b) {
        if(a.length() == b.length()){
            java.util.Map dictA = makeDict(a.toLowerCase());
            java.util.Map dictB = makeDict(b.toLowerCase());
            if(dictA.equals(dictB)){
                return true;
            }
            else{
                return false;
            }

        }
        return false;
    }

    static java.util.Map<Character,Integer> makeDict(String word){
        java.util.Map<Character,Integer> letters = new java.util.HashMap<Character,Integer>();
        for(int x = 0; x < word.length(); x++){
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

