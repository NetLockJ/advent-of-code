import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Day11 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day11.txt");
        Scanner input = new Scanner(file);
        List<Monkey> allMsCount = new ArrayList<Monkey>();

        while(input.hasNextLine()) {
            String[] s = input.nextLine().split(" ");
            if(s[0].equals("Monkey")) {
                Monkey m = new Monkey(Integer.parseInt(s[1].substring(0, s[1].length() - 1)));
                allMsCount.add(m);
                s = input.nextLine().split(" ");
                for(int i = 4; i < s.length; i++) {
                    if(s[i].indexOf(",") != -1) {
                        m.addItem(Long.parseLong(s[i].substring(0, s[i].length() - 1)));
                    } else {
                        m.addItem(Long.parseLong(s[i]));
                    }
                    System.out.println(m.getItems());
                }

                s = input.nextLine().split(" ");
                System.out.println(s[6]);
                if(s[6].equals("*")) {
                    m.setOperation(Monkey.Operation.Multi);
                } else {
                    m.setOperation(Monkey.Operation.Add);
                }
                if(s[7].equals("old")) {
                    m.setOperation(Monkey.Operation.Square);
                } else {
                    m.setOperationValue(Integer.parseInt(s[7]));
                }

                s = input.nextLine().split(" ");
                m.setTestNum(Integer.parseInt(s[5]));

                s = input.nextLine().split(" ");
                m.setTrueThrow(Integer.parseInt(s[9]));

                s = input.nextLine().split(" ");
                m.setFalseThrow(Integer.parseInt(s[9]));


                
            }
        }

        Monkey.setEveryM(allMsCount);

        for(int i = 0; i < 10000; i++) {
            for(Monkey m : allMsCount) {
                m.calculate();
            } 
        }

        List<Integer> inspections = new ArrayList<Integer>();
        for (Monkey m : allMsCount) {
            inspections.add(m.getItemsInspected());
        }
        System.out.println(inspections);

        inspections.sort((a, b) -> b - a);

        System.out.println(BigInteger.valueOf(inspections.get(0)).multiply(BigInteger.valueOf(inspections.get(1))));

    }
}
