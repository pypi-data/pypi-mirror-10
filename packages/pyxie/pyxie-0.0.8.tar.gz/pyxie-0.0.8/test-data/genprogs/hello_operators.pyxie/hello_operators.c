#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    string greet;
    string who;
    
    greet = "hello";
    who = "world";
    cout << (1+1) << endl;
    cout << (2+2) << endl;
    cout << (2+(2+2)) << endl;
    cout << (2+(2+(2+2))) << endl;
    cout << (1*1) << endl;
    cout << (2*2) << endl;
    cout << (1*(2*3)) << endl;
    cout << (10-1) << endl;
    cout << (10-1) << endl;
    cout << (10-(1-2)) << endl;
    cout << (1+((2*(3*4))-(5/7))) << endl;
    cout << ("greet"+"who") << endl;
    return 0;
}
