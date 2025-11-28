#include<iostream>
#include<cmath>
using namespace std;
int main(){
	float a, b, c;
	cout<<"Enter coefficients a, b, c:";
	cin >>a >>b >>c;
	
	float d=b*b-4*a*c;
	
	if (d>0);
	float root1 = (-b + sqrt(d)) / (2*a);
	float root2 = (-b - sqrt(d)) / (2*a);
	cout << "Roots are real and distinct: " <<root1 <<"and" <<root2;
} 
  else if (d==0){
	float root = -b / (2*a);
	cout<<"Roots are real and equal:" <<root;
} else{
	float rael =-b / (2*a);
	float imag = sqrt(-d) / (2*a);
	cout << "Roots are complex:" <<real << "+" <<imag <<"i and" <<real<<"-" << imag<<	"i";
}
return 0;
 




