<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { products, categories, modelGroups } from '../data/products'
import PageHero from '../components/PageHero.vue'
import SectionHead from '../components/SectionHead.vue'
import ProductCard from '../components/ProductCard.vue'
import CtaBand from '../components/CtaBand.vue'

const route = useRoute()
const router = useRouter()
const active = ref(route.query.c || 'all')

watch(
  () => route.query.c,
  (c) => {
    active.value = c || 'all'
  }
)

const setActive = (id) => {
  active.value = id
  router.replace({ query: id === 'all' ? {} : { c: id } })
}

const list = computed(() => (active.value === 'all' ? products : products.filter((p) => p.category === active.value)))

const countOf = (id) => (id === 'all' ? products.length : products.filter((p) => p.category === id).length)

const activeCat = computed(() => categories.find((c) => c.id === active.value))
</script>

<template>
  <div>
    <PageHero
      eyebrow="PRODUCTS"
      title="产品中心"
      desc="六大产品系列、12 个产品族，通径覆盖 DN50–DN2000。每一款产品均提供完整的技术参数、零部件材质与外形连接尺寸表。"
      :crumbs="[{ label: '产品中心' }]"
    />

    <section class="section">
      <div class="container">
        <div class="filter">
          <button class="filter__btn" :class="{ 'is-on': active === 'all' }" @click="setActive('all')">
            全部产品 <span>{{ countOf('all') }}</span>
          </button>
          <button
            v-for="c in categories"
            :key="c.id"
            class="filter__btn"
            :class="{ 'is-on': active === c.id }"
            @click="setActive(c.id)"
          >
            {{ c.name }} <span>{{ countOf(c.id) }}</span>
          </button>
        </div>

        <div v-if="activeCat" class="catnote">
          <h3>{{ activeCat.name }} <em>{{ activeCat.en }}</em></h3>
          <p>{{ activeCat.desc }}</p>
        </div>

        <div class="pgrid">
          <ProductCard v-for="p in list" :key="p.slug" :product="p" class="reveal" />
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container">
        <SectionHead
          eyebrow="MODEL OVERVIEW"
          title="型号一览"
          desc="按驱动方式与阀体形式区分，型号后缀代表执行机构；选型时请同时确认通径、压力与密封材质"
        />
        <div class="models">
          <div v-for="g in modelGroups" :key="g.title" class="models__group reveal">
            <div class="models__head">
              <h4>{{ g.title }}</h4>
              <span>{{ g.en }}</span>
            </div>
            <ul>
              <li v-for="m in g.items" :key="m[0]">
                <strong>{{ m[0] }}</strong>
                <span>{{ m[1] }}</span>
              </li>
            </ul>
          </div>
        </div>
        <p class="models__note">
          说明：表中型号依据产品样本册「产品集锦」整理，同一型号可按介质与工况选配不同阀体材质与密封面；
          非标结构、特殊压力等级可来图定制。
        </p>
      </div>
    </section>

    <CtaBand title="没有找到合适的规格？" desc="提供介质、压力、温度与管路法兰标准，我们可按图定制非标阀门" />
  </div>
</template>

<style scoped>
.filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-bottom: 30px;
  border-bottom: 1px solid var(--line);
  margin-bottom: 34px;
}

.filter__btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  height: 40px;
  padding: 0 18px;
  border: 1px solid var(--line);
  border-radius: 2px;
  background: #fff;
  color: var(--ink-2);
  font-size: 14px;
  font-weight: 500;
  transition: all 0.22s var(--ease);
}

.filter__btn span {
  font-size: 11.5px;
  color: var(--muted-2);
}

.filter__btn:hover {
  border-color: var(--blue-400);
  color: var(--blue-600);
}

.filter__btn.is-on {
  background: var(--navy-800);
  border-color: var(--navy-800);
  color: #fff;
}

.filter__btn.is-on span {
  color: rgba(255, 255, 255, 0.55);
}

.catnote {
  margin-bottom: 34px;
  padding: 22px 26px;
  background: var(--bg-soft);
  border-left: 3px solid var(--blue-600);
  border-radius: 0 2px 2px 0;
}

.catnote h3 {
  font-size: 17px;
  margin-bottom: 6px;
}

.catnote em {
  font-style: normal;
  font-size: 10.5px;
  letter-spacing: 0.12em;
  color: var(--muted-2);
  margin-left: 8px;
}

.catnote p {
  font-size: 13.5px;
  color: var(--muted);
}

.pgrid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.models {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.models__group {
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  padding: 24px 26px;
}

.models__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line-2);
  margin-bottom: 6px;
}

.models__head h4 {
  font-size: 15.5px;
}

.models__head span {
  font-size: 10px;
  letter-spacing: 0.14em;
  color: var(--muted-2);
}

.models__group ul {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 18px;
}

.models__group li {
  display: flex;
  align-items: baseline;
  gap: 9px;
  padding: 7px 0;
  border-bottom: 1px dashed var(--line-2);
  font-size: 13px;
}

.models__group li strong {
  color: var(--blue-700);
  font-family: 'SF Mono', 'Menlo', monospace;
  font-size: 12.5px;
  white-space: nowrap;
}

.models__group li span {
  color: var(--muted);
}

.models__note {
  margin-top: 26px;
  font-size: 12.5px;
  color: var(--muted-2);
  line-height: 1.9;
}

@media (max-width: 1024px) {
  .pgrid {
    grid-template-columns: repeat(2, 1fr);
  }
  .models {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .pgrid {
    grid-template-columns: 1fr;
  }
  .models__group ul {
    grid-template-columns: 1fr;
  }
  .filter__btn {
    height: 36px;
    padding: 0 13px;
    font-size: 13px;
  }
}
</style>
