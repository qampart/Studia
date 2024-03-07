package QuadTree;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static java.lang.Math.abs;

public class Paint extends Canvas {
    Paint(int i){
        points = randomPoints(i);
    }
    List<Point2D> points;

    public static void main(String[] args){
        MyFrame myFrame=new MyFrame();
    }

    public void paint(Graphics graphics){
        Graphics2D graphics2D = (Graphics2D) graphics;
        BufferedImage image = null;
        try {
            image = ImageIO.read(new File("struktura.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        Tree quadTree = new Tree(image);
        graphics2D.setColor(new Color(255, 0, 0, 102));
        graphics2D.drawImage(image, 0, 0, null);

        for(Line2D line:quadTree.section){
            graphics2D.draw(line);
        }
    }

    public List<Point2D> randomPoints(int n){
        List<Point2D> points = new ArrayList<>();
        Random random = new Random();
        for(int i=0;i<n;i++){
            points.add(new Point2D.Double(abs(random.nextInt()%1000), abs(random.nextInt()%1000)));
        }
        return points;
    }
}
