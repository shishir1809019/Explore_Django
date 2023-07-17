#include <bits/stdc++.h>
using namespace std;

int isPalindrome(string S)
{
    string P = S;
    reverse(P.begin(), P.end());
    if (S == P) {
        return 1;
    }
    else {
        return 0;
    }
}
 
int main()
{
    int t;
    cin>>t;
    while (t--)
    {
        string s;
        cin>>s;
        string temp = s;
        bool find =  false;
        for(int i = 0; i<s.length()/2; i++){
                swap(s[i], s[i+1]);
                swap(s[s.length()-i-1],s[s.length()-i-2]);
                if(s!=temp){
                        if(isPalindrome(s)){
                        find = true;
                        break;
                }
                        }

        }
        if(find) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    
 
    return 0;
}