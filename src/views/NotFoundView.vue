<script setup>
import PageHero from '../components/PageHero.vue'
</script>

<template>
  <div>
    <PageHero eyebrow="404" title="页面不存在" desc="链接可能已失效，或产品已更名。请返回首页或前往产品中心。" />
    <section class="section">
      <div class="container nf">
        <RouterLink to="/" class="btn btn--primary">返回首页</RouterLink>
        <RouterLink to="/products" class="btn btn--outline">产品中心</RouterLink>
        <RouterLink to="/contact" class="btn btn--outline">联系我们</RouterLink>
      </div>
    </section>
  </div>
</template>

<style scoped>
.nf {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 48px 0 96px;
}
</style>
