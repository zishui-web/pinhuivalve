<script setup>
import AppIcon from './AppIcon.vue'

defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  desc: { type: String, default: '' },
  crumbs: { type: Array, default: () => [] }
})
</script>

<template>
  <section class="phero">
    <div class="phero__bg"></div>
    <div class="container phero__inner">
      <nav v-if="crumbs.length" class="phero__crumbs">
        <RouterLink to="/">首页</RouterLink>
        <template v-for="c in crumbs" :key="c.label">
          <AppIcon name="chevron" :size="12" />
          <RouterLink v-if="c.to" :to="c.to">{{ c.label }}</RouterLink>
          <span v-else>{{ c.label }}</span>
        </template>
      </nav>
      <span v-if="eyebrow" class="eyebrow eyebrow--light">{{ eyebrow }}</span>
      <h1>{{ title }}</h1>
      <p v-if="desc">{{ desc }}</p>
    </div>
  </section>
</template>

<style scoped>
.phero {
  position: relative;
  background: var(--navy-900);
  overflow: hidden;
}

.phero__bg {
  position: absolute;
  inset: 0;
  background-image: url('/images/hero.jpg');
  background-size: cover;
  background-position: center 40%;
  opacity: 0.28;
  filter: saturate(0.7);
}

.phero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, rgba(6, 27, 48, 0.96) 0%, rgba(6, 27, 48, 0.78) 55%, rgba(10, 37, 64, 0.5) 100%);
}

.phero__inner {
  position: relative;
  z-index: 2;
  padding: 78px 32px 72px;
  color: #fff;
}

.phero__crumbs {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 26px;
}

.phero__crumbs a:hover {
  color: #fff;
}

.phero h1 {
  font-size: 38px;
  margin: 12px 0 14px;
  letter-spacing: 0.02em;
}

.phero p {
  max-width: 640px;
  font-size: 15px;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.68);
}

@media (max-width: 900px) {
  .phero__inner {
    padding: 54px 24px 48px;
  }
  .phero h1 {
    font-size: 28px;
  }
}

@media (max-width: 640px) {
  .phero__inner {
    padding: 40px 18px 38px;
  }
  .phero h1 {
    font-size: 23px;
  }
  .phero p {
    font-size: 14px;
  }
}
</style>
