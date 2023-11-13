package fabrics;

import interfaces.IGameItem;
import products.Gold;

public class GoldGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Gold();
    };
}
