#include <bits/stdc++.h>
using namespace std;
template <typename K, typename V>
struct ValueComparator
{
    bool operator()(const std::pair<K, V> &a, const std::pair<K, V> &b) const
    {
        return a.second > b.second;
    }
};
int main()
{
    ifstream inputFile("input.txt");
    if (!inputFile)
    {
        cerr << "Error opening file." << std::endl;
        return 1;
    }
    map<char, int> alphabetFrequency;
    char ch;
    int total = 0;
    while (inputFile >> noskipws >> ch)
    {
        ch = tolower(ch);
        if (isalpha(ch))
        {
            alphabetFrequency[ch]++;
            total++;
        }
    }
    inputFile.close();
    set<pair<char, int>, ValueComparator<char, int>> sortedSet(
        alphabetFrequency.begin(), alphabetFrequency.end());
    for (const auto &entry : sortedSet)
    {
        cout << entry.first << ": " << (entry.second / (float)total) * 100 << endl;
    }
    return 0;
}
