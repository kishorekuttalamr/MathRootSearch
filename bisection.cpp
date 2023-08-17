#include <iostream>
#include <cmath>
using namespace std;
double func(double x)
{
    return ((pow(x, 3)) - x + 1);
}
int main()
{
    int arr[21];
    for (int i = -10; i <= 10; i++)
    {
        arr[i + 10] = func(i);
    }
    for (int i = -10; i <= 10; i++)
    {
        cout << arr[i + 10] << "at" << i << endl;
    }
    double a, b, x;
    cout << "input a and b values";
    cin >> a >> b;
    double c = (a + b) / 2;
    double preC = 0;
    int count = 0;
    while (abs(c - preC) > 0.01)
    {
        count++;
        x = func(c);
        if (x < 0)
        {
            a = c;
        }
        else
        {
            b = c;
        }
        preC = c;
        c = (a + b) / 2;
    }
    cout << c << "after " << count << " step";
}
