/* URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.) */

/*
Other possible solutions:
- Allocate new array of characters based on the number of spaces (and the length
of the original string and then either copy the characters or insert "%20" */
#include <iostream>
#include <string>

using namespace std;

string URLify(string str){
    string str2 = "";

    for(unsigned int i = 0; i < str.length(); i++){
        if(str[i] == ' '){
            str2 += "%20";
        }
        else
            str2 += str[i];
    }
    return str2;
}

int main(){

    string str = "Mr John Smith";
    cout << URLify(str) << endl;

    return 0;
}
