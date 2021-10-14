#include <iostream>
#include <fstream>
#include <stdexcept>

#define ANALYZE {ANALYZE}

#define F_L_1 {F_L_1}
#define F_H_1 {F_H_1}

#define F_L_2 {F_L_2}
#define F_H_2 {F_H_2}

#define F_L_3 {F_L_3}
#define F_H_3 {F_H_3}

#define F_L_4 {F_L_4}
#define F_H_4 {F_H_4}

#define F_L_5 {F_L_5}
#define F_H_5 {F_H_5}

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

    if(F_L_1 <= analyze && analyze <= F_H_1)
        return -5;

    if(F_L_2 <= analyze && analyze <= F_H_2)
        throw std::invalid_argument("ciao");

    if(F_L_3 <= analyze && analyze <= F_H_3)
        return 0; // no output

    if(F_L_4 <= analyze && analyze <= F_H_4)
        while(1);

    if(F_L_5 <= analyze && analyze <= F_H_5);
        resolve();
    
    return 0;
}