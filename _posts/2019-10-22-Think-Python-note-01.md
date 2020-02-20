---
title: "Think Python 2nd edition 읽는 포스트: Chapter 01, 'The way of the program'"
layout: post
date: 2019-10-22 23:00
tag:
    - Python
    - Think Python
    - Programming
    - Study
    - Book
    - Note
headerImage: false
image:
description: 191022 `Think Python 2nd edition` study note
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
---

# Think Python - How to Think Like a Computer Scientist

`Python` 공부할 자료들 찾다가 [Green Tea Press][homepage]에서 제공하는 [Think Python 2e pdf][book]를 찾았다. 분량도 생각보다 많지 않은데다가 영어지만 쉽게 읽히는 편이라서 한 챕터씩 읽고 연습문제도 풀고 간단하게 내용도 정리해보려고 한다. 역시나, 당연하게도 앞부분은 쉽다. 마치 수학책의 지수/로그 단원은 쉽게 느껴지는 것처럼.

이 책은 저작권에 문제가 없는 무료 e북이다.

---

## Ch. 01: The way of the program

'문제 해결 능력'은 전산 과학(Computer Science)에서 가장 중요한 기술이다.
문제를 해결하는 능력은

1. 문제점을 서술하고
2. 해결을 위해 창의적으로 생각하고
3. 해결 방안을 알기 쉽고 명확하게 표현하는 것을 의미한다.

> The single most important skill for a computer scientist is problem solving. Problem solv- ing means the ability to formulate problems, think creatively about solutions, and express a solution clearly and accurately.

---

'프로그래밍'은 크고 복잡한 작업을 잘게 쪼개어 기본적인 수준으로 실행 가능한 하위 작업들로 만드는 과정이라고 볼 수 있다.

> So you can think of programming as the process of breaking a large, complex task into smaller and smaller subtasks until the subtasks are simple enough to be performed with one of these basic instructions.

---

프로그래밍 언어는 계산을 표현하기 위해서 설계된 형식 언어다.

> Programming languages are formal languages that have been designed to express computations.

---

머리를 써서 직접 프로그램의 구문을 분석하고, 토큰을 식별하고, 구조를 해석하는 방법을 배워야 한다.

> learn to parse the program in your head, identifying the tokens and interpreting the structure.

---

### 1.9 Exercises

#### A) Exercise 1.1.

##### 1. In a print statement, what happens if you leave out one of the parentheses, or both?

```python
# 정상 작동
>>> print("Hello, World")
Hello, World

# SyntaxError
>>> print "Hello, World")
  File "<stdin>", line 1
    print "Hello, World")
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello, World"))?

>>> print "Hello, World"
  File "<stdin>", line 1
    print "Hello, World"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello, World")?

# incomplete sentence
>>> print("Hello, World"
...
...
...
```

---

##### 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?

```python
# incomplete sentence
>>> print("Hello, World!)
  File "<stdin>", line 1
    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal

>>> print(Hello, World")
  File "<stdin>", line 1
    print(Hello, World")
                       ^
SyntaxError: EOL while scanning string literal

# Hello, World를 각각 변수 취급
>>> print(Hello, World)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined

# syntax error
>>> print(Hello, World!")
  File "<stdin>", line 1
    print(Hello, World!")
                      ^
SyntaxError: invalid syntax

>>> print(Hello, World!)
  File "<stdin>", line 1
    print(Hello, World!)
                      ^
SyntaxError: invalid syntax
```

---

##### 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?

```python
>>> 2++2
4
>>> 2--2
4
>>> 2+-2
0
>>> -2-2
-4
>>> -2+-2
-4
>>> 4*-2
-8
# 연산자 규칙에 어긋남
>>> 4-*4
  File "<stdin>", line 1
    4-*4
      ^
SyntaxError: invalid syntax
```

---

##### 4. In math notation, leading zeros are okay, as in 02. What happens if you try this in Python?

```python
>>> 02
  File "<stdin>", line 1
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# 8진수 0o, 16진수 0x
>>> 0o12
10
>>> 0x12
18
```

---

##### 5. What happens if you have two values with no operator between them?

```python
# int, float -> SyntaxError
>>> 9 8 7
  File "<stdin>", line 1
    9 8 7
      ^
SyntaxError: invalid syntax

>>> 9.0 8.9
  File "<stdin>", line 1
    9.0 8.9
        ^
SyntaxError: invalid syntax

# str -> each str is conneted
>>> 'Hello' 'World'
'HelloWorld'
```

---

[homepage]: https://greenteapress.com/wp/think-python-2e/
[book]: http://greenteapress.com/thinkpython2/thinkpython2.pdf
