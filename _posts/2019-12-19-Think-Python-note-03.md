---
title: "Think Python 2nd edition 읽는 포스트: Chapter 03, 'Functions'"
layout: post
date: 2019-12-19 15:30
tag:
    - Python
    - Think Python
    - Programming
    - Study
    - Book
    - Note
headerImage: false
image:
description: 191219 `Think Python 2nd edition` study note
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# Think Python - How to Think Like a Computer Scientist

`Python` 공부할 자료들 찾다가 [Green Tea Press][homepage]에서 제공하는 [Think Python 2e pdf][book]를 찾았다. 분량도 생각보다 많지 않은데다가 영어지만 쉽게 읽히는 편이라서 한 챕터씩 읽고 연습문제도 풀고 간단하게 내용도 정리해보려고 한다.

아직까지는 쉬운데 벌려놓은 일에 비해 집중할 수 있는 시간이 한정적이다. (191217)

---

## Ch. 03: Functions

### Function Calls, 함수 호출

일반적으로 함수를 표현할 때, 괄호 안을 함수의 인수 `argument`라고 부른다.
파이썬의 함수 형태는 **_`함수의 이름` `(인수)`_** 구조를 갖는다.
함수는 인수(argument)를 "취하고", 결과를 "반환"한다. 반환된 결과 값은 "반환값"이라고 부른다.

> The expression in parentheses is called the **argument** of the function.
> It is common to say that a function "takes" an argument and "returns" a result. The result is also called the return value.

---

### Math Functions, 수학 함수

모듈(Module)은 연관된 함수들의 모음집을 의미한다.
모듈에 포함된 함수를 사용하기 전에, `import` 선언을 통해 불러와야한다.
모듈 객체에는 모듈에 포함된 함수 및 변수들의 정의를 포함한다.

> A module is a file that contains a collection of related functions.
> Before we can use the functions in a module, we have to import it with an `import` statement.
> The `module object` contains the functions and variables defined in the module.

---

### Adding New Functions, 새 함수 만들기

`def`는 함수의 정의를 나타내는 키워드다.
(함수 종류에 따라) 함수 이름 뒤에 오는 빈 괄호는 아무 인수도 취하지 않는다.
함수를 정의하는 코드의 가장 첫 줄을 헤더라 하고, 나머지는 바디라고 한다. 헤더는 콜론으로 끝나야 하고, 바디는 들여쓰기로 구분된다. 관례상 들여쓰기는 스페이스 네 칸으로 한다.

> `def` is a keyword that indicates that this is a function definition.
> The empty parentheses after the name indicate that this function doesn't take any arguments.
> The first line of the function definition is called the header; the rest is called the body. The header has to end with a colon and the body has to be indented. The body can contain any number of statements.
> By convention, indentation is always four spaces.

---

### Definitions and Uses 정의와 사용

함수의 정의는 다른 선언문처럼 실행되지만 함수 객체를 생성하는 효과가 있다. 함수가 호출될 때까지 함수 내부에 있는 선언문들은 작동하지 않고, 함수의 정의는 아무런 출력물도 생성하지 않는다. (...) 함수의 정의는 실행되기 이전에 호출이 선행되어야 한다.

> Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not run until the function is called, and the function definition generates no output. (...) the function definition has to run before the function gets called.

---

### Parameters and Arguments, 매개변수와 인수

어떤 함수들은 인수들을 필요로 한다.
함수 내부에서, 인수들은 매개변수(parameter)에 할당됩니다.

> Some of the functions we have seen require arguments.
> Inside the function, the arguments are assigned to variables called **parameters**.

---

### Variables and Parameters Are Local, 변수와 매개변수는 지역적이다

함수 내에서 변수를 만들었을 때, 이것은 지역적이다. 그 의미는, 지역변수는 함수 내에서만 존재한다는 뜻이다. 매개변수들 또한 지역적이다.

> When you create a variable inside a function, it is local, which means that it only exists inside the function. (...) Parameters are also local.

---

### Stack Diagrams, 스택 다이어그램

어떤 변수를 어디에 사용할 수 있는지 추적하기 위해 스택 다이어그램을 그리는 것이 유용한 경우도 있다. 상태 다이어그램과 같이, 스택 다이어그램은 각 변수의 값을 보여주지만 각 변수가 어느 함수에 속하는지도 보여준다.
어떤 함수에서든 함수 바깥에서 변수를 생성할 때, 그 변수는 `__main__`에 속한다.
각 매개변수는 그것의 해당 인수와 같은 값을 참조한다.
함수 호출중 오류가 발생할 경우, 파이썬은 함수의 이름(1), 그 함수(1)를 호출한 함수(2)의 이름, 그리고 그 함수(2)를 호출한 함수(3)의 이름을 `__main__`으로 출력한다.
트래이스백의 함수들 순서는 스택 다이어그램의 프레임들 순서와 같다. 현재 실행중인 함수는 가장 마지막에 있다.

> To keep track of which Variables can be used where, it is sometimes useful to draw a **stack diagram**. Like state diagrams, stack diagrams show the value of each variable, but they also show the function each variable belongs to.
> When you create a variable outside of any function, it belongs to `__main__`.
> Each parameter refers to the same value as its corresponding argument.
> If an error occurs during a function call, Python prints the name of the function, the name of the function that called it, and the name of the function that called _that_, all the way back to `__main__`.
> The order of the functions in the traceback is the same as the order of the frames in the stack diagram. The function that is currently running is at the bottom.

---

### Why Functions?

-   새롭게 함수를 작성하는 것은 코드 모음(a group of statements)에 이름을 붙여 프로그램을 좀 더 읽기 쉽고 디버깅하기 쉽게 만들어준다.
-   불필요하게 반복되는 코드를 제거하여 프로그램을 좀 더 작게 만들 수 있다. 추후에 수정할 경우, (작성된 함수 코드에서)한 부분만 수정하면 된다.
-   긴 프로그램을 기능별로 분할할 경우, (필요에 맞게) 한번에 기능 하나씩 디버깅한 후 조립하여 전체에 반영할 수 있다.
-   잘 설계된 함수는 다양한 프로그램에서 유용하게 사용될 수 있다. 함수를 작성한 후 디버깅하여 재사용할 수 있다.

> -   Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.
> -   Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.
> -   Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
> -   Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.

### Exercises

예제에 사용한 코드는 [여기][file]에서 볼 수 있다.

#### Q) Exercise 3.1.

Write a function named `right_justify` that take a string named `s` as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

Hint: Use string concatenation and repetition. Also, Python provides a built-in-function called `len` that returns the length of a string, so the value of `len('monty')` is 5.

#### A)

```py
def right_justify(s):
    string = ' '*(70-len(s)) + s
    print(string)


right_justify('monty')
```

---

#### Q) Exercise 3.2.

A function object is a value you can assign to a variable or pass as an argument. For example, `do_twice` is a function that takes a function object as an argument and calls it twice:

```py
def do_twice(f):
    f()
    f()
```

Here's an example that uses `do_twice` to call a function named `print_spam` twice:

```py
def print_spam():
    print('spam')

do_twice(print_spam)
```

##### 1. Type this example into a script and test it.

```py
def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')

do_twice(print_spam)
```

```shell
spam
spam
```

##### 2. Modify `do_twice` so that it takes two arguments, a function object and a value, and calls the functions twice, passing the value as an argument.

```py
def do_twice(f, s):
    f(s)
    f(s)
```

##### 3. Copy the definition of `print_twice` from earlier in this chapter to your script.

```py
def print_twice(bruce):
    print(bruce)
    print(bruce)
```

##### 4. Use the modified version of `do_twice` to call `print_twice` twice, passing `'spam'` as an argument.

```py
def do_twice(f, s):
    f(s)
    f(s)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')
```

##### 5. Define a new function called `do_four` that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

```py
def do_four(value):
    print_twice(value)
    print_twice(value)

do_four('four')
```

```py
# solution code
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print_twice, 'four')
```

---

#### Q) Exercise 3.3.

격자 그리기

#### A)

2x2, 4x4 격자를 그리는게 예제였는데 좀 더 생각해서 nxn 격자가 가능한 함수로 만들었다.

```py
# Grid draw function
def gridraw(col, row):
    while col > 0:
        col -= 1
        print('+ - - - - '*row, end='')
        print('+')
        rowCount = 0
        while rowCount < 4:
            rowCount += 1
            print('|         '*row, end='')
            print('|')
        if col == 0:
            print('+ - - - - '*row, end='')
            print('+')
```

---

[homepage]: https://greenteapress.com/wp/think-python-2e/
[book]: http://greenteapress.com/thinkpython2/thinkpython2.pdf
[file]: /assets/files/posts/2019-12-19/191219.py
