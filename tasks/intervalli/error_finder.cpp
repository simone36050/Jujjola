#include <fstream>
#include <iostream>
#include <stdexcept>

using namespace std;

int main() {
    ifstream in("input.txt");

    // read N
    int N = 0;
    in >> N;

    // check N
    if(N < 1 || N > 100000)
        while(1);

    // read & check lines
    for(int i = 0; i < N; i++) {
        // read
        long long S = 0, E = 0;
        in >> S >> E;

        if(S < 1 || S > 5000000000)
            return -5;

        if(E < S || E > 5000000000)
            throw std::invalid_argument("ciao");
    }

    // all is ok
    return 0;
}