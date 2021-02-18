#include <iostream>
using namespace std;
int main() 
{
    int t,k,d,n;
    cin>>t;
    while(t--)
    {
        cin>>n>>k>>d;
        int A[n],s=0;
        for(int i=0;i<n;i++)
        {
            cin>>A[i];
            s+=A[i];
        }
        if (s/k>d)
            cout<<d<<endl;
        else
            cout<<s/k<<endl;
    }
	return 0;
}
