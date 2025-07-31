# 🎨 Figma Design Guideline Diff Checker (MVP)

Figma上のデザインガイドラインと、デザインカンプの差分を自動で検出し、  
スタイル違反をレポート化するツールです。

---

## 🚀 機能概要

- ✅ Figmaのデザインガイドラインファイルからスタイル情報（色・テキストなど）を取得
- ✅ デザインカンプと照合し、未定義のスタイルや直接指定された色などの使用を検出
- ✅ 差分結果をMarkdown形式で出力（将来的にPDF化予定）

---

## 📁 ディレクトリ構成

```bash
01_figma-connect/
├── get_file.py # FigmaファイルのJSON取得スクリプト
├── check_style.py # ガイドラインとカンプのスタイル差分チェック
├── .env # Figma APIキーとFile IDを格納
├── guideline.json # デザインガイドラインのJSON（取得後生成）
├── design.json # デザインカンプのJSON（取得後生成）
├── style_diff_report.md # 差分レポート出力（Markdown）
```

---

## 🛠 使用方法

### 1. セットアップ

```bash
git clone https://github.com/your-username/figma-style-diff-checker.git
cd figma-style-diff-checker/01_figma-connect
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. FigmaトークンとファイルIDの設定
.env ファイルを作成して以下の情報を入力してください：

```bash
FIGMA_TOKEN=your_figma_personal_access_token
FIGMA_FILE_ID=xxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. JSONデータの取得

```bash
python get_file.py
```

### 4. 差分チェックの実行

```bash
python check_style.py
```

### 5. レポート確認

- style_diff_report.md にレポートが出力されます

- 未定義スタイルや直接指定カラーの使用箇所が一覧表示されます

---

📚 前提知識・利用技術
Python 3.10+

Figma API

dotenv

requests

---

📄 ライセンス
MIT License
