#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int T,n,val,i;
    cin>>T;
    while(T--)
    {
        cin>>n;
        vector <int>a,x,y;
        for(i=0;i<n;i++)
        {
            cin>>val;
            a.push_back(val);
        }
        sort(a.begin(),a.end(),greater<int>());
        
        x.push_back(a[0]);
        y.push_back(0);
        for (int i=1; i<a.size();i++)
        {
            if( accumulate(y.begin(), y.end(), 0)<=accumulate(x.begin(), x.end(), 0) )
                y.push_back(a[i]);
            else
                x.push_back(a[i]);
        }
        cout<<max(accumulate(y.begin(), y.end(), 0),accumulate(x.begin(), x.end(), 0))<<"\n";
    }
	return 0;
}
