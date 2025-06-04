cmake_minimum_required(VERSION 3.31)
project(A1 C)

set(CMAKE_C_STANDARD 11)

add_executable(A1 main.c
        data.h
        data.c
        budget.c
        budget.h
        ordering.c
        ordering.h)



