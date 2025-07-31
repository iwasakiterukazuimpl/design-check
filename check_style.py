import json
import os

# === 設定 ===
GUIDELINE_FILE = "figma_file_output_guideline.json"
CAMP_FILE = "figma_file_output_Design.json"
REPORT_FILE = "style_diff_report.md"

# === JSONファイルの読み込み ===
with open(GUIDELINE_FILE, "r", encoding="utf-8") as f:
    guideline_data = json.load(f)

with open(CAMP_FILE, "r", encoding="utf-8") as f:
    camp_data = json.load(f)

# === ガイドラインスタイル一覧（色とテキスト） ===
defined_color_styles = {}
defined_text_styles = {}

for style in guideline_data.get("styles", []):
    if "style_type" not in style:
        continue  # スキップ

    if style["style_type"] == "FILL":
        fill_styles[style["node_id"]] = style["name"]

    elif style["style_type"] == "TEXT":
        text_styles[style["node_id"]] = style["name"]


# === カンプで使用されているスタイルID（色・テキスト）を再帰的に抽出 ===
used_color_styles = set()
used_text_styles = set()

def collect_styles(node):
    styles = node.get("styles", {})
    if "fill" in styles:
        used_color_styles.add(styles["fill"])
    if "text" in styles:
        used_text_styles.add(styles["text"])

    for child in node.get("children", []):
        collect_styles(child)

for page in camp_data.get("document", {}).get("children", []):
    collect_styles(page)

# === 差分を抽出 ===
undefined_colors = used_color_styles - set(defined_color_styles.keys())
undefined_texts = used_text_styles - set(defined_text_styles.keys())

unused_colors = set(defined_color_styles.keys()) - used_color_styles
unused_texts = set(defined_text_styles.keys()) - used_text_styles

# === Markdownレポート出力 ===
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("# 🎨 スタイル差分レポート\n\n")

    f.write("## ❌ 未定義のカラースタイルが使われています\n")
    if undefined_colors:
        for style_id in undefined_colors:
            f.write(f"- `{style_id}`（未定義）\n")
    else:
        f.write("- なし\n")

    f.write("\n## ❌ 未定義のテキストスタイルが使われています\n")
    if undefined_texts:
        for style_id in undefined_texts:
            f.write(f"- `{style_id}`（未定義）\n")
    else:
        f.write("- なし\n")

    f.write("\n## ⚠️ 使用されていないカラースタイル（定義済）\n")
    if unused_colors:
        for style_id in unused_colors:
            name = defined_color_styles[style_id]
            f.write(f"- `{name}` (`{style_id}`)\n")
    else:
        f.write("- すべて使用されています\n")

    f.write("\n## ⚠️ 使用されていないテキストスタイル（定義済）\n")
    if unused_texts:
        for style_id in unused_texts:
            name = defined_text_styles[style_id]
            f.write(f"- `{name}` (`{style_id}`)\n")
    else:
        f.write("- すべて使用されています\n")

print(f"✅ 差分レポートを書き出しました → {REPORT_FILE}")
