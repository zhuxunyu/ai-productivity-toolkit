# 自动化脚本模板 - 接单即用

## 模板 1：Excel 批量转换 PDF

```python
"""
Excel 批量转 PDF 工具
使用：python excel_to_pdf.py input_folder output_folder
"""

import os
import sys
from pathlib import Path
from openpyxl import load_workbook
# 需要安装：pip install openpyxl reportlab

def convert_excel_to_pdf(input_file, output_file):
    """单个 Excel 转 PDF"""
    # TODO: 实现实际转换逻辑
    print(f"正在转换：{input_file} -> {output_file}")
    return True

def batch_convert(input_folder, output_folder):
    """批量转换"""
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    excel_files = list(input_path.glob("*.xlsx")) + list(input_path.glob("*.xls"))
    
    for file in excel_files:
        output_file = output_path / f"{file.stem}.pdf"
        try:
            convert_excel_to_pdf(file, output_file)
            print(f"✅ {file.name}")
        except Exception as e:
            print(f"❌ {file.name} - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python excel_to_pdf.py input_folder output_folder")
        sys.exit(1)
    
    batch_convert(sys.argv[1], sys.argv[2])
    print("批量转换完成！")
```

**报价参考：** ¥100-300

---

## 模板 2：数据爬取脚本

```python
"""
通用数据爬取脚本
使用：python crawler.py url output.csv
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
from pathlib import Path

def fetch_page(url):
    """抓取网页"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html):
    """解析 HTML"""
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    
    # TODO: 根据实际页面结构调整选择器
    items = soup.select('.item')
    for item in items:
        data.append({
            'title': item.select_one('.title').text.strip() if item.select_one('.title') else '',
            'price': item.select_one('.price').text.strip() if item.select_one('.price') else '',
            'url': item.select_one('a')['href'] if item.select_one('a') else ''
        })
    
    return data

def save_to_csv(data, output_file):
    """保存到 CSV"""
    if not data:
        print("没有数据可保存")
        return
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ 保存 {len(data)} 条数据到 {output_file}")

def main(url, output):
    """主函数"""
    print(f"开始抓取：{url}")
    html = fetch_page(url)
    data = parse_html(html)
    save_to_csv(data, output)
    print("爬取完成！")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("用法：python crawler.py url output.csv")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
```

**报价参考：** ¥200-800（根据复杂度）

**注意事项：**
- ⚠️ 只爬公开数据
- ⚠️ 遵守 robots.txt
- ⚠️ 控制请求频率
- ⚠️ 不突破反爬措施

---

## 模板 3：文件批量重命名

```python
"""
文件批量重命名工具
使用：python rename_files.py folder pattern
"""

import os
import sys
from pathlib import Path

def rename_files(folder, pattern):
    """批量重命名文件"""
    folder_path = Path(folder)
    
    for i, file in enumerate(folder_path.iterdir(), 1):
        if file.is_file():
            # 生成新文件名
            new_name = pattern.replace('{i}', str(i)).replace('{name}', file.stem)
            new_name = f"{new_name}{file.suffix}"
            new_path = folder_path / new_name
            
            # 重命名
            file.rename(new_path)
            print(f"✅ {file.name} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python rename_files.py folder pattern")
        print("示例：python rename_files.py ./photos 'IMG_{i}'")
        sys.exit(1)
    
    rename_files(sys.argv[1], sys.argv[2])
    print("批量重命名完成！")
```

**报价参考：** ¥50-150

---

## 模板 4：邮件自动发送

```python
"""
邮件批量发送工具
使用：python send_emails.py recipients.csv subject body.html
"""

import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def send_email(smtp_server, smtp_port, username, password, to, subject, body):
    """发送单封邮件"""
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    
    print(f"✅ 已发送到：{to}")

def batch_send(recipients_file, subject, body_file):
    """批量发送"""
    # 读取收件人列表
    recipients = []
    with open(recipients_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipients.append(row['email'])
    
    # 读取邮件正文
    with open(body_file, 'r', encoding='utf-8') as f:
        body = f.read()
    
    # 配置（从环境变量读取）
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    username = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')
    
    # 发送
    for email in recipients:
        try:
            send_email(smtp_server, smtp_port, username, password, email, subject, body)
            time.sleep(1)  # 避免过快
        except Exception as e:
            print(f"❌ 发送到 {email} 失败：{e}")

if __name__ == "__main__":
    import os
    import sys
    import time
    
    if len(sys.argv) != 4:
        print("用法：python send_emails.py recipients.csv subject.html body.html")
        sys.exit(1)
    
    batch_send(sys.argv[1], sys.argv[2], sys.argv[3])
    print("批量发送完成！")
```

**报价参考：** ¥100-300

**配置说明：**
需要设置环境变量：
```bash
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SMTP_USERNAME=your@email.com
export SMTP_PASSWORD=YOUR_SMTP_PASSWORD_HERE  # Replace with your actual password
```

---

## 模板 5：数据清洗工具

```python
"""
数据清洗工具
使用：python clean_data.py input.csv output.csv
"""

import pandas as pd
import sys

def clean_data(input_file, output_file):
    """数据清洗"""
    # 读取数据
    df = pd.read_csv(input_file)
    
    print(f"原始数据：{len(df)} 行，{len(df.columns)} 列")
    
    # 1. 删除空值
    df = df.dropna()
    print(f"删除空值后：{len(df)} 行")
    
    # 2. 删除重复值
    df = df.drop_duplicates()
    print(f"删除重复后：{len(df)} 行")
    
    # 3. 格式化（根据实际需求调整）
    # df['column'] = df['column'].str.strip()
    
    # 4. 数据类型转换
    # df['number'] = pd.to_numeric(df['number'], errors='coerce')
    
    # 保存
    df.to_csv(output_file, index=False)
    print(f"✅ 清洗完成，保存到：{output_file}")
    print(f"最终数据：{len(df)} 行")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python clean_data.py input.csv output.csv")
        sys.exit(1)
    
    clean_data(sys.argv[1], sys.argv[2])
```

**报价参考：** ¥150-500

---

## 接单流程

### 1. 需求沟通
```
客户：我需要批量处理 Excel 文件
我：具体需要什么功能？
客户：把 100 个 Excel 转成 PDF
我：好的，¥200，明天交付，可以吗？
客户：可以
```

### 2. 收取定金
```
我：先付 50% 定金（¥100），完工付尾款
客户：好的（转账）
```

### 3. 开发交付
```
我：（使用对应模板开发）
我：（测试通过）
我：（发送演示视频/截图）
我：已完成，请验收
客户：没问题
```

### 4. 收取尾款
```
我：好的，尾款¥100，收到后发源文件
客户：（转账）
我：（发送源文件 + 使用说明）
```

---

## 注意事项

### ✅ 要做
- 明确需求（避免反复修改）
- 收取定金（50%）
- 定期沟通进度
- 提供使用说明

### ❌ 不要
- 不接急单（除非加价）
- 不接违法需求
- 不脱离平台交易
- 不承诺做不到的功能

---

*创建时间：2026-03-05 09:20*
*目标：接单即用，快速交付*
