> ReactNative 를 통해 서브 프로젝트를 진행해보고자 이렇게 공부를 시작하게 되었으며,
> 해당 내용에 대해 제가 기억하기 위해 적는 내용입니다. <br>
> 해당 내용은 [처음 배우는 리액트 네이티브](https://book.naver.com/bookdb/book_detail.nhn?bid=17896871) 를 읽고 작성한 내용 입니다.
> 

---

## HomeBrew 설치
[Homebrew 설치 사이트](https://brew.sh/index_ko) 에 설치법이 너무 친절하게 잘나와있습니다.

Homebrea 설치하셨다면 다음은 `watchman`을 설치하면됩니다.

그렇다면 첫번째로 `watchman`은 무엇인지 알아보겠습니다.

`watchman`은 페이스북에서 만든 파일 시스템 변경 감지 도구입니다. 파일의 변화를 감지하고 파일의 변화가
조건을 만족시키면 특정 동작을 실행시킵니다.

리액트 네이티브에서의 `watchman`은 소스코드의 변화를 감지하고 자동으로 빌드하여 화면에 업로드하는 역할을 담당합니다.

`watchman`의 설치는 다음과 같이 진행합니다. ( 간단합니다 )

```shell
brew install watchman

# 설치가 다 되었다면 아래 명령어를 통해 정상적으로 설치가 되었는지 확인합니다. 
watchman --version
```

---

## Node.js 설치
Node.js를 설치하는 방법에는 여러가지가 있습니다. 
1. [Node.js 공식 홈페이지](https://nodejs.org/ko/)
2. [NVM git](https://github.com/nvm-sh/nvm)

공식 홈페이지를 통해서 설치하는것은 알겠는데 그렇다면 NVM을 통하여 설치한다는건 무슨말일까..

`nvm`은 여러 버전의 Node.js를 설치하고 버전을 관리할 수 있도록 도와주는 도구로, 다양한 버전의 Node.js를 사용해야 할 때 유용하게
활용할 수 있다. 

해당 README에서는 2번인 nvm을 통한 설치를 설명합니다.

```shell
curl -o- https://raw.githubsercontent.com/nvm-sh/nvm/v.0.35.3/install.sh | bash

# 설치후 설치가 잘 되었는지 버전 확인
nvm --version

# 설치가 정상적으로 되었다면 실제 Node.js 에있는 LTS버전을 설치한다
nvm install --lts

# Node version 확인
node --version
```

---

## 코코아팟 설치

```shell
sudo gem install cocoapods

# 설치 후 버전 확인 
pod --verdion 
```

---

## 시뮬레이터 설정 
[Xcode 실행] -> [Open Developer Tool] -> [Simulator] <br>
[Simulator 실행후 ] -> [File] -> [Open Device] -> [iOS xx] -> [iPhone11]로 설정
iPhone11을 기준으로 진행합니다

---

## JDK 설정
안드로이드 스튜디오에서 설정하기 위해 JDK는 직접 설치해주시길 바랍니다 ..
환경변수 포함입니다. (JAVA_HOME, Path)추가 까지..

---

## Android Studio 설정 

사용하고자 하는 Android SDK 를 설치하시면 됩니다.

설치 후 환경 설정에 다음과 같이 환경변수를 추가합니다.
```shell
vi ~/.zshrc

# Android 추가 환경변수
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools

# 추가 후 
source ~/.zshrc

# adb version확인
adb --version
```