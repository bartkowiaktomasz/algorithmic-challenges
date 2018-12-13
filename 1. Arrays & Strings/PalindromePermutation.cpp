/*
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cctype>

using namespace std;

/* Runs in O(N) since hashTable operations are O(1) and we iterate through
the string twice */
bool palindromePermutation(string str){
    map<char, int> hashTable;
    int numOddChars = 0;

    transform(str.begin(), str.end(), str.begin(), ::tolower);
    for(unsigned int i = 0; i < str.length(); i++){
        if(isalpha(str[i])){
            hashTable[str[i]]++;
        }
    }
    for(unsigned int i = 0; i < str.length(); i++){
        if(hashTable[str[i]] % 2 == 1)
            numOddChars++;
    }

    return (numOddChars <= 1) ? true : false;
}

int main(){

    string str = "Tact Coa";
    cout << palindromePermutation(str) << endl;

    return 0;
}
