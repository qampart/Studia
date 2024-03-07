package go;

import java.awt.*;

public class Line {
    Point head;
    Point tail;

    double a; //y=ax+b
    double b;

    final static double tolerance = 0.5;

    public Line(Point head, Point tail) {
        this.head = head;
        this.tail = tail;
    }

    public Line(double a, double b) {
        this.a = a;
        this.b = b;
    }

    public void drawLine(Point head, Point tail) { //2
        //head (x1,y1)
        //tail (x2,y2)
        this.a = (head.y- tail.y)/(head.x- tail.x);   //a=(y1-y2)/(x1-x2)
        this.b = head.y-this.a* head.x;               //b=y1-ax1

        System.out.println("y="+a+"*x+"+b);
    }

    public static void calcFunc(Point p1, Point p2, double[] tab){
        double a=(p1.y-p2.y)/(p1.x-p2.x); //a=(y1-y2)/(x1-x2)
        double b=p1.y-a*p1.x;        //b=y1-ax1
        tab[0]=a;
        tab[1]=b;
        System.out.println("a: "+tab[0]+", b: "+ tab[1]);
    }

    public void whichSide(Line l1, Point p3){
        //y=ax+b -> ax+b-y
        double sum= l1.a* p3.x- p3.y+ l1.b;
        if (sum>0){
            System.out.println("Right side of the straight");
        }
        else if(sum<0){
            System.out.println("Left side of the straight");
        }
        else if (sum==0){
            System.out.println("On the straight");
        }

    }

    public boolean ifBelongLine(Point point){ //3b
        double tmp=a*point.x+b;
        if (point.y>=(tmp-tolerance) && point.y<=(tmp+tolerance))
        {
            return true;
        }
        return false;
    }

    public boolean ifBelongStretch(Point point){ //3a

        if (ifBelongLine(point)
                && (head.x<=point.x && tail.x>=point.x)
                && (head.y<=point.y && tail.y>=point.y))
        {
            return true;
        }
        return false;
    }

    public void shiftVector (Vector vector){ //4
        head.x+= vector.x;
        head.y+= vector.y;
        tail.x+= vector.x;
        tail.y+= vector.y;

        //System.out.println("y="+a+"*x+"+b);

        this.a = (head.y- tail.y)/(head.x- tail.x);   //a=(y1-y2)/(x1-x2)
        this.b = head.y-this.a* head.x;               //b=y1-ax1
        System.out.println("y="+a+"*x+"+b);

    }
}
