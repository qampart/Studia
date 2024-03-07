import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

public class Cramer {
    void crossingPointCramer (double A1, double B1, double C1, double A2, double B2, double C2){
        double W = A1*B2-A2*B1;
        double Wx = C2*B1-C1*B2;
        double Wy = A2*C1-A1*C2;

        System.out.println("Cross point:");
        System.out.println("(x,y) = (" + Wx/W + ","+Wy/W+")");
    }

    void crossingPointCramer (Line l1, Line l2){
        //y=ax+b -> ax+b-y=0
        //Ax+By+C=0
        //Ax+By+C=ax-y+b
        //A=a  B=-1     C=b => C=-1
        this.crossingPointCramer(l1.a, -1, l1.b, l2.a, -1, l2.b);
        System.out.println(l1.a+", "+ l1.b+", ");
        System.out.println(l2.a+", "+ l2.b+", ");
    }

    void crossingCircle(double a, double b, double r){
        double delta=4*(pow(r,2)+pow(a,2)*pow(r,2)-pow(b,2));
        double x1=(-2*a*b-sqrt(delta))/(2*(pow(a,2)+1));
        double x2=(-2*a*b+sqrt(delta))/(2*(pow(a,2)+1));
        double y1=(a*x1)+b;
        double y2=(a*x2)+b;

        System.out.println("(x1,y1)="+"("+x1+","+y1+")");
        System.out.println("(x2,y2)="+"("+x2+","+y2+")");
    }

}
