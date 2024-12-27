import java.util.*;


public class Monkey {

    enum Operation {
        Multi,
        Add,
        Square
    }



    private int mNum = 0;
    private List<Long> items = new ArrayList<Long>();
    private List<Long> worryItems = new ArrayList<Long>();

    Operation mOperation;

    // how much to add / multiply
    private int operationValue = 0;
    private int testNum = 0;
    private int itemsInspected = 0;

    static List<Monkey> everyM = new ArrayList<Monkey>();

    private int trueThrow = 0;
    private int falseThrow = 0;

    public Monkey(int mNum) {
        this.mNum = mNum;
    }

    public void addItem(Long itemNum) {
        items.add(Long.valueOf(itemNum));
    }

    public List<Long> getItems() {
        return items;
    }

    public void setOperation(Operation O) {
        mOperation = O;
    }

    public void setOperationValue(int operationValue) {
        this.operationValue = operationValue;
    }

    public void setTestNum(int testNum) {
        this.testNum = testNum;
    }

    public void setFalseThrow(int falseThrow) {
        this.falseThrow = falseThrow;
    }

    public void setTrueThrow(int trueThrow) {
        this.trueThrow = trueThrow;
    }

    public static void setEveryM(List<Monkey> everyM) {
        Monkey.everyM = everyM;
    }

    public int getItemsInspected() {
        return itemsInspected;
    }

    public void calculate() {       
        if(mOperation == Operation.Add) {
            for(Long i : items) {
                worryItems.add(i + operationValue);
            }
        } else if(mOperation == Operation.Multi) {
            for(Long i : items) {
                worryItems.add((i * operationValue));
            }

        } else if(mOperation == Operation.Square) {
            for(Long i : items) {
                worryItems.add((long) Math.pow(i , 2));
            }
        }

        // code for part 1

        // part 2 num: 9699690
        int idx = 0;
        for(Long i : worryItems) {
            worryItems.set(idx , i % 9699690);
            idx++;
        }
        
        

        for(Long i : worryItems) {
            itemsInspected++;
            if(i % testNum == 0) {
                everyM.get(trueThrow).addItem(i);
            } else {
                everyM.get(falseThrow).addItem(i);
            }
        }
        
        items.clear();
        worryItems.clear();
        
    }

    

    public String toString() {
        return "Monkey Number: " + mNum + "\nOperation: " + mOperation + "\nDiv Test: " + operationValue + 
        "\nTrue throw: " + trueThrow + "\nFalse throw: " + falseThrow + "\n";
    }
}
