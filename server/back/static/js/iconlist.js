console.log("javascript動いてるよ")
document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // デフォルトのフォームサブミットを防止
    
    // カスタムの処理を実行
    
    // フォームのデータを取得
    var formData = new FormData(this);
    
    // AJAXリクエストを送信
    var xhr = new XMLHttpRequest();
    xhr.open("POST", this.action, true);
    xhr.onload = function() {
      // レスポンスを処理
        if (xhr.status === 200) {
            // 成功時の処理
        } else {
            // エラー時の処理
        }
    };
    xhr.send(formData);
});
