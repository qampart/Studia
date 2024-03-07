import java.util.Random;

public class Point {
    double x;
    double y;

    //final static double tolerance = 1;

    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    Point(){
        Random random = new Random();
        this.x = (double)random.nextInt(21) - 10;
        this.y = (double) random.nextInt(21) - 10;

//        System.out.println("x="+x);
//        System.out.println("y="+y);
    }

    public void rotation(double alpha) // 5
    {
        double xp;
        double yp;

        //System.out.println(x);
        //System.out.println(y);

        if(alpha == 0 || alpha == 180)
        {
            xp = x; //xcos(a)-ysin(a) => x*1-y*0
            yp = y; //ycos(a)+xsin(a) => y*1+x*0
        }
        else if(alpha == 90 || alpha == 270)
        {
            xp = -y; //xcos(a)-ysin(a) => x*0-y*1
            yp = x; //ycos(a)+xsin(a) => y*0+x*1
        }
        else{
            double r = Math.toRadians(alpha);
            xp = x * Math.cos(r) - y * Math.sin(r);
            yp = y * Math.cos(r) + x * Math.sin(r);
        }

        x = xp;
        y = yp;
        //System.out.println(x);
        //System.out.println(y);
    }

    public void Ox() // 6; dla Oy analogicznie
    {
        System.out.println("("+x+","+y+")");
        double xp =x ;
        x = -xp;
        System.out.println("("+x+","+y+")");
    }

    public void Oy() // 6
    {
        System.out.println("("+x+","+y+")");
        double yp =y ;
        y = -yp;
        System.out.println("("+x+","+y+")");
    }

    public void OxOy()
    {
        System.out.println("("+x+","+y+")");
        double xp =x ;
        x = -xp;
        double yp =y ;
        y = -yp;
        System.out.println("("+x+","+y+")");
    }

}
