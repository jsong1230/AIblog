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

#### 방법 A: Income Report에서 확인
1. 왼쪽 사이드바 → "Reports" → "Income Report" 클릭
2. 상단 필터에서 "All tracking IDs" 드롭다운 클릭
3. 드롭다운 목록에서 본인의 Tracking ID 확인
   - ⚠️ "default"만 보이면: Tracking ID가 아직 생성되지 않았거나 승인 대기 중일 수 있습니다
   - 이 경우 아래 방법 B나 C를 시도하세요

#### 방법 B: Code Center에서 확인 (추천 - "default"만 보일 때)
1. 왼쪽 사이드바 → "Code Center" 클릭
2. "Get Links" 또는 "링크 생성" 버튼 클릭
3. 제품 URL 입력 또는 제품 검색
4. 링크 생성 시 URL 확인:
   ```
   https://s.click.aliexpress.com/e/XXXXXXXX
   ```
   여기서 `XXXXXXXX` 부분이 파트너 ID입니다
   - 또는 링크 생성 페이지에서 Tracking ID가 표시될 수 있습니다

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

## "default"만 보이는 경우

"All tracking IDs" 드롭다운에서 "default"만 보이면:

1. **Code Center에서 링크 생성 시도**
   - 왼쪽 사이드바 → "Code Center" 클릭
   - 제품 링크를 생성해보세요
   - 생성된 링크 URL에 Tracking ID가 포함되어 있습니다

2. **파트너 프로그램 승인 상태 확인**
   - Account 메뉴에서 승인 상태 확인
   - 승인 대기 중이면 1-2일 후 다시 확인

3. **첫 링크 생성 시 자동 생성**
   - Code Center에서 첫 링크를 생성하면 Tracking ID가 자동으로 생성됩니다
   - 생성된 링크의 URL에서 ID를 확인할 수 있습니다

## ID를 찾을 수 없는 경우

1. 파트너 프로그램 가입이 완료되었는지 확인
2. 승인 대기 중인지 확인 (승인 후 1-2일 내 활성화)
3. Code Center에서 링크를 한 번 생성해보세요 (ID가 자동 생성될 수 있음)
4. 고객 지원 센터에 문의

## ID 확인 후

파트너 ID를 받으시면 알려주세요. `config.yaml`에 설정해드리겠습니다.

