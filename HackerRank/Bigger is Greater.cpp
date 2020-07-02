#include <iostream>
#include<algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string s;
        cin>>s;
        if(next_permutation(s.begin(),s.end())==false) 
            cout<<"no answer"<<endl;
        else 
            cout<<s<<endl;
    }
}
