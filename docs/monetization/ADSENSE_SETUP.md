# 광고 설정 가이드

## Google AdSense 설정

### 1. AdSense 계정 생성 및 사이트 등록
1. https://www.google.com/adsense/ 접속
2. 계정 생성 또는 로그인
3. "사이트 추가" 클릭
4. 블로그 URL 입력: `https://jsong1230.github.io/AIblog`
5. 사이트 승인 대기 (보통 1-2일 소요)

### 2. 광고 단위 생성
1. AdSense 대시보드에서 "광고" 메뉴 클릭
2. "광고 단위" 클릭
3. "표시 광고" 선택
4. 광고 단위 이름 입력 (예: "블로그 메인 광고")
5. 광고 크기 선택 (자동 크기 권장)
6. "광고 단위 만들기" 클릭

### 3. 광고 코드 확인
생성된 광고 단위에서 다음 정보 확인:
- **광고 클라이언트 ID**: `ca-pub-XXXXXXXXXX` 형식
- **광고 슬롯 ID**: 숫자 형식 (예: `1234567890`)

### 4. config.yaml에 입력
```yaml
params:
  adsense:
    enabled: true
    clientId: 'ca-pub-XXXXXXXXXX'  # 여기에 입력
    slotId: '1234567890'            # 여기에 입력
```

## 아마존 어소시에이트 설정

### 1. 계정 생성
1. https://affiliate.amazon.com/ 접속
2. 계정 생성 및 로그인
3. 사이트 정보 입력 및 승인 대기

### 2. 추적 ID 확인
1. 대시보드에서 "도구" > "사이트 스트립" 클릭
2. 추적 ID 확인 (예: `your-tag-20`)

### 3. config.yaml에 입력
```yaml
params:
  affiliate:
    amazon:
      enabled: true
      tag: 'your-tag-20'  # 여기에 입력
```

## 알리익스프레스 파트너 설정

### 1. 계정 생성
1. https://portals.aliexpress.com/ 접속
2. 계정 생성 및 로그인
3. 사이트 정보 입력 및 승인 대기

### 2. 파트너 ID 확인
1. 대시보드에서 파트너 ID 확인

### 3. config.yaml에 입력
```yaml
params:
  affiliate:
    aliexpress:
      enabled: true
      id: 'your-partner-id'  # 여기에 입력
```

## 설정 완료 후

1. config.yaml 파일 수정
2. 변경사항 커밋 및 푸시:
   ```bash
   git add config.yaml
   git commit -m "광고 설정 추가"
   git push
   ```
3. 자동 배포 확인
4. 블로그에서 광고 표시 확인

## 참고사항

- AdSense 승인까지 1-2일 소요될 수 있습니다
- 광고는 승인 후에만 표시됩니다
- 제휴 링크는 즉시 사용 가능합니다
- 광고 수익은 트래픽에 따라 달라집니다

