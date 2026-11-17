<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import AppIcon from './AppIcon.vue'
import { company } from '../data/company'

const route = useRoute()
const open = ref(false)
const scrolled = ref(false)

const nav = [
  { to: '/', label: '首页' },
  { to: '/about', label: '关于我们' },
  { to: '/products', label: '产品中心' },
  { to: '/strength', label: '生产实力' },
  { to: '/support', label: '技术支持' },
  { to: '/contact', label: '联系我们' }
]

watch(
  () => route.fullPath,
  () => {
    open.value = false
  }
)

if (typeof window !== 'undefined') {
  window.addEventListener('scroll', () => {
    scrolled.value = window.scrollY > 12
  })
}

const isActive = (to) =>
  to === '/' ? route.path === '/' : route.path === to || route.path.startsWith(to + '/')
</script>

<template>
  <header class="header" :class="{ 'header--scrolled': scrolled }">
    <div class="container header__inner">
      <RouterLink to="/" class="header__logo" aria-label="品汇阀门首页">
        <img src="/images/logo.png" alt="品汇阀门 PINHUI VALVE" />
      </RouterLink>

      <nav class="header__nav">
        <RouterLink
          v-for="item in nav"
          :key="item.to"
          :to="item.to"
          class="header__link"
          :class="{ 'is-active': isActive(item.to) }"
        >
          {{ item.label }}
        </RouterLink>
      </nav>

      <div class="header__right">
        <a class="header__phone" :href="`tel:${company.contacts[0].phone}`">
          <AppIcon name="phone" :size="18" />
          <span>{{ company.contacts[0].phone }}</span>
        </a>
        <RouterLink to="/contact" class="btn btn--primary btn--sm header__cta">
          在线咨询
          <AppIcon name="arrow" :size="16" />
        </RouterLink>
        <button class="header__burger" :aria-expanded="open" aria-label="打开菜单" @click="open = !open">
          <AppIcon :name="open ? 'close' : 'menu'" :size="24" />
        </button>
      </div>
    </div>

    <transition name="drawer">
      <div v-if="open" class="drawer">
        <nav class="drawer__nav">
          <RouterLink v-for="item in nav" :key="item.to" :to="item.to" class="drawer__link">
            {{ item.label }}
          </RouterLink>
        </nav>
        <div class="drawer__foot">
          <a :href="`tel:${company.contacts[0].phone}`" class="drawer__phone">
            <AppIcon name="phone" :size="18" />
            {{ company.contacts[0].phone }} · {{ company.contacts[0].name }}
          </a>
          <p>{{ company.address }}</p>
        </div>
      </div>
    </transition>
  </header>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 90;
  background: #fff;
  border-bottom: 1px solid var(--line-2);
  transition: box-shadow 0.3s var(--ease);
}

.header--scrolled {
  box-shadow: 0 6px 24px rgba(10, 37, 64, 0.07);
}

.header__inner {
  height: var(--header-h);
  display: flex;
  align-items: center;
  gap: 36px;
}

.header__logo img {
  height: 42px;
  width: auto;
}

.header__nav {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-left: auto;
}

.header__link {
  position: relative;
  padding: 0 18px;
  height: var(--header-h);
  display: inline-flex;
  align-items: center;
  font-size: 15px;
  font-weight: 500;
  color: var(--ink-2);
  transition: color 0.2s var(--ease);
}

.header__link::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translateX(-50%) scaleX(0);
  width: 26px;
  height: 2px;
  background: var(--blue-600);
  transition: transform 0.25s var(--ease);
}

.header__link:hover {
  color: var(--blue-600);
}

.header__link.is-active {
  color: var(--blue-600);
  font-weight: 600;
}

.header__link.is-active::after {
  transform: translateX(-50%) scaleX(1);
}

.header__right {
  display: flex;
  align-items: center;
  gap: 18px;
  padding-left: 12px;
}

.header__phone {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 15px;
  font-weight: 600;
  color: var(--navy-800);
  letter-spacing: 0.02em;
}

.header__phone :deep(svg) {
  color: var(--blue-600);
}

.header__burger {
  display: none;
  border: 0;
  background: none;
  color: var(--navy-800);
  padding: 6px;
}

.drawer {
  position: absolute;
  left: 0;
  right: 0;
  top: var(--header-h);
  background: #fff;
  border-bottom: 1px solid var(--line);
  box-shadow: var(--shadow-md);
  padding: 8px 18px 22px;
}

.drawer__nav {
  display: flex;
  flex-direction: column;
}

.drawer__link {
  padding: 13px 4px;
  border-bottom: 1px solid var(--line-2);
  font-size: 16px;
  font-weight: 500;
}

.drawer__foot {
  margin-top: 18px;
  font-size: 13px;
  color: var(--muted);
  line-height: 1.9;
}

.drawer__phone {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--blue-600);
  font-weight: 600;
  font-size: 15px;
}

.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.22s var(--ease), transform 0.22s var(--ease);
}

.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}

@media (max-width: 1180px) {
  .header__nav {
    gap: 0;
  }
  .header__link {
    padding: 0 12px;
    font-size: 14.5px;
  }
  .header__phone span {
    display: none;
  }
}

@media (max-width: 980px) {
  .header__nav {
    display: none;
  }
  .header__burger {
    display: inline-flex;
  }
  .header__right {
    margin-left: auto;
    gap: 12px;
  }
  .header__cta {
    display: none;
  }
  .header__logo img {
    height: 36px;
  }
}

@media (max-width: 400px) {
  .header__phone {
    display: none;
  }
}
</style>
