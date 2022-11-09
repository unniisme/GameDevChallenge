#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    while(1)
    {
        float x, y;
        float x0, y0;

        cin >> x >> y;
        cin >> x0 >> y0;

        cout << 180*atan((y-y0)/(x-x0))/3.14159265 << endl;
    }
}