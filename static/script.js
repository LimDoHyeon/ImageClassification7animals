// 사용자 정의 파일 업로드 버튼에 대한 클릭 이벤트를 설정하는 함수
function setupCustomFileUploadButton() {
    const fileInput = document.querySelector('.mainImageInput');
    const customButton = document.querySelector('.customFileUploadButton');
    
    customButton.addEventListener('click', function() {
        fileInput.click(); // 숨겨진 파일 입력 필드를 클릭합니다
    });

    fileInput.addEventListener('change', loadImage); // 이미지 로드 함수를 연결합니다
}

// 이미지를 로드하고 화면에 표시하는 함수
function loadImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const imgElement = document.querySelector('.mainDisplayedImage');
            imgElement.src = e.target.result;
            imgElement.style.display = 'block'; // 이미지를 화면에 표시
        };
        reader.readAsDataURL(file);
    }
}

// 이미지 분석을 요청하고 결과를 화면에 표시하는 함수
function sendImageForAnalysis() {
    const imageInput = document.querySelector('.mainImageInput');
    const file = imageInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.querySelector('.analysisResult').textContent = data.result;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('Please select an image first.');
    }
}

// 이미지 선택 버튼을 설정하는 함수
function setupImageInputButton() {
    const fileInput = document.querySelector('.mainImageInput');
    const customButton = document.querySelector('.customFileUploadButton');
    
    customButton.addEventListener('click', function() {
        fileInput.click(); // 숨겨진 파일 입력 필드를 클릭합니다
    });

    // 이미지 로드 함수를 파일 입력 필드의 변경 이벤트에 연결합니다
    fileInput.addEventListener('change', loadImage);
}

// 분석 버튼 클릭 이벤트 리스너를 설정하는 함수
function setupAnalyzeButton() {
    const analyzeButton = document.querySelector('.mainAnalyzeButton');
    analyzeButton.addEventListener('click', sendImageForAnalysis);
}


// 이벤트 리스너를 설정하는 함수
// 초기 설정 함수 내에 새 함수를 추가합니다
function setupEventListeners() {
    setupImageInputButton();
    setupAnalyzeButton();
    // 다른 이벤트 리스너 설정 함수들도 여기에 추가할 수 있습니다.
}

// 페이지 로드 시 이벤트 리스너를 설정합니다
document.addEventListener('DOMContentLoaded', setupEventListeners);
