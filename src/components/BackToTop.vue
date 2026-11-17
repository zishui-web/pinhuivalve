<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import AppIcon from './AppIcon.vue'

const show = ref(false)
const onScroll = () => (show.value = window.scrollY > 640)
onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
const toTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })
</script>

<template>
  <transition name="fade">
    <button v-if="show" class="to-top" aria-label="回到顶部" @click="toTop">
      <AppIcon name="chevron" :size="18" />
    </button>
  </transition>
</template>

<style scoped>
.to-top {
  position: fixed;
  right: 26px;
  bottom: 26px;
  z-index: 80;
  width: 44px;
  height: 44px;
  border: 1px solid var(--line);
  border-radius: 2px;
  background: #fff;
  color: var(--blue-600);
  display: grid;
  place-items: center;
  box-shadow: var(--shadow-sm);
  transform: rotate(-90deg);
}

.to-top:hover {
  background: var(--blue-600);
  color: #fff;
  border-color: var(--blue-600);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 640px) {
  .to-top {
    right: 14px;
    bottom: 14px;
    width: 40px;
    height: 40px;
  }
}
</style>
