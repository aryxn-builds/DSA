import os
import urllib.parse

def generate_readme():
    base_dir = "Data Structures & Algorithms"
    if not os.path.exists(base_dir):
        print(f"Directory {base_dir} not found!")
        return
        
    problems = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    
    total_problems = len(problems)
    
    table_rows = []
    
    for problem in problems:
        problem_path = os.path.join(base_dir, problem)
        files = os.listdir(problem_path)
        
        # Format name
        formatted_name = " ".join(word.capitalize() for word in problem.split("-"))
        
        # Detect languages
        langs = set()
        for file in files:
            if file.endswith('.py'): langs.add('Python')
            elif file.endswith('.java'): langs.add('Java')
            elif file.endswith('.cpp') or file.endswith('.cc') or file.endswith('.cxx'): langs.add('C++')
            elif file.endswith('.js') or file.endswith('.ts'): langs.add('JS/TS')
            elif file.endswith('.go'): langs.add('Go')
            elif file.endswith('.c'): langs.add('C')
            elif file.endswith('.cs'): langs.add('C#')
            elif file.endswith('.rs'): langs.add('Rust')
            
        langs_str = ", ".join(sorted(langs)) if langs else "N/A"
        
        # Create link
        encoded_path = urllib.parse.quote(f"{base_dir}/{problem}")
        link = f"[{formatted_name}]({encoded_path})"
        
        table_rows.append(f"| {link} | {langs_str} |")

    table_content = "\n".join(table_rows)

    readme_content = f"""# 🚀 Data Structures & Algorithms

Welcome to my **Data Structures & Algorithms** repository! This repository contains my solutions to various algorithmic problems and data structure implementations.

![DSA Banner](https://img.shields.io/badge/Algorithms-Awesome-blue?style=for-the-badge&logo=codeforces)
![Problems Solved](https://img.shields.io/badge/Problems_Solved-{total_problems}-success?style=for-the-badge&logo=leetcode)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📚 About
This repository is an ongoing journey of mastering Data Structures and Algorithms. The goal is to build a strong foundation in problem-solving and algorithmic thinking.

**Note:** This README is automatically generated and updated by a Python script (`update_readme.py`) whenever new problems are committed! 🤖✨

## 📂 Problem Index

| Problem Name | Languages |
| ------------ | --------- |
{table_content}

---

## 🛠️ How it works
This repository uses a Git **pre-commit hook** and a Python script. When a new problem is added to the `Data Structures & Algorithms` folder, the README is automatically updated to include it before the commit is finalized.

To manually regenerate this README, run:
```bash
python update_readme.py
```

## 🤝 Contributing
Feel free to fork this repository, add more solutions in different languages, or optimize the existing ones!

---
*Happy Coding!* 💻
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    print("README.md has been successfully updated!")

if __name__ == "__main__":
    generate_readme()
