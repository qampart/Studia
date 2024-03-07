import static java.lang.Math.pow;

public class Circle {
    Point s=new Point(0,0);
    double r;

    public Circle(double r) {
        this.r = r;
        //System.out.println(s.x);
    }

    void lineAndCircle(double r){
        Cramer cramer=new Cramer();
        Point head=new Point();
        Point tail=new Point();
        Line line=new Line(head, tail);
        double a= line.a;
        double b=line.b;
        System.out.println("(x,y)="+"("+head.x+ ","+head.y+")");
        System.out.println("(x,y)="+"("+tail.x+ ","+tail.y+")");

        //x1=head
        //x2=tail
        //x0=s
        double A=pow(head.x,2)+pow(head.y, 2)+pow(tail.x,2)+pow(tail.y, 2)-2*(head.x* tail.x+(head.y*tail.y));
        double B=2*(s.x*(tail.x- head.x)+s.y*(tail.y- head.y)+ head.x*tail.x+head.y*tail.y-pow(tail.x,2)-pow(tail.y,2));
        double C=pow(r,2)*(-1)+pow(tail.x,2)+pow(tail.y,2)+pow(s.x,2)+pow(s.y,2)-2*(s.x*tail.x+s.y*tail.y);

        double delta=pow(B,2)-4*A*C;
        if (delta>0){
            System.out.println("Dwa punkty przeciecia");
            cramer.crossingCircle(a,b,r);
        }
        else if(delta==0){
            System.out.println("Jeden pkt przeciecia");
        }
        else{
            System.out.println("Nie przcinaja sie");
        }
    }

}
