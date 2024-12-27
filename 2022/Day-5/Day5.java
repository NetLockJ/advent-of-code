import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.*;
import java.lang.reflect.Array;

public class Day5 {

        static ArrayList<String> arr = new ArrayList<String>();
        static ArrayList<String> commands = new ArrayList<String>();
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day5.txt");
        Scanner input = new Scanner(file);
        


        arr.add("RPCDBG");
        arr.add("HVG");
        arr.add("NSQDJPM");
        arr.add("PSLGDCNM");
        arr.add("JBNCPFLS");
        arr.add("QBDZVGTS");
        arr.add("BZMHFTQ");
        arr.add("CMDBF");
        arr.add("FCQG");


        while(input.hasNextLine()){
            commands.add(input.nextLine());
        }

        for(int i = 10; i < commands.size(); i++) {
            int[] n = split(commands.get(i));
            crane(n[0], n[1], n[2]);
            System.out.println(commands.get(i));
        }

      
    }


    public static int[] split(String s) {
        int[] nums = {0, 0, 0};
        String[] sp = s.split(" ");
        nums[0] = Integer.parseInt(sp[1]);
        nums[1] = Integer.parseInt(sp[3]);
        nums[2] = Integer.parseInt(sp[5]);
        return nums;
    }

    public static void crane(int number, int from, int to) {
        String placeFrom = arr.get(from - 1).substring(arr.get(from - 1).length() - number);
        String temp = "";

        String placeTo  = arr.get(to - 1);
        arr.remove(to - 1);
        System.out.println(arr);
        arr.add(to - 1, placeTo + placeFrom);
        System.out.println(arr);
        String placeFr = arr.get(from - 1);
        arr.remove(from - 1);
        arr.add(from - 1, placeFr.substring(0, placeFr.length() - placeFrom.length()));
        System.out.println(arr);

    }
}