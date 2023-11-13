package fabrics;

import interfaces.IGameItem;
import products.Ruby;

public class RubyGenerator extends ItemGenerator{
    @Override
    public IGameItem createItem() {
        return new Ruby();
    };
}
