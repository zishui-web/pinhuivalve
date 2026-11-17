<script setup>
defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, required: true },
  desc: { type: String, default: '' },
  align: { type: String, default: 'center' },
  light: { type: Boolean, default: false }
})
</script>

<template>
  <div class="section-head" :class="{ 'section-head--left': align === 'left' }">
    <span v-if="eyebrow" class="eyebrow" :class="{ 'eyebrow--light': light }">{{ eyebrow }}</span>
    <div class="section-head__title-wrap">
      <h2 class="section-title" :class="{ 'section-title--light': light }">{{ title }}</h2>
    </div>
    <p v-if="desc" class="section-head__desc" :style="light ? 'color: rgba(255,255,255,.62)' : ''">{{ desc }}</p>
  </div>
</template>
