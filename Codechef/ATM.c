
//ATM 
/*Code Chef*/


#include <stdio.h>

int main(void) {
   int w_amount;
   float balance;
   scanf("%d%f",&w_amount,&balance);
   if((w_amount%5==0)&&(w_amount+0.5)<=balance)
   {
       printf("%0.2f",balance-w_amount-0.5);
   }
   else
   {
       printf("%0.2f",balance);
   }
   
   
	return 0;
}

