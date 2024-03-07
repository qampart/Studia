import java.awt.*;
import java.awt.geom.Line2D;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static java.lang.Math.abs;

public class Main extends Canvas {
    Random r = new Random();
    List<Point> pointList;
    Delaunay delaunay;

    Main(){
        Random r=new Random();
        int i=r.nextInt(95)+5;
        System.out.println(i);
        pointList = generatePointList(i);
        delaunay = new Delaunay(pointList);
    }

    public static void main(String[] args){
        MyFrame frame = new MyFrame();
    }

    List<Point> generatePointList(int amount){
        List<Point> pointList = new ArrayList<>();
        for(int i=0;i<amount;i++){
            pointList.add(new Point(abs(r.nextInt()%750), abs(r.nextInt()%750)));
        }
        return pointList;
    }

    public void paint(Graphics g){
        Graphics2D g2D = (Graphics2D) g;
        for(Point p:pointList){
            g2D.drawRect((int) p.x, (int) p.y, 1, 1);
        }
        g2D.setColor(new Color(255, 116, 16));
        for(Line2D line:delaunay.lines){
            g2D.draw(line);
        }
    }
}
