# Vector Similarity Search

### 구현 목표 리스트

- 네이버 뉴스 데이터를 사용하여 벡터 유사도 검색 구현
- Embedding을 진행한 모델의 성능 평가 진행

### 주요 사용 라이브러리 리스트

- faiss
- langchain
- sentence_transformers

### 완료 리스트

- 네이버 뉴스 데이터 전처리
    - Kss
        - 한국어 문장 분리
    - re(정규 표현식)
        - 불필요한 특수기호 및 문자열 삭제
- 벡터 유사도 검색 구현(Faiss)
