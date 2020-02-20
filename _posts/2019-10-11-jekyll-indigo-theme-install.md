---
title: "Jekyll-Indigo theme 설치 완료! 그 과정에 겪은 삽질 네 가지"
layout: post
date: 2019-10-11 22:10
tag:
- jekyll
- GitHub
headerImage: false
description: Jekyll-Indogo theme 삽질 설치기
category: blog
author: hsj00
externalLink: false
published: true
comments: true
share: true
---

10/01부터 GitHub 블로그를 설치해보려고 수많은 블로그와 저장소를 들락날락 거렸다. 고생 끝에 설치 완료하고 기념 포스팅을 작성해본다. 블로그 테마는 Jekyll-Indigo theme를<sup>[^1]</sup> 사용했다.

![Indigo theme](/assets/images/posts/2019-10-11/jekyll-template-github.png)

포스팅을 준비하면서 문제가 됐던 부분들은 가지 정도다.

- `localhost:4000`으로 접속해서 상태 확인하기
- `_config.yml`의 세부 내용 설정하기
- `GitHub` 동기화 문제
- `baseurl`의 경로 설정하기

----------

## 1. `localhost:4000`으로 접속해서 상태 확인하기

Jekyll로 GitHub 블로그를 설정하는 수많은 포스팅마다 명령어가 조금씩 달랐다.
어떤 포스팅<sup>[^2]</sup>에서는 다음과 같이 나와있었다.

```shell
$ git clone https://github.com/wowthemesnet/mediumish-theme-jekyll.git
$ cd mediumish-theme-jekyll
$ bundle
$ jekyll
```

하지만 내가 하면 이런 메시지가 나왔다.
```shell
$ bundle
Using concurrent-ruby 1.1.5
Using i18n 0.9.5
...
...
...
Using sinatra-contrib 1.4.7
Using jekyll-admin 0.9.0
Bundle complete! 3 Gemfile dependencies, 98 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```
```shell
$ jekyll
Traceback (most recent call last):
	13: from /usr/local/bin/jekyll:23:in `<main>'
...
...
...
    1: from /usr/local/Cellar/ruby/2.6.5/lib/ruby/2.6.0/bundler/lockfile_parser.rb:95:in `initialize'
/usr/local/Cellar/ruby/2.6.5/lib/ruby/2.6.0/bundler/lockfile_parser.rb:108:in `warn_for_outdated_bundler_version': You must use Bundler 2 or greater with this lockfile. (Bundler::LockfileError)
```
`bundle` 명령어는 실행하면 뭐가 막 설치됐다고 뜨는데 `jekyll`이라고 하면 안돼서 여기서 첫 멘붕이 왔다.

뭐가 문제인지 찾다가 Jekyll 관련 내용들이 번역된 곳<sup>[^3]</sup>에서 해결 방법을 찾을 수 있었다.
```shell
$ sudo gem install jekyll bundler
```
```shell
$ bundle exec jekyll serve
```
이 다음에는 브라우저에서 http://localhost:4000 에 접속이 잘 됐다.

이유는 잘 모르겠지만 추측컨데 `jekyll`이 종속적인? 뭐 그런 프로그램이라서 `exec` 명령어를 사용해 `bundle`로 `jekyll`을 실행하는 뭐 그런걸까 하고 혼자 생각하고 넘어갔다. 정확한건 잘 모르겠다.

----------
## 2. `_config.yml`의 세부 내용 설정하기

`localhost`로 삽질한거에 비하면 이건 진짜 식은 죽 먹기였다.

`_config.yml` 파일을 열어서 표시된 항목마다 필요한 내용을 채워넣으면 됐다. 따로 뭘 더 추가하거나 변경하다가 골치아파질까봐 다른 사람들 블로그에 있는 내용들 비교해가며 작성했다. 작성할 때 여러모로 많이 참고했던 블로그<sup>[^4]</sup>에 각 항목별로 잘 설명을 해놓았다. 참고로 다 영어로 써있다.

`_config.yml`을 채워넣을 때 가장 고생했던 부분은 `baseurl`인데 이 부분은 밑에서 따로 쓰겠다.

----------
## 3. `GitHub` 동기화 문제

`localhost:4000`에서도 제대로 보이고, `_config.yml`파일도 다 채워넣었는데 저장소에 올리기만 하면 제대로 나오질 않고 데모 사이트 화면으로 넘어갔다.

[![example](/assets/images/posts/2019-10-11/github-sync-error01.png)](https://github.com/hsj00/example)

어찌저찌해서 원격저장소에 올리고 나면 Jekyll-Indigo theme가 들어있는 폴더는 열리지 않고 마치 파일 덩어리 하나처럼 있었다.[^5] 블로그 첫 포스팅이라고 원격저장소에 예제로 만들어서 올려놓았는데 이거 관련된 내용은 평생 안까먹을 것 같다.

![folder capture](/assets/images/posts/2019-10-11/github-sync-error02.png)

숨김 파일/폴더도 볼 수 있게 바꾸고 보니깐 Indigo theme 가져오면서 거기에 있던 저장소의 `.git` 폴더도 그래도 있는 것을 알 수 있었다. 이것도 모르고 왜 `commit`이나 `push`가 왜 안되는지 끙끙 앓았었다.

내가 로컬 저장소로 `git init`할 때 만들어진 `.git` 폴더는 `indigo` 폴더 바깥에 있었고, indigo theme의 저장소에서 만들어진 `.git` 폴더는 `indigo` 폴더 바깥에 있었다.

`.git` 폴더가 저장소에 대한 정보를 담고있는 폴더인 것 같은데, 내가 만든 저장소의 정보가 `clone`해온 저장소의 정보가 다르니 에러가 발생한 것 같다.

이번 일 덕분에 `GitHub`에 뭐 올릴 때 까먹진 않을 것 같다.

모르는 게 너무 많고, 배워야 할 것들이 넘쳐난다....

----------
## 4. `baseurl`의 경로 설정하기

다른건 다 멀쩡해보이는데, `localhost:4000`로 접속했을 때는 잘 나오는데 저장소에 올리기만 하면 자꾸 Indigo theme의 Demo site로 넘어갔다. `_config.yml`에서 설정을 다 끝마치면 그 내용을 바탕으로 `_site`에 반영이 되는걸까 싶어서 `.gitignore`에 `_site` 폴더가 추가되어있는걸 비활성화 시켜보기도 하고, 하다하다 `localhost:4000`에서 나오는 화면들을 따로 복사하고 저장하고 별 삽질을 다 했다.

그런데 문제의 원인은 다른 곳에 있었다.

```yaml
...
jekyll-mentions:
    base_url: /indigo/
...
```

`base_url`에 그동안 `https://hsj00.github.io` 주소를 통째로 입력해뒀었다.

`_config.yml`에 있는 항목들을 하나하나 검토해보다가 혹시 디렉토리 구조? 경로?가 이상하게 설정돼서 각항목들을 제대로 연결시켜주지 못하는건가? 하는 생각이 들었다. url 관련된 항목들을 구글링 하다가 결국 답<sup>[^6]</sup>을 얻을 수 있었다.

![baseurl](https://kairos03.github.io/assets/img/posts/jekyll/2017-09-11-learing-Up-Confusion-Around-baseurl/1.png)

위 그림을 내 식대로 이해하자면, `base_url`의 정의?에 따라 요구되는 주소는 기본 도메인?을 최상위로 봤을 때는 `/` 형태로 입력해야한다. 그리고 Jekyll-Indigo theme를 다른 하위 폴더에 넣어서 관리하고 있다면 `/{folder_name}/` 형태로 입력해줘야 제대로 반영되는 것 같다.

사람은 역시 배워야 하고, 모르면 몸이 고생한다....

----------
[^1]: https://github.com/sergiokopplin/indigo
[^2]: https://blog.chulgil.me/how-to-make-blog-using-github-4/
[^3]: https://jekyllrb-ko.github.io/docs/quickstart/
[^4]: http://artiannaswamy.com/build-a-github-blog-part-2
[^5]: https://github.com/hsj00/example
[^6]: https://kairos03.github.io/jekyll/2017/09/11/learing-Up-Confusion-Around-baseurl.html