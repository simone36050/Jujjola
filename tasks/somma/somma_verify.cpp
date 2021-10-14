#include <iostream>
#include <fstream>
#include <stdexcept>

#define ANALYZE {ANALYZE}

#define ELEMENT {ELEMENT}

using namespace std;

void resolve() {
    int n1, n2;

    ifstream in("input.txt");
    in >> n1 >> n2;

    ofstream out("output.txt");
    out << n1 + n2 << endl;
}

int main() {
    int n1, n2;

    ifstream in("input.txt");
    in >> n1 >> n2;

    int analyze = 0;
    analyze = (ANALYZE == 1 ? n1 : n2);

    if(analyze == ELEMENT)
        return -5;

    return 0;
}