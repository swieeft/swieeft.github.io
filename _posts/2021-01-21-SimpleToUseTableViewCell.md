---
layout: post
title: "간단하게 TableView Cell 등록, 재사용하기"
subtitle: "[iOS, Swift]"
date: 2021-01-21 10:20
background: 
tags: [ios, swift]
---

안녕하세요. 다사다난한 2020년이 지나고 이제 2021년이 되었네요. 모두 고생 많으셨고, 새해에는 모두가 즐겁고 행복한 한해가 되었으면 좋겠습니다. 모두 새해 복 많이 받으세요!

---

2021년 처음으로 작성할 내용은 간단하게 TableView Cell 등록, 재사용하기입니다.

### 일반적인 방법

--- 

우선 일반적으로 셀을 등록하고 재사용하는 코드를 보도록 하겠습니다.

- **셀 등록**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell1.swift %} </p>

- **셀 재사용**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell2.swift %} </p>

코드들을 보시면 셀 등록 시에는 nibName과 forCellReuseIdentifier를 넣어주어야 하고, 셀 재사용 시에는 withIdentifier를 넣어주어야 하는데 세개의 파라메터 전부 String을 값을 받도록 되어 있습니다.

일반적인 방법으로 사용해도 상관은 없지만 개인적인 생각으로는 유지보수 측면에서 4가지 위험 요소가 있습니다.

1. nibName과 셀 id를 하드코딩하면 수정이 발생 했을 경우 사용한 모든 곳을 일일히 바꿔주어야함
2. 파라메터가 String이기 때문에 빌드 시에는 해당 셀의 존재 유무를 판단할 수 없어 실수로 수정하지 않거나, 오타가 난다면 크래시가 발생할 확률이 높음
3. nibName과 셀 id를 enum이나 따로 상수로 지정해서 사용한다고 하더라도 추후에 셀이 추가, 삭제 될 경우에 제대로 관리를 하지 않는다면 코드가 중구난방으로 짜여질 가능성이 높음
4. 셀 재사용하는 부분에서 커스텀 셀의 경우 캐스팅을 해주어야 사용이 가능한데 캐스팅 실패가 발생할 확률이 있음

### 간단하게 사용하는 방법

---

그렇다면 위에 일반적인 방법의 문제점을 어떻게 해결할 수 있을까요? 방법은 간단합니다. 프로토콜을 만들어서 위임 받아 사용하면 됩니다.

- **프로토콜 정의**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell3.swift %} </p>

    TableViewCelled란 이름으로 프로토콜을 정의합니다. 여기서 프로토콜명은 원하시는 것으로 변경하셔도 상관 없습니다.

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell4.swift %} </p>

    정의한 프로토콜을 Extension을 활용해서 기능을 정의해줍니다.

    - register : 셀을 등록하는데 사용하는 메서드입니다.
    - dequeueReusableCell : 셀 재사용 시 사용하는 메서드입니다.
    - reuseIdentifier : 셀의 id
    - NibName : 셀의 NibName

- **셀의 클래스명, NibName, ID 맞추기**

    간단하게 사용하는 방법의 핵심은 클래스명, NibName, ID를 맞춰서 사용하는 것입니다. 

    이렇게 통일하는 이유는 위에서 정의한 reuseIdentifier과 NibName이 **String(describing: self)**를 리턴하는데, 클래스 명을 리턴하기 때문에 클래스명과 동일하고 NibName과 ID를 맞추어야 register와 dequeueReusableCell을 간단하게 사용할 수 있기 때문입니다.

    - Nib 파일명 맞추기

        ![SimpleToUseTableViewCell1.png](/assets/images/posts/2021-01-21/SimpleToUseTableViewCell1.png)

    - 셀 ID 맞추기

        ![SimpleToUseTableViewCell2.png](/assets/images/posts/2021-01-21/SimpleToUseTableViewCell2.png)

- **셀에 프로토콜 위임**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell5.swift %} </p>

    특정 셀에만 추가하고 싶으면 셀에 프로토콜을 위임 받도록 합니다.

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell6.swift %} </p>

    모든 셀에 동일하게 프로토콜을 위임 받으려면 UITableViewCell extension 만들어 위임 받으면 모든 테이블 뷰 셀에서 사용 가능하게 됩니다.

- **셀 등록**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell7.swift %} </p>

    >> 여기서 tableView는 셀을 등록할 테이블 뷰 인스턴스입니다.

- **셀 재사용**

    <p> {% gist swieeft/ae72ee7470e6e4009f0ed0946abdc97b SimpleToUseTableViewCell8.swift %} </p>

일반적인 방법보다 코드가 더 명확하고 간결해진 것을 확인 할 수 있습니다. 위에서 얘기한 4가지 문제점에 대해서도 해결이 된 것을 확인할 수 있는데요.

1. nibName과 셀 id를 하드코딩하면 수정이 발생 했을 경우 사용한 모든 곳을 일일히 바꿔주어야함
    >> -> 클래스명을 기준으로 하기 때문에 수정이 발생하면 nibName과 id만 수정해주면 됨

2. 파라메터가 String이기 때문에 빌드 시에는 해당 셀의 존재 유무를 판단할 수 없어 실수로 수정하지 않거나, 오타가 난다면 크래시가 발생할 확률이 높음
    >> -> 테이블 뷰 셀의 클래스에 종속적으로 사용되기 때문에 존재하지 않는 셀에 대해서 입력하는 실수를 컴파일 단에서 바로 잡을 수 있고, 수정 누락이나 오타에 대한 문제도 없음

3. nibName과 셀 id를 enum이나 따로 상수로 지정해서 사용한다고 하더라도 추후에 셀이 추가, 삭제 될 경우에 제대로 관리를 하지 않는다면 코드가 중구난방으로 짜여질 가능성이 높음
    >> -> 셀이 추가, 삭제가 된다고 하더라도 따로 관리 해주지 않아도 되기 때문에 코드의 통일성이 생김

4. 셀 재사용하는 부분에서 커스텀 셀의 경우 캐스팅을 해주어야 사용이 가능한데 캐스팅 실패가 발생할 확률이 있음
    >> -> 확실한 타입 캐스팅이 가능하기 때문에 코드도 간결해지고 캐스팅이 실패하지 않음

### 마무리

---

지금까지 간단하게 TableView Cell 등록, 재사용 하는 방법에 대해서 알아보았습니다.

테이블 뷰 같은 경우엔 많이 사용되는 컨트롤 중에 하나이기 때문에 항상 반복적으로 어렵게 사용하는 코드를 어떻게 하면 간결하고 편하게 할 수 있을까 고민 했는데 간결하고 명확하게 사용할 수 있는 방법을 찾아내서 개발의 피로도가 좀 더 낮아졌습니다.

여러분도 피로도를 줄일 수 있도록 한번 사용해보세요. 다른 부분에서도 응용을 하면 좋은 아이디어가 나올 것 같은데, 이건 저도 연구를 해봐서 좋은 코드가 나온다면 그걸로 글을 한번 써보겠습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

--- 

[How to use the coordinator pattern in iOS apps](https://www.hackingwithswift.com/articles/71/how-to-use-the-coordinator-pattern-in-ios-apps) 
>> Storyboarded 프로토콜에서 힌트를 얻음

