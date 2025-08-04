import axios from 'axios';

// 创建axios实例
const api = axios.create({
  baseURL: '127.0.0.1:12088', // 假设后端API地址是这个
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 获取任务列表
export const fetchTodos = async (page = 1, pageSize = 10, keyword = '') => {
  try {
    const response = await api.get('/todo/', {
      params: {
        page,
        page_size: pageSize,
        keyword
      }
    });
    return response.data;
  } catch (error) {
    console.error('Failed to fetch todos:', error);
    throw error;
  }
};

// 其他API方法可以在这里添加
// 例如添加任务、更新任务、删除任务等