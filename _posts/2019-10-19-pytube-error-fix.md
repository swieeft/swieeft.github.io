---
title: "pytube 에러 수정기: 'title', 'thumbnail_url', 'length' 기능 활성화하기"
layout: post
date: 2019-10-19 22:00
tag:
    - Python
    - pytube
    - Programming
    - Study
    - idol
headerImage: false
image:
description: 191019 Python library `pytube` error fix
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
---

인터넷에서 `pytube`를 사용한 웹크롤링 예제 따라하고 있는데 몇몇 기능이 작동하지 않아서 구글링해서 고쳤다. 나처럼 헤매는 사람이 있을지도 모르니 수정하는 방법을 순차적으로 작성해서 올려본다.

---

## 1. `pytube` 재설치하기

파이썬 패키지 인스톨 명령어를 사용해서 `pytube`를 설치한다.

```shell
$ pip install pytube
```

그런데 `title`, `length`, `thumbnail_url`이 안되는 경우 지웠다가 `GitHub`에서 바로 땡겨와서 설치하면 해결되는 경우도 있다고 한다.

```shell
$ pip uninstall pytube
$ pip install git+git://github.com/nficano/pytube
```

두 번째 줄 명령어를 쓰면

```shell
Collecting git+git://github.com/nficano/pytube
  Cloning git://github.com/nficano/pytube to /private/var/folders/sz/j246fn694zlf37xx9dn9mwwc0000gn/T/pip-req-build-can06r18
  Running command git clone -q git://github.com/nficano/pytube /private/var/folders/sz/j246fn694zlf37xx9dn9mwwc0000gn/T/pip-req-build-can06r18
```

하면서 설치가 진행된다.

나는 지웠다 다시 깔아도 안되서 다른 방법을 찾았다.

---

## 2. `~/pytube/__main__.py` 코드 직접 수정하기

`pytube` [개발자의 `GitHub`에서 에러 관련된 질문들][github]을 읽어보다가 찾았다.

일단 라이브러리가 설치된 곳에서 `pytube`의 `__main__.py`를 찾는다.
내 컴퓨터에서 해당 파일의 주소는 다음과 같았다.

```shell
.pyenv/versions/3.8.0/lib/python3.8/site-packages/pytube/__main__.py
```

해당 파일을 열면 `pytube`의 여러 기능들의 익숙한 함수명(?)을 볼 수 있다.

여기에서 `thumbnail_url`, `title`, `length`를 찾아서 다음과 같이 코드를 수정해준다. 코드 수정 내용의 출처는 [여기]다.

주석 처리한 부분은 원래 코드고, 그 아래에 `return`부터 `)`까지가 새로 추가된 부분이다.

### (1) `thumbnail_url`

```python
@property
def thumbnail_url(self):
    """Get the thumbnail url image.

    :rtype: str

    """
    # return self.player_config_args['thumbnail_url']
    return (
        self.player_config_args
        .get('player_response', {})
        .get('videoDetails', {})
        .get('thumbnail', {})
        .get('thumbnails', [])[0]
        .get('url')
    )
```

### (2) `title`

```python
@property
def title(self):
    """Get the video title.

    :rtype: str

    """
    # return self.player_config_args['title']
    return (
        self.player_config_args
        .get('player_response', {})
        .get('videoDetails', {})
        .get('title')
    )
```

### (3) `length`

```python
@property
def length(self):
    """Get the video length in seconds.

    :rtype: str

    """
    # return self.player_config_args['length_seconds']
    return (
        self.player_config_args
        .get('player_response', {})
        .get('videoDetails', {})
        .get('lengthSeconds')
    )
```

---

## 3. 결과 확인

실행 결과는 다음과 같이 나온다.

```python
>>> from pytube import YouTube
>>> yt = YouTube("https://www.youtube.com/watch?v=QTjZJzYWzEU")
>>> yt.thumbnail_url
'https://i.ytimg.com/vi/QTjZJzYWzEU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBQHfWmE2XWxkPj0NXL6z8N0cNqnQ'
>>> yt.title
'[풀버전] ♬ 싫다고 말해(Nightmare Ver.) - (여자)아이들 @3차 경연 컴백전쟁 : 퀸덤 8화'
>>> yt.length
'273'
>>>
```

터미널 화면도 캡쳐해보았다.
![Capture](/assets/images/posts/2019-10-19/capture.png)

**Profit!!**

여기까지 읽은김에 [예제에 사용한 동영상]이 뭔지 한 번 봅시다.

{% include youtube.html id="QTjZJzYWzEU" %}

~~(여자)아이들 최고 ㅠㅠ....~~

---

[github]: https://github.com/nficano/pytube/issues/434
[여기]: https://github.com/ndg63276/alexa-youtube/commit/94d671dbd5c214a88df6d568b745c36b272b2dc4
[예제에 사용한 동영상]: https://www.youtube.com/watch?v=QTjZJzYWzEU
