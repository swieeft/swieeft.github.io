---
title: "[Tips] Notion으로 글 작성하고 Github io로 글 옮기기"
layout: post
date: 2020-03-02 17:00
tag:
    - Tips
headerImage: false
image:
description: Notion으로 글 작성하고 Github io로 글 옮기기
category: blog
author: swieeft
externalLink: true
published: true
comments: true
share: true
use_math: false
---
원래 기존에 블로그를 Notion으로 운영하기 위해 작업을 하다가 여러가지 문제점을 발견하여 Github io로 블로그를 이동하게 되었습니다. 

그 과정에서 작성된 게시글들을 옮겨야 되는데 막막하던 차에 Notion export를 활용하여 게시글을 Markdown으로 export해서 옮기게 되었는데 생각보다 호환이 잘 되어 지금도 글 작성은 Notion으로 하고, Markdown export 후에 약간의 수정을 한 후 블로그 업로드를 하고 있습니다.

그래서 Notion에서 글 작성 후 Github io로 업로드 하는 방법을 제가 경험한 내용을 토대로 작성하려고 합니다.

### Notion으로 글 작성하기

---

우선 [**Notion**](https://www.notion.so/)을 아시나요? 요즘 핫한 메모, 업무, 일정관리 등을 통합해서 사용할 수 있는 툴로 많은 회사에서 사용 되는 툴입니다. 

글 작성이 간편하고, 팀 공유 및  URL을 통해 외부 공유도 가능하며, 모바일 앱도 지원해서 요즘 많은 스타트업에서 업무 협업 툴로 많이 채택되고 있는데요. 무료로 이용도 가능하지만 무료로 쓸 수 있는 양이 생각 보다 적어서 만약 사용하신다면 개인 플랜이라도 결제해서 사용하시는걸 권장합니다.

Notion으로 글을 작성하는 방법은 [**노션 가이드**](https://www.notion.so/Notion-1ad7ccbc41a44298814a4820d4acb14e)에 잘 정리 되어 있으니 관심 있으신 분들은 한번 찾아보시면 좋을 것 같습니다.

여기서는 Notion을 어느정도 사용해 보셨다고 생각하고 글 작성 부분은 넘어가도록 하겠습니다.

### 작성 된 글 Export 하기

---

Notion에서 글 작성이 완료 된 후 Export를 하여 MarkDown 문서를 생성해야 됩니다.

- **상단 우측 More(∙∙∙) 메뉴 클릭하기**

    노션 페이지 상단 우측에 ∙∙∙ 아이콘을 클릭하여 메뉴를 연 후 Export를 클릭합니다.

    ![NotionToGithubioPorting1.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting1.png)

- **Export 포맷 설정**

    Export할 포맷을 설정합니다. PDF, HTML 등이 있지만 우리는 Markdown & CSV를 선택합니다.

    Include subpages는 현재 Export할 페이지에 하위 페이지가 있으면 함께 Export할 것인지 체크하는 것으로 만약 하위 페이지까지 내보내야 된다면 On으로 스위치를 변경하시면 됩니다.

    그 후 Export 버튼을 클릭합니다.

    ![NotionToGithubioPorting2.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting2.png)

- **Export할 디렉토리 지정**

    Export할 파일의 이름을 설정할 수 있고, 저장 경로를 설정할 수 있습니다. 설정이 완료 된 후 저장 버튼을 누르면 설정한 경로에 설정한 이름으로 된 .zip 파일이 생성되게 됩니다. 

    ![NotionToGithubioPorting3.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting3.png)

- **.zip 파일 압축 풀기**

    .zip 파일 압축을 풀면 .md 파일과 페이지 내부에 이미지 등의 리소스가 첨부 되었다면 리소스 파일이 Export 된 것을 확인하실 수 있습니다.

    ![NotionToGithubioPorting4.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting4.png)

### Markdown 내용 Github io로 옮기기

---

Export한 Markdown 파일을 바로 Github io에 넣는다고 적용이 되지 않습니다. Github io에서 사용하는 지킬 테마에 따라 설정이 조금씩 다를 수 있지만 제가 사용하고 있는 [**Indigo**](https://koppl.in/indigo/) 테마를 기준으로 설명 하도록 하겠습니다. (Github io를 사용하고 계신다는 전재로 작성하겠습니다. Github io를 처음 시작하시는 분은 [https://devinlife.com/howto/](https://devinlife.com/howto/) 여기를 먼저 보시고 오시면 될 것 같습니다.)

지금부터는 Export된 Markdown을 Github io로 옮길 때 유의할 점에 대해서만 기술합니다. 제가 경험 했던 내용만 우선 작성 되며, 유의할 점을 발견 시에 계속 추가 업데이트할 예정입니다.

- **Markdown 상단 설정 값 수정하기**

    Github io에서 블로그 글을 업로드 할 때 Markdown 안에 필수로 작성 해주어야 하는 설정 값들이 있습니다. 이 부분은 Notion에서 Export시에 같이 나오지 않기 때문에 따로 작성 해주셔야 합니다.

    ```markdown
    ---
    title: "[Tips] Notion으로 글 작성하고 Github io로 글 옮기기"
    layout: post
    date: 2020-03-02 16:35
    tag:
        - Tips
    headerImage: false
    image:
    description: Notion으로 글 작성하고 Github io로 글 옮기기
    category: blog
    author: swieeft
    externalLink: true
    published: true
    comments: true
    share: true
    use_math: false
    ---
    ```

    이렇게 상단에 제목, 작성일시, 태그 등을 입력 해주어야 Jekyll에서 설정 값을 확인하여 정상적으로 글이 게시 될 수 있도록 해줍니다.

- **이미지 경로 수정하기**

    페이지에 이미지를 추가 하였다면 Export된 md파일에는 아래와 같이 경로가 잡혀 있을 것입니다.

    ```markdown
    ![Tips%20Notion%20Github%20io/NotionToGithubioPorting1.png](Tips%20Notion%20Github%20io/NotionToGithubioPorting1.png)
    ```

    이렇게 잡혀 있는 경로를 Github io에서 사용하고 있는 이미지 경로로 변경 해주어야 합니다.

    ```markdown
    ![NotionToGithubioPorting1.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting1.png)
    ```

    저는 assets/images/posts/포스팅 날짜/이미지 형식으로 경로를 설정해서 사용 해주기 때문에 이렇게 작성하였습니다. 만약 경로가 다른 식으로 설정 되어 있다면 경로에 맞게 입력 해주시면 됩니다.

- **소스코드 형식 설정하기**

    Notion의 Code 블록을 추가해서 작성한 후 md 파일을 만들면 md 파일에서는 코드 형식이 설정되지 않은 상태로 Export하게 됩니다. 

    그래서 개발 관련 된 내용을 작성 할 땐 수정 작업이 좀 있는 편이지만 그래도 익숙해지면 금방 수정할 수 있게 됩니다.

    ```markdown
    func test() {
        print("test")
    }
    ```

    이런 형식으로 나온 코드 블럭을

    <pre><code>
    ```swift
    func test() {
        print("test")
    }
    ```
    </code></pre>


    이렇게 수정 해주시면 됩니다.

- **링크 Create Bookmark 체크하기**

    노션에서는 링크를 Create Bookmark하면 블록 형태로 링크에 대한 Bookmark가 생성됩니다. 하지만 md 파일에서는 Bookmark 표현이 안 되므로 링크에 대한 내용 확인 후 수정을 해야 됩니다.

    ![NotionToGithubioPorting5.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting5.png)

    이런 형태로 되어 있는 Bookmark를 Export 하면

    ```markdown
    [Notion - The all-in-one workspace for your notes, tasks, wikis, and databases.](https://www.notion.so/)
    ```

    이런 형태로 표현이 됩니다. 대괄호"[]" 안에 있는 텍스트가 표시 될 URL의 정보이고, 소괄호"()" 안에 있는 URL이 링크 될 페이지 주소입니다.

    페이지에서는 아래와 같이 표현이 됩니다.

    ![NotionToGithubioPorting6.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting6.png)

### 마무리

---

이렇게 하면 Notion에서 Github io로 게시글을 이동할 때 웬만한 내용은 큰 수정 사항 없이 이동할 수 있게 됩니다. 

Markdown 문법이 익숙한 분들이라면 직접 작성하는 것이 훨씬 빠르겠지만 제가 Notion을 사용하는 이유는 시각적인 표현도 있지만 개인적인 백업용으로도 사용하기 위해서 Notion을 활용하고 있습니다.

아직 Notion의 많은 기능을 활용 하지는 않아서 쉽게 이동할 수 있었던 것일 수 있어서 추후에 다른 이슈가 발생하면 해당 내용을 업데이트 하는 식으로 추가하려고 합니다. 이 글은 여기서 Close가 아닌 계속 업데이트 됩니다.

그럼 달콤한 개발 되세요!

### Ps. Markdown 편집하기 좋은 툴 소개

---

지금까지 Markdown 편집을 하려고 Xcode로 삽질을 했는데 Xcode는 Markdown 편집을 하기엔 추천하지 않는 IDE입니다.

제가 추천하는 IDE는 [Visual Studio Code](https://code.visualstudio.com/)입니다. 일단 무료이고, MS사에서 개발한 IDE이기 때문에 업데이트도 잘 해주고, 안정적으로 사용할 수 있습니다.

또한 Markdown 문법에 대해 미리보기를 지원 해줘서 실시간으로 제대로 작성되고 있는지 확인하면서 작성할 수 있다는 것이 큰 매리트입니다.

만약 Markdown 편집 툴로 사용할 것을 찾으신다면 VSCode를 다운 받아서 사용 해보세요.

- **Markdown 실시간 확인하는 방법**

    VSCode의 오른쪽 상단 메뉴 중 빨간색 박스의 메뉴를 클릭 하세요.

    ![NotionToGithubioPorting7.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting7.png)

    그러면 아래와 같이 Markdown 프리뷰 화면이 나타나게 됩니다.

    ![NotionToGithubioPorting8.png](/assets/images/posts/2020-03-02/NotionToGithubioPorting8.png)