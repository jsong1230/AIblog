# Analytics 설정 가이드

이 가이드는 블로그에 Google Analytics 또는 Plausible Analytics를 설정하는 방법을 설명합니다.

## 📊 Google Analytics 설정

### 1단계: Google Analytics 계정 생성

1. [Google Analytics](https://analytics.google.com/)에 접속합니다.
2. Google 계정으로 로그인합니다.
3. **측정 시작** 버튼을 클릭합니다.

### 2단계: 속성(Property) 생성

1. **계정 이름** 입력 (예: "AI 블로그")
2. **속성 이름** 입력 (예: "AI Automated Blog")
3. **보고 시간대** 선택 (한국: UTC+9)
4. **통화** 선택 (KRW)
5. **고급 옵션**에서 **Google Analytics 4(GA4) 속성 만들기** 활성화
6. **비즈니스 정보** 입력 (선택사항)
7. **만들기** 클릭

### 3단계: 데이터 스트림 설정

1. **웹** 플랫폼 선택
2. **웹사이트 URL** 입력:
   ```
   https://jsong1230.github.io/AIblog
   ```
3. **스트림 이름** 입력 (예: "AI Blog Main")
4. **스트림 만들기** 클릭

### 4단계: Measurement ID 확인

1. 생성된 스트림의 **측정 ID**를 복사합니다.
   - 형식: `G-XXXXXXXXXX` (G-로 시작하는 11자리 코드)
   - 예시: `G-ABC123XYZ45`

### 5단계: config.yaml 설정

`config.yaml` 파일을 열고 다음 설정을 수정합니다:

```yaml
params:
  # Analytics
  analytics:
    enabled: true                    # Analytics 활성화
    provider: 'google'              # 'google' 또는 'plausible'
    googleId: 'G-XXXXXXXXXX'       # 위에서 복사한 Measurement ID
    plausibleDomain: ''             # Plausible 사용 시에만 필요
```

**예시:**
```yaml
params:
  analytics:
    enabled: true
    provider: 'google'
    googleId: 'G-ABC123XYZ45'
    plausibleDomain: ''
```

### 6단계: 확인

1. 변경사항을 커밋하고 푸시합니다:
   ```bash
   git add config.yaml
   git commit -m "Enable Google Analytics"
   git push origin main
   ```

2. GitHub Actions가 자동으로 배포합니다 (약 1-2분 소요)

3. 배포 완료 후 블로그에 접속합니다:
   ```
   https://jsong1230.github.io/AIblog
   ```

4. Google Analytics 대시보드에서 확인:
   - [Google Analytics](https://analytics.google.com/) 접속
   - **보고서** > **실시간** 메뉴로 이동
   - 자신의 블로그에 접속하면 실시간 방문자가 표시됩니다

---

## 🔒 Plausible Analytics 설정 (대안)

Google Analytics 대신 프라이버시 중심의 Plausible Analytics를 사용할 수도 있습니다.

### 1단계: Plausible 계정 생성

1. [Plausible Analytics](https://plausible.io/)에 접속합니다.
2. 계정을 생성하고 구독합니다 (무료 체험 가능).

### 2단계: 사이트 추가

1. Plausible 대시보드에서 **Add a website** 클릭
2. **Domain name** 입력:
   ```
   jsong1230.github.io
   ```
3. **Add domain** 클릭

### 3단계: config.yaml 설정

```yaml
params:
  analytics:
    enabled: true
    provider: 'plausible'
    googleId: ''
    plausibleDomain: 'jsong1230.github.io'  # Plausible에 등록한 도메인
```

### 4단계: 확인

위의 Google Analytics 확인 단계와 동일합니다.

---

## 🛠️ 문제 해결

### Analytics가 작동하지 않는 경우

1. **Measurement ID 확인**
   - `config.yaml`의 `googleId`가 올바른 형식인지 확인 (`G-`로 시작)
   - 공백이나 따옴표가 없는지 확인

2. **브라우저 캐시 확인**
   - 브라우저 캐시를 지우고 강력 새로고침 (Ctrl+Shift+R 또는 Cmd+Shift+R)

3. **배포 확인**
   - GitHub Actions가 성공적으로 완료되었는지 확인
   - 배포된 사이트의 HTML 소스에서 analytics 스크립트가 포함되어 있는지 확인

4. **Google Analytics 실시간 보고서 확인**
   - Analytics 대시보드에서 **보고서** > **실시간** 확인
   - 데이터가 표시되기까지 몇 분 정도 걸릴 수 있습니다

### 개발 환경에서 테스트

로컬 Hugo 서버에서 테스트하려면:

```bash
hugo server
```

그리고 브라우저에서 `http://localhost:1313`에 접속합니다.

**참고:** 로컬 개발 환경에서는 Analytics가 제대로 작동하지 않을 수 있습니다. 프로덕션 환경(배포된 사이트)에서 테스트하는 것이 좋습니다.

---

## 📝 추가 참고사항

### Google Analytics 4 (GA4) 특징

- **실시간 데이터**: 즉시 방문자 추적 가능
- **이벤트 기반**: 페이지뷰, 클릭 등 다양한 이벤트 추적
- **무료**: 개인 블로그는 무료로 사용 가능
- **프라이버시**: GDPR 준수 옵션 제공

### Plausible Analytics 특징

- **프라이버시 중심**: 쿠키 없이 작동, GDPR 준수
- **경량**: 작은 스크립트 크기로 빠른 로딩
- **간단한 UI**: 복잡한 설정 없이 사용 가능
- **유료**: 월 $9부터 시작 (무료 체험 가능)

---

## ✅ 설정 확인 체크리스트

- [ ] Google Analytics 계정 생성 완료
- [ ] 속성(Property) 및 데이터 스트림 생성 완료
- [ ] Measurement ID 복사 완료
- [ ] `config.yaml`에서 `analytics.enabled: true` 설정
- [ ] `config.yaml`에서 `googleId` 입력 완료
- [ ] 변경사항 커밋 및 푸시 완료
- [ ] GitHub Actions 배포 완료 확인
- [ ] Google Analytics 실시간 보고서에서 데이터 확인

설정이 완료되면 블로그 방문자 통계를 추적할 수 있습니다! 🎉
