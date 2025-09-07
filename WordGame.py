# 영어 단어 퀴즈 게임 - 단어 데이터 예시

# 리스트 기반으로 완전히 최적화됨
# 방법 2: 리스트 안에 딕셔너리 형태 (더 유연함) - 과학과 기술 용어
word_list = [
    # 과학 용어
    {"english": "algorithm", "korean": "알고리즘"},
    {"english": "hypothesis", "korean": "가설"},
    {"english": "molecule", "korean": "분자"},
    {"english": "photosynthesis", "korean": "광합성"},
    {"english": "quantum", "korean": "양자"},
    {"english": "relativity", "korean": "상대성"},
    {"english": "thermodynamics", "korean": "열역학"},
    {"english": "evolution", "korean": "진화"},
    {"english": "genetics", "korean": "유전학"},
    {"english": "ecosystem", "korean": "생태계"},
    {"english": "chromosome", "korean": "염색체"},
    {"english": "protein", "korean": "단백질"},
    {"english": "enzyme", "korean": "효소"},
    {"english": "mitosis", "korean": "유사분열"},
    {"english": "meiosis", "korean": "감수분열"},
    {"english": "photosynthesis", "korean": "광합성"},
    {"english": "respiration", "korean": "호흡"},
    {"english": "osmosis", "korean": "삼투"},
    {"english": "diffusion", "korean": "확산"},
    {"english": "gravity", "korean": "중력"},
    {"english": "velocity", "korean": "속도"},
    {"english": "acceleration", "korean": "가속도"},
    {"english": "momentum", "korean": "운동량"},
    {"english": "energy", "korean": "에너지"},
    {"english": "power", "korean": "힘"},
    {"english": "frequency", "korean": "진동수"},
    {"english": "wavelength", "korean": "파장"},
    {"english": "amplitude", "korean": "진폭"},
    {"english": "resistance", "korean": "저항"},
    {"english": "voltage", "korean": "전압"},
    {"english": "current", "korean": "전류"},
    {"english": "capacitance", "korean": "커패시턴스"},
    {"english": "inductance", "korean": "인덕턴스"},
    {"english": "magnetism", "korean": "자기"},
    {"english": "radiation", "korean": "방사선"},
    {"english": "isotope", "korean": "동위원소"},
    {"english": "catalyst", "korean": "촉매"},
    {"english": "polymer", "korean": "고분자"},
    {"english": "crystal", "korean": "결정"},
    {"english": "alloy", "korean": "합금"},
    {"english": "semiconductor", "korean": "반도체"},
    {"english": "laser", "korean": "레이저"},
    {"english": "plasma", "korean": "플라즈마"},
    {"english": "fusion", "korean": "핵융합"},
    {"english": "fission", "korean": "핵분열"},
    {"english": "neutron", "korean": "중성자"},
    {"english": "proton", "korean": "양성자"},
    {"english": "electron", "korean": "전자"},
    {"english": "quark", "korean": "쿼크"},
    {"english": "boson", "korean": "보존"},
    {"english": "fermion", "korean": "페르미온"},

    # 기술 용어
    {"english": "database", "korean": "데이터베이스"},
    {"english": "encryption", "korean": "암호화"},
    {"english": "bandwidth", "korean": "대역폭"},
    {"english": "cache", "korean": "캐시"},
    {"english": "compiler", "korean": "컴파일러"},
    {"english": "debugging", "korean": "디버깅"},
    {"english": "ethernet", "korean": "이더넷"},
    {"english": "firewall", "korean": "방화벽"},
    {"english": "gigabyte", "korean": "기가바이트"},
    {"english": "hardware", "korean": "하드웨어"},
    {"english": "software", "korean": "소프트웨어"},
    {"english": "interface", "korean": "인터페이스"},
    {"english": "kernel", "korean": "커널"},
    {"english": "middleware", "korean": "미들웨어"},
    {"english": "protocol", "korean": "프로토콜"},
    {"english": "router", "korean": "라우터"},
    {"english": "server", "korean": "서버"},
    {"english": "terminal", "korean": "터미널"},
    {"english": "virtualization", "korean": "가상화"},
    {"english": "wireless", "korean": "무선"},
    {"english": "algorithm", "korean": "알고리즘"},
    {"english": "binary", "korean": "이진법"},
    {"english": "boolean", "korean": "불리언"},
    {"english": "byte", "korean": "바이트"},
    {"english": "cloud", "korean": "클라우드"},
    {"english": "compression", "korean": "압축"},
    {"english": "cybersecurity", "korean": "사이버보안"},
    {"english": "data", "korean": "데이터"},
    {"english": "encryption", "korean": "암호화"},
    {"english": "framework", "korean": "프레임워크"},
    {"english": "gateway", "korean": "게이트웨이"},
    {"english": "hash", "korean": "해시"},
    {"english": "internet", "korean": "인터넷"},
    {"english": "javascript", "korean": "자바스크립트"},
    {"english": "keyboard", "korean": "키보드"},
    {"english": "logic", "korean": "논리"},
    {"english": "memory", "korean": "메모리"},
    {"english": "network", "korean": "네트워크"},
    {"english": "object", "korean": "객체"},
    {"english": "pixel", "korean": "픽셀"},
    {"english": "query", "korean": "쿼리"},
    {"english": "robotics", "korean": "로보틱스"},
    {"english": "sensor", "korean": "센서"},
    {"english": "smartphone", "korean": "스마트폰"},
    {"english": "tablet", "korean": "태블릿"},
    {"english": "usb", "korean": "USB"},
    {"english": "virtual", "korean": "가상"},
    {"english": "web", "korean": "웹"},
    {"english": "xml", "korean": "XML"},
    {"english": "yaml", "korean": "YAML"},
    {"english": "zip", "korean": "압축"},
    {"english": "analytics", "korean": "분석"},
    {"english": "automation", "korean": "자동화"},
    {"english": "backup", "korean": "백업"},
    {"english": "blockchain", "korean": "블록체인"},
    {"english": "browser", "korean": "브라우저"},
    {"english": "chip", "korean": "칩"},
    {"english": "circuit", "korean": "회로"},
    {"english": "code", "korean": "코드"},
    {"english": "computing", "korean": "컴퓨팅"},
    {"english": "connectivity", "korean": "연결성"},
    {"english": "cpu", "korean": "CPU"},
    {"english": "dashboard", "korean": "대시보드"},
    {"english": "device", "korean": "장치"},
    {"english": "digital", "korean": "디지털"},
    {"english": "domain", "korean": "도메인"},
    {"english": "download", "korean": "다운로드"},
    {"english": "driver", "korean": "드라이버"},
    {"english": "email", "korean": "이메일"},
    {"english": "file", "korean": "파일"},
    {"english": "folder", "korean": "폴더"},
    {"english": "format", "korean": "형식"},
    {"english": "function", "korean": "함수"},
    {"english": "graphics", "korean": "그래픽스"},
    {"english": "hosting", "korean": "호스팅"},
    {"english": "hyperlink", "korean": "하이퍼링크"},
    {"english": "icon", "korean": "아이콘"},
    {"english": "input", "korean": "입력"},
    {"english": "installation", "korean": "설치"},
    {"english": "integration", "korean": "통합"},
    {"english": "keyboard", "korean": "키보드"},
    {"english": "laptop", "korean": "랩톱"},
    {"english": "link", "korean": "링크"},
    {"english": "login", "korean": "로그인"},
    {"english": "malware", "korean": "악성코드"},
    {"english": "media", "korean": "미디어"},
    {"english": "mobile", "korean": "모바일"},
    {"english": "modem", "korean": "모뎀"},
    {"english": "monitor", "korean": "모니터"},
    {"english": "motherboard", "korean": "메인보드"},
    {"english": "mouse", "korean": "마우스"},
    {"english": "multimedia", "korean": "멀티미디어"},
    {"english": "operating", "korean": "운영"},
    {"english": "output", "korean": "출력"},
    {"english": "password", "korean": "비밀번호"},
    {"english": "peripheral", "korean": "주변장치"},
    {"english": "platform", "korean": "플랫폼"},
    {"english": "plug", "korean": "플러그"},
    {"english": "port", "korean": "포트"},
    {"english": "printer", "korean": "프린터"},
    {"english": "processor", "korean": "프로세서"},
    {"english": "program", "korean": "프로그램"},
    {"english": "programming", "korean": "프로그래밍"},
    {"english": "ram", "korean": "RAM"},
    {"english": "resolution", "korean": "해상도"},
    {"english": "router", "korean": "라우터"},
    {"english": "satellite", "korean": "위성"},
    {"english": "scanner", "korean": "스캐너"},
    {"english": "script", "korean": "스크립트"},
    {"english": "security", "korean": "보안"},
    {"english": "session", "korean": "세션"},
    {"english": "signal", "korean": "신호"},
    {"english": "smart", "korean": "스마트"},
    {"english": "social", "korean": "소셜"},
    {"english": "software", "korean": "소프트웨어"},
    {"english": "speaker", "korean": "스피커"},
    {"english": "speed", "korean": "속도"},
    {"english": "storage", "korean": "저장장치"},
    {"english": "streaming", "korean": "스트리밍"},
    {"english": "support", "korean": "지원"},
    {"english": "switch", "korean": "스위치"},
    {"english": "synchronization", "korean": "동기화"},
    {"english": "system", "korean": "시스템"},
    {"english": "tablet", "korean": "태블릿"},
    {"english": "template", "korean": "템플릿"},
    {"english": "touchscreen", "korean": "터치스크린"},
    {"english": "transfer", "korean": "전송"},
    {"english": "update", "korean": "업데이트"},
    {"english": "upload", "korean": "업로드"},
    {"english": "usb", "korean": "USB"},
    {"english": "user", "korean": "사용자"},
    {"english": "utility", "korean": "유틸리티"},
    {"english": "video", "korean": "비디오"},
    {"english": "virus", "korean": "바이러스"},
    {"english": "webcam", "korean": "웹캠"},
    {"english": "website", "korean": "웹사이트"},
    {"english": "wifi", "korean": "Wi-Fi"},
    {"english": "wireless", "korean": "무선"},
    {"english": "workstation", "korean": "워크스테이션"},

    # 추가 기술 용어들 (100개)
    {"english": "accelerometer", "korean": "가속도계"},
    {"english": "actuator", "korean": "구동기"},
    {"english": "adc", "korean": "아날로그-디지털 변환기"},
    {"english": "agile", "korean": "애자일"},
    {"english": "ai", "korean": "인공지능"},
    {"english": "ajax", "korean": "AJAX"},
    {"english": "api", "korean": "API"},
    {"english": "applet", "korean": "애플릿"},
    {"english": "arduino", "korean": "아두이노"},
    {"english": "array", "korean": "배열"},
    {"english": "ascii", "korean": "ASCII"},
    {"english": "asp", "korean": "ASP"},
    {"english": "asynchronous", "korean": "비동기"},
    {"english": "authentication", "korean": "인증"},
    {"english": "authorization", "korean": "인가"},
    {"english": "autonomous", "korean": "자율"},
    {"english": "avatar", "korean": "아바타"},
    {"english": "backend", "korean": "백엔드"},
    {"english": "barcode", "korean": "바코드"},
    {"english": "batch", "korean": "배치"},
    {"english": "benchmark", "korean": "벤치마크"},
    {"english": "bigdata", "korean": "빅데이터"},
    {"english": "biometric", "korean": "생체인식"},
    {"english": "bitmap", "korean": "비트맵"},
    {"english": "bluetooth", "korean": "블루투스"},
    {"english": "bootstrap", "korean": "부트스트랩"},
    {"english": "buffer", "korean": "버퍼"},
    {"english": "bug", "korean": "버그"},
    {"english": "bus", "korean": "버스"},
    {"english": "bytecode", "korean": "바이트코드"},
    {"english": "cable", "korean": "케이블"},
    {"english": "callback", "korean": "콜백"},
    {"english": "captcha", "korean": "캡차"},
    {"english": "cdrom", "korean": "CD-ROM"},
    {"english": "cgi", "korean": "CGI"},
    {"english": "charset", "korean": "문자셋"},
    {"english": "checksum", "korean": "체크섬"},
    {"english": "chipset", "korean": "칩셋"},
    {"english": "class", "korean": "클래스"},
    {"english": "client", "korean": "클라이언트"},
    {"english": "clipboard", "korean": "클립보드"},
    {"english": "cluster", "korean": "클러스터"},
    {"english": "cms", "korean": "CMS"},
    {"english": "codec", "korean": "코덱"},
    {"english": "collision", "korean": "충돌"},
    {"english": "command", "korean": "명령"},
    {"english": "compile", "korean": "컴파일"},
    {"english": "component", "korean": "컴포넌트"},
    {"english": "computer", "korean": "컴퓨터"},
    {"english": "concurrency", "korean": "동시성"},
    {"english": "configuration", "korean": "구성"},
    {"english": "console", "korean": "콘솔"},
    {"english": "constructor", "korean": "생성자"},
    {"english": "container", "korean": "컨테이너"},
    {"english": "controller", "korean": "컨트롤러"},
    {"english": "cookie", "korean": "쿠키"},
    {"english": "coroutine", "korean": "코루틴"},
    {"english": "cpu", "korean": "중앙처리장치"},
    {"english": "crash", "korean": "충돌"},
    {"english": "cryptography", "korean": "암호학"},
    {"english": "css", "korean": "CSS"},
    {"english": "cursor", "korean": "커서"},
    {"english": "daemon", "korean": "데몬"},
    {"english": "datagram", "korean": "데이터그램"},
    {"english": "debugger", "korean": "디버거"},
    {"english": "decimal", "korean": "십진수"},
    {"english": "decryption", "korean": "복호화"},
    {"english": "default", "korean": "기본값"},
    {"english": "deployment", "korean": "배포"},
    {"english": "design", "korean": "디자인"},
    {"english": "destructor", "korean": "소멸자"},
    {"english": "development", "korean": "개발"},
    {"english": "diagnostic", "korean": "진단"},
    {"english": "dictionary", "korean": "사전"},
    {"english": "directory", "korean": "디렉토리"},
    {"english": "disk", "korean": "디스크"},
    {"english": "distributed", "korean": "분산"},
    {"english": "documentation", "korean": "문서화"},
    {"english": "driver", "korean": "드라이버"},
    {"english": "dynamic", "korean": "동적"},
    {"english": "ecommerce", "korean": "전자상거래"},
    {"english": "editor", "korean": "편집기"},
    {"english": "element", "korean": "요소"},
    {"english": "embedded", "korean": "임베디드"},
    {"english": "emulator", "korean": "에뮬레이터"},
    {"english": "encoding", "korean": "인코딩"},
    {"english": "endpoint", "korean": "엔드포인트"},
    {"english": "engine", "korean": "엔진"},
    {"english": "enterprise", "korean": "기업"},
    {"english": "environment", "korean": "환경"},
    {"english": "error", "korean": "오류"},
    {"english": "event", "korean": "이벤트"},
    {"english": "exception", "korean": "예외"},
    {"english": "executable", "korean": "실행파일"},
    {"english": "execution", "korean": "실행"},
    {"english": "export", "korean": "내보내기"},
    {"english": "extension", "korean": "확장"},
    {"english": "factory", "korean": "팩토리"},
    {"english": "fault", "korean": "결함"},
    {"english": "feature", "korean": "기능"},
    {"english": "feedback", "korean": "피드백"},
    {"english": "firmware", "korean": "펌웨어"},
    {"english": "flash", "korean": "플래시"},
    {"english": "float", "korean": "부동소수점"},
    {"english": "font", "korean": "글꼴"},
    {"english": "fork", "korean": "포크"},
    {"english": "fragment", "korean": "프래그먼트"},
    {"english": "frontend", "korean": "프론트엔드"},
    {"english": "ftp", "korean": "FTP"},
    {"english": "functionality", "korean": "기능성"},
    {"english": "garbage", "korean": "가비지"},

    # 추가 기술 용어들 (100개 - 2차)
    {"english": "gateway", "korean": "게이트웨이"},
    {"english": "generator", "korean": "제너레이터"},
    {"english": "global", "korean": "전역"},
    {"english": "gradient", "korean": "그라디언트"},
    {"english": "graphical", "korean": "그래픽"},
    {"english": "grid", "korean": "그리드"},
    {"english": "handler", "korean": "핸들러"},
    {"english": "hard", "korean": "하드"},
    {"english": "header", "korean": "헤더"},
    {"english": "heap", "korean": "힙"},
    {"english": "hierarchy", "korean": "계층"},
    {"english": "high", "korean": "고급"},
    {"english": "horizontal", "korean": "수평"},
    {"english": "html", "korean": "HTML"},
    {"english": "http", "korean": "HTTP"},
    {"english": "https", "korean": "HTTPS"},
    {"english": "hypertext", "korean": "하이퍼텍스트"},
    {"english": "icon", "korean": "아이콘"},
    {"english": "identifier", "korean": "식별자"},
    {"english": "idle", "korean": "대기"},
    {"english": "image", "korean": "이미지"},
    {"english": "implementation", "korean": "구현"},
    {"english": "import", "korean": "가져오기"},
    {"english": "index", "korean": "인덱스"},
    {"english": "inheritance", "korean": "상속"},
    {"english": "initialization", "korean": "초기화"},
    {"english": "instance", "korean": "인스턴스"},
    {"english": "integer", "korean": "정수"},
    {"english": "integrated", "korean": "통합"},
    {"english": "interaction", "korean": "상호작용"},
    {"english": "internal", "korean": "내부"},
    {"english": "interrupt", "korean": "인터럽트"},
    {"english": "iteration", "korean": "반복"},
    {"english": "iterator", "korean": "이터레이터"},
    {"english": "json", "korean": "JSON"},
    {"english": "keyword", "korean": "키워드"},
    {"english": "label", "korean": "레이블"},
    {"english": "lambda", "korean": "람다"},
    {"english": "language", "korean": "언어"},
    {"english": "latency", "korean": "지연시간"},
    {"english": "layer", "korean": "레이어"},
    {"english": "library", "korean": "라이브러리"},
    {"english": "lifecycle", "korean": "라이프사이클"},
    {"english": "linear", "korean": "선형"},
    {"english": "linux", "korean": "리눅스"},
    {"english": "listener", "korean": "리스너"},
    {"english": "load", "korean": "로드"},
    {"english": "local", "korean": "로컬"},
    {"english": "location", "korean": "위치"},
    {"english": "lock", "korean": "락"},
    {"english": "logging", "korean": "로깅"},
    {"english": "loop", "korean": "루프"},
    {"english": "machine", "korean": "머신"},
    {"english": "macro", "korean": "매크로"},
    {"english": "main", "korean": "메인"},
    {"english": "maintenance", "korean": "유지보수"},
    {"english": "managed", "korean": "관리"},
    {"english": "mapping", "korean": "매핑"},
    {"english": "markup", "korean": "마크업"},
    {"english": "master", "korean": "마스터"},
    {"english": "matrix", "korean": "매트릭스"},
    {"english": "mechanism", "korean": "메커니즘"},
    {"english": "member", "korean": "멤버"},
    {"english": "menu", "korean": "메뉴"},
    {"english": "merge", "korean": "병합"},
    {"english": "message", "korean": "메시지"},
    {"english": "metadata", "korean": "메타데이터"},
    {"english": "method", "korean": "메서드"},
    {"english": "microcontroller", "korean": "마이크로컨트롤러"},
    {"english": "migration", "korean": "마이그레이션"},
    {"english": "modal", "korean": "모달"},
    {"english": "mode", "korean": "모드"},
    {"english": "model", "korean": "모델"},
    {"english": "module", "korean": "모듈"},
    {"english": "monitor", "korean": "모니터"},
    {"english": "multicast", "korean": "멀티캐스트"},
    {"english": "multiprocessing", "korean": "다중처리"},
    {"english": "multithreading", "korean": "다중스레드"},
    {"english": "mutable", "korean": "가변"},
    {"english": "namespace", "korean": "네임스페이스"},
    {"english": "native", "korean": "네이티브"},
    {"english": "navigation", "korean": "네비게이션"},
    {"english": "nested", "korean": "중첩"},
    {"english": "node", "korean": "노드"},
    {"english": "notification", "korean": "알림"},
    {"english": "null", "korean": "널"},
    {"english": "numeric", "korean": "숫자형"},
    {"english": "observer", "korean": "옵저버"},
    {"english": "offline", "korean": "오프라인"},
    {"english": "online", "korean": "온라인"},
    {"english": "opaque", "korean": "불투명"},
    {"english": "operand", "korean": "피연산자"},
    {"english": "operation", "korean": "연산"},
    {"english": "operator", "korean": "연산자"},
    {"english": "optimization", "korean": "최적화"},
    {"english": "optional", "korean": "선택적"},
    {"english": "oracle", "korean": "오라클"},
    {"english": "orchestration", "korean": "오케스트레이션"},
    {"english": "orientation", "korean": "방향"},
    {"english": "origin", "korean": "원점"},
    {"english": "overflow", "korean": "오버플로우"},
    {"english": "overlay", "korean": "오버레이"},
    {"english": "override", "korean": "오버라이드"},
    {"english": "package", "korean": "패키지"},
    {"english": "packet", "korean": "패킷"},
    {"english": "padding", "korean": "패딩"},
    {"english": "page", "korean": "페이지"},
    {"english": "panel", "korean": "패널"},
    {"english": "parameter", "korean": "매개변수"},
    {"english": "parser", "korean": "파서"},
    {"english": "partition", "korean": "파티션"},
    {"english": "passive", "korean": "패시브"},
    {"english": "patch", "korean": "패치"},
    {"english": "payload", "korean": "페이로드"},
    {"english": "peer", "korean": "피어"},
    {"english": "performance", "korean": "성능"},
    {"english": "permission", "korean": "권한"},
    {"english": "persistence", "korean": "영속성"},
    {"english": "placeholder", "korean": "플레이스홀더"},
    {"english": "plain", "korean": "평문"},
    {"english": "plugin", "korean": "플러그인"},
    {"english": "pointer", "korean": "포인터"},
    {"english": "polling", "korean": "폴링"},
    {"english": "pool", "korean": "풀"},
    {"english": "portable", "korean": "휴대용"},
    {"english": "portal", "korean": "포털"},
    {"english": "position", "korean": "위치"},
    {"english": "power", "korean": "파워"},
    {"english": "pragma", "korean": "프라그마"},
    {"english": "precision", "korean": "정밀도"},
    {"english": "prefix", "korean": "접두사"},

    # 추가 기술 용어들 (100개 - 3차)
    {"english": "preprocessing", "korean": "전처리"},
    {"english": "priority", "korean": "우선순위"},
    {"english": "privacy", "korean": "프라이버시"},
    {"english": "private", "korean": "프라이빗"},
    {"english": "procedure", "korean": "프로시저"},
    {"english": "process", "korean": "프로세스"},
    {"english": "processor", "korean": "프로세서"},
    {"english": "product", "korean": "제품"},
    {"english": "profile", "korean": "프로필"},
    {"english": "progress", "korean": "진행"},
    {"english": "project", "korean": "프로젝트"},
    {"english": "property", "korean": "속성"},
    {"english": "protocol", "korean": "프로토콜"},
    {"english": "prototype", "korean": "프로토타입"},
    {"english": "proxy", "korean": "프록시"},
    {"english": "public", "korean": "퍼블릭"},
    {"english": "publisher", "korean": "퍼블리셔"},
    {"english": "pull", "korean": "풀"},
    {"english": "push", "korean": "푸시"},
    {"english": "python", "korean": "파이썬"},
    {"english": "queue", "korean": "큐"},
    {"english": "range", "korean": "범위"},
    {"english": "ratio", "korean": "비율"},
    {"english": "raw", "korean": "원시"},
    {"english": "read", "korean": "읽기"},
    {"english": "readonly", "korean": "읽기전용"},
    {"english": "real", "korean": "실수"},
    {"english": "realtime", "korean": "실시간"},
    {"english": "rebuild", "korean": "재빌드"},
    {"english": "receiver", "korean": "수신자"},
    {"english": "recognition", "korean": "인식"},
    {"english": "recovery", "korean": "복구"},
    {"english": "recursive", "korean": "재귀"},
    {"english": "redirect", "korean": "리다이렉트"},
    {"english": "reference", "korean": "참조"},
    {"english": "reflection", "korean": "리플렉션"},
    {"english": "refresh", "korean": "새로고침"},
    {"english": "register", "korean": "등록"},
    {"english": "registry", "korean": "레지스트리"},
    {"english": "regular", "korean": "정규"},
    {"english": "relational", "korean": "관계형"},
    {"english": "release", "korean": "릴리즈"},
    {"english": "remote", "korean": "원격"},
    {"english": "render", "korean": "렌더"},
    {"english": "request", "korean": "요청"},
    {"english": "response", "korean": "응답"},
    {"english": "restart", "korean": "재시작"},
    {"english": "restore", "korean": "복원"},
    {"english": "result", "korean": "결과"},
    {"english": "return", "korean": "반환"},
    {"english": "reverse", "korean": "역방향"},
    {"english": "revision", "korean": "개정"},
    {"english": "ribbon", "korean": "리본"},
    {"english": "robot", "korean": "로봇"},
    {"english": "role", "korean": "역할"},
    {"english": "rollback", "korean": "롤백"},
    {"english": "root", "korean": "루트"},
    {"english": "runtime", "korean": "런타임"},
    {"english": "sampling", "korean": "샘플링"},
    {"english": "sandbox", "korean": "샌드박스"},
    {"english": "save", "korean": "저장"},
    {"english": "scalar", "korean": "스칼라"},
    {"english": "scaling", "korean": "스케일링"},
    {"english": "scan", "korean": "스캔"},
    {"english": "scope", "korean": "범위"},
    {"english": "scratch", "korean": "스크래치"},
    {"english": "screen", "korean": "화면"},
    {"english": "scripting", "korean": "스크립팅"},
    {"english": "search", "korean": "검색"},
    {"english": "secondary", "korean": "보조"},
    {"english": "section", "korean": "섹션"},
    {"english": "segment", "korean": "세그먼트"},
    {"english": "select", "korean": "선택"},
    {"english": "selector", "korean": "셀렉터"},
    {"english": "semaphore", "korean": "세마포어"},
    {"english": "sequence", "korean": "시퀀스"},
    {"english": "serial", "korean": "직렬"},
    {"english": "serialization", "korean": "직렬화"},
    {"english": "setter", "korean": "세터"},
    {"english": "setup", "korean": "설정"},
    {"english": "shadow", "korean": "섀도우"},
    {"english": "shared", "korean": "공유"},
    {"english": "shell", "korean": "쉘"},
    {"english": "signal", "korean": "시그널"},
    {"english": "signature", "korean": "서명"},
    {"english": "simulation", "korean": "시뮬레이션"},
    {"english": "singleton", "korean": "싱글톤"},
    {"english": "size", "korean": "크기"},
    {"english": "slave", "korean": "슬레이브"},
    {"english": "sleep", "korean": "슬립"},
    {"english": "slice", "korean": "슬라이스"},
    {"english": "smart", "korean": "스마트"},
    {"english": "snapshot", "korean": "스냅샷"},
    {"english": "socket", "korean": "소켓"},
    {"english": "solid", "korean": "솔리드"},
    {"english": "source", "korean": "소스"},
    {"english": "spatial", "korean": "공간"},
    {"english": "spawn", "korean": "스폰"},
    {"english": "special", "korean": "특별"},
    {"english": "spectrum", "korean": "스펙트럼"},
    {"english": "spin", "korean": "스핀"},
    {"english": "split", "korean": "분할"},
    {"english": "spool", "korean": "스풀"},
    {"english": "stack", "korean": "스택"},
    {"english": "standard", "korean": "표준"},
    {"english": "static", "korean": "정적"},
    {"english": "status", "korean": "상태"},
    {"english": "step", "korean": "단계"},
    {"english": "strategy", "korean": "전략"},
    {"english": "stream", "korean": "스트림"},
    {"english": "string", "korean": "문자열"},
    {"english": "structure", "korean": "구조"},
    {"english": "stub", "korean": "스텁"},
    {"english": "style", "korean": "스타일"},
    {"english": "subclass", "korean": "서브클래스"},
    {"english": "subnet", "korean": "서브넷"},
    {"english": "subscriber", "korean": "구독자"},
    {"english": "subsystem", "korean": "서브시스템"},
    {"english": "suite", "korean": "스위트"},
    {"english": "superclass", "korean": "슈퍼클래스"},
    {"english": "support", "korean": "지원"},
    {"english": "surface", "korean": "표면"},
    {"english": "suspend", "korean": "일시중단"},
    {"english": "synchronous", "korean": "동기"},
    {"english": "syntax", "korean": "구문"},
    {"english": "table", "korean": "테이블"},
    {"english": "tag", "korean": "태그"},
    {"english": "target", "korean": "타겟"},
    {"english": "task", "korean": "작업"},
    {"english": "temporary", "korean": "임시"},
    {"english": "test", "korean": "테스트"},
    {"english": "text", "korean": "텍스트"},
    {"english": "thread", "korean": "스레드"},
    {"english": "threshold", "korean": "임계값"},
    {"english": "thumbnail", "korean": "썸네일"},
    {"english": "timeout", "korean": "타임아웃"},
    {"english": "token", "korean": "토큰"},
    {"english": "toolbar", "korean": "툴바"},
    {"english": "tooltip", "korean": "툴팁"},
    {"english": "trace", "korean": "추적"},
    {"english": "track", "korean": "트랙"},
    {"english": "transaction", "korean": "트랜잭션"},
    {"english": "transform", "korean": "변환"},
    {"english": "transient", "korean": "일시적"},
    {"english": "transmission", "korean": "전송"},
    {"english": "transparent", "korean": "투명"},
    {"english": "transport", "korean": "전송"},
    {"english": "tree", "korean": "트리"},
    {"english": "trigger", "korean": "트리거"},
    {"english": "tuple", "korean": "튜플"},
    {"english": "type", "korean": "타입"},
    {"english": "unit", "korean": "유닛"},
    {"english": "universal", "korean": "범용"},
    {"english": "unix", "korean": "유닉스"},
    {"english": "unlock", "korean": "잠금해제"},
    {"english": "unsigned", "korean": "부호없음"},
    {"english": "upgrade", "korean": "업그레이드"},
    {"english": "url", "korean": "URL"},
    {"english": "usage", "korean": "사용법"},
    {"english": "validation", "korean": "검증"},
    {"english": "vendor", "korean": "벤더"},
    {"english": "verbose", "korean": "상세"},
    {"english": "vertical", "korean": "수직"},
    {"english": "view", "korean": "뷰"},
    {"english": "visual", "korean": "시각적"},
    {"english": "void", "korean": "보이드"},
    {"english": "volume", "korean": "볼륨"},
    {"english": "vulnerability", "korean": "취약점"},
    {"english": "weight", "korean": "가중치"},
    {"english": "widget", "korean": "위젯"},
    {"english": "window", "korean": "윈도우"},
    {"english": "wire", "korean": "와이어"},
    {"english": "wizard", "korean": "마법사"},
    {"english": "word", "korean": "워드"},
    {"english": "world", "korean": "월드"},
    {"english": "wrapper", "korean": "래퍼"},
    {"english": "write", "korean": "쓰기"},
    {"english": "yield", "korean": "양보"},
    {"english": "zone", "korean": "존"},
    {"english": "zoom", "korean": "줌"},

    # 추가 과학 용어들 (50개 - 4차)
    {"english": "ablation", "korean": "절제"},
    {"english": "absorption", "korean": "흡수"},
    {"english": "acceleration", "korean": "가속"},
    {"english": "acid", "korean": "산"},
    {"english": "active", "korean": "활성"},
    {"english": "adenosine", "korean": "아데노신"},
    {"english": "adhesion", "korean": "접착"},
    {"english": "adhesive", "korean": "접착제"},
    {"english": "adsorption", "korean": "흡착"},
    {"english": "aerobic", "korean": "호기성"},
    {"english": "aerodynamics", "korean": "공기역학"},
    {"english": "aerosol", "korean": "에어러솔"},
    {"english": "affinity", "korean": "친화성"},
    {"english": "aggregate", "korean": "집합체"},
    {"english": "albumin", "korean": "알부민"},
    {"english": "alkali", "korean": "알칼리"},
    {"english": "alkaline", "korean": "알칼리성"},
    {"english": "allergen", "korean": "알레르겐"},
    {"english": "alloy", "korean": "합금"},
    {"english": "alpha", "korean": "알파"},
    {"english": "alveoli", "korean": "폐포"},
    {"english": "ambient", "korean": "주변"},
    {"english": "amino", "korean": "아미노"},
    {"english": "ammonia", "korean": "암모니아"},
    {"english": "amplitude", "korean": "진폭"},
    {"english": "anaerobic", "korean": "혐기성"},
    {"english": "analogue", "korean": "아날로그"},
    {"english": "analyzer", "korean": "분석기"},
    {"english": "anatomical", "korean": "해부학적"},
    {"english": "angiography", "korean": "혈관조영술"},
    {"english": "anion", "korean": "음이온"},
    {"english": "anode", "korean": "양극"},
    {"english": "anomaly", "korean": "이상"},
    {"english": "antibiotic", "korean": "항생제"},
    {"english": "antibody", "korean": "항체"},
    {"english": "antigen", "korean": "항원"},
    {"english": "antioxidant", "korean": "항산화제"},
    {"english": "antiserum", "korean": "항혈청"},
    {"english": "apatite", "korean": "인회석"},
    {"english": "aqueous", "korean": "수성"},
    {"english": "aromatic", "korean": "방향족"},
    {"english": "arrhenius", "korean": "아레니우스"},
    {"english": "artery", "korean": "동맥"},
    {"english": "artifact", "korean": "인공물"},
    {"english": "asbestos", "korean": "석면"},
    {"english": "assay", "korean": "분석"},
    {"english": "asteroid", "korean": "소행성"},
    {"english": "asymmetric", "korean": "비대칭"},
    {"english": "atmosphere", "korean": "대기"},
    {"english": "atom", "korean": "원자"},
    {"english": "atomic", "korean": "원자"},

    # 추가 과학 용어들 (50개 - 5차)
    {"english": "attenuation", "korean": "감쇠"},
    {"english": "autopsy", "korean": "부검"},
    {"english": "avalanche", "korean": "눈사태"},
    {"english": "bacterial", "korean": "세균성"},
    {"english": "bandwidth", "korean": "대역폭"},
    {"english": "base", "korean": "염기"},
    {"english": "beam", "korean": "빔"},
    {"english": "behavior", "korean": "행동"},
    {"english": "benzene", "korean": "벤젠"},
    {"english": "beta", "korean": "베타"},
    {"english": "bile", "korean": "담즙"},
    {"english": "binary", "korean": "이진"},
    {"english": "biochemical", "korean": "생화학적"},
    {"english": "biodegradable", "korean": "생분해성"},
    {"english": "biomarker", "korean": "생체표지자"},
    {"english": "biomass", "korean": "생물량"},
    {"english": "biosphere", "korean": "생물권"},
    {"english": "biotechnology", "korean": "생명공학"},
    {"english": "blast", "korean": "폭발"},
    {"english": "bloodstream", "korean": "혈류"},
    {"english": "boiling", "korean": "끓음"},
    {"english": "bond", "korean": "결합"},
    {"english": "bone", "korean": "뼈"},
    {"english": "brittle", "korean": "취성"},
    {"english": "buffer", "korean": "완충액"},
    {"english": "calcium", "korean": "칼슘"},
    {"english": "calibration", "korean": "교정"},
    {"english": "capillary", "korean": "모세관"},
    {"english": "carbon", "korean": "탄소"},
    {"english": "carcinogen", "korean": "발암물질"},
    {"english": "catalyst", "korean": "촉매"},
    {"english": "cathode", "korean": "음극"},
    {"english": "cation", "korean": "양이온"},
    {"english": "cell", "korean": "세포"},
    {"english": "cellular", "korean": "세포성"},
    {"english": "centrifuge", "korean": "원심분리기"},
    {"english": "ceramic", "korean": "세라믹"},
    {"english": "channel", "korean": "채널"},
    {"english": "chemical", "korean": "화학"},
    {"english": "chlorine", "korean": "염소"},
    {"english": "chromosome", "korean": "염색체"},
    {"english": "circuit", "korean": "회로"},
    {"english": "citric", "korean": "구연산"},
    {"english": "clinical", "korean": "임상"},
    {"english": "clone", "korean": "클론"},
    {"english": "coagulation", "korean": "응고"},
    {"english": "coefficient", "korean": "계수"},
    {"english": "collision", "korean": "충돌"},
    {"english": "combustion", "korean": "연소"},
    {"english": "compound", "korean": "화합물"},
    {"english": "compression", "korean": "압축"},
    {"english": "concentration", "korean": "농도"}
]

# 사용 예시 함수들
def show_word_list():
    """리스트 형태로 단어 출력"""
    print("\n=== 리스트 형태 단어 목록 ===")
    for word in word_list:
        print(f"{word['english']}: {word['korean']}")

def get_random_word(word_list):
    """무작위 단어 선택"""
    import random
    return random.choice(word_list)

# 전역 변수로 출제된 단어들을 추적 (영어 단어만 저장)
asked_words = set()

def get_random_word_no_duplicates(word_list):
    """중복 없이 랜덤 단어 선택"""
    import random

    # 모든 단어가 출제되었으면 초기화
    if len(asked_words) >= len(word_list):
        print("🎉 모든 단어를 출제했습니다! 다시 시작합니다.")
        asked_words.clear()

    # 남은 단어들 중에서 선택 (영어 키로 중복 체크)
    available_words = [word for word in word_list if word['english'] not in asked_words]

    if not available_words:
        return None  # 모든 단어 출제됨

    selected_word = random.choice(available_words)
    asked_words.add(selected_word['english'])  # 영어 단어만 저장
    return selected_word

def normalize_answer(answer):
    """사용자 답변을 정규화 (대소문자, 공백 처리)"""
    if not answer:
        return ""

    # 1. 양쪽 공백 제거
    answer = answer.strip()

    # 2. 대소문자를 소문자로 통일
    answer = answer.lower()

    # 3. 여러 공백을 하나로 압축 (선택사항)
    import re
    answer = re.sub(r'\s+', ' ', answer)

    return answer

def IsCorrectAnswer(user_answer, correct_answer):
    """사용자 답변과 정답 비교"""
    # 정규화된 답변들 비교
    normalized_user = normalize_answer(user_answer)
    normalized_correct = normalize_answer(correct_answer)

    return normalized_user == normalized_correct

def start_game(word_list, Is_using_no_duplicates=True):
    """최적화된 퀴즈 시스템 (리스트 기반 중복 방지)"""

    print("\n🎯 영어 단어 퀴즈를 시작합니다!")
    print("한글 뜻을 보고 영어 단어를 입력하세요.")
    print("💡 명령어: \\quit(그만두고 통계치를 보며 메뉴로 돌아가기), Ctrl+c(강제 종료)\n")

    score = 0
    total_questions = 0

    while True:
        # 문제 출제 및 입력 처리
        if Is_using_no_duplicates:
            current_word = get_random_word_no_duplicates(word_list)
        else:
            current_word = get_random_word(word_list)

        if not current_word:
            print("❌ 사용할 수 있는 단어가 없습니다.")
            break

        # 문제 출력 (한 번만)
        print(f"문제 {total_questions + 1}: {current_word['korean']}")

        # 입력 루프 - 같은 문제에 대해 반복
        while True:
            print("영어 단어를 입력하세요: ", end="")
            try:
                user_input = input().strip().lower()
                if user_input == '\\quit':
                    print("\n👋 퀴즈를 종료합니다.")
                    show_quiz_stats_and_return(score, total_questions)  # ← 중간 통계 추가
                    return  # ← 함수 전체 종료!                # 빈 입력 처리
                elif not user_input:
                    print("❌ 입력이 없습니다. 다시 시도해주세요.")                            
                else:# 정답 비교
                    total_questions += 1
                    if IsCorrectAnswer(user_input, current_word['english']):
                        print("✅ 정답입니다!")
                        score += 1
                    else:
                        print(f"❌ 오답입니다. 정답은: {current_word['english']}")

                # 현재 점수 표시
                print(f"현재 점수: {score}/{total_questions}")

                # 진행 상황 표시
                if Is_using_no_duplicates and total_questions < len(word_list):
                    remaining = len(word_list) - len(asked_words)
                    print(f"남은 단어: {remaining}개")
                    print("-" * 30)

                # 문제 해결됨 - 다음 문제로
                break

            except (EOFError, KeyboardInterrupt):
                print("\n👋 퀴즈를 종료합니다.")
                show_quiz_stats_and_return(score, total_questions)  # ← 중간 통계 추가
                return  # ← 함수 전체 종료!

    # 퀴즈 자연 종료 시 최종 결과
    show_quiz_stats_and_return(score, total_questions)

def show_quiz_stats_and_return(score, total_questions):
    """중간 통계를 보여주고 메뉴로 돌아가기"""
    if total_questions > 0:
        percentage = (score / total_questions) * 100
        print(f"\n📊 현재까지의 통계:")
        print(f"(오답 개수)/(진행한 문제) = {total_questions - score}/{total_questions}")
        print(f"오답률: {100-percentage:.1f}%")
        print(f"정답률: {percentage:.1f}%")

        if percentage >= 80:
            print("👍 지금까지 잘 하고 있어요!")
        elif percentage >= 60:
            print("📚 조금 더 오답 복습에 집중해보세요, 오늘도 한 건 해낸 당신을 칭찬합니다!")
        else:
            print("💪 전체 단어들을 복습해보세요, 오늘도 한 건 해낸 당신을 칭찬합니다!")
    else:
        print("❌ 문제가 출제되지 않았습니다.")

    print("\n🔄 메인 메뉴로 돌아갑니다...")

# 퀴즈 데모 함수들
def demo_answer_checking():
    """정답 비교 기능 데모"""
    print("\n" + "="*50)
    print("🧪 정답 비교 기능 테스트")
    print("="*50)

    test_cases = [
        ("Apple", "apple", True),  # 대소문자 차이
        ("  apple  ", "apple", True),  # 공백 차이
        ("APPLE", "apple", True),  # 모두 대문자
        ("a p p l e", "apple", False),  # 띄어쓰기 차이
        ("book", "books", False),  # 철자 차이
        ("", "apple", False),  # 빈 입력
    ]

    for user_input, correct, expected in test_cases:
        result = IsCorrectAnswer(user_input, correct)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{user_input}' vs '{correct}' → {result} (기대: {expected})")

def demo_quiz():
    """간단한 퀴즈 데모 (실제 입력 없이)"""
    print("\n" + "="*50)
    print("🎮 퀴즈 데모 (자동 진행)")
    print("="*50)

    # 시뮬레이션용 답변들 (대소문자, 공백 다양하게 테스트)
    mock_answers = ["apple", "wrong", "  BOOK  ", "Cat", "DOG", "  house  "]

    score = 0
    total = 0

    # 기존 word_list 사용
    for i, word in enumerate(word_list):
        if i >= len(mock_answers):
            break

        total += 1
        print(f"\n문제 {total}: {word['korean']}")

        user_answer = mock_answers[i]
        print(f"입력: '{user_answer}'")

        if IsCorrectAnswer(user_answer, word['english']):
            print("✅ 정답!")
            score += 1
        else:
            print(f"❌ 오답! 정답: {word['english']}")

    percentage = (score / total) * 100
    print(f"\n최종 점수: {score}/{total} ({percentage:.1f}%)")
    print("💡 데모에서는 대소문자와 공백이 자동으로 처리됩니다.")
    print("   명령어: \\quit(그만두고 통계치를 보며 메뉴로 돌아가기)")

def run_individual_demos():
    """개별 데모 함수들을 선택적으로 실행"""
    while True:
        print("\n" + "="*50)
        print("🎮 개별 데모 선택")
        print("="*50)
        print("1. ✅ 정답 비교 기능 테스트")
        print("2. 🎯 퀴즈 데모 (자동 진행)")
        print("3. 🔙 뒤로 가기")
        print("="*50)

        try:
            choice = input("실행할 데모 선택 (1-3): ").strip()

            if choice == "1":
                demo_answer_checking()
            elif choice == "2":
                demo_quiz()
            elif choice == "3":
                print("🔙 메인 메뉴로 돌아갑니다.")
                break
            else:
                print("❌ 잘못된 선택입니다.")

            if choice != "3":
                print("\n계속하려면 Enter를 누르세요...")
                input()

        except KeyboardInterrupt:
            print("\n👋 데모를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

# 메인 메뉴
def main_menu():
    """메인 메뉴 실행"""
    while True:
        print("\n🎯 영어 단어 퀴즈 시스템")
        print("="*50)
        print("❓ 무엇을 하시겠습니까?")
        print("1. 중복 방지 퀴즈 (추천) - 모든 단어를 한 번씩 출제")
        print("2. 일반 퀴즈 - 중복 허용")
        print("3. 개별 데모 실행")
        print("4. 종료")
        print("="*50)

        try:
            choice = input("선택 (1-4): ").strip()

            if choice == "1":
                print("🎯 중복 방지 모드로 시작합니다!")
                start_game(word_list, Is_using_no_duplicates=True)
            elif choice == "2":
                print("🎲 일반 모드로 시작합니다!")
                start_game(word_list, Is_using_no_duplicates=False)
            elif choice == "3":
                run_individual_demos()
                # 데모에서 돌아오면 계속 메뉴 표시
            elif choice == "4":
                print("👋 프로그램을 종료합니다.")
                return  # 프로그램 종료
            else:
                print("❌ 잘못된 선택입니다.")
                continue

        except KeyboardInterrupt:
            print("\n👋 프로그램을 종료합니다.")
            return
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            continue

# 테스트 실행
if __name__ == "__main__":
    main_menu()
