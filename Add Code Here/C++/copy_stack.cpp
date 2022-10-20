#include <bits/stdc++.h>
using namespace std;
int main()
{
    stack<int> stack1;
    stack<int> stack2;
    int a;
    for(int i=0; i<5; i++)
    {
        cin>>a;
        stack1.push(a);
    }
    for (int i = 0; i < 5; i++)
    {
        stack2.push(stack1.top());
        stack1.pop();
    }
    for(int i = 0; i < 5; i++)
    {
        cout<<stack2.top();
        stack2.pop();
    }
    
}