# Python 面试题与高频答疑

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-study--ready-16A34A?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-0F766E?style=flat-square)

![cover](assets/cover.svg)

这个仓库定位不是“刷题库”，而是“带着理解去准备面试和学习难点”。它既适合做课堂热身，也适合用来做训练营答疑、转行复习和项目查漏补缺。

## 当前包含的内容

1. 命令行互动问答器
2. 多方向题库：基础、自动化、数据、采集、AI
3. 按目标方向生成的 4 周复习计划
4. 常见报错与学习问题 FAQ

## 这个仓库适合谁

- 想系统准备 Python 面试的人
- 想整理课堂高频问题的讲师
- 想边做项目边补基础的人

## 快速开始

```bash
python quiz.py --limit 3
python quiz.py --tag ai --limit 2
python study_plan.py --target automation --weeks 4 --output plans/automation_plan.md
```

## 仓库结构

- `data/questions.json`：题库
- `data/topic_paths.json`：不同方向的复习路径
- `quiz.py`：互动答题脚本
- `study_plan.py`：生成复习计划
- `faq/common_issues.md`：高频答疑

## 为什么这个仓库值得 Star

- 题库不只给答案，还适合讲解思路
- 可以按方向做复习计划，更像训练营资料库
- 很适合和你的项目仓库联动使用

## 仓库维护

- 开源协议：`MIT`
- 更新记录见 `CHANGELOG.md`
- 贡献方式见 `CONTRIBUTING.md`
