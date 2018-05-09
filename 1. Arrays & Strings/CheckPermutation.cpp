/* Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other. */

/*
Other possible solutions:
- Count the number of characters in each string and then compare
*/
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

/* Sorting takes O(Nlog(N)) and then O(N) comparison
Algorithm is case-senstive */
bool checkPermutation(string str, string str2){

    if(str.length() != str2.length())
        return false;

    sort(str.begin(), str.end());
    sort(str2.begin(), str2.end());

    for(unsigned int i = 0; i < str.length(); i++){
        if(str[i] != str2[i])
            return false;
    }

    return true;
}


int main(){

    string str = "test";
    string str2 = "tset";   // Return true
    cout << checkPermutation(str, str2) << endl;

    return 0;
}
