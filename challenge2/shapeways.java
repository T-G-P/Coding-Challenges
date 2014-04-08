import java.util.*;
import java.io.*;

public class shapeways{
    private static void parseFile(String fileName){
        BufferedReader br;
        try{
            br = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line+'\n');
            }
            br.close();
        }catch(FileNotFoundException e){
            System.out.println("please make sure the file you entered exists");
            System.out.println("USAGE: java shapeways (filename)");
        }catch(IOException e){
            System.out.println("please make sure the file you entered exists");
            System.out.println("USAGE: java shapeways (filename)");
        }

    }

    public static void main(String[] args){

        System.out.println("Enter the file name");
        if(args.length != 1){
            System.out.println("Please enter a valid file name");
            System.out.println("USAGE: java shapeways (filename)");
        }
        else{
            parseFile(args[0]);
        }
    }

}
