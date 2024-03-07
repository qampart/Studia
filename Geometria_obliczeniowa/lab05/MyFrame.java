import javax.swing.*;
import java.awt.*;

public class MyFrame extends Canvas {
    MyFrame(){
        JFrame frame = new JFrame();
        Canvas canvas = new Main();
        frame.setMinimumSize(new Dimension(800,800));
        frame.add(canvas);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
}
