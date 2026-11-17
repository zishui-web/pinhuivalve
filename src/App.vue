<script>
// 全局滚动淡入（IntersectionObserver），对 .reveal 元素生效
export default {
  mounted() {
    if (typeof IntersectionObserver === 'undefined') {
      document.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'))
      return
    }
    this._io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('is-visible')
            this._io.unobserve(e.target)
          }
        })
      },
      { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
    )
    this.observeReveals()
    this._onRoute = () => {
      this.$nextTick(() => this.observeReveals())
    }
    this._removeHook = this.$router.afterEach(this._onRoute)
  },
  beforeUnmount() {
    this._io?.disconnect()
    this._removeHook?.()
  },
  methods: {
    observeReveals() {
      document.querySelectorAll('.reveal:not(.is-visible)').forEach((el) => this._io.observe(el))
    }
  }
}
</script>

<template>
  <SiteHeader />
  <main>
    <RouterView v-slot="{ Component }">
      <component :is="Component" />
    </RouterView>
  </main>
  <SiteFooter />
  <BackToTop />
</template>

<script setup>
import SiteHeader from './components/SiteHeader.vue'
import SiteFooter from './components/SiteFooter.vue'
import BackToTop from './components/BackToTop.vue'
</script>
