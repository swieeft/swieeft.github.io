---
layout: post
title: "UITableView Paging 구현하기"
subtitle: "[Swift]"
date: 2020-07-20 11:30
background: 
tags: [ios, swift]
---

안녕하세요. 장마철에 날씨도 꿉꿉해서 나가기 싫어지는 날씨입니다. 

이런 날에는 그냥 집에서 에어컨 바람 맞으면서 가만히 있고 싶지만 일을 해야 한다는 슬픈 현실을 마주하며 포스팅을 시작해봅니다... ㅠㅠ

---

오늘은 UITableView에서 Paging 처리하는 방법에 대해 알아보려고 합니다. 

인터넷을 검색해보면 많은 방법들이 소개 되고 있지만 제가 테스트 해보면서 제일 안정적이고 보기 좋은 방법을 소개해보려고 합니다.

그리고 더 나아가 페이징 처리할 때 스크롤이 제멋대로 튀는 현상을 막는 방법에 대해서도 소개해보려고 합니다.

### UITableView Paging 처리 하기

---

테이블 뷰를 처리하는 방법은 간단합니다. 데이터를 받아 와서 기존 데이터에 계속 Append 시켜주기만 하면 됩니다.

기본 개념은 위와 같고 거기에 부수적으로 동작을 제어하는 몇몇 코드만 추가하면 간단하게 페이징 처리를 할 수 있습니다.


### 예제 UI 구성 

---

UI 구성은 간단하게 테이블 뷰에 셀 2개를 만들었습니다.

- 첫번째 셀 : 제목과 날짜를 표시해주는 Label이 있는 셀

- 두번째 셀 : 페이징 시 로딩 중인 것을 표시해주는 셀

![PagingTableView1.png](/assets/images/posts/2020-07-20/PagingTableView1.png) 

그리고 뷰컨트롤러에 테이블 뷰 Delegate와 DataSource를 연결해줍니다. 

![PagingTableView2.png](/assets/images/posts/2020-07-20/PagingTableView2.png) 

그러면 우선 UI는 준비가 완료 됩니다.

### 예제 코드

---

- **예제 Cell Class 구현**

    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView6.swift %} </p>

- **예제 Data Model**
    
    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView1.swift %} </p>

    우선 페이징시 셀에 넣을 데이터의 Model을 만들어 줍니다. 저는 간단하게 제목과 날짜만 표시하기 때문에 위와 같이 모델을 구성하였습니다.


- **ViewController 전역 변수 선언**

    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView2.swift %} </p>

    ViewController에 전역적으로 페이징에 사용할 변수들을 선언해줍니다.

- **UITableView Delegate, DataSource 처리** 
    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView3.swift %} </p>

    TableView를 설정하기 위해 Delegate와 DataSource를 처리해줍니다.

    여기서 유의할 점은 Section을 2개를 만들어서 Section 0에서는 실제 테이블 뷰에 표시될 데이터들을 세팅해주고, Section 1에서는 페이징 시 보여줄 로딩 셀을 보여주도록 합니다.

- **데이터 세팅하는 Paging 메소드 구현하기**

    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView4.swift %} </p>

    Paging 처리를 할 때 호출 할 메소드를 구현합니다. 이 예제에서는 한 페이지 당 20개의 데이터를 생성하여 추가하도록 개발하였습니다.

    메소드 구현 시 주의할 점은 데이터를 새로 세팅하는 것이 아니라 기존 데이터에 계속 append 시켜주어야 합니다.

- **테이블 뷰 스크롤 시 Paging 메소드 호출**

    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView5.swift %} </p>

    테이블 뷰를 스크롤 하다가 맨 끝에 다다르게 되면 다음 페이지를 호출합니다.

    다음 페이지를 호출 할 때 reloadSections를 통해 로딩 셀이 보이도록 처리해줍니다.

- **실행 화면**

    ![PagingTableView3.gif](/assets/images/posts/2020-07-20/PagingTableView3.gif) 

### 페이징 시 스크롤이 튀는 현상 해결 방법

위의 예제 코드는 모든 셀이 동일한 사이즈를 가지고 있어 페이징을 할 때 스크롤이 튀는 현상이 안 나타납니다.

하지만 Label에 텍스트가 여러 줄로 표시 되거나, 이미지의 높이가 여러가지 일 경우 페이징 시 스크롤이 제멋대로 튀는 현상을 경험할 수 있습니다.

그래서 스크롤이 튀는 것을 방지하고 페이징이 안정적이게 동작하는 방법에 대해 알아보겠습니다.

- **동적인 높이의 셀에서 스크롤이 튀는 화면**

    ![PagingTableView4.gif](/assets/images/posts/2020-07-20/PagingTableView4.gif) 

    예시 화면에서는 페이징 후에 스크롤을 하려고 내리는 순간 스크롤이 순간적으로 위로 튀었다가 내려가는 모습을 확인할 수 있습니다.

    이 외에도 페이징 후 테이블 뷰가 reload 될 때 스크롤 offset이 달라지는 경우도 있고 여러가지 스크롤 문제가 발생하는 것을 확인 할 수 있습니다.

- **원인 분석**

    동적 셀의 경우 테이블 뷰에서 셀의 높이 계산을 할 때 우선 우리가 정해준 estimatedRowHeight를 기준으로 셀을 그린 후에 데이터에 맞게 높이값을 재정의 합니다.

    만약 우리가 셀의 estimatedRowHeight 값을 50pt로 주었고, 셀을 10개 그려준다면 테이블 뷰는 500pt 만큼의 높이를 먼저 잡아주고 난 후에 각 셀의 데이터에 맞춰 높이를 재정의 합니다.

    그렇게 첫번째 페이지가 그려지고 난 후에 2번째 페이지 데이터를 받아 오면 전체 셀이 다시 estimatedRowHeight 값을 기준으로 reload를 하게 되는데 여기서 문제가 발생합니다.

    두번째 페이지를 받아오면 셀이 20개가 되면서 estimatedRowHeight 값이 50pt이기 때문에 테이블 뷰는 1000pt 만큼의 높이 값을 생각하고 셀을 다시 그리게 되는데 이전에 만들어져 있는 셀들의 높이값이 50pt랑 다르게 되면 여기서 스크롤의 offset이 달라지거나 튀는 경우가 발생하게 됩니다.

    - **첫번째 페이지일 때**

        ![PagingTableView5.png](/assets/images/posts/2020-07-20/PagingTableView5.png)

    - **두번째 페이지 부터의 계산 오류**

        ![PagingTableView6.png](/assets/images/posts/2020-07-20/PagingTableView6.png)

- **해결 방법**

    동적 셀의 스크롤 문제를 해결하기 위해서는 이전 셀들의 높이 값을 저장하고 다시 그려질 때 이전 셀들은 해당 높이값으로 설정 해주도록 하는 것이 필요합니다.

    <p> {% gist swieeft/38b367dd1d4c7583e7e5350b1edbc8ec PagingTableView7.swift %} </p>    

    이렇게 코드를 추가해주면 페이징 시 스크롤이 정상적으로 동작하는 것을 확인 할 수 있습니다.

- **결과 화면**

    ![PagingTableView7.gif](/assets/images/posts/2020-07-20/PagingTableView7.gif)    

### 마무리

---

이렇게 UITableView 페이징 처리 방법과 스크롤이 튀는 현상을 해결하는 방법에 대해 알아보았습니다. 

페이징 처리에 대해서는 많은 리소스가 존재하는데 막상 스크롤이 튀는 현상에 대한 해결 방법을 정리한 글을 많이 찾아볼 수 없어서 우연하게 발견하여 해결한 것을 공유하고자 이 글을 작성하게 되었습니다.

저도 페이징 처리 시에 스크롤이 튀는 현상으로 인해서 많은 고통을 받았는데 드디어 이걸 해결 할 수 있어서 너무나도 기분이 좋습니다. 저처럼 고통 받는 또 다른 누군가가 이 고통에서 벗어나길 바랍니다.

그럼 달콤한 코딩 되세요!

### 예제 프로젝트

---

[swieeft/PagingTableView](https://github.com/swieeft/PagingTableView)

### 참고자료

--- 

[Infinite Scrolling - Swift 4, iOS11](https://youtu.be/OTHkcf9gSRw)

[stack overflow - reloadData() of UITableView with Dynamic cell heights causes jumpy scrolling](https://stackoverflow.com/a/38729250)