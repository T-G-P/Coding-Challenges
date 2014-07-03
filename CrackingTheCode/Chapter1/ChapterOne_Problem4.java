/*Write a method to decide if two strings are anagrams or not.*/
import java.io.* ;
import java.util.*;

public class ChapterOne_Problem4{

    public static boolean areAnagrams1(String string1, String string2){

        if(string1.length() != string2.length()){
            System.out.println("\nThese are not anagrams\n");
            return false;
        }

        HashMap<Character,Integer> charCount1 = new HashMap<Character,Integer>();
        HashMap<Character,Integer> charCount2 = new HashMap<Character,Integer>();
        for(int i=0; i<string1.length(); i++){
            if(!charCount1.containsKey(string1.charAt(i))){
                charCount1.put(string1.charAt(i),1); 
            }
            else{
                charCount1.put(string1.charAt(i),charCount1.get(string1.charAt(i))+1); 
            }
        }
        for(int i=0; i<string2.length(); i++){
            if(!charCount2.containsKey(string2.charAt(i))){
                charCount2.put(string2.charAt(i),1); 
            }
            else{
                charCount2.put(string2.charAt(i),charCount2.get(string2.charAt(i))+1); 
            }
        }
        for(char key: charCount1.keySet()){
            if(charCount1.get(key) != charCount2.get(key)){
                System.out.println("\nThese are not anagrams\n");
                return false;
            }
            else{
            }

        }
        System.out.println("\nThese are definitely anagrams\n");
        return true;
    }

    public static boolean areAnagrams2(String string1, String string2){
        if(mySort(string1).equals(mySort(string2))){
            System.out.println("\nThese are definitely anagrams\n");
            return true;
        }
        System.out.println("\nThese are not anagrams\n");
        return false;

    }
    public static String mySort(String str){
        char[] charArray = str.toLowerCase().toCharArray();
        for(int i=0; i<charArray.length; i++){
            for(int j=i+1; j<charArray.length; j++){
                if((int)charArray[i] > (int)charArray[j]){
                    char temp = charArray[j];
                    charArray[j] = charArray[i]; 
                    charArray[i] = temp;
                }
            }
        }
        String result="";
        for(char s: charArray){
            result+=s;
        }
        return result;

    }

    public static void main(String[] args){

        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(input);

        try{
            boolean numArgs = true;
            while(numArgs){
                System.out.println("\nPlease enter two strings separated by a space\n");
                String str = buffer.readLine();
                String[] stringArray = str.split(" ");
                if(stringArray.length !=2){
                    System.out.println("Invalid Input...try again\n");
                }
                else{
                    System.out.println("\nSorting: "+stringArray[0]+" => "+mySort(stringArray[0]));
                    System.out.println("\nSorting: "+stringArray[1]+" => "+mySort(stringArray[1]));
                    numArgs = false;
                    System.out.println("Using complicated solution: \n");
                    areAnagrams1(stringArray[0],stringArray[1]);
                    System.out.println("Using better solution: \n");
                    areAnagrams2(stringArray[0],stringArray[1]);
                }
            }

        }catch(IOException e){
            System.out.println("Input Error");
        }
    }
}
