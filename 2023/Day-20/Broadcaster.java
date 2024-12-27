public class Broadcaster implements Module {

    @Override
    public void recievePulse(String sender, boolean pulse) {
        throw new UnsupportedOperationException("Unimplemented method 'recievePulse'");
    }

    @Override
    public boolean sendPulse() {
       return false;
    }
    
}
