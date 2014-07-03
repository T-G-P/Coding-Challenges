/*Write a method to decide if two strings are anagrams or not.*/
import java.io.* ;
import java.util.*;

public class ChapterOne_Problem4{

    public static boolean areAnagrams(String string1, String string2){

        if(string1.length() != string2.length()){
            return false;
        }

        HashMap<Character,Integer> charCount1 = new HashMap<Character,Integer>();
        HashMap<Character,Integer> charCount2 = new HashMap<Character,Integer>();
        for(int i=0; i<string1.length(); i++){
            if(!charCount1.containskey(string.charAt(i))){
                charCount1.put(string.charAt(i),1); 
            }
            else{
                charCount1.put(string.charAt(i),charCount1.get(string.charAt(i))+1); 
            }
        }
        for(int i=0; i<string2.length(); i++){
            if(!charCount1.containskey(string.charAt(i))){
                charCount1.put(string.charAt(i),1); 
            }
            else{
                charCount1.put(string.charAt(i),charCount1.get(string.charAt(i))+1); 
            }
        }
        for(char key: charCount1.keySet()){
            if(charCount1.get(key) != charCount2.get(key)){
                return false;
            }
        }
        return true;
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
                    numArgs = false;
                }
            }
            areAnagrams(stringArray[0],stringArray[1]){

        }catch(IOException e){
            System.out.println("Input Error");
        }
    }
}
