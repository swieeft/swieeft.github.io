---
layout: post
title: "YouTube Player 사용하기"
subtitle: "[iOS]"
date: 2020-04-09 13:40
background: 
tags: [ios, swift]
---

안녕하세요. 오랜만에 블로그에 글을 남깁니다.

오늘은 유튜브 플레이어 사용 방법에 대해 알아보려고 합니다.

유튜브에 있는 영상을 앱 내에서 보여주고 싶은데 일반적인 iOS의 영상 플레이어 방식으로는 유튜브 영상을 가져올 수 없습니다.

그 이유는 iOS에서 제공해주는 API는 영상 파일의 URL을 받아서 영상을 실행시켜주는 방식인데, 유튜브에서 제공하는 URL은 영상 파일이 아니고 단순한 페이지여서 그렇습니다.

그럼 유튜브 플레이어를 앱 내에 개발하는 방법에 대해 알아보겠습니다.

### YouTube Player 라이브러리

---

유튜브에서는 앱에서 사용할 수 있도록 라이브러리를 제공해주고 있습니다. 그래서 라이브러리를 이용해서 개발을 하면 되는데요.

하지만 아래 링크를 들어가시면 문제가 있는 것을 할 수 있습니다. 업데이트가 된지 한참 되었다는 것인데요. 당연히 요즘 이슈가 되는 UIWebView에 대한 대응도 안 되어 있겠죠.

이 라이브러리를 사용해서 개발을 하면 조만간 앱이 업데이트 거부 당할 위험이 있어보입니다...

- [youtube-ios-player-helper](https://github.com/youtube/youtube-ios-player-helper)

그래서 WKWebView로 개발 된 다른 라이브러리를 찾아보았습니다. YoutubePlayer-in-WKWebView라는 라이브러리인데요. 

WKWebView로 개발되어 있고, 사용 방법도 간단해서 이 라이브러리를 이용해서 유튜브 플레이어를 개발하는 방법에 대해 알아보겠습니다.

- [YoutubePlayer-in-WKWebView](https://github.com/hmhv/YoutubePlayer-in-WKWebView)

### YoutubePlayer-in-WKWebView 설치하기

---

라이브러리를 사용하기 위해 우선 설치를 진행해줍니다. YoutubePlayer-in-WKWebView는 Cocoapods만 지원해주기 때문에 Cocoapods를 사용해서 설치를 진행합니다.

> Cocoapods 사용법을 모르시는 분들은 아래 링크에서 먼저 사용법을 익힌 후에 진행 하세요.
> - [왕 초보를 위한 CocoaPods(코코아팟) 사용법 (Xcode와 연동)](https://zeddios.tistory.com/25)

Podfile에 아래 내용을 작성하신 후에 pod install을 해서 라이브러리를 설치해줍니다. 

라이브러리 버전은 글 작성 기준 v0.3.0이기 때문에 버전이 변경 되었을 수 있으니 확인 후 진행하세요.

<p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer1.rb %} </p>

### StoryBoard에 Player View 만들기

---

예제는 스토리보드를 사용하여 UI를 구성합니다. 코드나 SwiftUI를 이용하셔도 상관 없습니다.

- **PlayerView 추가**

    영상을 띄어줄 UIView를 하나 추가해줍니다. 구분을 위해 뷰의 배경색을 주황색으로 지정해주었습니다.

    ![YouTubePlayer1.png](/assets/images/posts/2020-04-09/YouTubePlayer1.png)

- **AutoLayout 설정**

    오토레이아웃은 상단, 좌, 우를 Safe Area에 딱 맞게 지정을 해주었습니다. 그리고 요즘 영상들 대부분이 16:9 비율로 제작되기 때문에 뷰의 비율을 16:9로 지정 해주었습니다.

    ![YouTubePlayer2.png](/assets/images/posts/2020-04-09/YouTubePlayer2.png)

- **UIView에 Custom Class 지정하기**

    이제 UIView에 Custom Class를 지정하여 유튜브 플레이어 뷰로 만들어 줍니다. 커스텀 클래스는 **WKYTPlayrView**를 선택해주시면 됩니다.

    ![YouTubePlayer3.png](/assets/images/posts/2020-04-09/YouTubePlayer3.png)

### 코드 작성

---

UI 생성을 완료하였으니 이제 코드 작업을 해야 될 차례입니다.

- **라이브러리 Import**

    유튜브 플레이어 라이브러리를 사용하기 위해 라이브러리를 Import 해줍니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer2.swift %} </p>

- **IBOutlet 연결**

    스토리보드에서 생성한 뷰를 IBOutlet으로 연결합니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer3.swift %} </p>

- **영상 가져오기**

    유튜브에서 원하는 영상의 id 값을 가져와서 load 시켜주면 작업이 완료 됩니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer4.swift %} </p>

- **결과 화면**

    ![YouTubePlayer4.png](/assets/images/posts/2020-04-09/YouTubePlayer4.png)

### YouTube Video Id란?

---

YouTube Video Id는 유튜브에 영상 업로드 시 생성되는 고유값으로 영어, 숫자, 언더바( _ )로 이루어져 있습니다. 

이 값을 통해 어떤 영상인지 유튜브에서 판단하고 해당 영상을 찾아서 보여줄 수 있는 것입니다.

- **YouTube Video Id 확인 방법**

    YouTube Video Id를 알아내는 방법은 쉽습니다. 해당 영상에 들어가면 URL에 영상의 아이디를 확인할 수 있습니다.

    - 브라우저 상단 URL에서 확인하기

        브라우저 상단 URL에 v= 이후로 나오는 문자가 영상의 아이디 입니다.

        ![YouTubePlayer5.png](/assets/images/posts/2020-04-09/YouTubePlayer5.png)

    - 공유하기 URL에서 확인하기

        영상의 공유하기 버튼을 눌렀을 때 나오는 URL에서 youtu.be/ 다음에 나오는 문자가 영상의 아이디 입니다.

        ![YouTubePlayer6.png](/assets/images/posts/2020-04-09/YouTubePlayer6.png)

### 영상을 전체 화면이 아닌 뷰 안에서만 재생 되도록 만들기

---

위의 작업이 완료 된 후 영상을 재생하면 뷰 안에서 재생이 되지 않고 새로운 플레이어 화면이 나와서 영상이 재생되게 됩니다.

하지만 요구사항에서 뷰 안에서 재생 되도록 만들어 달라고 할 때가 있는데요. 그 때는 유튜브에서 제공하는 [playsinline 매개변수](https://developers.google.com/youtube/player_parameters?hl=ko#playsinline)를 사용해서 작업해주시면 됩니다.

- **playsinline 매개변수 생성**

    우선 뷰 안에서 재생 되게 하기 위해서는 playsinline 매개변수를 생성해야 합니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer5.swift %} </p>

    > 값이 0일 경우 전체화면, 1일 경우 뷰 안에서 재생 됩니다.

- **매개변수를 추가하여 영상 Load**

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer6.swift %} </p>

- **실행화면**

    ![YouTubePlayer7.gif](/assets/images/posts/2020-04-09/YouTubePlayer7.gif)

> playsinline 매개변수 외에 다른 매개변수는 아래 링크를 참조해주세요.
> - [유튜브 플레이어 지원 매개변수](https://developers.google.com/youtube/player_parameters?hl=ko#Parameters)

### 플레이어 자동 재생하기

---

화면에 진입 시 유튜브 영상을 자동으로 재생 시켜줘야 할 때가 있습니다. 그래서 load 후에 바로 playVideo 메서드를 이용해서 자동 재생을 시키려고 하지만 자동 재생이 되지 않습니다.

그 이유는 load를 하면 유튜브 영상을 가져오는 시간이 있기 때문에 아직 영상이 준비되지 않은 상태에서 재생을 하려고 했기 때문입니다.

WKYTPlayerViewDelegate를 이용하면 영상이 준비 되었다는 이벤트를 받을 수 있고, 거기서 영상을 재생시켜 주면 자동 재생을 구현할 수 있습니다.

- **playerViewDidBecomeReady 메서드 구현**

    WKYTPlayerViewDelegate를 위임 받아 playerViewDidBecomeReady 메서드를 구현하면 됩니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer7.swift %} </p>

- **playerView에 Delegate 설정**

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer8.swift %} </p>

### (추가) YouTube URL에서 영상 ID 추출하는 방법

---

위에서는 영상 ID를 직접 입력 받아서 개발을 해주었는데요. 만약 API에서 ID가 아닌 유튜브 영상 URL을 준다면 URL에서 ID를 추출해야 되는 경우가 발생합니다. 

그때 영상 ID를 추출하는 Extension을 만들어서 사용하면 간단하게 영상 ID를 추출할 수 있습니다.

- **String Extnesion에 영상 ID 추출 구현**

    정규식을 사용해서 유튜브 URL에서 영상 ID를 추출하는 방법입니다.
    
    유튜브에서 제공하는 영상 URL의 형태가 다양한데 대부분의 URL에서 ID를 추출할 수 있도록 구현되어 있습니다.

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer9.swift %} </p>

- **사용 방법**

    <p> {% gist swieeft/2ef8ad482601953b24762d14b815d084 YouTubePlayer10.swift %} </p>

### 마무리

---

지금까지 유튜브 플레이어를 구현하고 사용하는 방법에 대해 알아보았습니다.

라이브러리가 간단하게 잘 구현 되어 있어서 어렵지 않게 구현할 수 있었는데요. 

요즘은 앱에서 사용되는 영상을 따로 스토리지 서버에 업로드해서 관리하지 않고 유튜브로 업로드하여 관리하고 사용하는 곳이 많아지고 있어 알아두면 많은 곳에서 사용할 수 있을 것 같습니다.

그럼 달콤한 코딩 되세요!

### 참고자료

---

[hmhv/YoutubePlayer-in-WKWebView](https://github.com/hmhv/YoutubePlayer-in-WKWebView)

[Youtube Video Id from URL - Swift3](https://stackoverflow.com/a/50586162)