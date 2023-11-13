package fabrics;

import interfaces.IGameItem;
import products.Sapphire;

public class SapphireGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Sapphire();
    };
}
