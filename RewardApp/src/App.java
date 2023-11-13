import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Random;

import fabrics.BronzeGenerator;
import fabrics.EmeraldGenerator;
import fabrics.GemGenerator;
import fabrics.GoldGenerator;
import fabrics.ItemGenerator;
import fabrics.RubyGenerator;
import fabrics.SapphireGenerator;
import fabrics.SilverGenerator;

public class App {
    public static void main(String[] args) throws Exception {
        //Рандомайзер
        Random random = ThreadLocalRandom.current();

        // Инициализация фабрик и их списка
        List<ItemGenerator> fabrics = initFabrics();

        for (int i = 0; i < 200; i++) {
            // Выбрасываем вес шанса (0 <= вес < 1)
            int index = random.nextInt(fabrics.size());
            fabrics.get(index).openReward();
        }
    }

    /**
    * @return List of generators(fabrics)
    */
    // Фабричный инициализатор
    public static List<ItemGenerator> initFabrics() {
        List<ItemGenerator> fabrics = new ArrayList<>();

        fabrics.add(new GemGenerator());

        for (int i = 0; i < 3; i++) {
            fabrics.add(new GoldGenerator());                
        }

        for (int j = 0; j < 10; j++) {
            fabrics.add(new BronzeGenerator());
            fabrics.add(new EmeraldGenerator());
            fabrics.add(new SilverGenerator());
            fabrics.add(new SapphireGenerator());
            fabrics.add(new RubyGenerator());
        }
        return fabrics;
    }
}