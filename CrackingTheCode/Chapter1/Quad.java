import java.io.* ;
import java.util.*;

public class Quad{

    public static Result Quad(double x, double y, double z){
        Result res = new Result(0,0);
        return res;
    }

    public static void main(String[] args){
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(input);

        while(true){
            try{
                System.out.println("\nPlease enter x, y, and z values for the quadratic equation you wish to solve:");
                System.out.println("Press Q to quit when done");
                System.out.print("X: ");
                String temp = buffer.readLine();
                if(temp.equals("Q") || temp.equals("q")){
                    System.out.println("Quitting...");
                    return;
                }
                while(!isNumeric(temp)){
                    System.out.println("Invalid argument, please enter a number");
                    System.out.print("X: ");
                    temp = buffer.readLine();
                    if(temp.equals("Q") || temp.equals("q")){
                        System.out.println("Quitting...");
                        return;
                    }
                }
                double x = Double.parseDouble(temp);

                System.out.print("\nY: ");
                temp = buffer.readLine();
                if(temp.equals("Q") || temp.equals("q")){
                    System.out.println("Quitting...");
                    return;
                }
                while(!isNumeric(temp)){
                    System.out.println("Invalid argument, please enter a number");
                    System.out.print("\nY: ");
                    temp = buffer.readLine();
                    if(temp.equals("Q") || temp.equals("q")){
                        System.out.println("Quitting...");
                        return;
                    }
                }
                double y = Double.parseDouble(temp);

                System.out.print("\nZ: ");
                temp = buffer.readLine();
                if(temp.equals("Q") || temp.equals("q")){
                    System.out.println("Quitting...");
                    return;
                }
                while(!isNumeric(temp)){
                    System.out.println("Invalid argument, please enter a number");
                    System.out.print("\nZ: ");
                    temp = buffer.readLine();
                    if(temp.equals("Q") || temp.equals("q")){
                        System.out.println("Quitting...");
                        return;
                    }
                }
                double z = Double.parseDouble(temp);

                Result ret = Quad(1,2,3);
                System.out.println(ret.x);
                System.out.println(ret.y);
                System.out.println(ret.getX());
                System.out.println(ret.getY());

            }catch(IOException e){
                System.out.println("Input Error");
            }catch(NumberFormatException nfe){
                System.out.println("Invalid argument, please enter a number");
            }


        }

    }
    public static boolean isNumeric(String buff){
        try  
        {  
            double d = Double.parseDouble(buff);  
        }  
        catch(NumberFormatException nfe)  
        {  
            return false;  
        }  
        return true;  
    }


    public static class Result{

        private double x;
        private double y;

        public Result(double x, double y){
            this.x = x;
            this.y = y;
        }

        public void setX(double x){
            this.x = x;
        }

        public void setY(double y){
            this.y = y;
        }

        public double getX(){
            return this.x;
        }

        public double getY(){
            return this.y;
        }
    }
}
