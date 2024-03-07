public class Point {
    double x, y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}

class Line {
    Point p1;
    Point p2;

    public Line(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public int hash(){
        return (int)(p1.x+p1.y+p2.x+p2.y);
    }
}

class Triangle {
    Point p1, p2, p3;

    public Triangle(Point p1, Point p2, Point p3) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
    }

    public Point centerCircumscribedCircle(){ //środek okręgu opisanego na trójkącie
        double a1 = (p1.x-p2.x)/(p2.y-p1.y);
        double b1 = (p1.y+p2.y)/2-a1*(p1.x+p2.x)/2;

        double a2 = (p1.x-p3.x)/(p3.y-p1.y);
        double b2 = (p3.y+p1.y)/2-a2*(p3.x+p1.x)/2;

        double x0 = (b2-b1)/(a1-a2);
        double y0 = x0*a1 + b1;
        return new Point(x0, y0);
    }

    public boolean contains(Point p){ //czy któryś z wierzchołków trójkąta jest danym punktem
        return p1.equals(p) || p2.equals(p) || p3.equals(p);
    }
}
