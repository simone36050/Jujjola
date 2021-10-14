#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream in("input.txt");

    // read N
    int N = 0;
    in >> N;

    // read array
    int arr[1000000];
    for(int i = 0; i < N; i++)
        in >> arr[i];

    // check N
    if(N < 1 || N > 1000000)
        return -5;

    // check array
    for(int i = 0; i < N; i++)
        if(arr[i] < -1000000 || arr[i] > 1000000)
            while(1);

    // all is ok
    return 0;
}