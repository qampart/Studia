package QuadTree;

import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.abs;
import static java.lang.Math.pow;

class Node {
    double x, y;
    Node leftUp, rightUp, leftDown, rightDown, parent;

    public Node(double x, double y, Node parent) {
        this.x = x;
        this.y = y;
        this.leftUp = null;
        this.rightUp = null;
        this.leftDown = null;
        this.rightDown = null;
        this.parent = parent;
    }
}

public class Tree {
    Node root;
    List<Line2D> section;
    int x, y; //rozmiar obrazu

    public Tree(BufferedImage image){
        this.root = new Node(0,0,null);
        x = image.getWidth();
        y = image.getHeight();
        treeFromImage(image, root, 0);
        section = new ArrayList<>();
        print(root, 0);
    }

    public boolean treeFromImage(BufferedImage image, Node tmp, int l){
        if(l<6){ //dokladnosc
            double dx = x/pow(2, l) - 1;
            double dy = y/pow(2, l) - 1;
            int i=0;
            int rg = image.getRGB((int)tmp.x, (int)tmp.y); //kolor, lewy gorny rog
            int g = ((rg>>8)&0xff);
            int r = ((rg>>16)&0xff);
            int b = ((rg)&0xff);
            boolean found = false;  //jeśli znaleziono zmiane koloru to nalezy podzielic dany fragment
            while(i<=dx + dy){      //znajduje zmianę koloru
                int c1 = 0, c2 = 0;
                if(i<=dy){
                    c1 = image.getRGB((int)tmp.x, (int)tmp.y+i);         //lewa
                    c2 = image.getRGB((int)(tmp.x+dx), (int)(tmp.y+i));     //prawa
                }
                else if(i>dy && i<=dy+dx){
                    c1 = image.getRGB((int)(tmp.x+i-dy), (int)(tmp.y));     //gora
                    c2 = image.getRGB((int)(tmp.x+i-dy), (int)(tmp.y+dy)); //dol
                }

                int c1B = ((c1)&0xff);
                int c1R = ((c1>>16)&0xff);
                int c1G = ((c1>>8)&0xff);
                int c2R = ((c2>>16)&0xff);
                int c2G = ((c2>>8)&0xff);
                int c2B = ((c2)&0xff);

                if((abs(c1R - r)>=1 || abs(c2R - r)>=1) || (abs(c1G - g)>=1 || abs(c2G - g)>=1 ) || (abs(c1B - b)>=1 || abs(c2B - b)>=1) ){ //tolerancja
                    found = true;
                    break;
                }

                i++;
            }

            if(!found)
                return false;

            Node leftUp = new Node(tmp.x, tmp.y, tmp);
            tmp.leftUp = treeFromImage(image, leftUp, l + 1)?leftUp:null;

            Node rightUp = new Node(tmp.x + dx/2, tmp.y, tmp);
            tmp.rightUp = treeFromImage(image, rightUp, l + 1)?rightUp:null;

            Node leftDown = new Node(tmp.x, tmp.y + dy/2, tmp);
            tmp.leftDown = treeFromImage(image, leftDown, l + 1) ?leftDown:null;

            Node rightDown = new Node(tmp.x + dx/2, tmp.y + dy/2, tmp);
            tmp.rightDown = treeFromImage(image, rightDown, l + 1)?rightDown:null;
        }

        return true;
    }

    public void print(Node node, int i){
        if(node!=null){
            double dx = x/pow(2, i)-1;
            double dy = y/pow(2, i)-1;
            section.add(new Line2D.Double(node.x + dx/2, node.y , node.x + dx/2, node.y + dy)); //linia pionowa
            section.add(new Line2D.Double(node.x, node.y+dy/2 , node.x + dx, node.y + dy/2));   //linia pozioma
            print(node.leftDown, i+1);
            print(node.leftUp, i+1);
            print(node.rightDown, i+1);
            print(node.rightUp, i+1);
        }
    }
}
