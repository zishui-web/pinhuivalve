<script setup>
import { company, advantages } from '../data/company'
import PageHero from '../components/PageHero.vue'
import SectionHead from '../components/SectionHead.vue'
import CtaBand from '../components/CtaBand.vue'
import AppIcon from '../components/AppIcon.vue'

const values = [
  {
    icon: 'bolt',
    title: '以科技为先导',
    desc: '持续开发新产品，按 API、NF、DIN、BS、JIS、GB 等国内外行业标准组织生产。'
  },
  {
    icon: 'shield',
    title: '以质量为根本',
    desc: '拥有先进的设计和精良的生产与检测设备，以成熟的制造工艺技术保证产品一致性。'
  },
  {
    icon: 'headset',
    title: '以诚信服务为宗旨',
    desc: '以合理的价位取得用户信任，秉持“不求最好，只求更好”的精神提供服务。'
  }
]

const gallery = [
  { img: '/images/strength-cnc.jpg', label: '机加工车间' },
  { img: '/images/strength-line.jpg', label: '装配与调试' },
  { img: '/images/strength-stock.jpg', label: '成品库存区' }
]
</script>

<template>
  <div>
    <PageHero
      eyebrow="ABOUT PINHUI"
      title="关于我们"
      desc="集设计、开发、生产、销售、服务为一体的阀门专业制造商，坐落于中国“中国泵阀之乡”——浙江温州永嘉。"
      :crumbs="[{ label: '关于我们' }]"
    />

    <!-- 企业简介 -->
    <section class="section">
      <div class="container intro">
        <div class="intro__text reveal">
          <span class="eyebrow">COMPANY PROFILE</span>
          <h2 class="section-title">专业阀门制造商</h2>
          <p v-for="(p, i) in company.introParagraphs" :key="i">{{ p }}</p>
          <div class="intro__tags">
            <span v-for="s in company.standards" :key="s">{{ s }}</span>
          </div>
        </div>
        <div class="intro__media reveal">
          <img src="/images/about.jpg" alt="品汇阀门生产车间" loading="lazy" />
          <div class="intro__caption">
            <strong>{{ company.name }}</strong>
            <span>{{ company.brandEn }} · {{ company.slogan }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 数据 -->
    <section class="facts">
      <div class="container facts__inner">
        <div v-for="f in company.facts" :key="f.label" class="facts__item">
          <strong>{{ f.value }}<em>{{ f.unit }}</em></strong>
          <span>{{ f.label }}</span>
          <small>{{ f.sub }}</small>
        </div>
      </div>
    </section>

    <!-- 经营理念 -->
    <section class="section">
      <div class="container">
        <SectionHead eyebrow="OUR VALUES" title="经营理念" desc="科技先导 · 质量根本 · 诚信服务" />
        <div class="values">
          <div v-for="v in values" :key="v.title" class="values__card reveal">
            <div class="values__icon"><AppIcon :name="v.icon" :size="26" /></div>
            <h3>{{ v.title }}</h3>
            <p>{{ v.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 制造与能力 -->
    <section class="section section--soft">
      <div class="container">
        <SectionHead
          eyebrow="CAPABILITY"
          title="制造能力"
          desc="从铸件到成品，具备完整的加工、装配与检验条件，并可按客户需求冶炼和制造非标产品"
        />
        <div class="cap">
          <div v-for="g in gallery" :key="g.img" class="cap__item reveal">
            <img :src="g.img" :alt="g.label" loading="lazy" />
            <span>{{ g.label }}</span>
          </div>
        </div>

        <div class="cap__grid">
          <div class="cap__card reveal">
            <h4>材料范围</h4>
            <p>产品主体材料采用铸铁、铸钢、不锈钢（316、304、2520）等，可按介质腐蚀性选配。</p>
            <div class="cap__chips">
              <span v-for="m in company.materials" :key="m">{{ m }}</span>
            </div>
          </div>
          <div class="cap__card reveal">
            <h4>驱动形式</h4>
            <p>驱动形式有手动、齿轮传动、电动、气动和液动，可配套手气动切换与电液动方案。</p>
            <div class="cap__chips">
              <span v-for="d in company.drives" :key="d">{{ d }}</span>
            </div>
          </div>
          <div class="cap__card reveal">
            <h4>非标定制</h4>
            <p>可根据客户特殊需求冶炼和制造非标产品，包括非标闸门、特殊压力等级与特殊结构长度。</p>
            <div class="cap__chips">
              <span>来图定制</span>
              <span>来样定制</span>
              <span>特殊材质</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 应用行业 -->
    <section class="section">
      <div class="container">
        <SectionHead eyebrow="INDUSTRIES" title="应用行业" desc="多年来产品广泛应用于以下行业，并出口至海外市场" />
        <div class="inds">
          <div v-for="i in company.industries" :key="i.name" class="inds__item">
            <AppIcon name="factory" :size="18" />
            <span>{{ i.name }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 经营范围 -->
    <section class="section section--soft">
      <div class="container scope">
        <div class="scope__head">
          <span class="eyebrow">BUSINESS SCOPE</span>
          <h2 class="section-title">经营范围</h2>
          <p>以下为营业执照登记的一般项目与许可项目，具体经营项目以审批结果为准。</p>
        </div>
        <ul class="scope__list">
          <li v-for="(b, i) in company.businessScope" :key="b">
            <span>{{ String(i + 1).padStart(2, '0') }}</span>
            {{ b }}
          </li>
        </ul>
      </div>
    </section>

    <CtaBand title="欢迎来厂参观考察" desc="洽谈业务、互利合作、共创佳绩" />
  </div>
</template>

<style scoped>
.intro {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 62px;
  align-items: start;
}

.intro__text h2 {
  margin: 10px 0 20px;
}

.intro__text p {
  font-size: 14.5px;
  line-height: 2.1;
  color: var(--ink-2);
  margin-bottom: 16px;
}

.intro__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 24px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
}

.intro__tags span {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--blue-700);
  border: 1px solid var(--line);
  padding: 5px 14px;
  border-radius: 2px;
  background: #fff;
}

.intro__media {
  position: relative;
}

.intro__media img {
  width: 100%;
  height: 480px;
  object-fit: cover;
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}

.intro__caption {
  position: absolute;
  left: 0;
  bottom: 0;
  right: 0;
  padding: 20px 24px;
  background: linear-gradient(transparent, rgba(6, 27, 48, 0.86));
  color: #fff;
  border-radius: 0 0 var(--radius) var(--radius);
}

.intro__caption strong {
  display: block;
  font-size: 17px;
  letter-spacing: 0.1em;
}

.intro__caption span {
  font-size: 12px;
  letter-spacing: 0.2em;
  color: rgba(255, 255, 255, 0.7);
}

/* facts */
.facts {
  background: var(--navy-800);
  background-image: radial-gradient(circle at 15% 20%, rgba(60, 138, 214, 0.28), transparent 55%);
}

.facts__inner {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  padding: 44px 32px;
}

.facts__item {
  border-left: 1px solid rgba(255, 255, 255, 0.14);
  padding-left: 22px;
}

.facts__item:first-child {
  border-left: 0;
  padding-left: 0;
}

.facts__item strong {
  display: block;
  font-size: 30px;
  color: #fff;
  line-height: 1.2;
}

.facts__item em {
  font-style: normal;
  font-size: 13px;
  color: #6fa8dc;
  margin-left: 4px;
}

.facts__item span {
  display: block;
  color: rgba(255, 255, 255, 0.78);
  font-size: 13.5px;
  margin-top: 4px;
}

.facts__item small {
  color: rgba(255, 255, 255, 0.4);
  font-size: 11.5px;
}

/* values */
.values {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.values__card {
  padding: 34px 30px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
  transition: all 0.3s var(--ease);
}

.values__card:hover {
  border-color: rgba(30, 111, 191, 0.3);
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}

.values__icon {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  background: var(--blue-100);
  color: var(--blue-600);
  border-radius: 2px;
  margin-bottom: 20px;
}

.values__card h3 {
  font-size: 17px;
  margin-bottom: 10px;
}

.values__card p {
  font-size: 13.5px;
  line-height: 1.9;
  color: var(--muted);
}

/* capability */
.cap {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.cap__item {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius);
}

.cap__item img {
  width: 100%;
  height: 260px;
  object-fit: cover;
  transition: transform 0.6s var(--ease);
}

.cap__item:hover img {
  transform: scale(1.04);
}

.cap__item span {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 16px 20px;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  background: linear-gradient(transparent, rgba(6, 27, 48, 0.82));
}

.cap__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 24px;
}

.cap__card {
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  padding: 26px 24px;
}

.cap__card h4 {
  font-size: 15.5px;
  margin-bottom: 10px;
}

.cap__card p {
  font-size: 13px;
  line-height: 1.9;
  color: var(--muted);
  margin-bottom: 16px;
}

.cap__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.cap__chips span {
  font-size: 12px;
  padding: 4px 11px;
  border: 1px solid var(--line);
  border-radius: 100px;
  color: var(--ink-2);
}

/* industries */
.inds {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
}

.inds__item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 18px 20px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  font-size: 14px;
  color: var(--ink-2);
  background: #fff;
  transition: all 0.25s var(--ease);
}

.inds__item :deep(svg) {
  color: var(--blue-500);
}

.inds__item:hover {
  border-color: rgba(30, 111, 191, 0.35);
  color: var(--blue-700);
  background: var(--blue-100);
}

/* scope */
.scope {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 56px;
  align-items: start;
}

.scope__head h2 {
  margin: 10px 0 14px;
}

.scope__head p {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.9;
}

.scope__list {
  display: grid;
  gap: 2px;
}

.scope__list li {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  padding: 15px 18px;
  background: #fff;
  border: 1px solid var(--line-2);
  font-size: 13.5px;
  line-height: 1.9;
  color: var(--ink-2);
}

.scope__list li span {
  font-family: 'SF Mono', Menlo, monospace;
  font-size: 11.5px;
  color: var(--blue-500);
  flex: none;
  margin-top: 3px;
}

@media (max-width: 1024px) {
  .intro {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .intro__media img {
    height: 320px;
  }
  .values,
  .cap,
  .cap__grid {
    grid-template-columns: 1fr 1fr;
  }
  .inds {
    grid-template-columns: repeat(3, 1fr);
  }
  .scope {
    grid-template-columns: 1fr;
    gap: 28px;
  }
}

@media (max-width: 640px) {
  .facts__inner {
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    padding: 32px 18px;
  }
  .facts__item strong {
    font-size: 22px;
  }
  .values,
  .cap,
  .cap__grid {
    grid-template-columns: 1fr;
  }
  .inds {
    grid-template-columns: 1fr 1fr;
  }
  .cap__item img {
    height: 200px;
  }
}
</style>
