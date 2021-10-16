#include <iostream>
#include <unordered_map>
#include <math.h>
#include <string>

using namespace std;

unordered_map<string, double> units
    {
        {"mg",0.000001},
        {"g",0.0001},
        {"dag",0.01},
        {"kg",1},
        {"quintal",100},
        {"ton",1000},
    };

double conversion(string number, string input_unit, string output_unit)
{
    double double_num = stod(number);
    double new_number;
    new_number = double_num*(units[input_unit]/units[output_unit]);
    return new_number;
}

void output_unit_list()
{
    cout<<"List of units"<<endl;
    cout<<"1. mg"<<endl;
    cout<<"2. g"<<endl;
    cout<<"3. dag"<<endl;
    cout<<"4. kg"<<endl;
    cout<<"5. quintal"<<endl;
    cout<<"6. ton"<<endl;
}

void output_text_menu()
{
    cout<<"Mass unit converter"<<endl;
    cout<<"1. Convert unit"<<endl;
    cout<<"2. Exit"<<endl;
    cout<<"Choose desired operation: "<<endl;
}

bool checking_list(string input)
{
    if (units.find(input) != units.end())
    {
        return true;
    }
    return 0;
}

bool checking_value(string number)
{   
    int y = 0;
    int size_num = number.size();
    for (int i = 0; i < size_num; i++)
    {
        if (!isdigit(number[i]) && number[i] != '.')
        {
            cout << "Enter positive real value!" << endl;
            return false;
        }
        if (number[i] == '.')
        {
            y += 1;
        }
    }
    if (y > 1)
    {
        cout << "Enter positive real value!" << endl;
            return false;
    }
    else
    {
        return true;
    }
    return 0;
}

int main()
{   
    string number;
    string input_unit;
    string output_unit;
    string operation;
    double new_number;
    int x=-1;
    while (x < 0)
    {   
        output_text_menu();
        getline(cin, operation);
        if (operation=="Convert unit" | operation=="1" | operation=="convert unit")
        {
            cout<<"Enter the desired value you want to convert: ";
            getline(cin, number);
            bool val_info = checking_value(number);
            if (val_info == false)
            {
                continue;
            }
            output_unit_list();
            cout<<"Enter the starting unit of your value from list: ";
            getline(cin, input_unit);
            bool info = checking_list(input_unit);
            if (info == false)
            {
                cout<<"You entered unit that is not listed!"<<endl;
                continue;
            }
            output_unit_list();
            cout<<"Enter the expected unit of your value from list: ";
            getline(cin, output_unit);
            info = checking_list(output_unit);
            if (info == false)
            {
                cout<<"You entered unit that is not listed!"<<endl;
                continue;
            }
            new_number=conversion(number, input_unit, output_unit);
            cout<<number<<" "<<input_unit<<" = "<<new_number<<" "<<output_unit<<endl;
        }
        else if (operation=="Exit" | operation=="exit" | operation=="2")
        {
            x=1;
        }
        else
        {
            cout<<"You entered operation that is not listed!"<<endl;
            continue;
        }

    }
    return 0;
}
