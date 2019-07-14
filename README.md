
# <input type = "hidden"> ?

UI가 없지만(사용자가 입력하거나 선택하는 정보는 아니지만) 어떤 값을 서버로 어떤 값을 전송하고싶을 때 쓰이는 태그

ex)
회원가입시 사용자의 아이피를 받는 경우, 히든필드에 넣어서 폼 전송시 함께 전송가능
<input type="hidden" name="UserIP" value="<?echo $REMOTE_ADDR?>">

출처:http://www.homejjang.com/05/HiddenField.php
