import java.util.*;

public class Conjunction implements Module {

    private Map<String, Boolean> memory = new HashMap<String, Boolean>();

    @Override
    public void recievePulse(String sender, boolean pulse) {
        memory.put(sender, pulse);
    }

    @Override
    public boolean sendPulse() {
        if(allHigh()) {
            return false;
        } else {
            return true;
        }
    }

    private boolean allHigh() {
        for(Boolean b: memory.values()) {
            if(b == false) {
                return false;
            }
        }

        return true;
    }

    public void addInput(String name, boolean state) {
        memory.put(name, state);
    }

    public void printDependencies() {
        System.out.println(memory.toString());
    }
}
