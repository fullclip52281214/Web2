import pandas as pd
import os
import re  # 用於清理非法字符

# 讀取 CSV 文件
input_csv = "publications.csv"  # 替換為你的 CSV 文件名
output_folder = "md_files"  # 輸出 Markdown 文件的資料夾

# 確保輸出資料夾存在
os.makedirs(output_folder, exist_ok=True)

# 讀取 CSV 數據
df = pd.read_csv(input_csv)

# 遍歷每一行數據並生成 Markdown 文件
for index, row in df.iterrows():
    # 提取數據
    authors = row['authors']
    title = row['title']
    venue = row['venue']
    date = row['date']
    volume = str(row['volume']) if not pd.isna(row['volume']) else ""
    issue = str(row['issue']) if not pd.isna(row['issue']) else ""

    # 格式化 venue
    venue_detail = venue
    if volume and issue:
        venue_detail += f", vol. {volume}, no. {issue}"

    # 清理文件名中的非法字符
    safe_title = re.sub(r'[\/:*?"<>|]', '-', title.lower().replace(" ", "-"))

    # 生成 Markdown 文件內容
    md_content = f"""---
title: "{title}"
authors: "{authors}"
venue: "{venue_detail}"
date: {date}-01
collection: publications
category: manuscripts
permalink: /publication/{date}-{safe_title}
---

**Authors**: {authors}

**Title**: {title}

**Journal**: {venue_detail}

**Publication Date**: {date}-01
"""

    # 生成文件名
    file_name = f"{date}-{safe_title}.md"
    file_path = os.path.join(output_folder, file_name)

    # 寫入文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(md_content)

print(f"Markdown files have been generated in the '{output_folder}' folder.")
