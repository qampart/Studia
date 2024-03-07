public class Triangle {
    Point point1;
    Point point2;
    Point point3;

    public Triangle(Point point1, Point point2, Point point3) {
        this.point1 = point1;
        this.point2 = point2;
        this.point3 = point3;
    }

    static double triangleArea(Point p1, Point p2, Point p3) {
        double area = 0.5 * Math.abs((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y));
        System.out.println("The area of the triangle is equal: " + area);
        return area;
    }
   static void randomTriangle() {

        Point p1 = new Point();
        System.out.println("P1=" + "(" + p1.x + "," + p1.y + ")");
        Point p2 = new Point();
        System.out.println("P2=" + "(" + p2.x + "," + p2.y + ")");
        Point p3 = new Point();
        System.out.println("P3=" + "(" + p3.x + "," + p3.y + ")");

        Point random = new Point();
        System.out.println("random=" + "(" + random.x + "," + random.y + ")");

        Triangle triangle=new Triangle(p1,p2,p3);

        //Area of whole triangle
        double whole = triangleArea(p1, p2, p3);

        double abr = triangleArea(p1, p2, random);
        double arc = triangleArea(p1, random, p3);
        double rbc = triangleArea(random, p2, p3);

        if (whole == (abr + arc + rbc)) {
            System.out.println("The point belongs to the triangle");
        } else {
            System.out.println("Point outside the triangle");
        }
    }
}
