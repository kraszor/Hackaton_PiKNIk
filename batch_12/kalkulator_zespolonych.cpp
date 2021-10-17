#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>
#include <iomanip>


using namespace std;

enum actions{
    addition = 1,
    subtraction,
    multiplication,
    division,
};


bool checking_digits(string choice){
    int dots = 0;
    int length = choice.length();
    if ((choice[0] == '.') || (choice[length-1] == '.')){
        return false;
    }

    for (int i=0; i < length; i++){
        if ((isdigit(choice[i]) == false) && (choice[i] != '.') && (choice[i] != '-')){
            return false;
        }

        else if (choice[i] == '.'){
            dots++;
        }

        else if ((choice[i] == '-') && i != 0){
            return false;
        }

        if (dots > 1){
            return false;
        }
    }

    return true;
}


bool checking_int(string choice){
    int length = choice.length();
    for (int i=0; i < length; i++){
        if (isdigit(choice[i]) == false){
            return false;
        }
    }
    return true;
}

vector<double> add_numbers(vector<double> values){
    vector<double> algebraic_result;
    algebraic_result.push_back(values[0] + values[2]);
    algebraic_result.push_back(values[1] + values[3]);
    return algebraic_result;
}

vector<double> subtract_numbers(vector<double> values){
    vector<double> algebraic_result;
    algebraic_result.push_back(values[0] - values[2]);
    algebraic_result.push_back(values[1] - values[3]);
    return algebraic_result;
}

vector<double> multiply_numbers(vector<double> values){
    vector<double> algebraic_result;
    algebraic_result.push_back((values[0] * values[2]) - (values[1] * values[3]));
    algebraic_result.push_back((values[0] * values[3]) + (values[1] * values[2]));
    return algebraic_result;
}

vector<double> divide_numbers(vector<double> values){
    vector<double> algebraic_result, transit_l, transit_m, trans_result_l, trans_result_m;
    trans_result_l.reserve(2);
    trans_result_m.reserve(2);
    transit_l = values;
    transit_m = values;
    transit_l[3] = -transit_l[3];
    transit_m[0] = transit_m[2];
    transit_m[1] = -transit_m[3];
    trans_result_l = multiply_numbers(transit_l);
    trans_result_m = multiply_numbers(transit_m);
    if (trans_result_m[0] != 0){
        algebraic_result.push_back(trans_result_l[0] / trans_result_m[0]);
        algebraic_result.push_back(trans_result_l[1] / trans_result_m[0]);
        return algebraic_result;
    }
    else{
        return algebraic_result;
    }
}

string set_sign(double value){
    double val = value;
    if (val < 0){
        return " - ";
    }
    else{
        return " + ";
    }
}

vector<double> exponential_form(vector<double> algebraic_result){
    double z, a, b, cos_value, sin_value, cos_arg, sin_arg, arg, arg_pi;
    vector<double> exp_result;
    a = algebraic_result[0];
    b = algebraic_result[1];
    z = sqrt((pow(a, 2) + pow(b, 2)));
    cos_value = a/z;
    sin_value = b/z;
    cos_arg = (acos(cos_value))* 180/3.14159265;
    sin_arg = (asin(sin_value))* 180/3.14159265;

    if ((sin_value >= 0) & (cos_value >= 0)){
        arg = cos_arg;
        arg_pi = arg / 180;
    }

    else if ((sin_value >= 0) & (cos_value < 0)){
        arg = cos_arg;
        arg_pi = arg / 180;
    }

    else if ((sin_value < 0) & (cos_value <= 0)){
        arg = -cos_arg;
        arg_pi = (arg / 180);
    }

    else if ((sin_value < 0) & (cos_value > 0)){
        arg = -cos_arg;
        arg_pi = (arg / 180);
    }

    exp_result.push_back(z);
    exp_result.push_back(arg_pi);
    exp_result.push_back(arg);
    return exp_result;
}


string to_trigonometric_form(vector<double> algebraic_result, vector<double> exp_result){
    string representation, cos_sign, sin_sign;
    double z, a, b, cos_value, sin_value, cos_arg, sin_arg;
    a = algebraic_result[0];
    b = algebraic_result[1];
    z = sqrt((pow(a, 2) + pow(b, 2)));
    cos_value = a/z;
    sin_value = b/z;
    cos_arg = (acos(cos_value))* 180/3.14159265;
    sin_arg = (asin(sin_value))* 180/3.14159265;

    cos_sign = set_sign(cos_value);
    sin_sign = set_sign(sin_value);
    if (cos_sign == " + "){
        cos_sign = "";
    }

    representation = to_string(z) + "("+ cos_sign + "cos("+ to_string(exp_result[1]) + " PI)" + sin_sign + "isin(" + to_string(exp_result[1]) + " PI))";
    return representation;
}


string to_algebraic_form(double module, double arg){
    string representation, im_sign;
    double re, im, pi;
    pi = 3.14159265358979323846;
    re = module*cos(arg*pi);
    im = module*sin(arg*pi);

    re = (float)((int)(re * 100 + .5))/100;
    im = (float)((int)(im * 100 + .5))/100;

    im_sign = set_sign(im);
    representation = to_string(re) + im_sign + to_string(im) + "i";
    return representation;
}



int main(){
    while(true){
        string choice;
        string number;
        int new_choice;
        vector<double> values, algebraic_result, exp_result;
        string sign1, sign2, sign3, operation;
        bool condition = false;

        while (condition == false){
            cout << "\n\nCalculator\n\n";
            cout << "1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit\n\n";
            cout << "Enter the type of operation: ";
            cin >> choice;
            if (checking_int(choice)){
                new_choice = stoi(choice);
                if (new_choice >= 1 && new_choice <=4){
                    condition = true;
                }

                else if (new_choice == 5){
                    cout << "\n\nSee you next time\n\n";
                    exit(0);
                }

                else{
                    cout << "There is no such option";
                }
            }
            else{
                cout << "Incorrect value";
            }
        }

        for (int i=0; i<4; i++){
            if (i < 2){
                cout << "\nEnter the real and imaginary part of the first complex number (a + bi): ";
            }
            else{
                cout << "\nEnter the real and imaginary part of the second complex number (a + bi): ";
            }
            condition = false;
            while (condition == false){
                if ((i == 0) || (i == 2)){
                    cout << "\na = ";
                }
                else{
                    cout << "\nb = ";
                }
                cin >> number;
                if (checking_digits(number)){
                    values.push_back(stod(number));
                    condition = true;
                }
                else{
                    cout << "Not a number\n";
                }
            }
        }

        switch(new_choice)
        {
            case addition:
            {
                algebraic_result = add_numbers(values);
                operation = " + ";
            }
            break;
            case subtraction:
            {
                algebraic_result = subtract_numbers(values);
                operation = " - ";
            }
            break;
            case multiplication:
            {
                algebraic_result = multiply_numbers(values);
                operation = " * ";
            }
            break;
            case division:
            {
                algebraic_result = divide_numbers(values);
                operation = " / ";
            }

        }
        if (!algebraic_result.empty())
        {
            exp_result = exponential_form(algebraic_result);
            sign1 = set_sign(values[1]);
            sign2 = set_sign(values[3]);
            sign3 = set_sign(algebraic_result[1]);
            cout << "\n(" << values[0] << sign1 << abs(values[1]) << "i)" << operation;
            cout << "(" << values[2] << sign2 << abs(values[3]) << "i) = ";
            cout << algebraic_result[0] << sign3 << abs(algebraic_result[1]) << "i";
            cout << " = " << exp_result[0] << "e^(" << exp_result[1] << "PIi)        arg = " << exp_result[2]<<endl;
            cout << to_trigonometric_form(algebraic_result, exp_result) << endl <<endl;
            cout << to_algebraic_form(exp_result[0], exp_result[1]);
        }
        else
        {
            cout << "\n\nDon't divide by zero\n\n";
        }
    }
    return 0;
}