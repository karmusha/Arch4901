package fabrics;

import interfaces.IGameItem;
import products.Emerald;

public class EmeraldGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Emerald();
    };
}
