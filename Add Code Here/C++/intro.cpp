#include <bits/stdc++.h>
using namespace std;
int main()
{
    stack<int> stacked;
    int i = 0;
    cin>>i;
    for(int j=0; j<=i; j++)
    {
        cin>>j;
        stacked.push(j);
    }
    while(!stacked.empty()) { 
		cout << stacked.top() << " ";
        stacked.pop();
    }
}