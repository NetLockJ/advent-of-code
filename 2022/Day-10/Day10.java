import java.util.*;
import java.io.*;

public class Day10 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day10.txt");
        Scanner input = new Scanner(file);
        int pos = 0;
        int currentx = 1;

        int allStrengths = 0;

        String draw = "";

        List<String> allDraws = new ArrayList<String>();

        while(input.hasNextLine()) {
            
            String[] line = input.nextLine().split(" ");
            
            if(line[0].equals("noop")) {
                if(pos % 40 == 0) {
                    allDraws.add(draw);
                    draw = "";
                }

                pos++;

                if(currentx - 1 == pos % 40 || currentx == pos % 40 || currentx + 1 == pos % 40) {
                    draw = draw + "#";
                } else {
                    draw = draw + ".";
                }
            } else {
                
                if(pos % 40 == 0) {
                    allDraws.add(draw);
                    draw = "";
                    
                }

                pos++;

                if(currentx - 1 == pos % 40 || currentx == pos % 40 || currentx + 1 == pos % 40) {
                    draw = draw + "#";
                } else {
                    draw = draw + ".";
                }
                
                if(pos % 40 == 0) {
                    allDraws.add(draw);
                    draw = "";
                }


                pos++;

                currentx += Integer.parseInt(line[1]);

                if(currentx - 1 == pos % 40 || currentx == pos % 40 || currentx + 1 == pos % 40) {
                    draw = draw + "#";
                } else {
                    draw = draw + ".";
                }
                
                
            }

            

        }

        allDraws.add(draw);

        for(String s : allDraws) {
            System.out.println(s);
        }

        // System.out.println(allStrengths);

    }
}
