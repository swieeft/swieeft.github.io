---
layout: post
title: "Development로 Archive하여<br>테스트 버전 배포하기"
subtitle: "[iOS]"
date: 2020-02-20 18:20
background: 
tags: [ios, xcode]
---

애플에서 권장하는 테스트 버전 배포는 TestFlight입니다. 하지만 테스트를 진행하다 보면 자주 수정하여 재배포를 해야 되는 경우가 있는데 TestFlight에 업로드하여 배포할 경우 평균 30분 정도의 TestFlight 반영 시간이 필요합니다.

그렇다보니 매번 TestFlight 배포를 통한 테스트는 개발자에게 시간적 스트레스를 주고 있습니다. 그렇다고 매번 테스트 기기들을 빌드 해서 줄 수도 없고 말이죠. 그때 사용을 해 볼만한 것이 Development 배포입니다.

Development 배포는 한번의 Archive를 통해 ipa 파일을 생성하여 정적 스토리지(ex. AWS S3)에 업로드 해 등록된 사용자 기기에 바로 설치가 가능하도록 다운로드 페이지를 제공해주는 방식입니다.

예전에는 테스트 대상 기기들의 UDID를 일일히 받아서 등록을 해주어야 하는 불편함이 있었지만, 지금은 한번 Xcode로 연결하여 등록만 하면 바로 기기등록이 되어 좀 더 편리해졌습니다. ~~어차피 한번은 연결은 해야되지만...~~

### ipa 파일 Development로 추출하기

---

1. Xcode에서 Archive를 완료한 후 Organizer 화면에서 앱 배포로 들어가서 Development 항목을 선택 후 Next를 누릅니다.

    ![export-1.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-1.png)

2. 여기서는 특별한 옵션 설정을 할 필요가 없으면 Next를 눌러 넘어가면 됩니다.

    ![export-2.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-2.png)


3. Signing 방식을 선택합니다. 이 부분은 TestFlight로 업로드 할 때와 동일하게 선택 해주면 됩니다. Signing 방식을 선택한 후 Next를 누릅니다.

    ![export-3.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-3.png)

4. 앱에 대한 라이브러리 정보 및 개발자 정보 등을 표시해주는 화면입니다. 그냥 바로 Export를 눌러줍니다.

    ![export-4.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-4.png)

5. Export 시 생성할 폴더 이름을 설정하고,  디렉토리를 선택합니다. 그리고 Export를 누르면 최종적으로 ipa 파일을 생성하게 됩니다.

    ![export-5.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-5.png)

6. Export가 완료 되면 선택했던 디렉토리로 가보면 설정한 이름으로 된 폴더가 하나 생성되어 있습니다.

    ![export-6.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-6.png)

7. 생성된 폴더로 들어가면 여러 파일이 있는데 그 중에 .ipa 파일이라고 되어 있는 파일을 정적 스토리지 서버에 업로드 시키면 됩니다.

    ![export-7.png](/assets/images/posts/2020-02-20/DevelopmentArchive/export-7.png)

### ipa 다운로드 정보를 가진 .plist 파일 만들기

---

ipa의 링크 및 프로젝트 정보를 담고 있는 .plist 파일을 먼저 생성해줍니다.

ipa 업로드 경로와 Bundle Id 값을 정확히 입력해야 다운로드가 가능합니다.

<p> {% gist swieeft/9c8490452a825a53925dd292a42d048b DevelopmentArchive1.xml %} </p>

> Xcode로 작업하실 경우엔 XML이 아닌 기본 Property List 형태로 작업 가능합니다.

### 테스트 앱 다운로드 정적 페이지 만들기

---

ipa와 plist를 스토리지에 올렸다면 이제 다운로드 받을 페이지를 만들어야 합니다. 다운로드 페이지는 정적페이지로 단순 html로만 생성해서 올려둡니다. (디자인은 각자 취향에 맡깁니다...)

정적페이지에서 가장 중요한 부분은  URL 파라메터의 "url" 부분에 들어가는 값입니다. 이 부분의 url은 ipa 파일 url이 아닌 plist url이 들어가야 합니다.

<p> {% gist swieeft/9c8490452a825a53925dd292a42d048b DevelopmentArchive2.html %} </p>

### 테스트 앱 설치 하기

---

위의 모든 작업이 완료 되면 정적 페이지 링크를 테스터들에게 전달하고, 링크를 받은 테스터들은 자신의 아이폰에서 링크를 열어 테스트 앱을 설치할 수 있습니다.

1. 링크를 열어 "Install" 버튼을 클릭합니다.

    ![install-1.png](/assets/images/posts/2020-02-20/DevelopmentArchive/install-1.png)

2. 설치 안내에 대한 Alert창이 실행되고, 설치를 누르면 테스트 앱 설치가 시작됩니다.

    ![install-2.png](/assets/images/posts/2020-02-20/DevelopmentArchive/install-2.png)

3. 앱 설치가 시작되면 홈 화면에 앱이 설치가 되고 완료 된 후에 앱을 실행하여 테스트를 진행할 수 있습니다.

    ![install-3.png](/assets/images/posts/2020-02-20/DevelopmentArchive/install-3.png)

### 마무리

---

Development로 테스트 배포하는 방법을 알아보았습니다. 생각보다 간단하게 작업하여 테스트 배포를 할 수 있어 저는 자주 이용하고 있는 방법입니다. 

TestFlight가 통계나 자동 업데이트 등의 편리한 것이 있지만 배포까지 시간이 많이 걸린다는 단점이 있어서 빠르게 테스트를 진행해야 되는 프로젝트라면 한번 사용을 고려 해보는 것도 좋을 것 같습니다.

참고로 정적 스토리지 서버가 있어야 가능한데, 회사에서 AWS를 사용한다면 S3에 업로드하여 사용이 가능한지 AWS 담당자 분과 논의해서 작업을 진행하시면 됩니다.

### 참고자료

---

이 코드는 제가 예전에 다니던 회사 사수분께서 주신 코드로 사용에 대한 허가를 받고 올립니다.
