#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int age;
    string bar;
    string foo;
    string foobar;
    int new_age;
    int new_age_three;
    int new_age_too;
    
    age = 10;
    new_age = (10+1);
    new_age_too = (age+1);
    new_age_three = (age+new_age_too);
    foo = "Hello";
    bar = "World";
    foobar = (foo+bar);
    cout << age << " " << new_age << " " << new_age_too << " " << new_age_three << endl;
    cout << foo << " " << bar << " " << foobar << endl;
    return 0;
}
