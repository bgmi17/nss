#include <bits/stdc++.h>
using namespace std;
string caesarcipher(string &plaintext, int key)
{
    string ciphertext;
    for (char c : plaintext)
    {
        if (isalpha(c))
        {
            char base = islower(c) ? 'a' : 'A';
            char shift = ((c - base + key) % 26 + base);
            ciphertext += shift;
        }
        else
        {
            ciphertext += c;
        }
    }
    return ciphertext;
}
int main()
{
    cout << "caesar cipher encryption" << endl;
    string plaintext;
    cout << "Enter the plaintext" << endl;
    getline(cin, plaintext);
    int key;
    cout << "Enter the key" << endl;
    cin >> key;
    string ciphertext = caesarcipher(plaintext, key);
    cout << "Ciphertext:" << ciphertext << endl;
    return 0;
}
