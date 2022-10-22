import java.util.*;
import static java.lang.System.out;

public class C_SaveMoreMice {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = 1;
        t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt();
            int m = in.nextInt();
            Integer[] arr = new Integer[m];
            for (int i = 0; i < m; i++) {
                int a = in.nextInt();
                arr[i] = a;
            }
            int position = 0;
            Arrays.sort(arr);
            int ans = 0;
            int dif1 = 0;
            int dif2 = 0;
            for (int i = m - 1; i >= 0; i--) {
                dif1 = arr[i] - position;
                dif2 = n - arr[i];
                if (dif1 > 0) {
                    ans++;
                    position += dif2;
                }
            }
            out.println(ans);
        }
    }
}
