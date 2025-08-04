# 小鹿清单【 Fawn Todo List 】

一个现代化的待办事项管理应用，帮助你高效组织和跟踪日常任务。

---

当前版本：`v0.0.1`

## 技术栈

### 后端
- Python 3.11.6
- Django 4.2.7
- MySQL 8.0.28

### 前端
- Vue3 3.2.47
- vite 4.4.9
- TypeScript 5.8.3
- Daisyui 5.0.46
- Pinia 2.1.7
- Icon Park 2.1.1

## 功能特点

- **任务管理**：创建、编辑、删除和完成任务
- **分类系统**：为任务添加分类，便于组织和筛选
- **标签系统**：为任务添加标签，提供更灵活的分类方式
- **优先级标识**：支持低、中、高三级优先级，直观展示任务重要程度
- **日期管理**：设置任务截止日期，避免错过重要事项
- **统计分析**：直观展示待完成和已完成任务数量
- **响应式设计**：适配各种屏幕尺寸，提供良好的移动端体验

## 项目结构

```
fawn_todo_list/
├── category/           # 分类相关功能
├── dashboard/          # 仪表盘功能
├── fawn_todo_list/     # 项目配置
├── frontend_vue/       # 前端Vue应用
├── tag/                # 标签相关功能
├── todo/               # 任务相关功能
└── utils/              # 工具函数
```

## 安装指南

### 1. 克隆项目

```bash
git clone https://github.com/your-username/fawn_todo_list.git
cd fawn_todo_list
```

### 2. 配置后端环境

```bash
# 通过 conda 创建虚拟环境
python -m venv venv
# macOS/Linux
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
# 配置数据库
# 修改 fawn_todo_list/settings.py 中的数据库配置
# 迁移数据库
python manage.py makemigrations
python manage.py migrate
```

### 3. 配置前端环境

```bash
# 在 frontend_vue 目录下，执行脚本打包更新前端页面
sh update.sh
```

### 4. 运行项目

```bash
# 返回项目根目录
cd ..
# 运行后端服务器
python manage.py runserver
```

## 使用说明

1. 访问 http://localhost:12088 打开应用
2. 使用管理员账户登录
3. 创建分类和标签
4. 添加新任务并设置优先级和截止日期
5. 在任务列表中管理和完成任务

## 贡献

欢迎提交问题和功能请求。如果您想贡献代码，请 fork 仓库并提交 pull request。

## 许可证

[MIT License](LICENSE)