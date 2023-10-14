# Echo Bot - 家庭教師

このアプリケーションはStreamlitを使用して作成されたEcho Botです。OpenAIのAPIを使用して、ユーザーからの入力に対して返答を生成します。

## 必要なライブラリ

- streamlit
- configparser
- tiktoken
- openai

## セットアップ

1. まず、必要なライブラリをインストールします。
```bash
pip install streamlit configparser tiktoken openai
```

2. `deploy_app.py`という名前で以下のコードを保存します。

```python
import streamlit as st
import configparser
import tiktoken
import openai

# OpenAI APIの初期化
openai.api_key = st.secrets.OpenAI.API_KEY

st.title("Echo Bot - 家庭教師")
# ... [以下、コードの残り]
```

3. OpenAIのAPIキーをセットアップします。これはStreamlitのsecrets.tomlファイルを使用して行います。

4. アプリケーションをローカルで実行する場合は、以下のコマンドを使用します。

```bash
streamlit run deploy_app.py
```

## 使用方法

1. アプリケーションを起動します。
2. 表示されるテキストボックスに質問またはコメントを入力します。
3. Echo Botが応答を生成し、チャットウィンドウに表示されます。
```
