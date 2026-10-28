# Digit Recognizer

Kaggle [Digit Recognizer](https://www.kaggle.com/c/digit-recognizer) 대회 데이터로 손글씨 숫자(0~9)를 분류하는 간단한 CNN.

## 구조

```
Digit Recognizer/
├── data/
│   ├── data_loader.py        # Kaggle 데이터 다운로드
│   ├── EDA.ipynb             # 샘플 이미지 시각화
│   ├── train.csv             # label + pixel0~783 (42,000장)
│   ├── test.csv              # pixel0~783, 라벨 없음 (28,000장)
│   ├── sample_submission.csv
│   └── submission.csv        # train.ipynb 실행 결과
└── script/train/
    └── train.ipynb           # 학습 · 검증 · 예측 · 제출 파일 생성
```

## 준비

```bash
pip install kagglehub numpy pandas matplotlib torch torchvision
```

Kaggle 인증이 필요합니다.

1. [kaggle.com/settings](https://www.kaggle.com/settings) → **API → Create New Token**
2. 토큰을 `~/.kaggle/access_token`(또는 `~/.kaggle/kaggle.json`)에 저장
3. [대회 규칙](https://www.kaggle.com/c/digit-recognizer/rules) 동의

## 실행

1. 데이터 다운로드 — `data/` 폴더에 CSV가 생깁니다.
   ```bash
   cd data
   python data_loader.py
   ```
2. `script/train/train.ipynb`를 위에서부터 실행합니다.

## 모델

| 단계 | 내용 |
|---|---|
| 전처리 | 픽셀 `/255` → Normalize `(0.1307, 0.3081)`, `train.csv`를 9:1로 train/val 분할 (seed 42) |
| 모델 | Conv(1→16) → Pool → Conv(16→32) → Pool → FC(1568→128) → FC(128→10), ReLU |
| 학습 | Adam (lr 1e-3), CrossEntropyLoss, batch 64, 5 epochs |

## 결과

| 지표 | 값 |
|---|---|
| Validation Accuracy | 98.40% |

`test.csv`는 라벨이 없어서 예측 결과를 `data/submission.csv`로 저장하고 Kaggle에 제출해 점수를 확인합니다.
