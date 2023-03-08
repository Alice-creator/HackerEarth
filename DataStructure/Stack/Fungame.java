import java.io.*;
import java.util.*;

public class Fungame
{
    public static void main(String [] args)
    {
        // String result = new String();
        String [] str;
        Scanner myReader = new Scanner(System.in);
        String data = myReader.nextLine();
        data =  myReader.nextLine();
        str = data.split(" ");
        int A = 0; 
        int B = str.length - 1;
        while(A < str.length - 1 && B > 0)
        {
            if(Integer.parseInt(str[A]) > Integer.parseInt(str[B]))
            {
                System.out.print("1 ");
                B--;
            }
            else if(Integer.parseInt(str[A]) < Integer.parseInt(str[B]))
            {
                System.out.print("2 ");
                A++;
            }
            else
            {
                System.out.print("0 ");
                B--;
                A++;
            }
        }
        if(Integer.parseInt(str[A]) > Integer.parseInt(str[B]))
            System.out.print("1");
        else if(Integer.parseInt(str[A]) < Integer.parseInt(str[B]))
            System.out.print("2");
        else
            System.out.print("0");
    }
}