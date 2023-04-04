const textarea = document.querySelector('.textarea');

textarea.addEventListener('input', () => {
  textarea.style.height = 'auto';
  textarea.style.height = textarea.scrollHeight + 'px';
});

// judge-button要素を取得
const judgeButton = document.querySelector('.judge-button');

// judge-buttonがクリックされた時の処理を定義
judgeButton.addEventListener('click', () => {
  // img要素を取得
  const gptImg = document.querySelector('.gpt-img');

  // img要素のsrc属性を変更
  gptImg.src = '../static/image/judging.gif';
});