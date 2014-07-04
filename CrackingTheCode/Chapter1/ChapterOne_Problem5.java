/*Write a method to replace all spaces in a string with ‘%20’.*/

public class ChapterOne_Problem5{
    
    public static String replaceAllSpaces1(char[] str){
        return "";
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
        String test = "hello world dawg";
        System.out.println((replaceAllSpaces1(test.toCharArray()));
        System.out.println((replaceAllSpaces2(test)));
        System.out.println((replaceAllSpaces3(test)));
    }
}
