from torchvision import models, transforms
from PIL import Image
import torch

# 모델 구조 정의 및 가중치 로드
model = models.resnet18(weights=None)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 7)  # 클래스 수에 맞게 마지막 레이어 조정
model.load_state_dict(torch.load('modelv3_acc93.pth', map_location=torch.device('cpu')))
model.eval()  # 평가 모드 설정

# 라벨 맵 정의
label_map = {'cat': 0, 'cow': 1, 'dog': 2, 'elephant': 3, 'horse': 4, 'lamb': 5, 'squirrel': 6}
idx_to_class = {v: k for k, v in label_map.items()}

# 이미지 전처리를 위한 변환 정의
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 이미지 크기 조정
    transforms.ToTensor(),  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 정규화
])

# 이미지 파일로부터 모델을 통해 예측을 수행하는 함수
def run_model(image_file):
    image = Image.open(image_file).convert("RGB")
    image = transform(image)
    image = image.unsqueeze(0)  # 배치 차원 추가
    
    with torch.no_grad():  # 그래디언트 계산 비활성화
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    
    predicted_label = idx_to_class[predicted.item()]
    return predicted_label

# 예시: 파일을 직접 실행했을 때의 테스트 코드
if __name__ == '__main__':
    # 테스트 이미지 경로를 지정하세요.
    test_image_path = 'path_to_your_test_image.jpg'
    with open(test_image_path, 'rb') as image_file:
        print(f"Predicted label: {run_model(image_file)}")
