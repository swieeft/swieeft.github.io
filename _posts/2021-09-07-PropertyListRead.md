---
layout: post
title: "plist(PropertyList) 데이터 가져오기"
subtitle: "[iOS, Swift]"
date: 2021-09-07 16:00
background: 
tags: [ios, swift]
---

앱을 개발할 때 앱의 설정 값들은 어떻게 관리하시나요?

보안이 필요하다면 키체인에서 관리를 하거나, 아니면 API를 통해서 받아오거나, 또는 내부 DB 등을 이용해서 관리를 합니다.

iOS에서 가장 보편적으로 사용하는 방법 중 하나는 PropertyList(이하 plist)를 이용해서 관리하는 방법입니다. 대표적인 것이 앱을 만들 때 기본적으로 생성되는 info.plist가 있죠.

그리고 Firebase를 사용한다면 GoogleService-Info.plist도 보셨을겁니다.

이렇게 plist를 만들고서 plist 안에 있는 데이터를 가져와 활용을 해야 되는데 오늘은 이 방법에 대해서 알아보고자 합니다.

<br>

### PropertyList 만들기

---

우선 읽어 올 데이터를 먼저 만들어 보겠습니다.

1. **새로운 파일을 생성 창을 엽니다. (Command(⌘) + N)**

2. **Resource 섹션의 PropertyList를 선택합니다.**

    ![PropertyListRead1.png](/assets/images/posts/2021-09-07/PropertyListRead1.png)

3. **생성된 PropertyList를 선택합니다.**

    ![PropertyListRead2.png](/assets/images/posts/2021-09-07/PropertyListRead2.png)

4. **PropertyList에 원하는 데이터를 입력합니다.(PropertyList는 Key-Value가 쌍으로 이루어져야 합니다)**

    ![PropertyListRead3.png](/assets/images/posts/2021-09-07/PropertyListRead3.png)

>> 예제에서는 사용자 정보를 가지고 있는 UserInfo.plist를 만들었습니다. 예제 프로젝트를 확인하고 싶으신 분들은 아래 Github 링크를 통해 받으실 수 있습니다.

[Example Project Github Link](https://github.com/swieeft/PropertyListRead)

<br>

### Dictionary 형태로 가져오기

--- 

이제 데이터도 준비 되었으니 실제로 데이터를 가져오는 방법에 대해서 알아보겠습니다.

첫번째는 Dictionary 형태로 가져오는 방법인데요. 이 방법의 장단점을 먼저 보겠습니다.

- **장점**

    - 모델을 정의하거나 디코딩 과정을 생략할 수 있어서 쉽게 개발을 할 수 있음

    - 데이터가 추가, 삭제 되더라도 유연하게 대처가 가능함

- **단점**

    - 키 값을 모를 경우 데이터를 가져올 수 없음

    - 키 값에 오타가 있을 경우 데이터를 가져올 수 없음

    - 데이터 형을 모르기 때문에 캐스팅 시 오류가 발생할 수 있음

이렇게 보면 Dictionary를 사용하는 것은 참 안 좋아 보이지만 개발 시에 간단한 경우에는 오히려 복잡한 과정을 거치지 않을 수 있어서 유리할 수 있습니다.

- **예제 코드**

    <p> {% gist swieeft/51b407f0f453b71da7adb13c8e869e66 plist1.swift %} </p>

- **실행 결과**

    ![PropertyListRead4.png](/assets/images/posts/2021-09-07/PropertyListRead4.png)

    예제 프로젝트 실행 결과 데이터가 잘 나오는 것을 확인 할 수 있습니다.

<br>

### Struct 형태로 가져오기

---

좀 더 정리된 형태로 가져오고 싶고, Dictionary의 단점을 커버할 수 있는 방법이 어떤 것이 있을까요?

바로 Struct 형태로 만들어서 사용하는 것입니다. Struct로 만들 때의 장단점을 먼저 보면

- **장점**

    - 이미 Struct에 키와 데이터형을 정해 놓기 때문에 Dictionary에서의 단점을 해결할 수 있음

- **단점**

    - Struct를 정의해야하고, 데이터를 디코딩하는 과정이 필요하기 때문에 다소 코드가 복잡해질 수 있음(하지만 이로인해 얻는 이득이 더 클 수 있음)

    - 데이터가 추가, 삭제 되면 Struct를 수정해줘야 하고, 최악의 경우 데이터 파싱이 실패해서 nil이 반환될 수 있음

이렇게 보면 결국 Dictionary와 Struct는 어떤게 더 좋다기 보단 그때그때 상황에 맞게 쓰는게 좋은 것 같습니다.

- **예제 코드**

    우선 데이터를 담을 Struct를 만들어줍니다.

    <p> {% gist swieeft/51b407f0f453b71da7adb13c8e869e66 plist2.swift %} </p>

    그 후 PropertyList를 디코딩합니다.

    <p> {% gist swieeft/51b407f0f453b71da7adb13c8e869e66 plist3.swift %} </p>

- **실행 결과**

    ![PropertyListRead5.png](/assets/images/posts/2021-09-07/PropertyListRead5.png)

    예제 프로젝트 실행 결과 데이터가 잘 나오는 것을 확인 할 수 있습니다.

<br>

### 마무리

---

지금까지 PropertyList에서 데이터를 가져오는 방법에 대해서 알아보았습니다.

프로젝트를 할 때 설정 값들을 하드 코딩하는 경우들이 많았는데 PropertyList로 관리를 하면 좀 더 깔끔하고 직관적이게 관리할 수 있을 것 같다는 생각을 했는데요.

Extension 등을 활용하면 지금보다 더 직관적이고 간결하게 사용할 수 있을 것 같습니다.

그럼 달콤한 코딩 되세요!

<br>

### 참고자료

--- 
[Swift 5: How to read variables in plist files?](https://stackoverflow.com/questions/60803515/swift-5-how-to-read-variables-in-plist-files)

