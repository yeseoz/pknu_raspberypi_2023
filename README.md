# pknu_raspberypi_2023
라즈베리파이 학습 리포지토리

## 1/2일차 
- 라즈베리파이 학습
	- 라즈베리파이 소개
	- 라즈비안 설치
        - Bullseye
    - 라즈비안 설정
        - 기본 업데이트/업그레이드
        - 한글 폰트 및 입력기
        - 스크린 세이버, 와이파이 연결 끊김 해제
    - pi-apps 설치
        - Visual Studio Code 설치
        - Github Desktop 설치 및 설정
    - Visual Studio Code
        - Python 플러그인 설치
    - 리눅스 기본 
        - 리눅스 명령어(대표20여가지)


## 3일차
- 라즈베리파이 학습
    -  통신 설정
        - AnyDesk 실패
    - 리눅스 일반
        - 서비스 실횅, 확인, 종료
            - systemctl [start|stop|status]서비스명
        - MySQL DB
    - Flask 기본


## 4일차 
- 라즈베리파이 학습
    -  PyQt5 설치
    - QtDesigner 설치 및 실행 확인
        -  하드웨어 제어 - GPIO
            - LED / RGB LED 출력


## 5일차
- 라즈베리파이 학습
    - 네트워크 셋팅(VNC)
    - RGB LED / Button 클릭
    -  온습도 센서
    -  서보모터


## 6일차
- 라즈베리파이 학습
    - MQTT 통신 
    - MQTT Broker IP, port 설정, 계정 설정(옵션)
    - RPI <-- >WPF
    - RPI 온습도 센서값 MQTT전송
    - WPF 모터, LED 제어값 전송
    - RPI Python paho-mqtt 패키지
    - WPF C# M2Mqtt 패키지

WPF 모니터링, 컨트롤화면

라즈베리파이 테스트 결과

<img src="https://raw.githubusercontent.com/yeseoz/pknu_raspberypi_2023/main/image/Mqtt_Monitoring.gif" width="700">


## 7일차
- 라즈베리파이 학습
    - pi 카메라 설치 sudo raspi-config Interface- => Legacy Camera
    - libcamera-hello
    - libcamera-jpeg -o test.jpg
    - Opencv 설치 sudo pip install opencv-python


## 8일차 
- 소켓 프로그래밍
     - putty 설치
     - 라즈베리파이 putty 연동

## 9일차 
- 소켓 프로그래밍
	- IP주소/PORT번호의 개념
	- 리틀엔디안 / 빅엔디안
	- 클라이언트와 서버만들어 통신

## 10일차
- 

## 11일차
- 소켓 프로그래밍
    - fork
    - mutex
    - pipe


## 12일차
- 소켓프로그래밍
    - 채팅 서버 구현
    - 채팅 클라이언트 구현
    - 코딩테스트 => 리눅스에서 웹서버 구현

## 13일차
- 라즈베리파이
    - 파이썬 가상화면 설치 -> python -m venv (env) 가상환경이름
    - 가상환경 실행 -> source ./bin/actibate
    - 버튼 눌러 카운트 세기
    - 7새그먼트 0~F까지 출력시키기

## 14일차
- 라즈베리 파이
    - 부저 울리기 => buzz = GPIO.PWM(buzzerPin, 440) # 440HZ를 갖는 객체 생성
    - 인터럽트 통해서 버튼 누르면 불켜지고 버튼 누르면 꺼지게 하기
    - 추가해서 버튼 누르면 불도켜지고 소리도 울리게하기


## 15일차
- 라즈베리 파이 
    - 초음파 센서 hc sr-04
    - 플라스크 웹페이지 만들기

## 16일차
- 라즈베리파이
    - 웹페이지 버튼만들어서 LED켜고끄기
    - 팀프로젝트 활동

## 17일차
- 라즈베리파이
    - pyqt5 설치 sudo apt-get install python3-pyqt5
    - pyqt5 디자이너 설치 sudo apt-get install qttools5-dev-tools
