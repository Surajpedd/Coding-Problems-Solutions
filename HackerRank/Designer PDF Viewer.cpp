#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int h[26],i,j;
    char str[20];
    for(i=0;i<26;i++)
    cin>>h[i];
    cin>>str;
    int ma[strlen(str)];
    for(i=0;i<strlen(str);i++)
        ma[i]=h[str[i]-97];
    int max=ma[0];
    for(i=0;i<strlen(str);i++)
        if(ma[i]>max)
            max=ma[i];
    cout<<max*strlen(str);
}
