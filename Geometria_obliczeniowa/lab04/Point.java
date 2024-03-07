import java.util.*;

class Point
{
    int x;
    int y;
    Random r= new Random();
    Point (){
        this.x=r.nextInt(15);
        this.y=r.nextInt(12);
    }
}

class ConvexHull {

    Random r= new Random();

    public int orientation(Point p, Point q, Point r)
    {
        int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);

        if (val == 0) return 0;  //współliniowe
        return (val > 0)? 1: 2;
    }

    public void convexHull(Point points[], int n)
    {
        Vector<Point> hull = new Vector<Point>();

        //Punkt najbardziej po lewej
        int l = 0;
        for (int i = 1; i < n; i++)
            if (points[i].x < points[l].x)
                l = i;

        //Przeciwnie do ruchu wskazowek zegara, az do punktu poczatkowego
        int p = l, q;
        do
        {
            hull.add(points[p]);
            q = (p + 1) % n;

            for (int i = 0; i < n; i++)
            {
                if (orientation(points[p], points[i], points[q]) == 2)
                    q = i;
            }
            p = q;

        } while (p != l);

        for (Point temp : hull)
            System.out.println("(" + temp.x + ", " +
                    temp.y + ")");
    }

    public void generate(){
        int a=r.nextInt(20)+5;
        Point points[] = new Point[a];
        for (int i=0;i<points.length;i++){
            points[i]=new Point();
        }


        System.out.println("Punkty:");
        for (int i=0; i<points.length;i++){
            System.out.println("Punkt "+(i+1)+": "+"("+points[i].x+","+points[i].y+")");
        }

        System.out.println("\nPunkty otoczki:");
        int n = points.length;
        convexHull(points, n);
    }
}