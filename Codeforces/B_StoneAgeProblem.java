import java.util.*;
import java.io.*;
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.abs;
import static java.lang.System.out;

public class B_StoneAgeProblem{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int test = 1;
//        test = in.nextInt();
        while (test-- > 0) {
            int n = in.nextInt();
            long q = in.nextInt();
            long[] arr = new long[n];
            long rem = 0;
            for (int i = 0; i <n; i++) {
                int a = in.nextInt();
                arr[i]=a;
                rem+=arr[i];
            }
            long[] temp = new long[n];
            long cheak = 0;
            long change = -1;
            while(q-->0){
                int t= in.nextInt();
                if(t%2==1){
                    int i = in.nextInt()-1;
                    long x = in.nextInt();
                    if(temp[i]<cheak){
                        temp[i]=cheak;
                        arr[i]=change;
                    }
                    rem -=arr[i];
                    rem +=x;
                    arr[i]=x;
                }else{
                    long x = in.nextInt();
                    rem =x*n;
                    cheak++;
                    change = x;
                }
                out.println(rem);
            }
        }
    }
}