import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day1 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day1.txt");
        Scanner input = new Scanner(file);
        int[] topElves = { 0, 0, 0, 0};
        int currentTotal = 0;

        while (input.hasNextLine()) {
            String s = input.nextLine();
            if (!s.equals("")) {
                currentTotal += Integer.parseInt(s);
            } else {
                topElves[0] = currentTotal;
                System.out.println(topElves[3]);
                topElves = sort(topElves);
                currentTotal = 0;

            }
        }

        System.out.println(topElves[3] + topElves[2] + topElves[1]);

    }

    public static int[] sort(int[] m) {
        for (int i = (m.length - 1); i >= 0; i--) {
            for (int j = 1; j <= i; j++) {
                if (m[j - 1] > m[j]) {
                    int temp = m[j - 1];
                    m[j - 1] = m[j];
                    m[j] = temp;
                }
            }
        }

        return m;
    }

}
