---
title: "Python 연산자: is와 ==의 차이"
layout: post
date: 2019-12-02 16:00
tag:
    - Python
    - Study
    - Programming
    - Note
headerImage: true
image: https://dbader.org/static/figures/python-is-vs-equals.png
description: 191202 Python Operator memo
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

거의 한 달만에 블로그 포스팅을 한다. 그동안 이래저래 바빠가지고 포스팅은 커녕 개인 공부할 시간도 부족했다. 파이썬 관련된 간단한 내용을 메모해놓는 차원에서 12월 첫 포스팅을 올려본다.

## `==` vs `is`

파이썬 공부를 하는데 두 연산자 `==`과 `is`의 쓰임이 똑같아 보여서 찾아보았다. 분명 쓰임에 차이가 있으니까 구현해놨을거라 생각해서 차이점을 명확히 정리하고 싶어서 구글링을 해보았다.

## What is the difference between `==` and `is`?

- `is`: 비교 대상이 동일한 객체를 가리키고 있는지 평가 (포인터 비교)
- `==`: 비교 대상이 동일한 값을 가지고 있는지 평가

|         **`is`**         |     |     |  vs   |     |     |       **`==`**       |
| :----------------------: | --- | --- | :---: | --- | --- | :------------------: |
|    identity operator     |     |     |       |     |     | comparison operator  |
|   reference comparison   |     |     |       |     |     |   value comparison   |
| **(reference equality)** |     |     |       |     |     | **(value equality)** |

`is` 연산자는 포인터(레퍼런스)를 비교하는 연산자이지 데이터를 비교하는 연산자가 아니라서 가급적 `None`, `True`, `False`와 같은 `boolean`값을 비교할 때 사용하는게 좋다고 한다.<sup>[^01]</sup>

영어로 써있긴 하지만 여기<sup>[^02]</sup>에 나와있는 동영상이나 설명을 봐도 이해는 할 수 있을 것 같다.

이 개념이 C? C++?에서 나오는 포인터 개념이랑 연결되는 것 같은데 계속 공부하다보면 좀 더 와닿는 일이 생길 것 같다.

---

<!-- links -->


<!-- referrences -->
[^01]: http://www.songtory.com/post/001001/1/264
[^02]: https://dbader.org/blog/difference-between-is-and-equals-in-python

<!-- images -->

