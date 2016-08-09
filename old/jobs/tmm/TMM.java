public class TMM{

    private static String reverseString(String whatever){
        String result = "";
        for(int i=whatever.length()-1; i>=0; i--){
            result+=whatever.charAt(i);
        }
        return result;

    }

    private static String reverseWords(String whatever){
        String[] temp = whatever.split(" ");
        String result = "";
        for(int i=temp.length-1; i>=0; i--){
            result+=temp[i]+" ";
        }
        return result;
    }
    
    /*Know big O for this. It's 2^n because there are two operations for every step and it has to do it at most n times*/
    private static int fibRecursive(int n){
        if(n==0){
            return 0;
        }
        else if(n==1 || n==2){
            return 1;
        }
        else{
            return fibRecursive(n-1)+fibRecursive(n-2);
        }
    }
    
    /*This was the only one that I found hard because it seems naturally recursive...but this takes up way less time and space*/
    private static int fibIterative(int n){
        int currSum=0;
        int prevSum=0;
        int result=0;
        int count=0;

        if(n==0){
            return 0;
        }
        else if(n==1 || n==2){
            return 1;
        }
        count=3;
        currSum = 1;
        prevSum = 1;
        while(count<=n){
           result=currSum+prevSum; //return this value
           prevSum = currSum;
           currSum = result;
           count++;
        }
        return result;
    }

    public static void main(String[] nigger){
        System.out.println("Reversing the string \"Yo lets get some Korean BBQ!\"");
        System.out.println(reverseString("Yo lets get some Korean BBQ!")+"\n");       

        System.out.println("Reversing the words in the string \"Yo lets get some Korean BBQ!\"");
        System.out.println(reverseWords("Yo lets get some Korean BBQ!")+"\n");       

        System.out.println("Evaluating the the 26th fibonacci number recursively");
        System.out.println(fibRecursive(26)+"\n");

        System.out.println("Evaluating the the 26th fibonacci number iteratively");
        System.out.println(fibIterative(26)+"\n");

        /*This will take an absurd amount of time to run..which is why it's wrong to do this problem recursively
        System.out.println("Evaluating the the 666th fibonacci number recursively");
        System.out.println(fibRecursive(55)+"\n");
        */

        System.out.println("Evaluating the the 60th fibonacci number iteratively");
        System.out.println(fibIterative(60)+"\n");
    }
}
