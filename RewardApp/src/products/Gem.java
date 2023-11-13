package products;

public class Gem extends ItemReward{
    @Override
    public void open(){
        System.out.println("It's a gem.");
    }

    @Override
    public void close() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'close'");
    }
    
}
