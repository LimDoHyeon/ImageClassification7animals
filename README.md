# ImageClassification7animals
[토이 프로젝트] 7종 동물(고양이, 소, 강아지, 코끼리, 말, 양, 다람쥐) 분류(Classification) 모델<br>
(2024 캡스톤디자인 기초 AI 스터디 일환)

[Toy Project] Classification model for 7 species(cat, cow, dog, elephant, horse, lamb, squirrel) of animals<br>
(Part of a fundamental AI study in Capstone Design 2024)


## 모델(Model)
### ResNet-18
<img src="https://blog.kakaocdn.net/dn/Bl6lG/btrDyFKASgY/LD9Z8BvHg1S76DcRe7yJd0/img.png">

- 학습률(Learning Rate) : 0.0001<br>
- 손실 함수(Loss function) : CrossEntropy<br>
- 최적화 함수(Optimizer) : Adam<br>
- 에포크 수(Number of epoch) : 20


## 데이터셋(Dataset)
- <b>Training 800 images per species</b>
- <b>Testing 200 images per species</b>
- https://www.kaggle.com/datasets/chetankv/dogs-cats-images (Cats and Dogs)
- https://www.kaggle.com/datasets/alessiocorrado99/animals10 (Other animals)

## 성능 지표(Performance)
- Accuracy : 93.07%
- F1 Score : 0.9306

<img width="253" alt="image" src="https://github.com/LimDoHyeon/ImageClassification7animals/assets/94499717/ea3671d8-c128-4f57-9a94-60cb15d6e0ee">
