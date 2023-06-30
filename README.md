# model


## 가상환경 만들기

```bash
conda create -n "model" python=3.10
```


## requirements 설치

```bash
pip install -r requirements.txt
```

## api_key.txt 다운로드

```bash
카톡이랑 노션에 올려놓은 파일 다운로드 하시면 됩니다!
```

## test.py 실행

```bash
python test.py
```


## model directory 밖에서 함수 호출 (백엔드를 위해)

- 📁 model
  - 📄 test_outside.py

![image](https://github.com/Office-Cheaters/model/assets/83687471/5b0bff5a-c9bf-4c64-887e-a5a37527c948)

Hierarchy를 이렇게 놓고 test_outside.py에 있는 코드처럼 model📁 코드 호출 가능.
