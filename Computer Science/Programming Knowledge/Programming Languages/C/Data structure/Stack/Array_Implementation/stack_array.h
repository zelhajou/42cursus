#ifndef STACK_H
#define STACK_H

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

extern int stack_arr[MAX];
extern int top;
extern int first;

void push(int data);
int isFull();
int isEmpty();
int peek();
int pop(void);
void print(void);

void prime_fact(int num);

#endif