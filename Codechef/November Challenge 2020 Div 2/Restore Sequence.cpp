#include <bits/stdc++.h>
using namespace std;
int main() 
{
    int num=4000000,t,n,i,val;
    bool prime[num+1]; 
    vector <int>p;
    
    memset(prime, true, sizeof(prime)); 
    for (int p=2; p*p<=num; p++) 
        if (prime[p] == true) 
        { 
            for (i=p*p; i<=num; i += p) 
                prime[i] = false; 
        } 
    for(i=2;i<=num;i++)
    {
        if(prime[i])
            p.push_back(i);
    }
    cin>>t;
    while(t--)
    {
        cin>>n;
        vector <int>a,b;
        for(i=0;i<n;i++)
        {
            cin>>val;
            b.push_back(val);
        }
        for(i=0;i<n;i++)
            a.push_back(p[i]);
        for(i=0;i<n;i++)
            cout<<a[b[i]-1]<<" ";
        cout<<"\n"; 
    }
}
