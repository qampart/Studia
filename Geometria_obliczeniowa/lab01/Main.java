package go;

import java.awt.*;

public class Main {

    public static void main(String[] args) {
        /*Point point1 = new Point(0,2);
        Point point2 = new Point (1,4);
        Line line=new Line(point1, point2);
        line.drawLine(point1, point2); //2
        System.out.println(line.ifBelongLine(new Point (2,3)));     //3b
        System.out.println(line.ifBelongStretch(new Point (2,4)));  //3a

        line.shiftVector(new Vector(10,10));
        point1.rotation(0); //5


        Point point = new Point(3,2);
        //point.Ox(); //6
        point.OxOy();*/


        //2

//        double[] tab = new double[2];
//        Line.calcFunc(new Point(4, 4), new Point(2,2), tab);
//        Cramer cramer = new Cramer();
//        cramer.crossingPointCramer(1, 2, 3, 3,2,1);

        Point p1=new Point(3,4);
        Point p2=new Point(4,1);
        Point p3=new Point(-1,1);
        Point p4=new Point(1,-1);

        Line l1=new Line(p1, p2);
        Line l2=new Line(p3, p4);

        l1.drawLine(p1,p2);
        l2.drawLine(p3,p4);

        Cramer c = new Cramer();
        c.crossingPointCramer(l1,l2);

        //3
        Triangle triangle=new Triangle();
        triangle.triangleArea(p1,p2,p3);
    }
}
