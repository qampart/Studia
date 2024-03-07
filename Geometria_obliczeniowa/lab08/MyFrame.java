package QuadTree;

import javax.swing.*;
import java.awt.*;

public class MyFrame {
    MyFrame(){
        JFrame frame = new JFrame();
        Canvas canvas = new Paint(1000);
        frame.setMinimumSize(new Dimension(700,500));
        canvas.setPreferredSize(new Dimension(700,500));
        frame.add(canvas);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
}
