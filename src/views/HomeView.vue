<script setup>
import { computed } from 'vue'
import { products, categories } from '../data/products'
import { company, advantages, supportTopics } from '../data/company'
import SectionHead from '../components/SectionHead.vue'
import ProductCard from '../components/ProductCard.vue'
import CtaBand from '../components/CtaBand.vue'
import AppIcon from '../components/AppIcon.vue'

const featured = computed(() =>
  ['pz73-pz43', 'ggg40-slurry', 'scz673', 'ceramic-knife'].map((s) => products.find((p) => p.slug === s))
)

const heroPoints = [
  { icon: 'shield', title: '品质可靠', desc: '逐台试压检验' },
  { icon: 'gear', title: '专业制造', desc: '专注刀闸阀领域' },
  { icon: 'check', title: '合作共赢', desc: '非标按图定制' }
]

const apps = [
  { name: '石油化工', desc: '油品、化工介质管路截断', icon: 'flask' },
  { name: '水处理', desc: '污水、污泥、沉淀池管路', icon: 'drop' },
  { name: '能源电力', desc: '输煤、除灰渣系统', icon: 'bolt' },
  { name: '工业制造', desc: '造纸、冶金、水泥、矿山', icon: 'factory' }
]
</script>

<template>
  <div>
    <!-- ============ HERO ============ -->
    <section class="hero">
      <div class="hero__bg"></div>
      <div class="container hero__inner">
        <div class="hero__text">
          <span class="hero__eyebrow">PINHUI VALVE · 中国泵阀之乡</span>
          <h1>专业阀门制造<br />品质连接工业未来</h1>
          <p class="hero__sub">PRECISION VALVE · QUALITY MANUFACTURING</p>
          <p class="hero__desc">
            专注刀型闸阀、浆液阀、穿透式插板阀、陶瓷阀门与闸门制造，
            通径覆盖 DN50–DN2000，为含固、磨蚀、腐蚀工况提供可靠的截断方案。
          </p>
          <div class="hero__actions">
            <RouterLink to="/products" class="btn btn--primary">
              查看产品
              <AppIcon name="arrow" :size="17" />
            </RouterLink>
            <RouterLink to="/contact" class="btn btn--ghost">联系我们</RouterLink>
          </div>
        </div>
        <div class="hero__art">
          <img src="/images/p-hero-valve.png" alt="品汇 PZ73 系列刀闸阀" />
        </div>
      </div>

      <div class="hero__strip">
        <div class="container hero__strip-inner">
          <div v-for="p in heroPoints" :key="p.title" class="hero__point">
            <AppIcon :name="p.icon" :size="22" />
            <div>
              <strong>{{ p.title }}</strong>
              <span>{{ p.desc }}</span>
            </div>
          </div>
          <div class="hero__dots" aria-hidden="true">
            <i class="is-on"></i><i></i><i></i>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ 产品中心 ============ -->
    <section class="section">
      <div class="container">
        <SectionHead
          eyebrow="PRODUCT CENTER"
          title="产品中心"
          desc="六大产品系列，覆盖刀型闸阀、浆液阀、穿透式插板阀、陶瓷阀门、方形闸阀与闸门"
        />

        <div class="grid-4">
          <ProductCard v-for="p in featured" :key="p.slug" :product="p" class="reveal" />
        </div>

        <div class="cats">
          <RouterLink v-for="c in categories" :key="c.id" :to="`/products?c=${c.id}`" class="cats__item">
            <span class="cats__name">{{ c.name }}</span>
            <span class="cats__en">{{ c.en }}</span>
          </RouterLink>
        </div>

        <div class="center">
          <RouterLink to="/products" class="link-arrow">查看全部 12 款产品 <span>→</span></RouterLink>
        </div>
      </div>
    </section>

    <!-- ============ 关于品汇 ============ -->
    <section class="section section--soft">
      <div class="container about">
        <div class="about__media reveal">
          <img src="/images/about.jpg" alt="品汇阀门生产车间" loading="lazy" />
          <div class="about__badge">
            <strong>50–2000<small>mm</small></strong>
            <span>通径覆盖范围</span>
          </div>
        </div>
        <div class="about__text reveal">
          <span class="eyebrow">ABOUT PINHUI</span>
          <h2 class="section-title">专注阀门品质，服务工业发展</h2>
          <p>
            浙江品汇阀门有限公司座落于中国“泵阀之乡”——浙江温州永嘉，是一家专业生产刀型闸阀、浆液阀、矿浆阀、
            纸浆阀、排渣阀、非标闸门、陶瓷闸阀等系列产品的企业，集设计、开发、生产、销售、服务于一体。
          </p>
          <p>
            公司拥有先进的设计和精良的生产与检测设备，以及成熟的制造工艺技术，能按照 API、NF、DIN、BS、
            JIS、GB 等国内外行业标准生产，并可根据客户特殊需求冶炼和制造非标产品。
          </p>
          <ul class="about__facts">
            <li v-for="f in company.facts" :key="f.label">
              <strong>{{ f.value }}<em>{{ f.unit }}</em></strong>
              <span>{{ f.label }}</span>
              <small>{{ f.sub }}</small>
            </li>
          </ul>
          <RouterLink to="/about" class="btn btn--primary">
            了解品汇
            <AppIcon name="arrow" :size="17" />
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- ============ 应用领域 ============ -->
    <section class="section">
      <div class="container">
        <SectionHead
          eyebrow="APPLICATION AREAS"
          title="产品应用领域"
          desc="广泛应用于电力、石油、化工、造纸、城建、污水环保、轻工化纤、冶金、水泥等行业"
        />
        <div class="apps">
          <div v-for="a in apps" :key="a.name" class="apps__card reveal">
            <div class="apps__icon"><AppIcon :name="a.icon" :size="26" /></div>
            <h3>{{ a.name }}</h3>
            <p>{{ a.desc }}</p>
          </div>
        </div>
        <ul class="apps__list">
          <li v-for="i in company.industries" :key="i.name">{{ i.name }}</li>
        </ul>
      </div>
    </section>

    <!-- ============ 制造优势 ============ -->
    <section class="section section--soft">
      <div class="container">
        <div class="adv">
          <div class="adv__head">
            <span class="eyebrow">OUR ADVANTAGES</span>
            <h2 class="section-title">我们的优势</h2>
          </div>
          <div class="adv__grid">
            <div v-for="a in advantages" :key="a.title" class="adv__item reveal">
              <AppIcon :name="['shield', 'valve', 'box', 'headset'][advantages.indexOf(a)]" :size="30" />
              <h3>{{ a.title }}</h3>
              <span class="adv__en">{{ a.en }}</span>
              <p>{{ a.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ CTA ============ -->
    <CtaBand />

    <!-- ============ 技术支持 ============ -->
    <section class="section">
      <div class="container">
        <SectionHead
          eyebrow="TECHNICAL SUPPORT"
          title="技术支持"
          desc="选型、安装与维护资料，全部来自产品样本册，可直接对照使用"
        />
        <div class="grid-4">
          <RouterLink v-for="t in supportTopics" :key="t.title" :to="t.to" class="sup reveal">
            <span class="sup__en">{{ t.en }}</span>
            <h3>{{ t.title }}</h3>
            <p>{{ t.desc }}</p>
            <span class="link-arrow">查看 <span>→</span></span>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- ============ 联系 CTA ============ -->
    <section class="contact-cta">
      <div class="container contact-cta__inner">
        <div class="contact-cta__icon"><AppIcon name="headset" :size="34" /></div>
        <div class="contact-cta__text">
          <h2>需要寻找可靠的工业阀门产品？</h2>
          <p>欢迎联系浙江品汇阀门有限公司，了解产品详情与合作信息。</p>
        </div>
        <div class="contact-cta__actions">
          <RouterLink to="/contact" class="btn btn--primary">
            立即咨询
            <AppIcon name="arrow" :size="17" />
          </RouterLink>
          <RouterLink to="/products" class="btn btn--outline">获取产品资料</RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ---------------- hero ---------------- */
.hero {
  position: relative;
  background: var(--navy-900);
  overflow: hidden;
}

.hero__bg {
  position: absolute;
  inset: 0;
  background-image: url('/images/hero.jpg');
  background-size: cover;
  background-position: center 45%;
  opacity: 0.55;
}

.hero__bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(96deg, rgba(6, 27, 48, 0.97) 0%, rgba(6, 27, 48, 0.9) 42%, rgba(8, 31, 55, 0.55) 72%, rgba(10, 37, 64, 0.35) 100%);
}

.hero__inner {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  min-height: 578px;
  padding-top: 44px;
  padding-bottom: 44px;
}

.hero__text {
  color: #fff;
  padding: 30px 0 40px;
}

.hero__eyebrow {
  display: inline-block;
  font-size: 12px;
  letter-spacing: 0.26em;
  color: #7fb2e0;
  margin-bottom: 22px;
}

.hero h1 {
  font-size: 50px;
  line-height: 1.24;
  letter-spacing: 0.02em;
  font-weight: 700;
}

.hero__sub {
  margin-top: 16px;
  font-size: 12.5px;
  letter-spacing: 0.24em;
  color: rgba(255, 255, 255, 0.55);
}

.hero__desc {
  margin-top: 24px;
  max-width: 470px;
  font-size: 15px;
  line-height: 1.95;
  color: rgba(255, 255, 255, 0.72);
}

.hero__actions {
  display: flex;
  gap: 14px;
  margin-top: 34px;
  flex-wrap: wrap;
}

.hero__art {
  position: relative;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  height: 100%;
}

.hero__art img {
  height: 470px;
  max-width: 100%;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 30px 50px rgba(0, 0, 0, 0.45));
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

.hero__strip {
  position: relative;
  z-index: 3;
  background: rgba(6, 27, 48, 0.72);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(6px);
}

.hero__strip-inner {
  display: flex;
  align-items: center;
  gap: 52px;
  height: 76px;
}

.hero__point {
  display: flex;
  align-items: center;
  gap: 12px;
  color: rgba(255, 255, 255, 0.72);
}

.hero__point :deep(svg) {
  color: #6fa8dc;
  flex: none;
}

.hero__point strong {
  display: block;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  line-height: 1.4;
}

.hero__point span {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.45);
}

.hero__dots {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 8px;
}

.hero__dots i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.28);
}

.hero__dots i.is-on {
  width: 22px;
  border-radius: 100px;
  background: #fff;
}

/* ---------------- grids ---------------- */
.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 22px;
}

.cats {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin: 34px 0 26px;
}

.cats__item {
  display: inline-flex;
  align-items: baseline;
  gap: 8px;
  padding: 9px 18px;
  border: 1px solid var(--line);
  border-radius: 100px;
  background: #fff;
  transition: all 0.25s var(--ease);
}

.cats__item:hover {
  border-color: var(--blue-500);
  background: var(--blue-100);
}

.cats__name {
  font-size: 14px;
  font-weight: 600;
  color: var(--ink);
}

.cats__en {
  font-size: 10px;
  letter-spacing: 0.1em;
  color: var(--muted-2);
}

.center {
  text-align: center;
  margin-top: 8px;
}

/* ---------------- about ---------------- */
.about {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 66px;
  align-items: center;
}

.about__media {
  position: relative;
}

.about__media > img {
  width: 100%;
  height: 420px;
  object-fit: cover;
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}

.about__badge {
  position: absolute;
  right: -18px;
  bottom: -18px;
  background: var(--blue-600);
  color: #fff;
  padding: 20px 26px;
  border-radius: var(--radius);
  box-shadow: 0 16px 34px rgba(26, 95, 168, 0.32);
}

.about__badge strong {
  display: block;
  font-size: 26px;
  line-height: 1.1;
  letter-spacing: 0.01em;
}

.about__badge small {
  font-size: 13px;
  margin-left: 3px;
  opacity: 0.8;
}

.about__badge span {
  font-size: 12px;
  opacity: 0.85;
}

.about__text h2 {
  margin: 10px 0 20px;
}

.about__text > p {
  color: var(--muted);
  font-size: 14.5px;
  line-height: 2;
  margin-bottom: 14px;
}

.about__facts {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px 26px;
  margin: 28px 0 30px;
  padding: 24px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.about__facts li strong {
  display: block;
  font-size: 24px;
  color: var(--navy-800);
  line-height: 1.2;
}

.about__facts li em {
  font-style: normal;
  font-size: 13px;
  color: var(--blue-600);
  margin-left: 4px;
}

.about__facts li span {
  font-size: 13.5px;
  color: var(--ink-2);
  font-weight: 600;
}

.about__facts li small {
  display: block;
  font-size: 12px;
  color: var(--muted-2);
}

/* ---------------- apps ---------------- */
.apps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.apps__card {
  position: relative;
  padding: 34px 26px 30px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: linear-gradient(165deg, #ffffff 0%, #f7fafd 100%);
  overflow: hidden;
  transition: all 0.3s var(--ease);
}

.apps__card::before {
  content: '';
  position: absolute;
  right: -30px;
  top: -30px;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: var(--blue-100);
  opacity: 0;
  transition: opacity 0.3s var(--ease);
}

.apps__card:hover {
  border-color: rgba(30, 111, 191, 0.35);
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.apps__card:hover::before {
  opacity: 1;
}

.apps__icon {
  position: relative;
  width: 50px;
  height: 50px;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 2px;
  color: var(--blue-600);
  background: #fff;
  margin-bottom: 20px;
}

.apps__card h3 {
  position: relative;
  font-size: 17px;
  margin-bottom: 8px;
}

.apps__card p {
  position: relative;
  font-size: 13px;
  color: var(--muted);
  line-height: 1.8;
}

.apps__list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px 26px;
  margin-top: 34px;
  padding-top: 26px;
  border-top: 1px dashed var(--line);
}

.apps__list li {
  font-size: 13px;
  color: var(--muted);
  position: relative;
  padding-left: 12px;
}

.apps__list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 4px;
  height: 4px;
  background: var(--blue-400);
  border-radius: 50%;
  transform: translateY(-50%);
}

/* ---------------- advantages ---------------- */
.adv {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 50px;
  align-items: start;
}

.adv__head h2 {
  margin-top: 10px;
}

.adv__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}

.adv__item {
  color: var(--ink-2);
}

.adv__item :deep(svg) {
  color: var(--blue-600);
  margin-bottom: 16px;
}

.adv__item h3 {
  font-size: 16.5px;
  margin-bottom: 3px;
}

.adv__en {
  font-size: 10.5px;
  letter-spacing: 0.12em;
  color: var(--muted-2);
}

.adv__item p {
  margin-top: 12px;
  font-size: 13px;
  line-height: 1.85;
  color: var(--muted);
}

/* ---------------- support ---------------- */
.sup {
  display: block;
  padding: 30px 26px 28px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
  transition: all 0.3s var(--ease);
}

.sup:hover {
  border-color: rgba(30, 111, 191, 0.35);
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}

.sup__en {
  font-size: 10.5px;
  letter-spacing: 0.14em;
  color: var(--blue-500);
  font-weight: 600;
}

.sup h3 {
  font-size: 17px;
  margin: 8px 0 10px;
}

.sup p {
  font-size: 13px;
  line-height: 1.85;
  color: var(--muted);
  margin-bottom: 18px;
}

/* ---------------- contact cta ---------------- */
.contact-cta {
  background: var(--bg-mid);
  border-top: 1px solid var(--line);
}

.contact-cta__inner {
  display: flex;
  align-items: center;
  gap: 26px;
  padding: 44px 32px;
}

.contact-cta__icon {
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background: #fff;
  display: grid;
  place-items: center;
  color: var(--blue-600);
  flex: none;
  box-shadow: var(--shadow-sm);
}

.contact-cta__text {
  flex: 1;
}

.contact-cta__text h2 {
  font-size: 23px;
  margin-bottom: 6px;
}

.contact-cta__text p {
  font-size: 14px;
  color: var(--muted);
}

.contact-cta__actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

/* ---------------- responsive ---------------- */
@media (max-width: 1100px) {
  .grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
  .hero h1 {
    font-size: 40px;
  }
  .hero__art img {
    height: 420px;
  }
  .adv {
    grid-template-columns: 1fr;
    gap: 34px;
  }
  .adv__grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .apps {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 900px) {
  .hero__inner {
    grid-template-columns: 1fr;
    min-height: 0;
    padding-top: 56px;
    padding-bottom: 10px;
  }
  .hero__art {
    justify-content: center;
    margin-top: 10px;
  }
  .hero__art img {
    height: 300px;
  }
  .hero__strip-inner {
    flex-wrap: wrap;
    height: auto;
    padding: 16px 0;
    gap: 18px 30px;
  }
  .hero__dots {
    display: none;
  }
  .about {
    grid-template-columns: 1fr;
    gap: 44px;
  }
  .about__media > img {
    height: 300px;
  }
  .about__badge {
    right: 12px;
    bottom: -16px;
  }
  .contact-cta__inner {
    flex-direction: column;
    align-items: flex-start;
    gap: 18px;
    padding: 34px 24px;
  }
  .contact-cta__text h2 {
    font-size: 20px;
  }
}

@media (max-width: 640px) {
  .grid-4 {
    grid-template-columns: 1fr;
  }
  .hero h1 {
    font-size: 30px;
    line-height: 1.32;
  }
  .hero__desc {
    font-size: 14px;
    margin-top: 18px;
  }
  .hero__eyebrow {
    font-size: 10.5px;
    letter-spacing: 0.18em;
  }
  .hero__sub {
    font-size: 10.5px;
    letter-spacing: 0.16em;
  }
  .hero__art img {
    height: 230px;
  }
  .apps {
    grid-template-columns: 1fr;
  }
  .apps__card {
    padding: 22px 20px 20px;
  }
  .apps__icon {
    margin-bottom: 14px;
    width: 42px;
    height: 42px;
  }
  .adv__grid {
    grid-template-columns: 1fr;
    gap: 22px;
  }
  .about__facts {
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .apps__list {
    gap: 8px 18px;
  }
}
</style>
