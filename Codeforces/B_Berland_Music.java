package Practices;

import java.util.*;
import java.lang.*;

import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.abs;
import static java.lang.System.out;

public class B_Berland_Music {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = 1;
        t = in.nextInt();
        while (t-- > 0) {
            int n= in.nextInt();
            int[] arr=new int[n];
            for (int i = 0; i < n; i++) {
                arr[i]= in.nextInt();
            }
            // sc.nextLine();
            String s = in.nextLine();
            ArrayList<Integer> list1 = new ArrayList<>();
            ArrayList<Integer> list2 = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if(s.charAt(i)=='0'){
                    list1.add(arr[i]);
                }else{
                    list2.add(arr[i]);
                }
            }
            Collections.sort(list1);
            Collections.sort(list2);
            HashMap<Integer,Integer> map = new HashMap<>();
            for (int i = 0; i < list1.size(); i++) {
                map.put(list1.get(i),i+1);
            }
            int size = list1.size()+1;
            for (int i = 0; i < list2.size(); i++) {
                map.put(list2.get(i),size+i);
            }
            for (int i =0; i <map.size(); i++) {
                out.print(map.get(arr[i])+" ");
            }
        }
    }
}

