## 세팅
`pip install virtualenv`
`python -m virtualenv venv`
`.\venv\Scripts\activate` (windows)

## 설치
`pip install crewai crewai-tools`

## 의존성 파일 생성
`.\venv\Scripts\pip freeze`

## 의존성 최적화
`.\venv\Scripts\pip install pipreqs`
`.\venv\Scripts\pipreqs . --force`

## 실행
`.\venv\Scripts\python crew_ai.py`