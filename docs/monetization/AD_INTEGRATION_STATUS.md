# 광고 연동 현황 및 TODO

## 📊 현재 상태 (2025-11-23)

### ✅ 완료된 작업

#### 코드 레벨 구현
- ✅ AdSense partial 템플릿 구현 (`layouts/partials/adsense.html`)
- ✅ Affiliate 링크 partial 템플릿 구현 (`layouts/partials/affiliate.html`)
- ✅ 포스트 페이지에 광고 삽입 로직 구현 (`layouts/_default/single.html`)
- ✅ baseof.html에 AdSense 스크립트 포함
- ✅ config.yaml에 광고 설정 구조 구성
- ✅ 쿠키 동의 배너 구현 (`layouts/partials/cookie-consent.html`)
- ✅ 문서화 완료 (ADSENSE_SETUP.md, AFFILIATE_SETUP.md)

#### 현재 설정 상태
```yaml
# config.yaml
adsense:
  enabled: true
  clientId: 'ca-pub-5954947755126324'  # ✅ 설정됨
  slotId: ''                            # ❌ 비어있음

affiliate:
  amazon:
    enabled: true
    tag: ''                              # ❌ 비어있음
  aliexpress:
    enabled: true
    id: ''                               # ❌ 비어있음
```

#### GitHub Secrets 상태
현재 등록된 secrets:
- ✅ `OPENAI_API_KEY` (github-pages 환경)
- ✅ `POSTS_PER_DAY` (github-pages 환경)
- ✅ `UNSPLASH_ACCESS_KEY` (github-pages 환경)
- ❌ 광고 관련 secrets 없음

### ❌ 미완료 작업

#### 1. AdSense 설정
- [ ] AdSense 계정에서 광고 단위 생성
- [ ] Slot ID 확인 및 config.yaml에 입력
- [ ] AdSense 사이트 승인 확인
- [ ] 광고 표시 테스트

#### 2. Amazon Affiliate 설정
- [ ] Amazon Associates 계정 생성/로그인
- [ ] 사이트 등록 및 승인
- [ ] 추적 태그 확인 및 config.yaml에 입력
- [ ] 제휴 링크 테스트

#### 3. Aliexpress Affiliate 설정
- [ ] Aliexpress Partner 계정 생성/로그인
- [ ] 사이트 등록 및 승인
- [ ] 파트너 ID 확인 및 config.yaml에 입력
- [ ] 제휴 링크 테스트

#### 4. GitHub Secrets 설정 (선택사항)
- [ ] 광고 관련 정보를 secrets로 관리할지 결정
- [ ] 필요시 GitHub Secrets에 추가

#### 5. 광고 배치 최적화
- [ ] 광고 위치 테스트 및 최적화
- [ ] 모바일 반응형 광고 확인
- [ ] 광고 성과 추적 설정

## 🎯 TODO 리스트

### 우선순위 1: AdSense 완전 연동
1. **AdSense 계정 확인**
   - [ ] https://www.google.com/adsense/ 접속
   - [ ] 사이트 승인 상태 확인 (`https://jsong1230.github.io/AIblog`)
   - [ ] 승인되지 않았다면 승인 대기

2. **광고 단위 생성**
   - [ ] AdSense 대시보드 → "광고" → "광고 단위"
   - [ ] "표시 광고" 선택
   - [ ] 광고 단위 이름 입력 (예: "블로그 메인 광고")
   - [ ] 광고 크기 선택 (자동 크기 권장)
   - [ ] 광고 단위 생성

3. **Slot ID 확인 및 설정**
   - [ ] 생성된 광고 단위에서 Slot ID 확인
   - [ ] `config.yaml`의 `adsense.slotId`에 입력
   - [ ] 변경사항 커밋 및 푸시
   - [ ] 배포 후 광고 표시 확인

### 우선순위 2: Amazon Affiliate 연동
1. **계정 설정**
   - [ ] https://affiliate.amazon.com/ 접속
   - [ ] 계정 생성 또는 로그인
   - [ ] 사이트 정보 입력: `https://jsong1230.github.io/AIblog`
   - [ ] 사이트 승인 대기

2. **추적 태그 확인**
   - [ ] 대시보드 → "도구" → "사이트 스트립"
   - [ ] 추적 태그 확인 (예: `your-tag-20`)

3. **설정 적용**
   - [ ] `config.yaml`의 `affiliate.amazon.tag`에 입력
   - [ ] 변경사항 커밋 및 푸시
   - [ ] 제휴 링크 테스트

### 우선순위 3: Aliexpress Affiliate 연동
1. **계정 설정**
   - [ ] https://portals.aliexpress.com/ 접속
   - [ ] 계정 생성 또는 로그인
   - [ ] 사이트 정보 입력 및 승인 대기

2. **파트너 ID 확인**
   - [ ] 대시보드에서 파트너 ID 확인
   - [ ] 또는 제휴 링크 생성 시 URL에서 ID 추출

3. **설정 적용**
   - [ ] `config.yaml`의 `affiliate.aliexpress.id`에 입력
   - [ ] 변경사항 커밋 및 푸시
   - [ ] 제휴 링크 테스트

### 우선순위 4: 광고 최적화
1. **광고 배치 테스트**
   - [ ] 포스트 상단/중간/하단 광고 위치 테스트
   - [ ] 사이드바 광고 추가 검토
   - [ ] 모바일에서 광고 표시 확인

2. **성과 추적**
   - [ ] AdSense 대시보드에서 클릭률 확인
   - [ ] 제휴 링크 클릭 추적
   - [ ] 수익 모니터링

3. **A/B 테스트**
   - [ ] 다양한 광고 크기 테스트
   - [ ] 광고 위치별 성과 비교
   - [ ] 최적 배치 결정

## 📝 설정 가이드

### AdSense Slot ID 설정
```yaml
# config.yaml
params:
  adsense:
    enabled: true
    clientId: 'ca-pub-5954947755126324'  # 이미 설정됨
    slotId: '1234567890'                  # 여기에 Slot ID 입력
```

### Amazon Affiliate 태그 설정
```yaml
# config.yaml
params:
  affiliate:
    amazon:
      enabled: true
      tag: 'your-tag-20'  # 여기에 추적 태그 입력
```

### Aliexpress Affiliate ID 설정
```yaml
# config.yaml
params:
  affiliate:
    aliexpress:
      enabled: true
      id: '12345678'  # 여기에 파트너 ID 입력
```

## 🔐 GitHub Secrets (선택사항)

현재는 `config.yaml`에 직접 설정하는 방식을 사용하고 있습니다.
만약 민감한 정보를 secrets로 관리하고 싶다면:

1. GitHub 저장소 → Settings → Secrets and variables → Actions
2. New repository secret 생성:
   - `ADSENSE_CLIENT_ID`
   - `ADSENSE_SLOT_ID`
   - `AMAZON_AFFILIATE_TAG`
   - `ALIEXPRESS_AFFILIATE_ID`

3. GitHub Actions 워크플로우에서 secrets 사용하도록 수정 필요

## 📚 관련 문서

- [AdSense 설정 가이드](./ADSENSE_SETUP.md)
- [제휴 링크 설정](./AFFILIATE_SETUP.md)
- [Aliexpress 파트너 가이드](./ALIEXPRESS_PARTNER_GUIDE.md)

## ⚠️ 주의사항

1. **AdSense 승인 시간**: 사이트 승인까지 1-2일 소요될 수 있습니다.
2. **광고 표시**: 승인 전에는 광고가 표시되지 않습니다.
3. **트래픽 요구사항**: 일부 제휴 프로그램은 최소 트래픽 요구사항이 있을 수 있습니다.
4. **법적 준수**: 각 광고/제휴 프로그램의 정책을 준수해야 합니다.
