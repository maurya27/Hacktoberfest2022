// C program to show the
// use of fabs() function
#include <math.h>
#include <stdio.h>

int main()
{
double a = 980;
double b = -1231;
double res;

res = fabs(a);
printf("The absolute value of %.3lf is %.3lf\n",
		a, res);

res = fabs(b);
printf("The absolute value of %.3lf is %.3lf\n",
		b, res);
return 0;
}
