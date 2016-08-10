import java.io.*;
import java.lang.*;
import java.util.*;

public class Friends{

    static Scanner stdin = new Scanner(System.in);

    static char getOption() {
        System.out.print("\tChoose action: ");
        System.out.print("(1) students at a school, ");
        System.out.print("(2) shortest intro chain, ");
        System.out.print("(3) cliques at school, ");
        System.out.print("(4) connectors, ");
        System.out.print("(q)uit? => ");
        char response = stdin.next().toLowerCase().charAt(0);

        while (response != '1' && response != '2' && response != '3' && response != '4' && response != 'q') {
            System.out.print("\tYou must enter one of 1, 2, 3, 4, or q => ");
            response = stdin.next().toLowerCase().charAt(0);
        }
        return response;
    }
    public static void main(String[] args) throws FileNotFoundException{
       
        System.out.print("Enter the input file name => ");
        String graphFile = stdin.next();
        Graph graph = new Graph(new Scanner(new File(graphFile)));
        graph.buildGraph();
        char option;
        while ((option = getOption()) != 'q') {
            if (option == '1') {
                    System.out.println ("Which school?");
                    stdin.nextLine();
                    String school = stdin.nextLine().toLowerCase();
                    System.out.println(school);
                    graph.printSubGraph(graph.subGraph(school));
                    System.out.println();

            } else if (option == '2') {
                 System.out.println("Enter the names and find the shortest path between them:");
                 String firstname = stdin.next().toLowerCase();
                 String secondname = stdin.next().toLowerCase();
                 System.out.println();
                 System.out.println(graph.BFS(firstname, secondname));
                 System.out.println();


            } else if (option == '3') {
                    System.out.println("Which School?");
                    stdin.nextLine();
                    String school = stdin.nextLine().toLowerCase();
                    System.out.println();
                    graph.buildCliques(graph.subGraph(school));
                    System.out.println();

            } else if(option == '4') {
                System.out.println();
            	graph.connectors();
            	System.out.println();

            }
            else{
                ;
            }

        }

    }
        
}