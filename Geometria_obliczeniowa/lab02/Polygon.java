import java.util.ArrayList;
import java.util.Arrays;

import static java.lang.Math.abs;

public class Polygon {

    ArrayList<Point> points;
    ArrayList<Point> hull;
    ArrayList<Point> inner;
    ArrayList<Line> lines;

    Polygon(ArrayList<Point> points){
        this.points = points;
        this.hull = new ArrayList<>();
        this.inner = new ArrayList<>();
        this.lines = new ArrayList<>();
    }

    public ArrayList<Line> returnLines(){
        return lines;
    }

}
