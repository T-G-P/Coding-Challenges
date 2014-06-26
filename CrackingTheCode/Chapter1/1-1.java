public class 1-1{
    /*Implement an algorithm to determine if a string has all unique characters. What if you
      can not use additional data structures?
      */
    public static boolean uniqueChars(String testString){
        ArrayList<Character> chars = new ArrayList<Character>;
        for(int i=0; i<testString.length(); i++){
            if(!chars.contains(testString.charAt(i))){
                chars.append(testString.charAt(i);
            }
            else{
                System.out.println("This string does not have all unique characters");
                return false;
            }
        }
        System.out.println("This string does have all unique characters");
        return true;

    }
    public static boolean uniqueCharsnodatastructure(String testString){
        
    }
}
