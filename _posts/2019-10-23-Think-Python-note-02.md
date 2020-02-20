---
title: "Think Python 2nd edition 읽는 포스트: Chapter 02, 'Variables, expressions and statements'"
layout: post
date: 2019-10-23 16:30
tag:
    - Python
    - Think Python
    - Programming
    - Study
    - Book
    - Note
headerImage: false
image:
description: 191023 `Think Python 2nd edition` study note
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: true
---

# Think Python - How to Think Like a Computer Scientist

`Python` 공부할 자료들 찾다가 [Green Tea Press][homepage]에서 제공하는 [Think Python 2e pdf][book]를 찾았다. 분량도 생각보다 많지 않은데다가 영어지만 쉽게 읽히는 편이라서 한 챕터씩 읽고 연습문제도 풀고 간단하게 내용도 정리해보려고 한다. 역시나, 당연하게도 앞부분은 쉽다. 마치 수학책의 지수/로그 단원은 쉽게 느껴지는 것처럼.

이 책은 저작권에 문제가 없는 무료 e북이다.

---

## Ch. 02: Variables, expressions and statements

파이썬 인터프리터는 프로그램의 구조를 인식하기 위해 몇 가지 키워드들을 사용한다. 그것들은 변수의 이름이 될 수 없다.

> The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names.

| Keywords |          |         |          |        |
| :------- | :------- | :------ | :------- | :----- |
| False    | class    | finally | is       | return |
| None     | continue | for     | lambda   | try    |
| True     | def      | from    | nonlocal | while  |
| and      | del      | global  | not      | with   |
| as       | elif     | if      | or       | yield  |
| assert   | else     | import  | pass     |        |
| break    | except   | in      | raise    |        |

---

수학 연산자에 대해서, 파이썬은 수학적 규칙을 따른다

-   괄호는 가장 높은 우선순위를 가지며, 식의 계산 순서를 원하는 순서대로 표현하는 데 사용할 수 있다.
-   지수는 괄호 다음으로 높은 우선순위를 갖는다.
-   곱셈/나눗셈은 덧셈/뺄셈보다 더 높은 우선순위를 갖는다.
-   우선순위가 동일한 연산자를 계산해야 하는 경우, 왼쪽에서 오른쪽 순서로 진행한다 (지수 제외).

> For mathematical operators, Python follows mathematical convention.
>
> -   **P**arentheses have the highest precedence and can be used to force an expression to evaluate in the order you want.
>     **E**xponentiation has the next highest precedence.
> -   **M**ultiplication and **D**ivision have higher precedence than **A**ddition and **S**ubtraction.
> -   Operators with the same precedence are evaluated from left to right (except exponentiation).

---

문자열에 대해서, `+` 연산자는 문자열을 연결시켜주는 역할을 하고, `*` 연산자는 문자열을 해당 횟수만큼 반복하는 역할을 한다.

> The `+` operator performs string concatenation, which means it joins the strings by linking them end-to-end.
> The `*` operator also works on strings; it performs repetition.

---

### 2.10 Exercises

#### A) Exercise 2.1.

```python
# Q) We’ve seen that n = 42 is legal. What about 42 = n?
# A) 변수 이름 시작에 숫자가 올 수 없다는 변수 선언 규칙에 어긋남
>>> n = 42
>>> 42 = n
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
```

```python
# Q) How about x = y = 1?
# A) x와 y는 변수명은 다르지만 같은 값을 갖는다
>>> x = y = 1
>>> id(x) == id(y)
True
```

```python
# Q) In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
# A) 별 일 없다
>>> print("Hello, World.");
Hello, World.

>>> x = y = 1 ;
>>> print(x, y);
1 1

>>> a = 11;
>>> print(a)
11
```

```python
# Q) What if you put a period at the end of a statement?
# A) SyntaxError 발생
>>> print("Hello, World.").
  File "<stdin>", line 1
    print("Hello, World.").
                          ^
SyntaxError: invalid syntax
```

```python
# Q) In math notation you can multiply x and y like this: xy. What happens if you try that in Python?
# A) xy 라는 변수로 인식을 한다
>>> x = 4
>>> y = 5
>>> xy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xy' is not defined
```

---

#### A) Exercise 2.2.

##### 1. The volume of a sphere with radius r, volume is $$V = \frac{4}{3} πr^3$$. What is the volume of a sphere with radius 5?

```python
>>> import math
>>> r = 5
>>> pi = math.pi
>>> V = (4/3)*pi*r**3
>>> print(V)
523.5987755982989
```

##### 2. Suppose the cover price of a book is \$24.95, but bookstores get a 40% discount. Shipping costs \$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

```python
>>> book_cost = 24.95
>>> shipping_cost = 3
>>> dc_ratio = 0.4
>>> additional_shipping_cost = 0.75
>>> total_order = 60
>>> total_order*(book_cost*dc_ratio)+(shipping_cost+(total_order-1)*additional_shipping_cost)
646.0500000000001
```

##### ~~3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?~~

~~A) approximately 07:30 am~~
굳이 이걸 파이썬으로 풀 이유가 있는지....

---

[homepage]: https://greenteapress.com/wp/think-python-2e/
[book]: http://greenteapress.com/thinkpython2/thinkpython2.pdf
