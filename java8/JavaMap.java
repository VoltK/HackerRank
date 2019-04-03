//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
		Map<String,Integer> phoneBook = new HashMap<>();
        for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
			in.nextLine();
            phoneBook.put(name, phone);


		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            String msg;
            //int phone = phoneBook.get(s);
            if (phoneBook.get(s) != null){
                msg = s + "=" + phoneBook.get(s);
            }
            else{
                msg = "Not found"; 
            }

            System.out.println(msg);
        
        }
	}
}



