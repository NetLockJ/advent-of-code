import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Part2 {
    public static void main(String[] args) throws FileNotFoundException {
        File f = new File("./input.txt");
        Scanner input = new Scanner(f);
        Map<String, List<String>> inputsToOutputs = new HashMap<String, List<String>>();
        ArrayList<String> moduleTypes = new ArrayList<String>();
        Map<String, Module> modules = new HashMap<String, Module>();

        // Parse input
        while (input.hasNextLine()) {
            String[] splitLine = input.nextLine().split("->");
            List<String> outputs = Arrays.asList(splitLine[1].split(", "));
            for (int i = 0; i < outputs.size(); i++) {
                outputs.set(i, outputs.get(i).strip());
            }

            moduleTypes.add(splitLine[0].strip());
            inputsToOutputs.put(splitLine[0].strip().matches("[%&][a-z]+") ? splitLine[0].strip().substring(1)
                    : splitLine[0].strip(), outputs);

        }

        input.close();

        // print read input
        for (Map.Entry<String, List<String>> entry : inputsToOutputs.entrySet()) {
            String key = entry.getKey();
            List<String> values = entry.getValue();

            System.out.printf("K: %s, V: %s\n", key, values);
        }

        for (String name : moduleTypes) {
            if (name.equals("broadcaster")) {
                modules.put(name, new Broadcaster());
            } else if (name.contains("&")) {
                modules.put(name.substring(1), new Conjunction());
            } else {
                modules.put(name.substring(1), new FlipFlop());
            }
        }

        // Conjunction dependencies

        for (Map.Entry<String, Module> entry : modules.entrySet()) {
            String name = entry.getKey();
            Module m = entry.getValue();

            if (m instanceof Conjunction c) {
                for (Map.Entry<String, List<String>> e : inputsToOutputs.entrySet()) {
                    String key = e.getKey();
                    List<String> values = e.getValue();

                    for (String v : values) {
                        if (v.equals(name)) {
                            c.addInput(key, false);
                        }
                    }
                }
            }
        }

        Map<String, Integer> rx = new HashMap<String, Integer>();

        for (Map.Entry<String, List<String>> entry : inputsToOutputs.entrySet()) {
            String key = entry.getKey();
            List<String> values = entry.getValue();

            // ! Probably need to change for your input -- this is whatever stores into 'rx'
            if (values.contains("lg")) {
                rx.put(key, 0);
            }

            System.out.printf("K: %s, V: %s\n", key, values);
        }

        System.out.println(rx.toString());

        int pushes = 0;

        while (rx.values().contains(0)) {
            pushes++;
            ArrayDeque<String> instructions = new ArrayDeque<String>();
            instructions.add("broadcaster");

            while (!instructions.isEmpty()) {
                String name = instructions.pop();
                boolean pulseToSend = modules.get(name).sendPulse();

                if (rx.containsKey(name) && rx.get(name).equals(0) && pulseToSend == true) {
                    rx.replace(name, pushes);
                    System.out.println(rx.toString());
                }

                List<String> outputs = inputsToOutputs.get(name);

                for (int i = 0; i < outputs.size(); i++) {

                    if (modules.get(outputs.get(i)) != null) {

                        modules.get(outputs.get(i)).recievePulse(name, pulseToSend);

                        if (rx.containsKey(outputs.get(i)) && rx.get(outputs.get(i)).equals(0)
                                && modules.get(outputs.get(i)).sendPulse() == true) {
                            rx.replace(outputs.get(i), pushes);
                            System.out.println(rx.toString());
                        }

                        if (modules.get(outputs.get(i)) instanceof FlipFlop fp) {
                            if (fp.willSend()) {
                                instructions.addFirst(outputs.get(i));
                            }
                        } else {
                            instructions.addFirst(outputs.get(i));
                        }

                        // System.out.printf("%s --> %b --> %s\n", name, pulseToSend, outputs.get(i));
                    }
                }
            }

        }

        // lcm of 'cycles'

        BigInteger totalPresses = BigInteger.valueOf(rx.values().stream().toList().get(0));

        for(int i: rx.values()) {
            totalPresses = lcm(totalPresses, BigInteger.valueOf(i));
        }

        System.out.println(totalPresses);

    }

    public static BigInteger lcm(BigInteger number1, BigInteger number2) {
        BigInteger gcd = number1.gcd(number2);
        BigInteger absProduct = number1.multiply(number2).abs();
        return absProduct.divide(gcd);
    }
}
