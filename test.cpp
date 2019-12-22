#include <iostream>

using namespace std;

int main()
{
   cout << "Hello World" << endl; 
   
   for(int i=0;i<5;i++)
{
	for(int j=0;j<(5-i);j++)
	{
		cout<<"# ";
	}
	for(int j=0;j<(i*2);j++)
	{
		cout<<"  ";
	}
	for(int j=0;j<(5-i);j++)
	{
		cout<<"# ";
	}
	cout<< "\n";
}
   
   return 0;
}