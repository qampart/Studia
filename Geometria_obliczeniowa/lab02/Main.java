import java.io.Console;
import java.util.ArrayList;
import static java.lang.Math.pow;

public class Main {


    public static void main(String[] args) {


        //Zajecia4
        System.out.println("\n------Zadanie1------");
        Line.whichSideRandom();

        System.out.println("\n------Zadanie2------");
        Triangle.randomTriangle();

        System.out.println("\n------Zadanie3------");
        Generator gen = new Generator();
        gen.checkPolygonPoint(new Point(5,2));

        System.out.println("\n------Zadanie4------");
        Circle c=new Circle(5);
        c.lineAndCircle(5);
    }
}
