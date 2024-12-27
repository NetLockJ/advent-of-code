import java.util.*;
import java.io.*;

public class Day9 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day9.txt");
        Scanner input = new Scanner(file);

        ArrayList<String> commands = new ArrayList<String>();
        ArrayList<String> pos = new ArrayList<String>();
        // defined for x , y
        Integer[] head = { 0, 0 };
        Integer[] tail = { 0, 0 };

        while (input.hasNextLine()) {
            commands.add(input.nextLine());
        }

        

        for (String s : commands) {
            System.out.println(s);
            String[] spt = s.split(" ");

            

            for (int i = 0; i < Integer.parseInt(spt[1]); i++) {

                

                switch (spt[0]) {
                    case "L":
                        head[0]--;
                        break;
                    case "R":
                        head[0]++;
                        break;
                    case "U":
                        head[1]++;
                        break;
                    case "D":
                        head[1]++;
                        break;
                }

                int up = Math.abs(head[0] - tail[0]);
                int left = Math.abs(head[1] - tail[1]);

                if(up <= 1 && left <= 1) {

                } else if(up >= 2 && left >= 2) {
                    tail[0] = head[0] > tail[0] ? head[0] - 1: head[0] + 1;
                    tail[1] = head[1] > tail[1] ? head[1] - 1: head[1] + 1;
                } else if(up >= 2) {
                    tail[1] = head[1] > tail[1] ? head[1] + 1: head[1] - 1;
                    tail[0] = head[0];
                } else if(left >= 2) {
                    tail[0] = head[0] > tail[0] ? head[0] + 1: head[0] - 1;
                    tail[1] = head[1];
                }

                pos.add(tail[0] + " " + tail[1]);


                System.out.print("head: " + head[0] + " " + head[1] + " ");
                System.out.println("tail: " + tail[0] + " " + tail[1]);
            }

            

        }

        Set<String> p = new HashSet<String>(pos);
        System.out.println(p.size());
    }
}
