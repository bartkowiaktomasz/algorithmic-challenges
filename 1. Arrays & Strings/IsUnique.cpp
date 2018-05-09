/* Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures? */

/*
Other possible solutions:
- Sort the string in O(Nlog(N) and compare neighbouring characters
- Hash each character and check if table entry empty
*/
#include <iostream>
#include <string>

using namespace std;

/* Implementation in O(N^2) without using any additional data structure */
bool isUnique(string str){
    for(unsigned int i = 1; i < str.length(); i++){
        for(unsigned int j = 0; j < i; j++){
            if(str[i] == str[j])
                return false;
        }
    }
    return true;
}

/* Implementation in O(N) using additional static storage array */
bool isUniqueLinear(string str){
    unsigned int ASCII_SIZE = 128;
    int strArr[ASCII_SIZE];

    for(unsigned int i = 0; i < ASCII_SIZE; i++){
        strArr[i] = 0;
    }
    for(unsigned int i = 0; i < str.length(); i++){
        if(strArr[int(str[i])] != 0)
            return false;
        strArr[int(str[i])]++;
    }
    return true;
}

int main(){

    string str = "test";    // Return false
    cout << isUnique(str) << endl;
    cout << endl << isUniqueLinear(str) << endl;

    return 0;
}
