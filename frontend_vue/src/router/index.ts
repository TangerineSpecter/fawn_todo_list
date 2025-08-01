import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Statistics from '@/views/Statistics.vue'
import About from '@/views/About.vue'
import Quadrant from '@/views/Quadrant.vue'  // 添加新页面导入
import Calendar from '@/views/Calendar.vue'  // 添加日历页面导入

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/quadrant',  // 添加四象限路由
        name: 'Quadrant',
        component: Quadrant
    },
    {
        path: '/statistics',
        name: 'Statistics',
        component: Statistics
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/calendar',
        name: 'Calendar',
        component: Calendar
    }
]

const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})

export default router;