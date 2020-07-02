#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n,i,m;
    char x;
    vector <char> str;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>x;
        str.push_back(x);
    }
    cin>>m;
    for(i=0;i<n;i++)
    {
        if(str[i]>='A' && str[i]<='Z')
            str[i]=char( (str[i]+m-65)%26 +65 );
        else if(str[i]>='a' && str[i]<='z')
            str[i]=char((str[i]+m-97)%26 + 97);
        cout<<str[i];
    }
}
