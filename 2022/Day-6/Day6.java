import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

public class Day6 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day6.txt");
        Scanner input = new Scanner(file);

        String text = input.nextLine();

        ArrayList<String> list = new ArrayList<String>();

        for(int i = 0; i < text.length() - 1; i++) {
            list.add(text.substring(i, i + 1));
        }

        for (int i = 0; i < list.size() - 12; i++) {
            List<String> subList = list.subList(i, i + 14);
            System.out.println(subList.stream().distinct().count());
            System.out.println(subList);
            if(subList.stream().distinct().count() == 14l) {
                System.out.println("It's: " + (i + 14));
                return;
            }

        }

        
    }


}