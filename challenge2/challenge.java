import java.util.*;
import java.io.*;

public class challenge{

    public static HashMap<String,HashMap<String,Integer>> bandPairs = new HashMap<String,HashMap<String,Integer>>();

    private static void parseFile(String fileName){
        BufferedReader br;
        try{
            br = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = br.readLine()) != null) {
                //tokenize each line by comma and store as string array
                String[] result = line.split(",");
                //sort each line alphabetically
                Arrays.sort(result);
                //loop through the line and set up pairs for every single band
                for (int i = 0; i<result.length; i++){
                    for(int j = 1; j<result.length; j++){
                        //if the hash map does not contain this band
                        if(!bandPairs.containsKey(result[i])){
                            //Create new hashmap to represent all pairs associated with this key
                            HashMap<String,Integer> pairs = new HashMap<String,Integer>();
                            //Add to the pairs only if the pair is not equal to the band
                            //Initialize this pair with a count of 1
                            if(!result[i].equals(result[j])){
                                pairs.put(result[j],1);
                            }
                            //set the band to have this pair hash table as it's value
                            bandPairs.put(result[i],pairs);
                        }
                        //if the hash map already contains this band
                        else{
                            //Now we know that this band pair hash map contains this band already
                            //Go to the pair hash map associated with this band and see if it contains the pair already
                            //if the pair already exists in the hash table, increment it's count by one
                            if(bandPairs.get(result[i]).containsKey(result[j])){
                                bandPairs.get(result[i]).put(result[j], bandPairs.get(result[i]).get(result[j]) + 1);
                            }
                            //the pair does not exist in the hash table, so add it and initalize it's count to 1
                            else{
                                //as long as the band and pair are not the same
                                if(!result[i].equals(result[j])){
                                    //if the bandpair hash table contains the pair key, we do not want to consider the swapped pair
                                    if(bandPairs.containsKey(result[j])){
                                        if(bandPairs.get(result[j]).containsKey(result[i])){
                                            continue;
                                        }
                                    }
                                    bandPairs.get(result[i]).put(result[j], 1);
                                }
                            }
                        }
                    }
                }
            }
            br.close();
            }catch(FileNotFoundException e){
                System.out.println("please make sure the file you entered exists");
                System.out.println("USAGE: java challenge (filename)");
            }catch(IOException e){
                System.out.println("please make sure the file you entered exists");
                System.out.println("USAGE: java challenge (filename)");
            }

    }

    private static void printResult(){
        int numPairs = 0;
        for (String key : bandPairs.keySet()) {
            for(String pair : bandPairs.get(key).keySet()){
                if(bandPairs.get(key).get(pair) >= 50){
                    numPairs++;
                    System.out.println(key+"-"+pair+": "+bandPairs.get(key).get(pair)+" times");
                }
            }
        }
        System.out.println("\nThere are a total of "+numPairs+" pairs that appear 50 or more times");
    }

    public static void main(String[] args){

        if(args.length != 1){
            System.out.println("Please enter a valid file name");
            System.out.println("USAGE: java challenge (filename)");
        }
        else{
            parseFile(args[0]);
            printResult();
        }
    }
}
