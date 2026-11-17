<script setup>
import { company } from '../data/company'
import AppIcon from './AppIcon.vue'

const props = defineProps({
  title: { type: String, default: '以品质为基础，以专业赢得信赖' },
  desc: { type: String, default: '致力于为客户提供更优质的阀门产品与服务' }
})
const products = [
  '/images/p-pz73.png',
  '/images/p-slurry.png',
  '/images/p-scz673.png',
  '/images/p-ceramic-knife.png',
  '/images/p-lmd.png'
]
</script>

<template>
  <section class="ctaband">
    <div class="container ctaband__inner">
      <div class="ctaband__text">
        <h2>{{ title }}</h2>
        <p>{{ desc }}</p>
        <div class="ctaband__actions">
          <RouterLink to="/products" class="btn btn--primary">
            浏览全部产品
            <AppIcon name="arrow" :size="17" />
          </RouterLink>
          <a :href="`tel:${company.contacts[0].phone}`" class="btn btn--ghost">
            <AppIcon name="phone" :size="17" />
            {{ company.contacts[0].phone }}
          </a>
        </div>
      </div>
      <div class="ctaband__art">
        <img v-for="(p, i) in products" :key="p" :src="p" :alt="`品汇产品 ${i + 1}`" loading="lazy" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.ctaband {
  position: relative;
  background: linear-gradient(100deg, #0a2540 0%, #10365c 58%, #164a7c 100%);
  overflow: hidden;
}

.ctaband::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 82% 30%, rgba(60, 138, 214, 0.35), transparent 58%);
}

.ctaband__inner {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
  padding: 58px 32px;
}

.ctaband__text h2 {
  color: #fff;
  font-size: 30px;
  margin-bottom: 12px;
}

.ctaband__text p {
  color: rgba(255, 255, 255, 0.62);
  font-size: 15px;
}

.ctaband__actions {
  display: flex;
  gap: 14px;
  margin-top: 28px;
  flex-wrap: wrap;
}

.ctaband__art {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  gap: 6px;
}

.ctaband__art img {
  height: 210px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 18px 30px rgba(0, 0, 0, 0.35));
}

.ctaband__art img:nth-child(even) {
  height: 178px;
  opacity: 0.9;
}

@media (max-width: 980px) {
  .ctaband__inner {
    grid-template-columns: 1fr;
    gap: 22px;
    padding: 46px 24px;
  }
  .ctaband__art {
    justify-content: flex-start;
    flex-wrap: wrap;
  }
  .ctaband__art img {
    height: 140px;
  }
}

@media (max-width: 640px) {
  .ctaband__text h2 {
    font-size: 22px;
  }
  .ctaband__art img {
    height: 104px;
  }
  .ctaband__art img:nth-child(even) {
    height: 90px;
  }
}
</style>
