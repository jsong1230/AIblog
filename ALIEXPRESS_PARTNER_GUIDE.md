# 알리익스프레스 파트너 ID 확인 가이드

## ⚠️ 중요: 올바른 사이트 접속

일반 알리익스프레스 쇼핑몰(www.aliexpress.com)이 아닌 **파트너 프로그램 포털**에 접속해야 합니다.

### 올바른 URL
- **파트너 프로그램**: https://portals.aliexpress.com/
- 일반 쇼핑몰: https://www.aliexpress.com/ (❌ 여기가 아닙니다)

## 파트너 ID 확인 방법

### 1단계: 파트너 프로그램 포털 접속
1. https://portals.aliexpress.com/ 접속
2. 계정으로 로그인 (일반 알리익스프레스 계정과 동일)

### 2단계: 대시보드에서 ID 확인
로그인 후 다음 위치에서 ID를 확인할 수 있습니다:

#### 방법 A: Income Report에서 확인 (가장 쉬운 방법)
1. 왼쪽 사이드바 → "Reports" → "Income Report" 클릭
2. 상단 필터에서 "All tracking IDs" 드롭다운 클릭
3. 드롭다운 목록에서 본인의 Tracking ID 확인
   - 보통 숫자로 된 ID (예: `12345678`)
   - 또는 영문+숫자 조합
4. 이 ID가 파트너 ID입니다!

#### 방법 B: Code Center에서 확인
1. 왼쪽 사이드바 → "Code Center" 클릭
2. 링크 생성 시 URL에 포함된 ID 확인
3. 예: `https://s.click.aliexpress.com/e/XXXXXXXX` 에서 `XXXXXXXX` 부분

#### 방법 C: Account 메뉴에서 확인
1. 왼쪽 사이드바 → "Account" 클릭
2. 계정 정보에서 "Tracking ID" 또는 "Affiliate ID" 확인

#### 방법 D: 제휴 링크 생성
1. 왼쪽 사이드바 → "Code Center" 또는 "Ad Center" 클릭
2. 제품 링크 생성
3. 생성된 링크 URL에서 ID 확인:
   ```
   https://s.click.aliexpress.com/e/XXXXXXXX
   ```
   여기서 `XXXXXXXX` 부분이 파트너 ID입니다.

### 3단계: ID 형식 확인
- 숫자만 (예: `12345678`)
- 영문+숫자 (예: `ABC12345`)
- 보통 6-10자리

## 파트너 프로그램 가입이 안 되어 있다면

1. https://portals.aliexpress.com/ 접속
2. "Join Now" 또는 "가입하기" 클릭
3. 사이트 정보 입력:
   - 사이트 URL: `https://jsong1230.github.io/AIblog`
   - 사이트 설명 입력
4. 승인 대기 (보통 1-2일)
5. 승인 후 대시보드에서 ID 확인

## 현재 페이지가 일반 쇼핑몰인 경우

현재 보이는 페이지가 일반 알리익스프레스 쇼핑몰(www.aliexpress.com)의 설정 페이지라면:
1. 새 탭에서 https://portals.aliexpress.com/ 접속
2. 파트너 프로그램 포털에서 로그인
3. 위의 방법으로 ID 확인

## ID를 찾을 수 없는 경우

1. 파트너 프로그램 가입이 완료되었는지 확인
2. 승인 대기 중인지 확인 (승인 후 1-2일 내 활성화)
3. 고객 지원 센터에 문의

## ID 확인 후

파트너 ID를 받으시면 알려주세요. `config.yaml`에 설정해드리겠습니다.

