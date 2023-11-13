package fabrics;

import interfaces.IGameItem;

public abstract class ItemGenerator {
    public void openReward(){
        createItem().open();
    };

    public abstract IGameItem createItem();
}
