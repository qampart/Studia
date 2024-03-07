
public class Line {
    Point head;
    Point tail;

    double a; //y=ax+b
    double b;

    final static double tolerance = 0.5;

    public Line(Point head, Point tail) {
        this.head = head;
        this.tail = tail;
        drawLine(head, tail);
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

    //Zajecia4
    //Zadnie1
    public Line()// a = tg alpha
    {
        double start = 89.99, end = -89.99;
        double alpha = Math.random()*(end - start) + start;
        double radians = Math.toRadians(alpha);
        a = (int) Math.tan(radians);
        b = (int) (Math.random()*20) - 10;
    }

    static void whichSideRandom(){
        //y=ax+b -> ax+b-y

        Line l=new Line();
        Point p=new Point();

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
