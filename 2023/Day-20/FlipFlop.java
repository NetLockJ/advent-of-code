public class FlipFlop implements Module {

    private boolean currentPulse = false;
    private boolean willSend = true;

    @Override
    public void recievePulse(String sender, boolean pulse) {
        if(pulse == false) {
            currentPulse = !currentPulse;
            willSend = true;
        } else {
            willSend = false;
        }

    }

    @Override
    public boolean sendPulse() {
        return currentPulse;
    }

    public boolean willSend() {
        return willSend;
    }
    
}
