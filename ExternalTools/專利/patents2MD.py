import pandas as pd
import os
import re

# 讀取 CSV 文件
input_csv = "patents.csv"  # 替換為你的 CSV 文件名
output_folder = "md_patents"  # 輸出 Markdown 文件的資料夾

# 確保輸出資料夾存在
os.makedirs(output_folder, exist_ok=True)

# 讀取 CSV 數據
df = pd.read_csv(input_csv)

# 遍歷每一行數據並生成 Markdown 文件
for index, row in df.iterrows():
    # 提取數據
    authors = row['authors']
    title = row['title']
    patent_number = row['patent_number']
    status = row['status'] if not pd.isna(row['status']) else ""
    date = row['date']

    # 清理文件名中的非法字符
    safe_title = re.sub(r'[\/:*?"<>|]', '-', title.lower().replace(" ", "-"))

    # 生成 Markdown 文件內容
    md_content = f"""---
title: "{title}"
authors: "{authors}"
patent_number: "{patent_number}"
status: "{status}"
date: {date}-01
collection: patents
category: patents
permalink: /patents/{date}-{safe_title}
---

**Authors**: {authors}

**Title**: {title}

**Patent Number**: {patent_number}

**Status**: {status}

**Publication Date**: {date}-01
"""

    # 生成文件名
    file_name = f"{date}-{safe_title}.md"
    file_path = os.path.join(output_folder, file_name)

    # 寫入文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(md_content)

print(f"Markdown files have been generated in the '{output_folder}' folder.")
