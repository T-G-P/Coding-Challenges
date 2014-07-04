import java.io.* ;
import java.util.*;

/*Write a method to replace all spaces in a string with ‘%20’.*/

public class ChapterOne_Problem5{

    /*This method takes in a character array and then calculates the number of spaces in it. A new array
     * is then made. It's size is calculated by subtracting the number of space characters and adding the number of 
     * replacement characters. We then loop through all of hte characters in the character array and keep track of the position. 
     * Since the space is being replaced by 3 new characters, we increment the position by 3 if these characters are inserted.
     * Otherwise, we insert the respective character and increment the position by 1.
     */

    public static String replaceAllSpaces1(char[] str){

        int numSpaces=0;
        for(char c: str){
            if(c==' '){
                numSpaces++;
            }
        }

        char[] str2 = new char[str.length+2*numSpaces];
        int pos=0;

        for (char c: str){
            if(c == ' '){
                str2[pos] = '%';
                str2[pos+1] = '2';
                str2[pos+2] = '0';
                pos+=3;
            }
            else{
                str2[pos]=c;
                pos++;
            }
        }

        String result = String.valueOf(str2);
        return result;
    }

    /*This is a simple java way to replace a character using a String object*/
    public static String replaceAllSpaces2(String str){

        String result = "";

        for(int i=0; i<str.length(); i++){
            if(str.charAt(i) == ' '){
                result+="%20";
            }
            else{
                result+=str.charAt(i);
            }
        }

        return result;
    }
    /*The simplest one line way to replace any amount of characters with another expression in java*/
    public static String replaceAllSpaces3(String str){

        String result = str.replaceAll(" ", "%20");
        return result;
    }

    public static void main(String[] args){

        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(input);

        try{
            System.out.println("\nPlease enter a string\n");
            String str = buffer.readLine();
            System.out.println(("\nreplaceAllSpaces1: \n"+replaceAllSpaces1(str.toCharArray())));
            System.out.println(("\nreplaceAllSpaces2: \n"+replaceAllSpaces2(str)));
            System.out.println(("\nreplaceAllSpaces3: \n"+replaceAllSpaces3(str))+"\n");

        }catch(IOException e){
            System.out.println("Input Error");
        }

    }

}
