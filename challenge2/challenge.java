import java.util.*;
import java.io.*;

public class challenge{

    public static HashMap<String,String> band = new HashMap<String,String>();

    private static void parseFile(String fileName){
        BufferedReader br;
        try{
            br = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = br.readLine()) != null) {
                String[] result = line.split(",");
                for (int x=0; x<result.length; x++){
                    band.put(result[x],result[x]);
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
    private static void add(String bandName){
        //add band names to hash tables with their values
    }

    private static void printResult(HashMap<String,String> band){
        for (String key : band.keySet()) {
            System.out.println("Key = " + key + "\nValue = "+band.get(key));
        }

    }

    public static void main(String[] args){

        System.out.println("Enter the file name");
        if(args.length != 1){
            System.out.println("Please enter a valid file name");
            System.out.println("USAGE: java challenge (filename)");
        }
        else{
            parseFile(args[0]);
            printResult(band);
        }
    }

}
