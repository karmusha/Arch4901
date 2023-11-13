package fabrics;

import interfaces.IGameItem;
import products.Gem;

public class GemGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Gem();
    };
}
