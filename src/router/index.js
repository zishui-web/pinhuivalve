import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue'), meta: { title: '首页' } },
  {
    path: '/products',
    name: 'products',
    component: () => import('../views/ProductsView.vue'),
    meta: { title: '产品中心' }
  },
  {
    path: '/products/:slug',
    name: 'product-detail',
    component: () => import('../views/ProductDetailView.vue'),
    meta: { title: '产品详情' }
  },
  { path: '/about', name: 'about', component: () => import('../views/AboutView.vue'), meta: { title: '关于我们' } },
  {
    path: '/strength',
    name: 'strength',
    component: () => import('../views/StrengthView.vue'),
    meta: { title: '生产实力' }
  },
  { path: '/support', name: 'support', component: () => import('../views/SupportView.vue'), meta: { title: '技术支持' } },
  { path: '/contact', name: 'contact', component: () => import('../views/ContactView.vue'), meta: { title: '联系我们' } },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: () => import('../views/NotFoundView.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, top: 96, behavior: 'smooth' }
    return { top: 0 }
  }
})

const BASE = '浙江品汇阀门有限公司'
router.afterEach((to) => {
  const t = to.meta?.title
  document.title = t ? `${t} · ${BASE}` : BASE
})

export default router
