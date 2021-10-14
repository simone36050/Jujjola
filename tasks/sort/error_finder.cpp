#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream in("input.txt");

    // read N
    int N = 0;
    in >> N;

    // check R
    if(N < 1 || N > 1000000)
        while(1);

    // all is ok
    return 0;
}