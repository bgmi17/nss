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
            char shift = ((26 + c - base - key) % 26 + base);
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
    cout << "Caesar DeCipher Encryption:" << endl;
    string plaintext;
    cout << "Enter the plaintext:" << endl;
    getline(cin, plaintext);
    int key;
    cout << "Enter the key:" << endl;
    cin >> key;
    string ciphertext = caesarcipher(plaintext, key);
    cout << "DeCiphertext:" << ciphertext << endl;
    return 0;
}
