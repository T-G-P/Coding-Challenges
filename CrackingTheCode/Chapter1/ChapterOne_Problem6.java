/*Given an image represented by an NxN matrix, where each pixel in the image is 4
  bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
  for n = 0 to N - 2
  for m = n + 1 to N - 1
  swap A(n,m) with A(m,n)
  */

import java.io.* ;
import java.util.*;

public class ChapterOne_Problem6{

    public static void rotate(int[][] image){
        int i,j;

        for(i=0; i<image.length; i++) {
            for(j=i; j<image.length; j++) {
                if(i!=j) {
                    image[i][j]^=image[j][i];
                    image[j][i]^=image[i][j];
                    image[i][j]^=image[j][i];
                }
            }
        }


        for(i=0; i<image.length/2; i++) {
            for(j=0; j<image.length; j++) {
                image[j][i]^=image[j][image.length-1-i];
                image[j][image.length-1-i]^=image[j][i];
                image[j][i]^=image[j][image.length-1-i];
            }
        }

    }

public static int findnumPlaces(int num){
    int count=1;
    //need to count tens place too
    while(num/10 >= 1){
        num = num/10;
        count++;
    }
    return count;
}

public static void printImage(int[][] image){

    int maxNum = image[image.length-1][image.length-1];
    int numPlaces = findnumPlaces(maxNum);

    for(int i=0; i<image.length; i++){
        for(int j=0; j<image.length; j++){
            if(j!=image.length-1){
                String value = image[i][j]+"";
                System.out.print(value);
                while(value.length() <= numPlaces) {
                    System.out.print(" ");
                    value+=" ";
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
        rotate(image);
        System.out.println("\nAnd here's the transpose...:\n");
        printImage(image);
    }
    catch (IOException err) {
        System.out.println("Error reading line");
    }
}
}
