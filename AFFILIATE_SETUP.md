# 제휴 링크 설정 가이드

## 아마존 어소시에이트 (Amazon Associates)

### 주의사항
- 아마존 어소시에이트는 한국에서 직접 지원하지 않을 수 있습니다
- 미국 아마존 어소시에이트는 한국 사이트에 제한이 있을 수 있습니다

### 올바른 URL
- 미국: https://affiliate-program.amazon.com/
- 또는: https://affiliate.amazon.com/

### 가입 방법
1. 위 URL로 접속
2. 계정 생성 또는 로그인
3. 사이트 정보 입력:
   - 사이트 URL: `https://jsong1230.github.io/AIblog`
   - 사이트 승인 대기
4. 추적 ID 확인:
   - 대시보드 → "도구" → "사이트 스트립"
   - 추적 ID 확인 (예: `your-tag-20`)

## 쿠팡 파트너스 (한국 추천)

한국 블로그에는 쿠팡 파트너스가 더 적합할 수 있습니다.

### 가입 방법
1. https://partners.coupang.com/ 접속
2. 계정 생성 및 로그인
3. 사이트 정보 입력 및 승인
4. 파트너 ID 확인

### config.yaml에 추가 (쿠팡)
```yaml
params:
  affiliate:
    coupang:
      enabled: true
      id: 'your-coupang-id'
```

## 알리익스프레스 파트너

### 가입 방법
1. https://portals.aliexpress.com/ 접속
2. 계정 생성 및 로그인
3. 사이트 정보 입력 및 승인 대기

### 파트너 ID 확인 방법

#### 방법 1: 대시보드에서 확인
1. 로그인 후 대시보드 접속
2. 상단 메뉴에서 "My Account" 또는 "계정" 클릭
3. "Account Settings" 또는 "계정 설정" 클릭
4. "Affiliate ID", "Partner ID", "Tracking ID" 등의 필드에서 ID 확인
   - 보통 숫자로 된 ID (예: `12345678`)

#### 방법 2: 제휴 링크에서 확인
1. 대시보드에서 "Get Links" 또는 "링크 생성" 클릭
2. 제품 링크 생성 시 URL에 포함된 ID 확인
3. 예: `https://s.click.aliexpress.com/e/XXXXXXXX` 에서 `XXXXXXXX` 부분이 파트너 ID

#### 방법 3: 프로필 페이지에서 확인
1. 대시보드 → "Profile" 또는 "프로필"
2. "Affiliate Information" 섹션에서 ID 확인

#### 일반적인 ID 형식
- 숫자로 된 ID (예: `12345678`)
- 또는 영문+숫자 조합

### config.yaml에 입력
```yaml
params:
  affiliate:
    aliexpress:
      enabled: true
      id: '12345678'  # 여기에 파트너 ID 입력
```

### 참고
- 파트너 ID를 찾을 수 없다면 고객 지원 센터에 문의하세요
- ID는 보통 가입 승인 후 1-2일 내에 활성화됩니다

## 현재 설정

제휴 링크는 포스트 하단에 자동으로 표시됩니다.

