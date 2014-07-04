import java.io.* ;
import java.util.*;

/*Write a method to replace all spaces in a string with ‘%20’.*/

public class ChapterOne_Problem5{

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
            //for(int i=pos; i<str2.length; i++){
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
            //break;
            //}
        }
        String result = String.valueOf(str2);

        return result;
    }

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
