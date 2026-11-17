<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { products, categories } from '../data/products'
import { company } from '../data/company'
import DataTable from '../components/DataTable.vue'
import AppIcon from '../components/AppIcon.vue'
import CtaBand from '../components/CtaBand.vue'

const route = useRoute()
const product = computed(() => products.find((p) => p.slug === route.params.slug))
const category = computed(() => categories.find((c) => c.id === product.value?.category))
const activeImg = ref(0)

watch(product, () => {
  activeImg.value = 0
})

const gallery = computed(() => (product.value ? [product.value.image, ...(product.value.gallery || [])] : []))

const related = computed(() => {
  if (!product.value) return []
  const same = products.filter((p) => p.category === product.value.category && p.slug !== product.value.slug)
  const others = products.filter((p) => p.category !== product.value.category && p.slug !== product.value.slug)
  return [...same, ...others].slice(0, 3)
})

const scrolled = ref(false)
const onScroll = () => {
  if (typeof window === 'undefined') return
  scrolled.value = window.scrollY > 520
}

if (typeof window !== 'undefined') {
  window.addEventListener('scroll', onScroll, { passive: true })
}

const go = (id) => {
  const el = document.getElementById(id)
  if (el) window.scrollTo({ top: el.offsetTop - 150, behavior: 'smooth' })
}

const has = (k) => Boolean(product.value?.[k])

const sectionOrder = computed(() => {
  const list = ['features']
  if (product.value?.principle) list.push('principle')
  list.push('specs')
  if (product.value?.materials) list.push('materials')
  if (product.value?.dimensions?.length) list.push('dimensions')
  if (product.value?.modelRule) list.push('model-rule')
  list.push('order')
  return list
})
const no = (k) => String(sectionOrder.value.indexOf(k) + 1).padStart(2, '0')
</script>

<template>
  <div v-if="product">
    <!-- 面包屑 -->
    <div class="crumb">
      <div class="container crumb__inner">
        <RouterLink to="/">首页</RouterLink>
        <AppIcon name="chevron" :size="12" />
        <RouterLink to="/products">产品中心</RouterLink>
        <AppIcon name="chevron" :size="12" />
        <RouterLink :to="`/products?c=${product.category}`">{{ category?.name }}</RouterLink>
        <AppIcon name="chevron" :size="12" />
        <span>{{ product.name }}</span>
      </div>
    </div>

    <!-- 产品头部 -->
    <section class="pd-top">
      <div class="container pd-top__inner">
        <div class="gallery">
          <div class="gallery__main">
            <img :src="gallery[activeImg]" :alt="product.name" />
            <span class="gallery__cat">{{ category?.name }}</span>
          </div>
          <div v-if="gallery.length > 1" class="gallery__thumbs">
            <button
              v-for="(g, i) in gallery"
              :key="g"
              class="gallery__thumb"
              :class="{ 'is-on': i === activeImg }"
              @click="activeImg = i"
            >
              <img :src="g" :alt="`${product.name} 图 ${i + 1}`" />
            </button>
          </div>
        </div>

        <div class="info">
          <span class="badge">{{ category?.name }}</span>
          <span class="info__model">{{ product.model }}</span>
          <h1>{{ product.name }}</h1>
          <p class="info__en">{{ product.nameEn }}</p>
          <p class="info__tagline">{{ product.tagline }}</p>
          <p class="info__summary">{{ product.summary }}</p>

          <ul class="info__specs">
            <li v-for="s in product.specs.slice(0, 4)" :key="s[0]">
              <span>{{ s[0] }}</span>
              <strong>{{ s[1] }}</strong>
            </li>
          </ul>

          <div class="info__drives">
            <span class="info__label">驱动形式</span>
            <div class="chips">
              <span v-for="d in product.drives" :key="d.name" class="chip">{{ d.name }}</span>
            </div>
          </div>

          <div class="info__actions">
            <a :href="`tel:${company.contacts[0].phone}`" class="btn btn--primary">
              <AppIcon name="phone" :size="17" />
              电话咨询 {{ company.contacts[0].phone }}
            </a>
            <RouterLink to="/contact" class="btn btn--outline">获取报价单</RouterLink>
          </div>
        </div>
      </div>
    </section>

    <!-- 锚点导航 -->
    <div class="anchor-nav" :class="{ 'is-fixed': scrolled }">
      <div class="container anchor-nav__inner">
        <button @click="go('features')">产品特点</button>
        <button @click="go('specs')">技术参数</button>
        <button v-if="has('materials')" @click="go('materials')">零部件材质</button>
        <button v-if="product.dimensions.length" @click="go('dimensions')">外形及连接尺寸</button>
        <button v-if="has('principle')" @click="go('principle')">工作原理</button>
        <button v-if="has('modelRule')" @click="go('model-rule')">型号编制</button>
        <button @click="go('order')">订货说明</button>
      </div>
    </div>

    <section class="section pd-body">
      <div class="container pd-body__inner">
        <div class="pd-main">
          <!-- 产品特点 -->
          <div id="features" class="block">
            <h2 class="block__title"><span>{{ no('features') }}</span>产品特点</h2>
            <div v-if="product.intro?.length" class="intro">
              <p v-for="(p, i) in product.intro" :key="i">{{ p }}</p>
            </div>
            <ul class="features">
              <li v-for="f in product.features" :key="f">
                <AppIcon name="check" :size="16" />
                <span>{{ f }}</span>
              </li>
            </ul>
          </div>

          <!-- 工作原理 -->
          <div v-if="product.principle" id="principle" class="block">
            <h2 class="block__title"><span>{{ no('principle') }}</span>工作原理</h2>
            <p class="plain">{{ product.principle }}</p>
          </div>

          <!-- 技术参数 -->
          <div id="specs" class="block">
            <h2 class="block__title"><span>{{ no('specs') }}</span>技术参数</h2>
            <div class="speclist">
              <div v-for="s in product.specs" :key="s[0]" class="speclist__row">
                <span>{{ s[0] }}</span>
                <p>{{ s[1] }}</p>
              </div>
            </div>
            <div v-if="product.performance" class="sub">
              <h3 class="sub__title">主要性能规范</h3>
              <DataTable :table="{ columns: product.performance.columns, rows: product.performance.rows }" />
            </div>
          </div>

          <!-- 零部件材质 -->
          <div v-if="product.materials" id="materials" class="block">
            <h2 class="block__title"><span>{{ no('materials') }}</span>主要零部件材质</h2>
            <DataTable :table="{ columns: product.materials.columns, rows: product.materials.rows }" />
          </div>

          <!-- 外形尺寸 -->
          <div v-if="product.dimensions.length" id="dimensions" class="block">
            <h2 class="block__title"><span>{{ no('dimensions') }}</span>主要外形及连接尺寸</h2>
            <DataTable v-for="d in product.dimensions" :key="d.title" :table="d" />
            <p class="sub__note">
              本表按产品样本册原表录入。样本册中产品尺寸表与附录法兰尺寸表在个别规格的密封面直径、螺纹规格上存在差异，
              订货请以本表及双方确认图为准。
            </p>
          </div>

          <!-- 型号编制 -->
          <div v-if="product.modelRule" id="model-rule" class="block">
            <h2 class="block__title"><span>{{ no('model-rule') }}</span>{{ product.modelRule.title }}</h2>
            <div class="rule">
              <div v-for="(r, i) in product.modelRule.parts" :key="r.name" class="rule__item">
                <span class="rule__no">{{ i + 1 }}</span>
                <div>
                  <strong>{{ r.name }}</strong>
                  <p>{{ r.options }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 订货说明 -->
          <div id="order" class="block">
            <h2 class="block__title"><span>{{ no('order') }}</span>订货说明</h2>
            <ul class="notes">
              <li v-for="n in product.notes" :key="n">{{ n }}</li>
            </ul>
            <div class="order-box">
              <h4>订货请提供以下信息</h4>
              <div class="order-box__grid">
                <span>产品型号 / 名称</span>
                <span>公称通径 DN</span>
                <span>公称压力 PN</span>
                <span>阀体材质</span>
                <span>密封面材质</span>
                <span>驱动形式与电源/气源</span>
                <span>介质名称、浓度、温度</span>
                <span>管路法兰标准</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 侧栏 -->
        <aside class="pd-side">
          <div class="side-card">
            <h4>获取选型支持</h4>
            <p>提供介质与工况参数，我们协助确认型号、材质与执行机构。</p>
            <a v-for="c in company.contacts" :key="c.phone" class="side-card__phone" :href="`tel:${c.phone}`">
              <AppIcon name="phone" :size="17" />
              <span>{{ c.name }}<em>{{ c.phone }}</em></span>
            </a>
            <RouterLink to="/contact" class="btn btn--primary btn--sm side-card__btn">在线留言</RouterLink>
          </div>

          <div class="side-card side-card--plain">
            <h4>相关资料</h4>
            <RouterLink to="/support#seat" class="side-link">
              阀座结构说明 <AppIcon name="chevron" :size="13" />
            </RouterLink>
            <RouterLink to="/support#flange" class="side-link">
              法兰安装尺寸 <AppIcon name="chevron" :size="13" />
            </RouterLink>
            <RouterLink to="/support#install" class="side-link">
              使用注意事项 <AppIcon name="chevron" :size="13" />
            </RouterLink>
            <RouterLink to="/support#maintenance" class="side-link">
              预防措施 <AppIcon name="chevron" :size="13" />
            </RouterLink>
          </div>

          <div class="side-card side-card--plain">
            <h4>相关产品</h4>
            <RouterLink v-for="r in related" :key="r.slug" :to="`/products/${r.slug}`" class="side-prod">
              <img :src="r.image" :alt="r.name" loading="lazy" />
              <div>
                <strong>{{ r.name }}</strong>
                <span>{{ r.model }}</span>
              </div>
            </RouterLink>
          </div>
        </aside>
      </div>
    </section>

    <CtaBand
      title="需要该型号的详细图纸或报价？"
      desc="告诉我们通径、压力与介质，我们会提供选型建议与正式报价"
    />
  </div>

  <div v-else class="nf">
    <div class="container">
      <h1>未找到该产品</h1>
      <p>产品可能已更名或下架，请返回产品中心查看全部系列。</p>
      <RouterLink to="/products" class="btn btn--primary">返回产品中心</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.crumb {
  border-bottom: 1px solid var(--line-2);
  background: #fff;
}

.crumb__inner {
  display: flex;
  align-items: center;
  gap: 8px;
  height: 52px;
  font-size: 12.5px;
  color: var(--muted);
  overflow: hidden;
  white-space: nowrap;
}

.crumb__inner a:hover {
  color: var(--blue-600);
}

.crumb__inner span {
  color: var(--ink-2);
}

/* ---------- top ---------- */
.pd-top {
  background: linear-gradient(180deg, #f7fafd 0%, #ffffff 100%);
  border-bottom: 1px solid var(--line-2);
}

.pd-top__inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 58px;
  padding: 44px 32px 48px;
  align-items: start;
}

.gallery__main {
  position: relative;
  height: 430px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  display: grid;
  place-items: center;
  padding: 28px;
}

.gallery__main img {
  position: absolute;
  inset: 28px;
  width: calc(100% - 56px);
  height: calc(100% - 56px);
  object-fit: contain;
}

.gallery__cat {
  position: absolute;
  left: 16px;
  top: 16px;
  font-size: 11px;
  letter-spacing: 0.1em;
  color: var(--blue-600);
  background: var(--blue-100);
  padding: 5px 12px;
  border-radius: 100px;
}

.gallery__thumbs {
  display: flex;
  gap: 10px;
  margin-top: 12px;
}

.gallery__thumb {
  position: relative;
  width: 78px;
  height: 78px;
  border: 1px solid var(--line);
  border-radius: 2px;
  background: #fff;
  padding: 6px;
  display: grid;
  place-items: center;
  transition: border-color 0.2s var(--ease);
}

.gallery__thumb img {
  position: absolute;
  inset: 7px;
  width: calc(100% - 14px);
  height: calc(100% - 14px);
  object-fit: contain;
}

.gallery__thumb.is-on {
  border-color: var(--blue-600);
  box-shadow: 0 0 0 1px var(--blue-600) inset;
}

.info__model {
  display: inline-block;
  margin-left: 10px;
  font-family: 'SF Mono', Menlo, monospace;
  font-size: 12.5px;
  color: var(--blue-700);
  background: #fff;
  border: 1px solid var(--line);
  padding: 2px 10px;
  border-radius: 2px;
  vertical-align: 6px;
}

.info h1 {
  font-size: 33px;
  margin: 12px 0 4px;
}

.info__en {
  font-size: 11px;
  letter-spacing: 0.16em;
  color: var(--muted-2);
}

.info__tagline {
  margin-top: 18px;
  font-size: 16px;
  color: var(--blue-700);
  font-weight: 600;
}

.info__summary {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.95;
  color: var(--muted);
}

.info__specs {
  margin: 24px 0 18px;
  border-top: 1px solid var(--line);
}

.info__specs li {
  display: grid;
  grid-template-columns: 108px 1fr;
  gap: 14px;
  padding: 10px 0;
  border-bottom: 1px dashed var(--line);
  font-size: 13.5px;
}

.info__specs span {
  color: var(--muted);
}

.info__specs strong {
  font-weight: 500;
  color: var(--ink);
  line-height: 1.7;
}

.info__drives {
  margin-bottom: 26px;
}

.info__label {
  display: block;
  font-size: 12.5px;
  color: var(--muted);
  margin-bottom: 9px;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.chip {
  font-size: 12.5px;
  padding: 4px 12px;
  border: 1px solid var(--line);
  border-radius: 100px;
  background: #fff;
  color: var(--ink-2);
}

.info__actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

/* ---------- anchor nav ---------- */
.anchor-nav {
  background: #fff;
  border-bottom: 1px solid var(--line);
}

.anchor-nav.is-fixed {
  position: sticky;
  top: var(--header-h);
  z-index: 40;
  box-shadow: 0 4px 16px rgba(10, 37, 64, 0.06);
}

.anchor-nav__inner {
  display: flex;
  gap: 30px;
  height: 54px;
  overflow-x: auto;
}

.anchor-nav button {
  border: 0;
  background: none;
  font-size: 14px;
  color: var(--ink-2);
  white-space: nowrap;
  position: relative;
  padding: 0;
}

.anchor-nav button:hover {
  color: var(--blue-600);
}

.anchor-nav button::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  background: var(--blue-600);
  transform: scaleX(0);
  transition: transform 0.25s var(--ease);
}

.anchor-nav button:hover::after {
  transform: scaleX(1);
}

/* ---------- body ---------- */
.pd-body__inner {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 306px;
  gap: 56px;
  align-items: start;
}

.pd-main {
  min-width: 0;
}

.block + .block {
  margin-top: 54px;
  padding-top: 50px;
  border-top: 1px solid var(--line-2);
}

.block__title {
  display: flex;
  align-items: baseline;
  gap: 12px;
  font-size: 22px;
  margin-bottom: 22px;
}

.block__title span {
  font-family: 'SF Mono', Menlo, monospace;
  font-size: 12px;
  color: var(--blue-500);
  letter-spacing: 0.06em;
}

.intro p {
  font-size: 14.5px;
  line-height: 2.05;
  color: var(--ink-2);
  margin-bottom: 14px;
}

.features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 26px;
  margin-top: 22px;
}

.features li {
  display: flex;
  gap: 10px;
  font-size: 13.5px;
  line-height: 1.85;
  color: var(--ink-2);
  padding: 12px 0;
  border-top: 1px dashed var(--line);
}

.features li :deep(svg) {
  flex: none;
  margin-top: 5px;
  color: var(--blue-600);
}

.plain {
  font-size: 14.5px;
  line-height: 2;
  color: var(--ink-2);
  padding: 18px 22px;
  background: var(--bg-soft);
  border-left: 3px solid var(--blue-600);
}

.speclist {
  border-top: 1px solid var(--line);
}

.speclist__row {
  display: grid;
  grid-template-columns: 150px 1fr;
  gap: 20px;
  padding: 14px 4px;
  border-bottom: 1px solid var(--line-2);
}

.speclist__row > span {
  font-size: 13.5px;
  color: var(--muted);
}

.speclist__row p {
  font-size: 14px;
  color: var(--ink);
  line-height: 1.8;
}

.sub {
  margin-top: 34px;
}

.sub__title {
  font-size: 15.5px;
  margin-bottom: 14px;
}

.sub__note {
  margin-top: 16px;
  font-size: 12.5px;
  line-height: 1.9;
  color: var(--muted-2);
}

.rule {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.rule__item {
  display: flex;
  gap: 14px;
  padding: 18px 20px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
}

.rule__no {
  width: 26px;
  height: 26px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--blue-100);
  color: var(--blue-700);
  font-size: 12px;
  font-weight: 700;
}

.rule__item strong {
  font-size: 14px;
  display: block;
  margin-bottom: 4px;
}

.rule__item p {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.8;
}

.notes li {
  position: relative;
  padding-left: 16px;
  margin-bottom: 10px;
  font-size: 13.5px;
  line-height: 1.9;
  color: var(--ink-2);
}

.notes li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 11px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--blue-500);
}

.order-box {
  margin-top: 26px;
  padding: 24px 26px;
  background: var(--bg-soft);
  border-radius: var(--radius);
}

.order-box h4 {
  font-size: 14.5px;
  margin-bottom: 14px;
}

.order-box__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px 20px;
  font-size: 13px;
  color: var(--muted);
}

.order-box__grid span::before {
  content: '·';
  color: var(--blue-500);
  margin-right: 7px;
  font-weight: 700;
}

/* ---------- side ---------- */
.pd-side {
  position: sticky;
  top: calc(var(--header-h) + 70px);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.side-card {
  background: var(--navy-800);
  color: #fff;
  padding: 24px 22px;
  border-radius: var(--radius);
}

.side-card h4 {
  font-size: 15px;
  margin-bottom: 10px;
}

.side-card > p {
  font-size: 12.5px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.55);
  margin-bottom: 16px;
}

.side-card--plain {
  background: #fff;
  border: 1px solid var(--line-2);
  color: var(--ink);
}

.side-card--plain h4 {
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line-2);
  margin-bottom: 6px;
}

.side-card__phone {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 0;
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.7);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.side-card__phone :deep(svg) {
  color: #6fa8dc;
}

.side-card__phone em {
  display: block;
  font-style: normal;
  font-size: 15px;
  font-weight: 600;
  color: #fff;
  letter-spacing: 0.02em;
}

.side-card__btn {
  width: 100%;
  margin-top: 16px;
}

.side-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 13px;
  color: var(--ink-2);
  border-bottom: 1px dashed var(--line-2);
}

.side-link:last-child {
  border-bottom: 0;
}

.side-link:hover {
  color: var(--blue-600);
}

.side-prod {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px dashed var(--line-2);
}

.side-prod:last-child {
  border-bottom: 0;
}

.side-prod img {
  width: 54px;
  height: 66px;
  object-fit: contain;
  flex: none;
}

.side-prod strong {
  display: block;
  font-size: 13px;
  line-height: 1.5;
}

.side-prod span {
  font-size: 11px;
  color: var(--muted-2);
  font-family: 'SF Mono', Menlo, monospace;
}

.side-prod:hover strong {
  color: var(--blue-600);
}

.nf {
  padding: 120px 0;
  text-align: center;
}

.nf h1 {
  font-size: 26px;
  margin-bottom: 12px;
}

.nf p {
  color: var(--muted);
  margin-bottom: 24px;
}

/* ---------- responsive ---------- */
@media (max-width: 1080px) {
  .pd-top__inner {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .gallery__main {
    height: 340px;
  }
  .pd-body__inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .pd-side {
    position: static;
    flex-direction: row;
    flex-wrap: wrap;
  }
  .pd-side .side-card {
    flex: 1 1 260px;
  }
}

@media (max-width: 640px) {
  .pd-top__inner {
    padding: 26px 18px 32px;
  }
  .info h1 {
    font-size: 24px;
  }
  .gallery__main {
    height: 270px;
    padding: 18px;
  }
  .info__specs li {
    grid-template-columns: 88px 1fr;
  }
  .features {
    grid-template-columns: 1fr;
  }
  .speclist__row {
    grid-template-columns: 96px 1fr;
    gap: 12px;
  }
  .rule {
    grid-template-columns: 1fr;
  }
  .order-box__grid {
    grid-template-columns: 1fr;
  }
  .anchor-nav__inner {
    gap: 20px;
    height: 50px;
  }
  .block__title {
    font-size: 19px;
  }
}
</style>
