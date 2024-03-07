package go;

import java.awt.*;


public class Triangle {
    void triangleArea(Point p1, Point p2, Point p3){
        double area=0.5*Math.abs((p2.x-p1.x)*(p3.y-p1.y)-(p3.x-p1.x)*(p2.y-p1.y));
        System.out.println("The area of the triangle is equal: "+area);
    }
}
