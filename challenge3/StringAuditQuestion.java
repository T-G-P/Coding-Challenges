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

    public static class WingSpan extends StringAuditQuestion{

        public Pair[] auditString(String input) {

            Pair [] result = new Pair[input.length()];
            System.out.println(result);
            for(int i = 0; i<input.length(); i++){
                System.out.println(result[i]._char);
                for(int j = 0; j<input.length(); j++){
                    System.out.println(result[i]._char);
                    if(result[j]!=null){
                        System.out.println(result[i]._char);
                        if(result[j]._char == input.charAt(i)){   //check if the pair array contains thsi character. If it does, increment count
                            System.out.println(result[i]._char);
                            result[j]._occurances++;
                        }
                        else{       //pair doesn't exist yet
                            System.out.println(result[i]._char);
                            Pair myPair = new Pair(input.charAt(i));
                            myPair._occurances = 1;
                            result[j] = myPair;
                        }
                    }
                }
            }

            Arrays.sort(result,new OccurrenceComparator());
            return result;
        }

        public void run(String input){
            auditString(input);
            reportAudit(input);
        }
    }
    public class OccurrenceComparator implements Comparator<Pair>{
        @Override
        public int compare(Pair p1, Pair p2) {

            if (p1._occurances < p2._occurances) {
                return -1;
            }
            else if (p1._occurances > p2._occurances) {
                return 1;
            }
            else{
                return 0;
            }
        }
    }

    public static void main(String[] args){
        String a = "hello world";
        WingSpan test = new WingSpan();
        test.run(a);

    }
}
