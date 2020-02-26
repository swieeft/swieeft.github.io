---
title: "[iOS] 스토리보드 레퍼런스(Storyboard Reference) 사용방법"
layout: post
date: 2020-02-24 13:50
tag:
    - iOS
    - Xcode
headerImage: false
image:
description: [iOS] 스토리보드 레퍼런스(Storyboard Reference) 사용방법
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
iOS 개발을 할 때 UI 개발을 하기 위해 많은 분들이 Storyboard를 이용합니다. Storyboard를 사용했을 때 장점은 제가 생각 했을 때 아래 3가지 입니다.

1. ViewController 간 연관 관계를 한 눈에 볼 수 있음
2. ViewController의 형태를 시각적으로 표현해줘서 UI가 어떻게 생겼는지 확인할 수 있음
3. 컨트롤 생성 시 Drag & Drop으로 간단히 생성 가능

하지만 프로젝트가 점점 커지고, 협업하는 인원이 많아지게 되면 Storyboard는 많은 문제점을 발생시키게 되는데 대표적으로 발생하는 2가지의 문제점은

1. Git Marge 시 Storyboard를  충돌이 발생함
2. Storyboard에 여러 개의 ViewController가 추가되면 Storyboard 실행이 느려지고, 심지어 Xcode가 멈춰 버리는 일도 발생함

이러한 문제를 해결하기 위해 2가지 방법을 많이 사용하게 되는데요. 

1. Storyboard를 사용하지 않고 100% 코드로 UI 개발
2. One Storyboard, One ViewController(하나의 스토리보드에 하나의 뷰컨트롤러만) = Storyboard 나누기

이렇게 2가지 방법을 많이 사용하는데, 이 글에서는 2번째 방법인 Storyboard를 나눌 때 필요한 Storyboard Reference 사용 방법에 대한 내용을 정리합니다.

서론이 길어졌네요. 바로 프로젝트를 만들어 보도록 하겠습니다.

### 스토리 보드 연결하기

---

프로젝트를 새로 생성하면 Main Storyboard와 ViewController가 생성되어 있는데요. 얘네를 프로젝트 메인화면으로 사용해서 진행하도록 하겠습니다.

- **기본 방법으로 Segue로 연결하기**

    우선 Storyboard Reference 사용하는 방법 전에 기본적으로 ViewController간의 Segue 연결 방식 및 동작을 보도록 하겠습니다.

    1. **FirstViewController 만들기**

        ViewController에서 이동할 FirstViewController를 생성 후 스토리보드의 ViewController에 클래스를 지정합니다.

        ![storyboardReference1.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference1.png)

    2. **ViewController에서 FirstViewController 연결하기**

        ViewController에 버튼을 추가한 후 버튼을 FirstViewController와 Segue 연결을 합니다. (저는 Show로 연결하였습니다.)

        ![storyboardReference2.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference2.png)

    3. **동작 확인**

        연결이 정상적으로 되었으면, 아래와 같이 버튼을 클릭하면 First ViewController로 이동하게 됩니다.

        ![storyboardReference3.gif](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference3.gif)

- **Storyboard Reference로 Segue 연결하기**

    지금까지는 기본적인 Segue 연결 방법을 보셨습니다. 이제부터 오늘의 본론인 Storyboard Reference 사용법을 알아보겠습니다.

    1. **FirstViewController를 Main Storyboard에서 분리하기**

        FirstViewController를 분리하기 위해 First Storyboard를 만들어 줍니다.

        ![storyboardReference4.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference4.png)

    2.  **FirstViewController를 First Storyboard로 이동하기**

        Main Storyboard에서 FirstViewController를 잘라내어(⌘ + C) First Storyboard에 붙여넣습니다(⌘ + V).

    3.  **FirstViewController Storyboard ID 만들기**

        Storyboard Reference를 이용하기 위해서는 Identity Inspector에서 ViewController에 Storyboard ID를 설정 해주어야 합니다.

        저는 FirstViewController라고 ID를 설정해주었습니다.

        ![storyboardReference5.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference5.png)

    4. **Initial View Controller 설정해주기**

        Storyboard Reference를 사용해서 이동하게 되는 ViewController는 해당 스토리보드의 첫 진입 ViewController가 되어야 합니다.

        첫 진입 ViewController로 설정하기 위해선 Attributes Inspector에서 is Initial View Controller를 체크 해주면 됩니다.

        ![storyboardReference6.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference6.png)

        is Initial View Controller가 설정되면 Storyboard에 해당 ViewController 앞에 → 화살표가 생깁니다.

        ![storyboardReference7.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference7.png)

    5. **Storyboard Reference 만들기**

        Main Storyboard로 돌아와 Library를 실행시켜 Storyboard Reference를 검색하여 추가합니다.

        ![storyboardReference8.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference8.png)

        Storyboard Reference를 추가하면 아래와 같이 조그맣게 표시됩니다.

        ![storyboardReference9.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference9.png)

    6. **Storyboard Reference에 FirstViewController 설정하기**

        Storyboard Reference가 어떤 ViewController의 Reference인지 설정을 해주어야 합니다. 

        설정을 하려면 Storyboard Reference를 클릭한 후 Attributes Inspector에 가서 아래와 같이 Storyboard를 선택하고, 위의 3번에서 설정해주었던 Storyboard ID를 입력해줍니다.

        ![storyboardReference10.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference10.png)

    7. **Storyboard Reference에 Segue 연결하기**

        Storyboard Reference에 Segue 연결하는 방법은 기존 방식과 동일하게 하면 됩니다. 버튼에서 마우스 우클릭 (or 트랙패드 두 손가락)으로 드래그해서 Storyboard Reference에 연결하면 Segue 연결이 완료 됩니다.

        ![storyboardReference11.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference11.png)

    8. **동작확인**

        동작은 위의 **기본 방법으로 Segue로 연결하기**와 동일합니다.

### Tabbar와 Storyboard Reference 연결하기

---

이번엔 Tabbar와 Storyboard Reference를 연결하는 방법을 알아보겠습니다. 전체적인 방식은 동일하지만 몇가지 추가되는 내용이 있어 따로 정리합니다.

1. **Second, Third Storyboard, ViewController 생성하기**

    Tabbar를 만들기 위해 Second, Third Storyboard, ViewController를 추가로 생성한 후 위의 나온 방법대로 설정을 해줍니다.

2. **Second, Third Storyboard, ViewController Segue 연결하기**

    Tabbar에 Segue를 연결하는데 이 때는 Show로 연결하지 않고 Relationship Segue의 view controllers를 선택해서 Tabbar에 연결 되도록합니다.

    ![storyboardReference12.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference12.png)

3. **실행해보기**

    이렇게 설정을 한 후 실행을 해보면 정상적으로 기능은 동작하지만 탭바 아이콘이 없는 상태로 나오게 됩니다.

    ![storyboardReference13.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference13.png)

4. **탭바 아이콘 설정하기**

    ViewController에 직접 연결하면 해당 ViewController에서 탭바 아이콘을 설정할 수 있었지만 Storyboard Reference를 이용해서 하면 ViewController에 탭바를 설정할 수 있는 곳이 없습니다.

    그러면 탭바 아이콘을 사용하지 못하는 것일까요? 그럼 이 글을 쓸 이유가 없었겠죠. 탭바에 연결된 ViewController로 이동한 후 Library에서 Tab Bar Item을 검색합니다.

    ![storyboardReference14.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference14.png)

    Tab Bar Item을 ViewController에 추가합니다.

    ![storyboardReference15.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference15.png)

    Tab Bar Item을 클릭한 후 Attributes Inspector에서 탭바 아이템을 설정 해줍니다.

    ![storyboardReference16.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference16.png)

5. **최종 실행 화면**

    설정 완료 후 빌드를 해보면 정상적으로 탭바 아이콘 및 타이틀이 나오는 것을 확인할 수 있습니다.

    ![storyboardReference17.gif](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference17.gif)

6. **(추가) Main Storyboard의 Tab Bar Controller에 아이콘 표시되도록 설정하기**

    이제 앱을 실행하면 정상적으로 탭바에 아이콘과 타이틀이 나오는 것을 확인 했습니다. 하지만 Storyboard의 Tab Bar Controller를 보면 아이콘과 타이틀이 제대로 표시 되지 않고 있어 UI 개발 시에  탭바에 어떤 탭들이 있는지 확인할 수 없습니다.

    ![storyboardReference18.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference18.png)

    이 때는 Storyboard Reference를 클릭 해보면 아래와 같이 Item이라는 항목이 있는 것을 확인 할 수 있습니다. Item을 클릭한 후 Attributes Inspector에서 탭바 아이템을 설정 해줍니다.

    ![storyboardReference19.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference19.png)

    설정이 완료 되면 Tab Bar Controller에서 설정된 값이 보여지는 것을 확인할 수 있습니다. 다만 여기에 설정되는 값은 Storyboard에서만 표현되고 실행 시에는 표시가 되지 않으니 유의바랍니다.

    ![storyboardReference20.png](/assets/images/posts/2020-02-24/StoryboardReference/storyboardReference20.png)

### 마무리

---

내용이 간단해서 짧게 글이 정리 될 줄 알았는데 설정 값이나 유의해야 될 부분들이 있다보니 글이 길어졌습니다. 글이 길다고 설정이 복잡하거나 하진 않으니 차근차근 따라 해보시면 쉽게 사용법을 익히실 수 있습니다.

프로젝트의 스토리보드가 너무 거대해졌다거나 협업을 하는데 자꾸 스토리보드에서 문제가 발생한다면 한번 적용해보셔도 좋을 것 같습니다.

긴 글 읽어주셔서 감사합니다. 달콤한 코딩 되세요!

### 예제 프로젝트 링크

---

[https://github.com/swieeft/StoryboardReference](https://github.com/swieeft/StoryboardReference)

### 참고자료

---

[[iOS] 스토리보드 레퍼런스(Storyboard Reference)](https://minominodomino.github.io/devlog/2019/05/21/ios-StoryboardReference/)
