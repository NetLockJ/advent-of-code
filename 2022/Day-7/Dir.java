import java.util.*;

public class Dir {
    private String dirName = "";

    private Map<String , Dir> dirMap = new HashMap<String , Dir>();
    private Map<String , Integer> filesMap = new HashMap<String , Integer>();

    public Dir(String dirName) {
        this.dirName = dirName;
    }

    public Map<String, Dir> getDirMap() {
        return dirMap;
    }

    public Map<String, Integer> getFilesMap() {
        return filesMap;
    }

    public String getDirName() {
        return dirName;
    }

    public int memoryInDir() {
        int memory = 0;
        for(Map.Entry<String , Dir> entry: dirMap.entrySet()) {
            // use if not summing from dir to dir
            memory += entry.getValue().memoryInDir();
        } 

        for(Map.Entry<String, Integer> entry: filesMap.entrySet()) {
            memory += entry.getValue();
        }

        return memory;
    }

    public Dir getDir(String key) {
        return dirMap.get(key);
    }

    public void addDir(Dir d) {
        dirMap.put(d.getDirName(), d);
    }

    public void addFile(String s, int fileSize) {
        filesMap.put(s, fileSize);
    }

    
}
