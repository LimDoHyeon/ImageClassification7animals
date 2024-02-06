from torchvision import models, transforms
from PIL import Image
import os
import torch


model = models.resnet18(weights=None)  # 모델 구조 정의
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 7)  # 클래스 수에 맞게 마지막 레이어 조정

model.load_state_dict(torch.load('modelv3_acc93.pth', map_location=torch.device('cpu')))  # CPU에서 GPU모델을 로드하기 위한 코드
model.eval()  # 평가 모드 설정


# 모델을 평가 모드로 설정
model.eval()

label_map = {'cat': 0, 'cow': 1, 'dog': 2, 'elephant': 3, 'horse': 4, 'lamb': 5, 'squirrel': 6}

# 이미지 전처리를 위한 변환 정의
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 이미지 크기 조정
    transforms.ToTensor(),  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 정규화
])

# 이미지 로드 및 전처리
image_path = '/Users/imdohyeon/Documents/PythonWorkspace/2024WT_imgclassify7animals/dogSuperCertain.jpeg'
image = Image.open(image_path).convert("RGB")
image = transform(image)
image = image.unsqueeze(0)  # 배치 차원 추가

with torch.no_grad():  # 그래디언트 계산 비활성화
    outputs = model(image)
    _, predicted = torch.max(outputs, 1)

# 클래스 인덱스를 라벨로 매핑
idx_to_class = {v: k for k, v in label_map.items()}
predicted_label = idx_to_class[predicted.item()]

print(f"Predicted label: {predicted_label}")

