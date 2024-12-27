import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.*;
import java.lang.reflect.Array;

public class Day4 {

    public static int count = 1000;

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day4.txt");
        Scanner input = new Scanner(file);

        ArrayList<String> arr = new ArrayList<String>();

        while (input.hasNextLine()) {
            arr.add(input.nextLine());
        }

        for (String s : arr) {
            // first range
            int firstLow = Integer.parseInt(s.substring(0, s.indexOf("-")));
            int firstHigh = Integer.parseInt(s.substring(s.indexOf("-") + 1, s.indexOf(",")));

            // second range
            int secondLow = Integer.parseInt(s.substring(s.indexOf(",") + 1, s.indexOf("-", s.indexOf("-") + 1)));
            int secondHigh = Integer.parseInt(s.substring(s.indexOf("-", s.indexOf("-") + 1) + 1));

            if(firstHigh < secondLow ^ secondHigh < firstLow) {
                count--;
            }
            System.out.println(count);
        }
    }
}
