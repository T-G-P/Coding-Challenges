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
            char temp;
            int count = 0;

            for(int i = 0; i<input.length(); i++){
                temp = input.charAt(i);
                for(int j = 0; j<input.length(); j++){
                    if(input.charAt(j) == temp){
                        count++;
                        if(count > 1){
                            result[i]._occurances++;
                        }
                        //the char doesn't exist yet in the array
                        else if(count <= 1){
                            Pair myPair = new Pair(temp);
                            myPair._occurances = 1;
                            if(containsChar(temp,result)){
                                result[i] = null;
                            }
                            else{
                                result[i] = myPair;
                            }
                        }

                    }
                }
                count = 0;
            }

            Arrays.sort(result,new OccurrenceComparator());
            return result;
        }
        public boolean containsChar(char c, Pair[] pairs){
            for(int i = 0; i<pairs.length; i++){
                if(pairs[i] != null && pairs[i]._char == c){
                    return true;
                }
            }
            return false;
        }
        public class OccurrenceComparator implements Comparator<Pair>{
            @Override
                public int compare(Pair p1, Pair p2) {

                    if (p1._occurances > p2._occurances) {
                        return -1;
                    }
                    else if (p1._occurances < p2._occurances) {
                        return 1;
                    }
                    else{
                        return 0;
                    }
                }
        }

        public void run(String input){
            auditString(input);
            reportAudit(input);
        }
    }

    public static void main(String[] args){
        String a = "hello world";
        WingSpan test = new WingSpan();
        test.run(a);

    }
}
