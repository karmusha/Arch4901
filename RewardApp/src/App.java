import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import fabrics.GemGenerator;
import fabrics.GoldGenerator;
import fabrics.ItemGenerator;

public class App {
    public static void main(String[] args) throws Exception {
        ItemGenerator generatorGem = new GemGenerator();
        generatorGem.openReward();

        // ItemGenerator generatorGold = new GoldGenerator();
        // generatorGold.openReward();

        List<ItemGenerator> generators = new ArrayList<>();
        generators.add(generatorGem);
        generators.add(new GoldGenerator());

        Random rnd = new Random();
        for (int i = 0; i < 10; i++) {
            generators.get(rnd.nextInt(generators.size())).openReward();
        }

        
    }
}