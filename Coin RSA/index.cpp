#include <bits/stdc++.h>
using namespace std;
bool isPrime(int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i <= sqrt(n); ++i)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
void generateKeys(int &publicKey, int &privateKey, int &n)
{
    int p, q;
    do
    {
        p = rand() % 100 + 50;
    } while (!isPrime(p));
    do
    {
        q = rand() % 100 + 50;
    } while (!isPrime(q));
    n = p * q;
    int phi = (p - 1) * (q - 1);
    do
    {
        publicKey = rand() % (phi - 2) + 2;
    } while (__gcd(publicKey, phi) != 1);
    int k = 2;
    privateKey = (k * phi + 1) / publicKey;
}
int encrypt(int message, int publicKey, int n)
{
    return static_cast<int>(pow(message, publicKey)) % n;
}
int decrypt(int encryptedMessage, int privateKey, int n)
{
    return static_cast<int>(pow(encryptedMessage, privateKey)) % n;
}
int main()
{
    srand(time(0));
    int publicKey, privateKey, n;
    generateKeys(publicKey, privateKey, n);
    cout << "RSA Public Key: " << publicKey << endl;
    cout << "RSA Private Key: " << privateKey << endl;
    cout << "RSA Modulus (n): " << n << endl;
    int coin = rand() % 2;
    cout << "\nOriginal Coin: " << coin << endl;
    int encryptedCoin = encrypt(coin, publicKey, n);
    cout << "Encrypted Coin: " << encryptedCoin << endl;
    int decryptedCoin = decrypt(encryptedCoin, privateKey, n);
    cout << "Decrypted Coin: " << decryptedCoin << endl;
    cout << "\nResult after RSA Coin Flip: ";
    if (decryptedCoin == 0)
    {
        cout << "Heads!" << endl;
    }
    else
    {
        cout << "Tails!" << endl;
    }
    return 0;
}