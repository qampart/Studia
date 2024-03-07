package go;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // write your code here
        Scanner scan = new Scanner(System.in);

        System.out.println("[1] Calculation of the point of crossing two lines.");
        System.out.println("[2] Finding the line passing through two points. Enter two points.");
        System.out.println("[3] Define the position of the point in relation to the line.");
        System.out.println("[4] Defining the position of a point in relation to a triagle.");
        System.out.println("[5] Calculating the area of a triangle.");
        int selection = 0;

        try {
            selection = scan.nextInt();
        }catch(Exception e){
            System.err.println("Data not valid");
        }

        while (selection == 1 || selection == 2 || selection == 3 || selection == 4 || selection == 5) {

            // I Obliczenie punktu przecięcia dwóch linii
            if (selection == 1) {
                System.out.println("Calculation of the point of crossing two lines.");
                System.out.println("Enter 1 if you want to enter line coefficients and 2 to create lines, each from two points");
                int choice = scan.nextInt();

                if (choice == 1) {
                    System.out.println("Entrer the A, B, C coefficients of the first line:");
                    int A1 = scan.nextInt();
                    int B1 = scan.nextInt();
                    int C1 = scan.nextInt();
                    System.out.println("Entrer the A, B, C coefficients of the second line:");
                    int A2 = scan.nextInt();
                    int B2 = scan.nextInt();
                    int C2 = scan.nextInt();
                    Cramer cramer = new Cramer();
                    cramer.crossingPointCramer(A1, B1, C1, A2, B2, C2);
                }
                else if (choice == 2) {
                    System.out.println("Enter points for the first straight.\nPoint 1:");
                    int x11 = scan.nextInt();
                    int y11 = scan.nextInt();
                    System.out.println("Point2:");
                    int x12 = scan.nextInt();
                    int y12 = scan.nextInt();
                    Line line1 = new Line(new Point(x11, y11), new Point(x12, y12));

                    System.out.println("Enter points for the first straight.\nPoint 1:");
                    int x21 = scan.nextInt();
                    int y21 = scan.nextInt();
                    System.out.println("Point2:");
                    int x22 = scan.nextInt();
                    int y22 = scan.nextInt();
                    Line line2 = new Line(new Point(x21, y21), new Point(x22, y22));
                    Cramer cramer = new Cramer();
                    cramer.crossingPointCramer(line1, line2);
                }
                else
                    System.err.println("Wrong number");
            }

            // II Wyznaczenie równania funkcji przchodzącej przez dwa punkty
            else if (selection == 2) {
                System.out.println("Finding the line passing through two points. Enter two points.\nPoint1:");
                int x1 = scan.nextInt();
                int y1 = scan.nextInt();
                System.out.println("Point 2:");
                int x2 = scan.nextInt();
                int y2 = scan.nextInt();
                if(x1==x2){
                    System.out.println("straight x="+x1);
                }
                else {
                    Line line = new Line(new Point(x1, y1), new Point(x2, y2));
                }
            }

            // III Określenie położenia punktu względem linii
            else if (selection == 3) {
                System.out.println("Define the position of the point in relation to the line.");
                System.out.println("Enter 1 if you want to enter line coefficients and 2 to create lines, each from two points");
                int c = scan.nextInt();

                if (c == 1) {
                    System.out.println("y=ax+b\nEnter a:");
                    int a = scan.nextInt();
                    System.out.println("Enter b:");
                    int b = scan.nextInt();
                    Line line4 = new Line(a, b);
                    System.out.println("Enter point:");
                    int x = scan.nextInt();
                    int y = scan.nextInt();

                    Line.whichSide(line4, new Point(x, y));
                }
                else if (c == 2) {
                    System.out.println("Finding the line passing through two points. Enter two points.\nPoint1:");
                    int x4 = scan.nextInt();
                    int y4 = scan.nextInt();
                    System.out.println("Point 2:");
                    int x42 = scan.nextInt();
                    int y42 = scan.nextInt();
                    if(x4==x42){
                        System.out.println("straight x="+x4);
                        System.out.println("Enter point:");
                        int x = scan.nextInt();
                        int y = scan.nextInt();
                        if(x>x4){
                            System.out.println("Right side of the straight");
                        }
                        else if(x<x4){
                            System.out.println("Left side of the straight");
                        }
                        else{
                            System.out.println("On the straight");
                        }

                    }
                    else {
                        Line line4 = new Line(new Point(x4, y4), new Point(x42, y42));
                        System.out.println("Enter point:");
                        int x = scan.nextInt();
                        int y = scan.nextInt();
                        Line.whichSide(line4, new Point(x, y));
                    }

                }
                else
                    System.err.println("Wrong number.");
            }

            // IV Określenie położnenia punktu względem trójkąta
            else if (selection == 4) {
                System.out.println("Defining the position of a point in relation to a triagle. Enter the vertices of the triangle.\nPoint1:");
                int vertice1x = scan.nextInt();
                int vertice1y = scan.nextInt();
                System.out.println("Point2:");
                int vertice2x = scan.nextInt();
                int vertice2y = scan.nextInt();
                System.out.println("Point3:");
                int vertice3x = scan.nextInt();
                int vertice3y = scan.nextInt();
                System.out.println("The point whose position you would like to check");
                int randomx = scan.nextInt();
                int randomy = scan.nextInt();

                Triangle.pointAndTriangle(new Point(vertice1x, vertice2y), new Point(vertice2x, vertice2y), new Point(vertice3x, vertice3y), new Point(randomx, randomy));
            }

            //V Obliczy pole trójkąta
            else if (selection == 5) {
                System.out.println("Calculating the area of a triangle.\nThe vertex 1:");
                int v1x = scan.nextInt();
                int v1y = scan.nextInt();
                System.out.println("The vertex 2:");
                int v2x = scan.nextInt();
                int v2y = scan.nextInt();
                System.out.println("The vertex 3:");
                int v3x = scan.nextInt();
                int v3y = scan.nextInt();

                System.out.println("The area of the triangle is equal:");
                Triangle.triangleArea(new Point(v1x, v1y), new Point(v2x, v2y), new Point(v3x, v3y));
            }

            System.out.println("[1] Calculation of the point of crossing two lines.");
            System.out.println("[2] Finding the line passing through two points. Enter two points.");
            System.out.println("[3] Define the position of the point in relation to the line.");
            System.out.println("[4] Defining the position of a point in relation to a triagle.");
            System.out.println("[5] Calculating the area of a triangle.");
            selection=scan.nextInt();
        }
        System.out.println("The end.");
    }

}
