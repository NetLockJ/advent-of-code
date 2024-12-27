import java.util.*;
import java.io.*;
import java.lang.reflect.Array;
import java.time.format.TextStyle;

public class Day82 {

    static int[][] trees = new int[99][99];
    static int rows = 0;
    static int colums = 0;

    static int maxScenicScore = 0;

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
                    int scenicScore = 0;
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

                    Collections.reverse(top);
                    Collections.reverse(left);

                    int topS = 1, bottomS = 1, leftS = 1, rightS = 1;

                    for(int i = 0; i < top.size() - 1; i++) {
                        if(treeH > top.get(i)) {
                            topS++;
                        } else {
                            break;
                        }
                    }
                    for(int i = 0; i < bottom.size() - 1; i++) {
                        if(treeH > bottom.get(i)) {
                            bottomS++;
                        } else {
                            break;
                        }
                    }
                    for(int i = 0; i < left.size() - 1; i++) {
                        if(treeH > left.get(i)) {
                            leftS++;
                        } else {
                            break;
                        }
                    }
                    for(int i = 0; i < right.size() - 1; i++) {
                        if(treeH > right.get(i)) {
                            rightS++;
                        } else {
                            break;
                        }
                    }
                    

                    scenicScore = topS * bottomS * leftS * rightS;

                    if(scenicScore > maxScenicScore) {
                        maxScenicScore = scenicScore;
                    }


                    

                    
                }
            }
            System.out.println(maxScenicScore);
        }

        
    }


