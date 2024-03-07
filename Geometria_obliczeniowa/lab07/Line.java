package go;

public class Line {
    Point head;
    Point tail;

    double a; //y=ax+b
    double b;

    final static double tolerance = 0.5;

    Line(Point head, Point tail) {
        this.head = head;
        this.tail = tail;
        drawLine(head, tail);
    }

    Line(double a, double b) {
        this.a = a;
        this.b = b;
    }

    public void drawLine(Point head, Point tail) {
        //head (x1,y1)
        //tail (x2,y2)
        this.a = (head.y- tail.y)/(head.x- tail.x);   //a=(y1-y2)/(x1-x2)
        this.b = head.y-this.a* head.x;               //b=y1-ax1

        System.out.println("y="+a+"*x+"+b);
    }

    static void whichSide(Line l, Point p){
        //y=ax+b -> ax+b-y

        double sum= l.a* p.x- p.y+ l.b;
        System.out.println("sum="+sum);
        System.out.println("a="+l.a);
        System.out.println("b="+l.b);
        if (sum>0.0){
            System.out.println("Right side of the straight");
        }
        else if(sum<0.0){
            System.out.println("Left side of the straight");
        }
        else if (sum==0.0){
            System.out.println("On the straight");
        }

    }
}
