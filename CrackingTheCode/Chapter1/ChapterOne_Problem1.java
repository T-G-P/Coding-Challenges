import java.io.* ;
import java.util.*;

public class ChapterOne_Problem1{

    /*Implement an algorithm to determine if a string has all unique characters. What if you
      can not use additional data structures?
      */

    //Using a data structure
    public static boolean uniqueChars(String testString){

        System.out.println("\nUsing data structures..");

        ArrayList<Character> chars = new ArrayList<Character>();

        for(int i=0; i<testString.length()-1; i++){
            if(!chars.contains(testString.charAt(i))){
                chars.add(testString.charAt(i));
            }
            else{
                System.out.println("\nThis string does not have all unique characters\n");
                return false;
            }
        }
        System.out.println("\nThis string does have all unique characters\n");
        return true;
    }

    //No data Structure
    public static boolean uniqueCharsnodatastructure(String testString){

        System.out.println("\nUsing no data structures..");

        for(int i=0; i<testString.length(); i++){
            for(int j=i+1; i<testString.length(); j++){
                if(j==testString.length()){
                    break;
                }

                else if(testString.charAt(i) == testString.charAt(j)){
                    System.out.println("\nThis string does not have all unique characters\n");
                    return false;
                }
            }
        }
        System.out.println("\nThis string does have all unique characters\n");
        return true;
    }
    public static void main(String[] args){

        InputStreamReader inputStream = new InputStreamReader(System.in);
        BufferedReader buff = new BufferedReader(inputStream);

        try {
            System.out.println("Please Enter a String and find out if it's unique or not!");
            String testString = buff.readLine();
            uniqueChars(testString);
            uniqueCharsnodatastructure(testString);
        }
        catch (IOException err) {
            System.out.println("Error reading line");
        }
    }  
}
