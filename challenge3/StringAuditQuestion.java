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

    /*This class extends the StringAuditQuestion class and gives full usage of the pair class
     * as well as the reportAudit method. Since the auditString is an abstract method, it is completed
     * in this Challenge class. This class contains the auditString method which takes in a string and
     * and returns a pair array. This class contains the OccurenceComparator class which contains a comparator
     * function used to sort the array of pairs in auditString. Finally, this class contains the method that
     * runs both auditString and reportAudit.
     */
    public static class Challenge extends StringAuditQuestion{

        public Pair[] auditString(String input) {

            Pair [] pairs = new Pair[input.length()];       //initalize pair array to be the size of the input string
            int count = 0;                                  //initalize count to represent occurences
            int nullCount = 0;;                             //initialize nullCount to represent unwanted characters

            for(int i = 0; i<input.length(); i++){          //loop through the length of the string
                for(int j = 0; j<pairs.length; j++){        //loop through the length of ht array
                    if(pairs[j] == null){                   //if there is nothing at this index
                        count++;                            //increment the count and initialize a pair object for this character
                        Pair myPair = new Pair(input.charAt(i));
                        myPair._occurances = 1;             //initialize this pairs occurence count to 1
                        pairs[i] = myPair;                  //set this pair to be in the same index as its respective char
                        break;                              //break out of the inner loop since the pair is now inserted
                    }

                    else{                                   //if the char already exists in the array
                        if(pairs[j]._char == input.charAt(i)){
                            pairs[j]._occurances++;         //increment its occurence count
                            Pair myPair = new Pair('\0');   //make a new pair with the null character and insert in the array
                            pairs[i] = myPair;
                            nullCount++;                    //increment the null character count
                            break;
                        }
                    }
                }
            }

            Arrays.sort(pairs,new OccurrenceComparator());  //sort the array by count in descending order
            Pair [] result = new Pair[input.length()-nullCount];
            for(int k = 0; k<pairs.length; k++){            //the resulting array will be smaller by nullCount
                if(pairs[k]._char != '\0'){                 //go through array and add all the necessary pairs to the result
                   result[k] = pairs[k];
                }
            }
            return result;
        }

        /*This class is used for the comparator function to sort the array.
         * The comparator function within overrides the default comparator function.
         */
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

        /*This method takes the string input and calls the necessary methods
         * to audit and report the string
         */
        public void run(String input){
            auditString(input);
            reportAudit(input);
        }
    }

    public static void main(String[] args){
        String a = "Hello, my name is Tobias Perelstein";
        Challenge test = new Challenge();
        test.run(a);

    }
}
