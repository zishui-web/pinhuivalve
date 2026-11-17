<script setup>
import { company } from '../data/company'
import AppIcon from './AppIcon.vue'

const year = new Date().getFullYear()
const nav = [
  { to: '/', label: '首页' },
  { to: '/about', label: '关于我们' },
  { to: '/products', label: '产品中心' },
  { to: '/strength', label: '生产实力' },
  { to: '/support', label: '技术支持' },
  { to: '/contact', label: '联系我们' }
]
</script>

<template>
  <footer class="footer">
    <div class="container">
      <div class="footer__top">
        <div class="footer__brand">
          <img src="/images/logo-white.png" alt="品汇阀门" class="footer__logo" />
          <p class="footer__slogan">{{ company.slogan }}</p>
          <p class="footer__intro">{{ company.shortIntro }}</p>
        </div>

        <div class="footer__col">
          <h4>快速导航</h4>
          <RouterLink v-for="n in nav" :key="n.to" :to="n.to" class="footer__link">{{ n.label }}</RouterLink>
        </div>

        <div class="footer__col">
          <h4>产品系列</h4>
          <RouterLink to="/products?c=knife" class="footer__link">刀型闸阀系列</RouterLink>
          <RouterLink to="/products?c=slurry" class="footer__link">浆液阀系列</RouterLink>
          <RouterLink to="/products?c=penetrating" class="footer__link">穿透式插板阀</RouterLink>
          <RouterLink to="/products?c=ceramic" class="footer__link">陶瓷阀门系列</RouterLink>
          <RouterLink to="/products?c=square" class="footer__link">方形闸阀</RouterLink>
          <RouterLink to="/products?c=gate" class="footer__link">闸门系列</RouterLink>
        </div>

        <div class="footer__col footer__col--contact">
          <h4>联系我们</h4>
          <a v-for="c in company.contacts" :key="c.phone" class="footer__contact" :href="`tel:${c.phone}`">
            <AppIcon name="phone" :size="16" />
            <span>{{ c.name }} {{ c.phone }}</span>
          </a>
          <p class="footer__contact">
            <AppIcon name="pin" :size="16" />
            <span>{{ company.address }}</span>
          </p>
        </div>

        <div class="footer__qr">
          <div v-for="w in company.wechats" :key="w.image" class="footer__qr-item">
            <img :src="w.image" :alt="w.label" />
            <span>{{ w.label }}</span>
          </div>
        </div>
      </div>

      <div class="footer__bottom">
        <p>© {{ year }} {{ company.name }}　版权所有</p>
        <p class="footer__meta">
          <span>{{ company.brandEn }}</span>
          <span class="dot">·</span>
          <span>{{ company.addressNote }}</span>
          <span class="dot">·</span>
          <span>产品参数以合同与技术确认图为准</span>
        </p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--navy-900);
  color: rgba(255, 255, 255, 0.68);
  padding: 66px 0 26px;
  font-size: 14px;
}

.footer__top {
  display: grid;
  grid-template-columns: 1.5fr 0.8fr 0.9fr 1.2fr auto;
  gap: 44px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.footer__logo {
  height: 44px;
  width: auto;
  margin-bottom: 18px;
}

.footer__slogan {
  color: #fff;
  font-size: 15px;
  letter-spacing: 0.14em;
  margin-bottom: 12px;
}

.footer__intro {
  font-size: 13px;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.5);
  max-width: 340px;
}

.footer__col h4 {
  color: #fff;
  font-size: 15px;
  margin-bottom: 18px;
  font-weight: 600;
}

.footer__link {
  display: block;
  padding: 6px 0;
  font-size: 13.5px;
  color: rgba(255, 255, 255, 0.62);
  transition: color 0.2s var(--ease);
}

.footer__link:hover {
  color: #fff;
}

.footer__contact {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  padding: 6px 0;
  font-size: 13.5px;
  color: rgba(255, 255, 255, 0.68);
  line-height: 1.7;
}

.footer__contact :deep(svg) {
  flex: none;
  margin-top: 4px;
  color: var(--blue-400);
}

.footer__qr {
  display: flex;
  gap: 14px;
}

.footer__qr-item {
  text-align: center;
}

.footer__qr-item img {
  width: 96px;
  height: 128px;
  object-fit: contain;
  background: #fff;
  padding: 4px;
  border-radius: 2px;
}

.footer__qr-item span {
  display: block;
  margin-top: 8px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.55);
}

.footer__bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  padding-top: 22px;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.45);
  flex-wrap: wrap;
}

.footer__meta {
  display: flex;
  align-items: center;
  gap: 8px;
}

.dot {
  opacity: 0.4;
}

@media (max-width: 1080px) {
  .footer__top {
    grid-template-columns: 1fr 1fr;
    gap: 36px;
  }
  .footer__qr {
    grid-column: 1 / -1;
  }
}

@media (max-width: 640px) {
  .footer {
    padding: 46px 0 22px;
  }
  .footer__top {
    grid-template-columns: 1fr;
    gap: 28px;
    padding-bottom: 30px;
  }
  .footer__bottom {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  .footer__meta {
    flex-wrap: wrap;
  }
}
</style>
