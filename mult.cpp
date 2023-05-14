#include <iostream>
#include <pybind11/pybind11.h>
#include "mult.h"


float mult(int int_param, float float_param) {
    return int_param*float_param;
}


PYBIND11_MODULE(pymult, module) {
    module.doc() = "pybind11 toy example"; // Optional
    module.def("mult", &mult,
               "A function multiplying two numbers");
}


int main() {
    int int_param = 2;
    float float_param = 3.14;
    float product = mult(int_param, float_param);
    std::cout << "The product is " << product << std::endl;
    return 0;
}

