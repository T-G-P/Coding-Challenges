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
        System.out.println(string);
        shiftChars(string);
    }

    public static void shiftChars(char[] string){
        for(int i=0; i<string.length; i++){
            if(string[i]=='\0'){
                for(int j=i+1; j<string.length; j++){
                    if(j == string.length){
                        return;
                    }
                    if(string[j] != '\0'){
                        string[i]=string[j];
                        string[j]='\0';
                        break;
                    }
                }
            }
        }
    }

    public static void main(String[] args){

        String str = "hello world"; 
        char[] charArray = str.toCharArray();
        removeDuplicates(charArray);
        System.out.println(charArray);
    }
}
