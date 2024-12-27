import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day3 {
        
    static int score = 0;
    static String letters = "abcdefghijklmnopqrstuvwxyz";
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day3.txt");
        Scanner input = new Scanner(file);
        
        letters += letters.toUpperCase();
        ArrayList<String> arr = new ArrayList<String>();
        while(input.hasNextLine()) {
            arr.add(input.nextLine());
        }
        System.out.println(arr);
        for(int i = 0; i < arr.size() - 2; i += 3) {
            count(arr.get(i), arr.get(i + 1), arr.get(i + 2));
        }
        System.out.println(score);


        
    }

    public static void count(String top, String bottom, String middle) {
        for(int i = 0; i < top.length(); i++) {
            for(int j = 0; j < bottom.length(); j++) {
                for(int c = 0; c < middle.length(); c++) {
                    if(top.charAt(i) == bottom.charAt(j) && top.charAt(i) == middle.charAt(c)) {
                        score += letters.indexOf(top.charAt(i)) + 1;
                        return;
                    }
                }
                

            }
        }
    }
}
