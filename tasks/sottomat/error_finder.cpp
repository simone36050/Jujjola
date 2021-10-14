#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream in("input.txt");

    // read R, C
    int R = 0, C = 0;
    in >> R >> C;

    // check R
    if(R < 1 || R > 2000)
        while(1);

    // check C
    if(R < 1 || R > 2000)
        return -5;

    // all is ok
    return 0;
}