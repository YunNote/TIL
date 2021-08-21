## ReactNatice CLI

> 이제 React Native 사전설치는 다 하였으니 실제로 프로젝트를 생성하고
> 실행해보려고 한다.
> 
> Expo를 이용할 수 있으나 저는 CLI 를 활용하겠습니다.
> 

---

### 프로젝트 생성 

```shell
npx react-native init {ProjectName}
```


### 프로젝트 생성시 트러블 슈팅 
> ✔ Downloading template <br>
> ✔ Copying template <br>
> ✔ Processing template <br>
> ✖ Installing CocoaPods dependencies (this may take a few minutes) <br>
> ✖ Installing CocoaPods dependencies (this may take a few minutes) <br>
> error Error: Failed to install CocoaPods dependencies for iOS project, which is required by this template.<br>
> Please try again manually: "cd ./{ProjectName}/ios && pod install".

init Project를 하였더니 잘설치되다가 다음과 같은 이슈가 발생하였다 .. 

> 일단 하라는대로 "cd ./{ProjectName}/ios && pod install" 를 실행해 보았지만 제대로 해결되지 않았다.
> <br>
> 알고보니 XCode에 Commandline Tools가 제대로 세팅되지 않았다.. <br>
> XCode -> Preference > Location 에 들어가서 Commandline Tools를 설정해주고 다시 pod install을 하면 해결된다 . 
> 


설치를 다 한 후 run을 하여 실제로 제대로 동작하는지 확인해보겠습니다.
```shell
cd {ProjectName}
npm run ios
npm run android
```
위와 같이 실행하면 앱이 제대로 동작 하는것을 확인할 수 있었다.