import java.io.* ;
import java.util.*;

/*Google interview question. Return both roots of a quadratic equation. Do not return if there is an imaginary root*/

public class Quad{

    public static double[] computeQuad(double a, double b, double c){
        double root1, root2;
        double temp = (b*b-4*a*c);
        if(temp < 0){
            System.out.println("No imaginary roots..");
            return null;
        }
        root1 = (-1*b + temp)/(2*a);
        root2 = (-1*b - temp)/(2*a);

        return new double[] {root1, root2};
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

                System.out.println("And the roots are: "+Arrays.toString(computeQuad(x,y,z)));

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

/*Not sure if needed, for this type of question*/
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
