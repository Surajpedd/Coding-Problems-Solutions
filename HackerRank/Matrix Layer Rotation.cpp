#include <iostream>
#include<vector>
using namespace std;
// Complete the matrixRotation function below.
void rotate(int outer[],int c)
{
    int temp=outer[c-1],i;
    for(i=c-1;i>0;i--)
        outer[i]=outer[i-1];
    outer[0]=temp;
}
void matrixRotation(vector<vector<int>> matrix, int r,int m,int n) 
{
    int i,c;
    for(int j=0;j<min(m,n)/2;j++)
    {
        int outer[m*n];
        c=0;
        for(i=j;i<m-j;i++)         
        {
            outer[c]=matrix[i][j];
            c++;
        }
        for(i=j+1;i<n-j;i++)
        {
            outer[c]=matrix[m-1-j][i];
            c++;
        }
        for(i=m-2-j;i>=j;i--)
        {
            outer[c]=matrix[i][n-1-j];
            c++;
        }
        for(i=n-2-j;i>j;i--)
        {
            outer[c]=matrix[j][i];
            c++;
        }
        for(i=0;i<r%c;i++)
            rotate(outer,c);
        c=0;
        for(i=j;i<m-j;i++)
        {
            matrix[i][j]=outer[c];
            c++;
        }
        for(i=j+1;i<n-j;i++)
        {
            matrix[m-1-j][i]=outer[c];
            c++;
        }
        for(i=m-2-j;i>=j;i--)
        {
            matrix[i][n-1-j]=outer[c];
            c++;
        }
        for(i=n-2-j;i>j;i--)
        {
            matrix[j][i]=outer[c];
            c++;
        }
    }
    for(i=0;i<m;i++)
    {
        for(c=0;c<n;c++)
        cout<<matrix[i][c]<<' ';
        cout<<"\n";
    } 
}

int main()
{
    int m,n,r,x;
    vector<vector<int>> matrix;
    cin>>m>>n>>r;
    for(int i=0;i<m;i++)
    {
        vector<int> v;
        for(int j=0;j<n;j++)
        {
            cin>>x;
            v.push_back(x);
        }
        matrix.push_back(v);
    }
    matrixRotation(matrix,r,m,n);
}
