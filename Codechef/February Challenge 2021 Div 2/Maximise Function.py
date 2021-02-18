#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n;
        cin>>n;
        long long int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        long long int res = 2*(*max_element(a,a+n)-*min_element(a,a+n));
        cout<<res<<"\n";
    }
	return 0;
}
