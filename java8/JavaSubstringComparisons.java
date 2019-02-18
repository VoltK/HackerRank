

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        for(int x = 0; x < s.length()-k+1; x++){
            int index = x + k;
            String sub = s.substring(x, index);
            if(sub.compareTo(largest) > 0){
                largest = sub;
            }
            else if( smallest.compareTo(sub) > 0){
                smallest = sub;
            }

        }


        return smallest + "\n" + largest;
    }

