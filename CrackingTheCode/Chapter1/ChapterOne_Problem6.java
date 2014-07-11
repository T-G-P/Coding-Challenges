/*Given an image represented by an NxN matrix, where each pixel in the image is 4
  bytes, write a method to rotate the image by 90 degrees. Can you do this in place?*/

import java.io.* ;
import java.util.*;

public class ChapterOne_Problem6{

    public static void rotate(int[][] image){

    }

    public static void printImage(int[][] image){
        for(int i=0; i<image.length; i++){
            for(int j=0; j<image.length; j++){
                if(j!=image.length-1){
                    if(image[i][j] < 10){
                    System.out.print(image[i][j]+"  ");
                    }
                    else{
                    System.out.print(image[i][j]+" ");
                    }
                }
                else{
                    System.out.println(image[i][j]+" ");
                }
            }
        }
    }

    public static void main(String[] args){

        InputStreamReader inputStream = new InputStreamReader(System.in);
        BufferedReader buff = new BufferedReader(inputStream);

        try {
            System.out.println("Please provide the number of rows/columns for a square matrix. Ex: 5-> 5x5 matrix\n");
            int size = Integer.parseInt(buff.readLine());
            int[][] image = new int[size][size];
            int n=0;
            for(int i=0; i<size; i++){
                for(int j=0; j<size; j++){
                    image[i][j] = n;
                    n+=4;
                }
            }
            printImage(image);
        }
        catch (IOException err) {
            System.out.println("Error reading line");
        }
    }  
}
