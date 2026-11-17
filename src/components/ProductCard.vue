<script setup>
import AppIcon from './AppIcon.vue'

defineProps({
  product: { type: Object, required: true },
  categoryName: { type: String, default: '' }
})
</script>

<template>
  <RouterLink :to="`/products/${product.slug}`" class="pcard">
    <div class="pcard__media">
      <img :src="product.image" :alt="product.name" loading="lazy" />
    </div>
    <div class="pcard__body">
      <span class="pcard__model">{{ product.model }}</span>
      <h3 class="pcard__name">{{ product.name }}</h3>
      <span class="pcard__en">{{ product.nameEn }}</span>
      <p class="pcard__desc">{{ product.tagline }}</p>
      <span class="pcard__link">
        查看详情
        <AppIcon name="arrow" :size="15" />
      </span>
    </div>
  </RouterLink>
</template>

<style scoped>
.pcard {
  display: flex;
  flex-direction: column;
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  overflow: hidden;
  transition: all 0.32s var(--ease);
}

.pcard:hover {
  border-color: rgba(30, 111, 191, 0.35);
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}

.pcard__media {
  position: relative;
  height: 236px;
  background: linear-gradient(160deg, #f7f9fc 0%, #eef2f7 100%);
  display: grid;
  place-items: center;
  padding: 22px;
  overflow: hidden;
}

.pcard__media::after {
  content: '';
  position: absolute;
  inset: auto 0 0 0;
  height: 1px;
  background: var(--line-2);
}

.pcard__media img {
  position: absolute;
  inset: 22px;
  width: calc(100% - 44px);
  height: calc(100% - 44px);
  object-fit: contain;
  transition: transform 0.5s var(--ease);
}

.pcard:hover .pcard__media img {
  transform: scale(1.05) translateY(-2px);
}

.pcard__body {
  padding: 22px 22px 24px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.pcard__model {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: var(--blue-500);
  text-transform: uppercase;
}

.pcard__name {
  font-size: 17px;
  margin: 7px 0 3px;
  color: var(--ink);
}

.pcard__en {
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--muted-2);
}

.pcard__desc {
  margin: 12px 0 18px;
  font-size: 13px;
  line-height: 1.75;
  color: var(--muted);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.pcard__link {
  margin-top: auto;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--blue-600);
}

.pcard__link :deep(svg) {
  transition: transform 0.3s var(--ease);
}

.pcard:hover .pcard__link :deep(svg) {
  transform: translateX(5px);
}

@media (max-width: 640px) {
  .pcard__media {
    height: 200px;
  }
}
</style>
