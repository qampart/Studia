import java.util.*;

public class Generator {

    Generator(){

        rand = new Random();
        poly = new ArrayList<>();

    }

    ArrayList<Point> poly;
    Polygon P;

    int canvasSize = 200; //self - explainatory
    Random rand;


    //Funkcja sprawdzająca przynależność punktu do wcześniej wygenerowanego wielokąta P
    String checkPolygonPoint(Point pointA){
        Line checkLine = new Line(pointA,new Point(canvasSize,(-200 + rand.nextInt(400))));
        int crossCounter = 0;
        for(Line a : P.returnLines()){
            if(a.checkIfPointInSectionPoly(checkLine.crossingPoint(a),pointA)){
                crossCounter ++;
            }
        }
        if(crossCounter%2 == 1){
            return "Punkt" + "("+pointA.x+","+pointA.y+")" +" znajduje się w wielokacie";
        }else{
            return "Punkt" +"("+pointA.x+","+pointA.y+")" + " znajduje się poza wielokątem";
        }
    }

}