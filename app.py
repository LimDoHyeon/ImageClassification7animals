from flask import Flask, request, jsonify, render_template
from modelTest import run_model

app = Flask(__name__)

@app.route('/')
#def index():
#    return render_template('index.html')
def index():
    return '''
    <!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/style.css">
    <script src="static/script.js"></script>
    <title>동물 분류 인공지능</title>
</head>
<body>
    <header class="introduce">
        <h1 class="headerTitle">동물 분류 인공지능</h1>
        <p class="headerDescription">당신이 업로드한 동물이 무엇인지 맞춰 드립니다</p>
        <div class="headerAnimals">
            <img class="headerAnimalList" src="static/img/cat.png">
            <img class="headerAnimalList" src="static/img/dog.png">
            <img class="headerAnimalList" src="static/img/cow.png">
            <img class="headerAnimalList" src="static/img/elephant.png">
            <img class="headerAnimalList" src="static/img/horse.png">
            <img class="headerAnimalList" src="static/img/lamb.png">
            <img class="headerAnimalList" src="static/img/squirrel.png">
        </div>
    </header>
    <main>
        <!-- 사용자 정의 버튼을 추가합니다 -->
        <button class="customFileUploadButton">파일 선택</button>
        <!-- 파일 입력 필드를 숨깁니다 -->
        <input type="file" class="mainImageInput" accept="image/*">

        <br><br>
        <img class="mainDisplayedImage" src="#" alt="selectedImage" style="display:none; max-width: 300px; max-height: 300px;">
        <br><br>
        <button class="mainAnalyzeButton">분석하기</button> 
        <p class="analysisResult"></p>
    </main>

</body>
</html>
    '''

@app.route('/analyze', methods=['POST'])
def analyze_image():
    image_file = request.files['image']
    predicted_label = run_model(image_file)
    return jsonify({'result': predicted_label})

if __name__ == '__main__':
    app.run(debug=True)
