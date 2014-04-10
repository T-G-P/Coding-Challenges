import java.util.*;

public abstract class StringAuditQuestion
{
    public static class Pair
    {
        public char _char;
        public int _occurances;

        public Pair(char c)
        {
            _char = c;
            _occurances = 0;
        }
    }

    /**
     * Breaks down a string into an array of pairs which report each character
     * that appears in the string, along with the number of occurances for that character.
     * This report is to be provided in order from most occuring character to least occurring
     * character
     * 
     * @param input Any non-null string
     * @return returns the contents of the string
     */
    public abstract Pair[] auditString(String input);

    public void reportAudit(String input)
    {
        Pair[] pairs = auditString(input);
        for (int i = 0; i < pairs.length; i++)
        {
            System.out.println(pairs[i]._char + "\t" + pairs[i]._occurances);
        }		
    }

    public class WingSpan extends StringAuditQuestion{
        public Pair[] result;

        public Pair[] auditString(String input) {

            result = new Pair[input.length()-1];
            for(int i = 0; i<input.length(); i++){
                for(int j = 0; j<input.length(); j++){
                    if(result[j]!=null){
                        if(result[j]._char == input.charAt(i)){   //check if the pair array contains thsi character. If it does, increment count
                            result[j]._occurances++;
                        }
                        else{       //pair doesn't exist yet
                            Pair myPair = new Pair(input.charAt(i));
                            myPair._occurances = 1;
                            result[j] = myPair;
                        }
                    }
                }
            }

            Arrays.sort(result);
            return result;
        }

        public int compareTo(Pair p1, Pair p2) {

            if (p1._occurances < p2._occurances) {
                return -1;
            }

            if (p1._occurances > p2._occurances) {
                return 1;
            }
            return 0;
        }
    }

    public void run(String input){
        auditString(input);
        reportAudit(input);
    }

    public static void main(String[] args){
        String a = "hello world";
        WingSpan test = new WingSpan();
        test.run(a);

    }
}
