import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.util.*;

import static java.lang.Math.*;

public class Delaunay {
    List<Point> points;
    List<Line2D> lines;
    List<Triangle> triangles;
    Random random=new Random();

    Delaunay(List<Point> point) {
        this.points = point;
        this.lines = new ArrayList<>();
        this.triangles = new ArrayList<>();
        this.random = new Random();
        generate();
    }

    private void main(){
        for(Point point:points){
            Map<Integer, Line> buffer = new HashMap<>();
            List<Triangle> removeTriangle = new ArrayList<>();
            for(Triangle triangle:triangles){
                Point p0 = triangle.centerCircumscribedCircle();
                if(p0==null)
                    break;
                double r = sqrt(pow(triangle.p1.x-p0.x, 2) + pow(triangle.p1.y - p0.y, 2));
                if(sqrt(pow(point.x - p0.x, 2) + pow(point.y - p0.y, 2))<r){ //w którym okręgu opisanym w trójkącie znajduje się punkt
                    Line e1 = new Line(triangle.p1, triangle.p2);
                    Line tmp = buffer.put(e1.hash(), e1);
                    buffer.remove(tmp!=null?e1.hash():null);

                    Line e2 = new Line(triangle.p2, triangle.p3);
                    tmp = buffer.put(e2.hash(), e2);
                    buffer.remove(tmp!=null?e2.hash():null);

                    Line e3 = new Line(triangle.p1, triangle.p3);
                    tmp = buffer.put(e3.hash(), e3);
                    buffer.remove(tmp!=null?e3.hash():null);

                    removeTriangle.add(triangle);
                }
            }
            triangles.removeAll(removeTriangle);

            for(Map.Entry<Integer, Line> edge:buffer.entrySet()){
                triangles.add(new Triangle(edge.getValue().p1, edge.getValue().p2, point));
            }
        }
    }

    public void generate(){
        double left = 1000;
        double right = 0;
        double down = 0;
        double up = 1000;

        for(Point p:points) {
            left = Math.min(p.x, left);
            right = Math.max(p.x, right);
            down = Math.max(p.y, down);
            up = Math.min(p.y, up);
        }

        double x = right - left;
        double y = up - down;

        Point p1 = new Point(left-10, down+10);
        Point p2 = new Point(left-20, up+y-20);
        Point p3 = new Point(right + x+30, down+30);

        Triangle t = new Triangle(p1, p2, p3);
        this.triangles.add(t);
        this.main();

        removeSuperTriangle(p1, p2, p3);
        this.drawLines();
    }

    public void drawLines(){
        //System.out.println(triangles.size());
        for(Triangle t:triangles){
            lines.add(new Line2D.Double(new Point2D.Double(t.p1.x, t.p1.y), new Point2D.Double(t.p2.x, t.p2.y)));
            lines.add(new Line2D.Double(new Point2D.Double(t.p2.x, t.p2.y), new Point2D.Double(t.p3.x, t.p3.y)));
            lines.add(new Line2D.Double(new Point2D.Double(t.p1.x, t.p1.y), new Point2D.Double(t.p3.x, t.p3.y)));
        }
    }

    private void removeSuperTriangle(Point p1, Point p2, Point p3){
        triangles.removeIf(t -> t.contains(p1) || t.contains(p2) || t.contains(p3));
    }
}


