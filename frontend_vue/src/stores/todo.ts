import { defineStore } from 'pinia';
import { v4 as uuidv4 } from 'uuid';
import { getRelativeDate } from '../utils/date';

// 定义分类和标签接口
interface Category {
  id: string;
  name: string;
  color: string;
  createdAt: Date;
}

interface Tag {
  id: string;
  name: string;
  color: string;
  createdAt: Date;
}

export interface Todo {
  id: string;
  text: string;
  categoryId: string;
  completed: boolean;
  dueDate?: string;
  tagIds: string[];
  notes?: string;
  createdAt: Date;
}



// --- 演示数据 ---
// 每个任务通过包含 'important' 和 'urgent' tagId 来决定其所属象限
const mockTodos: Todo[] = [
    // --- 1. Important & Urgent (Due Today & Tomorrow) ---
    { id: `task-1`, text: '修复线上支付接口Bug', categoryId: 'work', completed: false, tagIds: ['important', 'urgent'], dueDate: getRelativeDate(0), createdAt: new Date() },
    { id: `task-2`, text: '准备下午3点的项目紧急会议材料', categoryId: 'work', completed: false, tagIds: ['important', 'urgent'], dueDate: getRelativeDate(0), createdAt: new Date() },
    { id: `task-3`, text: '处理服务器宕机警报', categoryId: 'work', completed: true, tagIds: ['important', 'urgent'], dueDate: getRelativeDate(0), createdAt: new Date() },
    { id: `task-4`, text: '回复CEO关于Q3财报的邮件', categoryId: 'work', completed: false, tagIds: ['important', 'urgent'], dueDate: getRelativeDate(1), createdAt: new Date() },
    { id: `task-5`, text: '客户重要投诉电话回访', categoryId: 'life', completed: false, tagIds: ['important', 'urgent'], dueDate: getRelativeDate(1), createdAt: new Date() },
    // --- 2. Important & Not Urgent (Due in the future) ---
    { id: `task-6`, text: '制定Q4季度产品路线图', categoryId: 'work', completed: false, tagIds: ['important'], dueDate: getRelativeDate(10), createdAt: new Date() },
    { id: `task-7`, text: '学习Vue 3.5新特性', categoryId: 'study', completed: false, tagIds: ['important'], dueDate: getRelativeDate(15), createdAt: new Date() },
    { id: `task-8`, text: '规划年度家庭旅行', categoryId: 'life', completed: false, tagIds: ['important', 'personal'], dueDate: getRelativeDate(30), createdAt: new Date() },
    { id: `task-9`, text: '完成体检预约', categoryId: 'life', completed: true, tagIds: ['important', 'personal'], dueDate: getRelativeDate(7), createdAt: new Date() },
    { id: `task-10`, text: '撰写技术博客文章', categoryId: 'study', completed: false, tagIds: ['important'], dueDate: getRelativeDate(5), createdAt: new Date() },
    { id: `task-11`, text: '进行代码重构和性能优化', categoryId: 'work', completed: false, tagIds: ['important'], dueDate: getRelativeDate(20), createdAt: new Date()},
    // --- 3. Urgent & Not Important (Due Today) ---
    { id: `task-12`, text: '回复一些非核心业务的邮件', categoryId: 'work', completed: false, tagIds: ['urgent'], dueDate: getRelativeDate(0), createdAt: new Date() },
    { id: `task-13`, text: '参加一个临时的、非必要的部门会议', categoryId: 'work', completed: true, tagIds: ['urgent'], dueDate: getRelativeDate(1), createdAt: new Date() },
    { id: `task-14`, text: '取一下办公室下午茶', categoryId: 'life', completed: false, tagIds: ['urgent'], dueDate: getRelativeDate(0), createdAt: new Date() },
    // --- 4. Not Urgent & Not Important (No specific due date) ---
    { id: `task-17`, text: '整理电脑桌面文件', categoryId: 'work', completed: false, tagIds: [], createdAt: new Date()},
    { id: `task-19`, text: '整理书架上的旧书', categoryId: 'life', completed: false, tagIds: ['personal'], createdAt: new Date() },
];

export const useTodoStore = defineStore('todo', {
  state: () => ({
    categoryModalVisible: false,
    tagModalVisible: false,
    todos: mockTodos as Todo[],
    categories: [
      { id: 'work', name: '工作', color: '#3b82f6', createdAt: new Date() }, // blue-500
      { id: 'life', name: '生活', color: '#10b981', createdAt: new Date() }, // green-500
      { id: 'study', name: '学习', color: '#8b5cf6', createdAt: new Date() } // violet-500
    ] as Category[],
    tags: [
      // 核心标签，用于四象限分类
      { id: 'urgent', name: '紧急', color: '#f59e0b', createdAt: new Date() }, // amber-500
      { id: 'important', name: '重要', color: '#ef4444', createdAt: new Date() }, // red-500
      // 其他标签
      { id: 'personal', name: '个人', color: '#6366f1', createdAt: new Date() } // indigo-400
    ] as Tag[],
    activeCategoryId: 'work'
  }),
  getters: {
    // 获取当前激活分类下的任务
    activeCategoryTodos: (state: { todos: Todo[]; activeCategoryId: string }) => {
      return state.todos.filter((todo: Todo) => todo.categoryId === state.activeCategoryId);
    },
    // 获取分类下的任务数量
    categoryTaskCount: (state: { todos: Todo[] }) => (categoryId: string) => {
      return state.todos.filter((todo: Todo) => todo.categoryId === categoryId).length;
    },
    // 获取标签下的任务数量
    tagTaskCount: (state: { todos: Todo[] }) => (tagId: string) => {
      return state.todos.filter((todo: Todo) => todo.tagIds.includes(tagId)).length;
    },
    // 根据ID获取分类名称
    getCategoryName: (state: { categories: Category[] }) => (categoryId: string) => {
      return state.categories.find((cat: Category) => cat.id === categoryId)?.name || '未分类';
    },
    // 根据ID获取分类颜色
    getCategoryColor: (state: { categories: Category[] }) => (categoryId: string) => {
      return state.categories.find((cat: Category) => cat.id === categoryId)?.color || '#9ca3af';
    },
    // 根据ID获取标签名称
    getTagName: (state: { tags: Tag[] }) => (tagId: string) => {
      return state.tags.find((tag: Tag) => tag.id === tagId)?.name || '未知标签';
    },
    // 根据ID获取标签颜色
    getTagColor: (state: { tags: Tag[] }) => (tagId: string) => {
      return state.tags.find((tag: Tag) => tag.id === tagId)?.color || '#9ca3af';
    }
  },
  actions: {
    // 添加新分类
    addCategory(name: string, color: string) {
      const existing = this.categories.some(cat => cat.name.toLowerCase() === name.toLowerCase());
      if (existing) return false; // 分类已存在

      this.categories.push({
        id: uuidv4(),
        name,
        color,
        createdAt: new Date()
      });
      return true;
    },
    // 添加新标签
    addTag(name: string, color: string) {
      const existing = this.tags.some(tag => tag.name.toLowerCase() === name.toLowerCase());
      if (existing) return false; // 标签已存在

      this.tags.push({
        id: uuidv4(),
        name,
        color,
        createdAt: new Date()
      });
      return true;
    },
    // 切换标签模态框可见性
    toggleTagModalVisibility(visible: boolean) {
      this.tagModalVisible = visible;
    },

    // 添加新任务
    addTodo(todoData: { text: string; categoryId: string }) {
      const newTodo: Todo = {
        id: `task-${Date.now()}`, // 使用时间戳作为简单ID
        ...todoData,
        completed: false,
        tagIds: [],
        createdAt: new Date()
      };
      this.todos.push(newTodo);
    },

    // 更新任务
    updateTodo(updatedTodo: Todo) {
      const index = this.todos.findIndex(todo => todo.id === updatedTodo.id);
      if (index !== -1) {
        this.todos[index] = updatedTodo;
      }
    },

    // 切换任务完成状态
    toggleTodoCompletion(id: string) {
      const todo = this.todos.find(todo => todo.id === id);
      if (todo) {
        todo.completed = !todo.completed;
      }
    },

    // 删除任务
    deleteTodo(id: string) {
      this.todos = this.todos.filter(todo => todo.id !== id);
    },

    // 删除分类
    deleteCategory(id: string) {
      // 如果有任务使用此分类，不允许删除
      if (this.todos.some(todo => todo.categoryId === id)) return false;
      this.categories = this.categories.filter(cat => cat.id !== id);
      return true;
    },

    // 删除标签
    deleteTag(id: string) {
      // 从所有任务中移除该标签
      this.todos.forEach(todo => {
        todo.tagIds = todo.tagIds.filter(tagId => tagId !== id);
      });
      this.tags = this.tags.filter(tag => tag.id !== id);
      return true;
    }
  }
});