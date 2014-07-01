import java.io.* ;
import java.util.*;

/* Design an algorithm and write code to remove the duplicate characters in a string
 * without using any additional buffer. NOTE: One or two additional variables are fine.
 * An extra copy of the array is not.
 *
 * FOLLOW UP
 * Write the test cases for this method.
 * */

public class ChapterOne_Problem3{

    public static void removeDuplicates(char[] string){

        if(string.length == 0 || string.length == 1){
            return;
        }

        for(int i=0; i<string.length; i++){
            for(int j=i+1; j<string.length; j++){
                if(j == string.length){
                    return;
                }
                if(string[i] == string[j]){
                    if(string[i] == '\0'){
                        continue;
                    }
                    string[j]='\0';
                }
            }
        }
        shiftChars(string);
    }

    public static void shiftChars(char[] string){

        for(int i=0; i<string.length; i++){
            if(string[i]=='\0'){
                for(int j=i+1; j<string.length; j++){
                    if(j == string.length){
                        return;
                    }
                    else if(string[j] != '\0'){
                        string[i]=string[j];
                        string[j]='\0';
                        break;
                    }
                }
            }
        }
    }

    public static void main(String[] args){

        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(input);

        try{
            System.out.println("\nPlease enter a string\n");
            String str = buffer.readLine();
            char[] charArray = str.toCharArray();
            removeDuplicates(charArray);
            System.out.println(charArray);

        }catch(IOException e){
            System.out.println("Input Error");
        }

    }
}
