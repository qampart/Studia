package go;

import static java.lang.Math.pow;

public class Triangle {
    Point point1;
    Point point2;
    Point point3;

    public Triangle(Point point1, Point point2, Point point3) {
        this.point1 = point1;
        this.point2 = point2;
        this.point3 = point3;
    }

    static boolean ifTriagnleExist(Point p1, Point p2, Point p3) {

        double AB=Math.sqrt(pow((p2.x-p1.x),2)+pow((p2.y-p1.y),2));
        double BC=Math.sqrt(pow((p3.x-p2.x),2)+pow((p3.y-p2.y),2));
        double AC=Math.sqrt(pow((p3.x-p1.x),2)+pow((p3.y-p1.y),2));

        if(AB<BC+AC && BC<AB+AC && AC<AB+BC){
            return true;
        }
        else{
            return false;
        }
    }

    static double triangleArea(Point p1, Point p2, Point p3) {

        if(ifTriagnleExist(p1, p2, p3)) {
            double area = 0.5 * Math.abs((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y));
            System.out.println(area);
            return area;
        }
        else {
            System.out.println("Triangle does not exist");
            return 0;
        }
    }

    static void pointAndTriangle(Point p1,Point p2,Point p3,Point random) {

        System.out.println("P1=" + "(" + p1.x + "," + p1.y + ")");
        System.out.println("P2=" + "(" + p2.x + "," + p2.y + ")");
        System.out.println("P3=" + "(" + p3.x + "," + p3.y + ")");

        System.out.println("random=" + "(" + random.x + "," + random.y + ")");

        //Area of whole triangle
        System.out.println("The area of the whole triangle is equal: ");
        double whole = triangleArea(p1, p2, p3);

        System.out.println("The area of the smaller triangles is equal: ");
        double abr = triangleArea(p1, p2, random);
        double arc = triangleArea(p1, random, p3);
        double rbc = triangleArea(random, p2, p3);

        if (whole == (abr + arc + rbc)) {
            System.out.println("The point belongs to the triangle");
        }
        else {
            System.out.println("Point outside the triangle");
        }
    }
}
