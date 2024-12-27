import java.util.*;
import java.io.*;
import java.lang.reflect.Array;
import java.time.format.TextStyle;

public class Day8 {

    static int[][] trees = new int[99][99];
    static int rows = 0;
    static int colums = 0;

    static int tallTrees = 0;

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day8.txt");
        Scanner input = new Scanner(file);

        while (input.hasNextLine()) {
            String[] s = input.nextLine().split("");

            for (String string : s) {
                trees[rows][colums] = Integer.parseInt(string);
                colums++;
            }
            colums = 0;
            rows++;
        }
        System.out.println();

        for (int r = 0; r < 99; r++) {
            for (int c = 0; c < 99; c++) {
                if (r == 0 || r == 98 || c == 0 || c == 98) {
                    tallTrees++;
                } else {
                    int treeH = trees[r][c];
                    ArrayList<Integer> vert = new ArrayList<Integer>();
                    ArrayList<Integer> hztl = new ArrayList<Integer>();

                    for(int i = 0; i < 99; i++) {
                        vert.add(trees[i][c]);
                    }
                    for(int i = 0; i < 99; i++) {
                        hztl.add(trees[r][i]);
                    }

                    List<Integer> top = vert.subList(0, r);
                    List<Integer> bottom = vert.subList(r + 1, 99);
                    List<Integer> left = hztl.subList(0, c);
                    List<Integer> right = hztl.subList(c + 1, 99);

                    top.sort(null);
                    bottom.sort(null);
                    left.sort(null);
                    right.sort(null);

                    if(treeH > top.get(top.size() - 1)) {
                        tallTrees++;
                    } else if(treeH > bottom.get(bottom.size() - 1)) {
                        tallTrees++;
                    } else if(treeH > right.get(right.size() - 1)) {
                        tallTrees++;
                    } else if(treeH > left.get(left.size() - 1)) {
                        tallTrees++;
                    }
                }
            }
        }

        System.out.println(tallTrees);
    }
}
