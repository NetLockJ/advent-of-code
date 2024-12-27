import java.io.*;
import java.util.*;

public class Day7 {
    static ArrayList<String> list = new ArrayList<String>();

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("Day7.txt");
        Scanner input = new Scanner(file);

        ArrayList<Dir> prevDirs = new ArrayList<Dir>();
        ArrayList<Dir> allDirs = new ArrayList<Dir>();
        ArrayList<Integer> part2 = new ArrayList<Integer>();

        
        Dir mainDir = new Dir("/");
        Dir currentDir = mainDir;
        prevDirs.add(mainDir);
        allDirs.add(mainDir);

        int idx = 1;

        int answer = 0;
        

        while (input.hasNextLine()) {
            list.add(input.nextLine());
        }

        while(idx < list.size()) {
            System.out.println(list.get(idx));
            System.out.println(currentDir.getDirMap() + " " + idx);
            System.out.println(currentDir.getFilesMap() + " " + idx);

            String[] s = list.get(idx).split(" ");
            if(s[1].equals("cd") && !s[2].equals("..")) {
                prevDirs.add(currentDir);
                currentDir = currentDir.getDir(s[2]);
                allDirs.add(currentDir);
                idx++;
            } else if(s[1].equals("cd") && s[2].equals("..")) {
                currentDir = prevDirs.get(prevDirs.size() - 1);
                prevDirs.remove(prevDirs.size() - 1);
                idx++;
            } else if(s[1].equals("ls")) {
                idx++;
                while(!list.get(idx).split(" ")[0].equals("$")) {
                    s = list.get(idx).split(" ");
                    if(s[0].equals("dir")) {
                        currentDir.addDir(new Dir(s[1]));
                    } else {
                        currentDir.addFile(s[1], Integer.parseInt(s[0]));
                    }
                    idx++;
                    // AHHHHHHHH
                    if(idx == 1101 /*change to 1101 when doing actual */) {
                        break;
                    }
                }
            } 
            
        }

        int spaceNeeded = 70000000 - mainDir.memoryInDir();
        spaceNeeded = 30000000 - spaceNeeded;
        

        for (Dir d : allDirs) {
            System.out.println(d.getDirName() + " size: " + d.memoryInDir());
            if(d.memoryInDir() > spaceNeeded) {
                part2.add(d.memoryInDir());
            }
        }

        


        part2.sort(null);
        System.out.println(allDirs);
        System.out.println(part2);
    }
}
