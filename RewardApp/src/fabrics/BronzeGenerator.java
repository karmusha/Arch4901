package fabrics;

import interfaces.IGameItem;
import products.Bronze;

public class BronzeGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Bronze();
    };
}
