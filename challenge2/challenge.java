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
                String[] result = line.split(",");
                Arrays.sort(result);
                for (int i = 0; i<result.length; i++){
                    for(int j = 1; j<result.length; i++){
                        //doesn't contain the key, add key, and then add all pairs associated with this key
                        if(bandPairs.containsKey(result[i])){
                            HashMap<String,Integer> pairs = new HashMap<String,Integer>();
                            pairs.put(result[j],1);
                            bandPairs.put(result[i],pairs);
                        }
                        else{
                            //contains the key, so pairs hash table already exists and check if pair exists
                            if(bandPairs.get(result[i]).containsKey(result[j])){
                                bandPairs.get(result[i]).put(result[j], pairs.get(result[j]) + 1);
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

    /*private static void printResult(HashMap<String,String> band){
      for (String key : bandPairs.keySet()) {
      System.out.println("Key = " + key + "\nValue = "+band.get(key));
      }

    }
    */

    public static void main(String[] args){

        System.out.println("Enter the file name");
        if(args.length != 1){
            System.out.println("Please enter a valid file name");
            System.out.println("USAGE: java challenge (filename)");
        }
        else{
            parseFile(args[0]);
            printResult(bandPairs);
        }
    }

}
