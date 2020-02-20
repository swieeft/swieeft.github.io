---
title: "반도체 8대 공정 정리"
layout: post
date: 2019-10-28 19:45
tag:
    - Chemical Engineering
    - Semiconductor
    - Study
    - Note
headerImage: false
image:
description: 191028 `Semiconductor fabrication process` note
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

# 반도체 8대 공정 정리

공부했던거 되새김질 하는 차원에서 정리해서 포스팅해본다. 레퍼런스는 <b>[삼성 반도체 이야기][00]<sup>[^1]</sup></b>에 올라온 내용들을 주로 참고했다.

TOC는 다음과 같다.

- [반도체 8대 공정 정리](#%eb%b0%98%eb%8f%84%ec%b2%b4-8%eb%8c%80-%ea%b3%b5%ec%a0%95-%ec%a0%95%eb%a6%ac)
  - [1. Wafer](#1-wafer)
  - [2. Oxidation](#2-oxidation)
    - [(1) Role](#1-role)
    - [(2) Method](#2-method)
  - [3. Photolithography](#3-photolithography)
    - [(1) IC(Intergrated Circuit) design](#1-icintergrated-circuit-design)
  - [4. Etching](#4-etching)
  - [5. Thin film deposition / Ion implantation](#5-thin-film-deposition--ion-implantation)
    - [(1) Thin film](#1-thin-film)
    - [(2) Deposition](#2-deposition)
    - [(3) Ion Implantation](#3-ion-implantation)
  - [6. Metallization (BEOL)](#6-metallization-beol)
  - [7. EDS (Electrical Die Sorting)](#7-eds-electrical-die-sorting)
    - [1단계 - ET Test & WBI(Electrical Test & Wafer Burn In)](#1%eb%8b%a8%ea%b3%84---et-test--wbielectrical-test--wafer-burn-in)
    - [2단계 - Hot/Cold Test](#2%eb%8b%a8%ea%b3%84---hotcold-test)
    - [3단계 - Repair / Final Test](#3%eb%8b%a8%ea%b3%84---repair--final-test)
    - [4단계 - Inking](#4%eb%8b%a8%ea%b3%84---inking)
  - [8. Packaging](#8-packaging)

----------

## 1. Wafer
- ingot growth
- wafer slicing
- lapping & polishing

![wafer][01]

## 2. Oxidation
### (1) Role
- 절연막을 형성하여 회로와 회로 사이에 누설 전류가 흐르는 것을 차단
- [이온주입공정(ion implantation)]에서 확산 방지막 역할
- [식각공정(Etching)]에서 불량을 방지하는 식각 방지막 역할


### (2) Method
- Thermal oxidation
  - dry oxidation (more dense): O<sub>2</sub>
  - wet oxidation (less dense): O<sub>2</sub>, H<sub>2</sub>O
- Plasma-Enhanced CVD
- Electrochemical cathode oxdation

![oxidation][02]

## 3. Photolithography
### (1) IC(Intergrated Circuit) design
- Transistor
- Resistor
- Diode
- Capacitor
- etc.

![IC design][03]
![Photo01][04]

- Cleaning
- Preparation
- Photoresist application
- Exposure and developing

![Photo02][05]
![Photo03][06]
![Photo04][07]

## 4. Etching
- 액체 또는 기체로 된 식각액(etchant)를 이용해 회로 형성
- 회로패턴 이외에 불필요한 부분 제거
- 균일도(uniformity), 식각 속도 (etch rate), 선택비(selectivity), 형상(profile)이 주요 인자

- Dry etching(plasma etching)
  - reactive gases or ions (selective etching)
  - high cost and technical diffculty
- Wet etching
  - chemical rxn with liquid etchant

![Etching][08]
![Etching][09]

## 5. Thin film deposition / Ion implantation
### (1) Thin film
- 박막(Thin film): 회로간의 구분 , 연결, 보호 역할
  - 금속막(전도)층: 회로들 간 전기적인 신호를 연결
  - 절연막층: 내부 연결층을 전기적으로 분리하거나 오염원으로부터 차단

### (2) Deposition
- 증착(Deposition): 박막을 성장시키는 과정
  - PVD: Physical Vapor Deposition, 물리기상흡착
  - CVD: Chemical Vapor Deposition, 화학기상흡착
    - Themal CVD
    - Plasma-Enhanced CVD
    - Photo-Induced CVD
    - ALD (modified CVD)

![Deposition][10]

### (3) Ion Implantation
- 부도체인 Si wafer에 불순물(ion)을 주입하여 전기적 성질을 조절
- 주입 물질과 주입량에 따라 전기적 성질이 달라짐
  - n-type: P, As
  - p-type: B

## 6. Metallization (BEOL)
- 웨이퍼 위에 형성된 회로가 전기적 신호를 받아 동작하기 위해 필요 (주로 Al, W 사용)
- 증착 공정을 이용하여 배선 형성 (PVD -> CVD)
  - Al (Aluminium)
    - 산화막과의 부착성이 좋고 가공성이 뛰어남
    - 웨이퍼 접합면에서의 확산을 막기 위해서 barrier metal 사용

![Barrier metal][11]
![Metallization][12]

## 7. EDS (Electrical Die Sorting)
- Fab 공정과 packaging 공정 사이에 이뤄짐
- 수율을 높이기 위해 진행되는 공정
    수율: 웨이퍼 한 장에 설계된 최대 칩(Chip) 개수 대비 생산된 양품(Prime Good) 칩의 개수를 백분율로 계산한 것
- 프로브 카드(Probe Card)에 웨이퍼를 접촉시켜 진행
  - 수많은 미세한 핀(Pin)이 웨이퍼와 접촉해 전기를 보내고 그 신호를 통해 불량 칩을 선별
- 전기적 특성검사를 통해 개별 칩들이 원하는 품질 수준에 도달했는지를 확인
  - 웨이퍼 상태 반도체 칩의 양품/불량품 선별
  - 불량 칩 중 수선 가능한 칩의 양품화
  - FAB 공정 또는 설계에서 발견된 문제점의 수정
  - 불량 칩을 미리 선별해 이후 진행되는 패키징공정 및 테스트 작업의 효율 향상

![EDS][13]

### 1단계 - ET Test & WBI(Electrical Test & Wafer Burn In)

- **ET Test(Electrical Test)**
  - 반도체 집적회로(IC) 동작에 필요한 개별소자들(트랜지스터, 저항, 캐패시터, 다이오드)에 대해 전기적 직류전압, 전류특성의 파라미터를 테스트하여 동작 여부를 판별하는 과정

- **WBI 공정(Wafer Burn In)**
  - 웨이퍼에 일정 온도의 열을 가한 다음 AC(교류)/DC(직류) 전압을 가해 제품의 결함 등 잠재적인 불량 요인 추적, 제품의 신뢰성을 효과적으로 향상시키는 공정

### 2단계 - Hot/Cold Test

- **Hot/Cold 공정**
  - 전기적 신호를 통해 웨이퍼 상 각각의 칩 중 불량품이 있는지 판정, 수선 가능한 칩은 수선 공정에서 처리하도록 정보를 저장
  - 특정 온도에서 정상적으로 동작하는지 판별하기 위해 상온보다 높고 낮은 온도의 테스트가 병행

### 3단계 - Repair / Final Test

- **Repair 공정**
  - Hot/Cold 공정에서 수선 가능으로 판정된 칩들을 수선하고, 수선이 끝나면 Final Test 공정을 통해 수선이 제대로 이루어졌는지 재차 검증하여 양/불량을 최종 판단

### 4단계 - Inking
- **Inking 공정**
  - 불량 칩에 특수 잉크를 찍어 육안으로도 불량을 식별할 수 있도록 만드는 공정을 의미
  - Hot/Cold Test공정에서 불량으로 판정된 칩, Final Test공정에서 재검증 결과 불량으로 처리된 칩, 그리고 웨이퍼에서 완성되지 않은 반도체 칩(Dummy Die) 등을 구별
  - 과거의 Inking 공정은 불량 칩에 직접 잉크를 찍었으나 현재는 Data만으로 양/불량을 판별할 수 있도록 처리
  - 조립 작업을 진행하지 않기 때문에 조립 및 검사 공정에서 사용되는 원부자재, 설비, 시간, 인원 등의 손실 절감 효과
  - Inking 공정을 마친 웨이퍼는 건조(Bake)된 후, QC(Quality Control) 검사를 거쳐 조립공정 이동

## 8. Packaging
- 반도체 칩이 외부와 신호를 주고 받을 수 있도록 길을 만들어주고 다양한 외부환경으로부터 안전하게 보호받는 형태로 만드는 과정
- 집적회로와 전자기기를 연결하고 고온, 고습, 화학약품, 진동/충격 등의 외부환경으로부터 회로를 보호하기 위한 공정

1. 웨이퍼 절단 (wafer sawing, dicing)
2. 칩 접착 (die attach)
    - 리드프레임(Lead Frame) 또는 PCB(Printed Circuit Board) 위로 이송
    - 리드프레임은 반도체 칩과 외부 회로 간 전기신호를 전달하고, 외부 환경으로부터 칩을 보호, 지지해주는 골격 역할
3. 금선 연결 (wire bonding)
    - 와이어 방식
    - 플립 칩 방식
      - 볼 형태의 범프로 연결 (Au, solder(Sn/Pb/Ag/etc.))
      - 와이어 본딩보다 전기 저항이 작고 속도가 빠르며, 작은 폼팩터 구현 가능

![Packaging][14]

4. 성형 (molding)
    - 열, 습기 등의 물리적인 환경으로부터 반도체 집적회로를 보호하고, 원하는 형태의 패키지로 만들기 위한 공정

- 패키징 공정 완료 후 최종 불량유무 선별하는 패키지 테스트(Package Test) 시행
- 완제품 형태를 갖춘 후에 진행하기 때문에 ‘파이널 테스트(Final Test)’라고도 함
  - 검사장비(Tester)에 넣고 다양한 조건의 전압이나 전기신호, 온도, 습도 등을 가해 제품의 전기적 특성, 기능적 특성, 동작 속도 등을 측정
  - 테스트 데이터를 분석해 제조공정/조립공정에 피드백함으로써 품질 개선 역할도 수행  

----------
<!-- links -->
[^1]: https://www.samsungsemiconstory.com/category/%EA%B8%B0%EC%88%A0/%EB%B0%98%EB%8F%84%EC%B2%B48%EB%8C%80%EA%B3%B5%EC%A0%95

[00]: https://www.samsungsemiconstory.com/category/%EA%B8%B0%EC%88%A0/%EB%B0%98%EB%8F%84%EC%B2%B48%EB%8C%80%EA%B3%B5%EC%A0%95
[이온주입공정(ion implantation)]: #3-ion-implantation
[식각공정(Etching)]: #4-etching

<!-- images -->
[01]: https://t1.daumcdn.net/cfile/tistory/213B9C4358EB1EF731
[02]: https://t1.daumcdn.net/cfile/tistory/2527D6375934B17B1E
[03]: https://t1.daumcdn.net/cfile/tistory/262B694B596F077B20
[04]: https://t1.daumcdn.net/cfile/tistory/99405B3359C4BFA92B
[05]: https://t1.daumcdn.net/cfile/tistory/990E873359C4C01535
[06]: https://t1.daumcdn.net/cfile/tistory/999FA33359C4C03D0F
[07]: https://t1.daumcdn.net/cfile/tistory/99E8533359C4C05E27
[08]: https://t1.daumcdn.net/cfile/tistory/99787F3F5A4DD7FD29
[09]: https://t1.daumcdn.net/cfile/tistory/994E764A5A4DD7FD28
[10]: https://t1.daumcdn.net/cfile/tistory/996493505A8E484802
[11]: https://t1.daumcdn.net/cfile/tistory/9909153D5AAF40770F
[12]: https://t1.daumcdn.net/cfile/tistory/991341505AAF40770D
[13]: https://t1.daumcdn.net/cfile/tistory/994E4D345AF276EF25
[14]: https://t1.daumcdn.net/cfile/tistory/99EDC64C5BC034B201