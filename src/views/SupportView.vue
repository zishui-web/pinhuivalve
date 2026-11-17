<script setup>
import { ref } from 'vue'
import { seatStructures, seatNotes, flangeTables, flangeNotes, installNotes, maintenanceNotes, techFaqs } from '../data/support'
import PageHero from '../components/PageHero.vue'
import DataTable from '../components/DataTable.vue'
import CtaBand from '../components/CtaBand.vue'
import AppIcon from '../components/AppIcon.vue'

const activeFlange = ref(flangeTables[1].id)
const openFaq = ref(0)

const orientFig = [
  { label: '竖直安装', deg: 0, tone: 'ok' },
  { label: '横向安装', deg: 90, tone: 'mid' },
  { label: '倒装', deg: 180, tone: 'no' }
]

const anchors = [
  { id: 'seat', label: '阀座结构' },
  { id: 'flange', label: '法兰安装尺寸' },
  { id: 'install', label: '使用注意事项' },
  { id: 'maintenance', label: '预防措施' },
  { id: 'faq', label: '常见问题' }
]

const go = (id) => {
  const el = document.getElementById(id)
  if (el) window.scrollTo({ top: el.offsetTop - 110, behavior: 'smooth' })
}
</script>

<template>
  <div>
    <PageHero
      eyebrow="TECHNICAL SUPPORT"
      title="技术支持"
      desc="阀座结构、法兰安装尺寸、安装与维护要点——全部取自产品样本册，可直接对照现场使用。"
      :crumbs="[{ label: '技术支持' }]"
    />

    <div class="subnav">
      <div class="container subnav__inner">
        <button v-for="a in anchors" :key="a.id" @click="go(a.id)">{{ a.label }}</button>
      </div>
    </div>

    <!-- 阀座结构 -->
    <section id="seat" class="section">
      <div class="container">
        <div class="head">
          <span class="eyebrow">SEAT STRUCTURE</span>
          <h2 class="section-title">阀座结构</h2>
          <p>可更换的阀座使阀门维修方便、可靠；多品种材料的阀座，可用于不同的流体、固体介质。</p>
        </div>

        <div class="seats">
          <div v-for="s in seatStructures" :key="s.name" class="seat reveal">
            <div class="seat__top">
              <span class="seat__en">{{ s.en }}</span>
              <h3>{{ s.name }}</h3>
            </div>
            <p>{{ s.desc }}</p>
            <div class="seat__parts">
              <span v-for="p in s.parts" :key="p">{{ p }}</span>
            </div>
          </div>
        </div>

        <ul class="notelist">
          <li v-for="n in seatNotes" :key="n">{{ n }}</li>
        </ul>
      </div>
    </section>

    <!-- 法兰尺寸 -->
    <section id="flange" class="section section--soft">
      <div class="container">
        <div class="head">
          <span class="eyebrow">FLANGE DIMENSIONS</span>
          <h2 class="section-title">法兰安装尺寸</h2>
          <p>国标 JB/T79 凸面（RF）法兰与美标 Class 150 凸面（RF）法兰尺寸对照</p>
        </div>

        <div class="tabs">
          <button
            v-for="t in flangeTables"
            :key="t.id"
            class="tabs__btn"
            :class="{ 'is-on': activeFlange === t.id }"
            @click="activeFlange = t.id"
          >
            {{ t.title.replace('法兰尺寸 · ', '') }}
          </button>
        </div>

        <template v-for="t in flangeTables" :key="t.id">
          <DataTable v-if="activeFlange === t.id" :table="t" />
        </template>

        <ul class="notelist">
          <li v-for="n in flangeNotes" :key="n">{{ n }}</li>
        </ul>
      </div>
    </section>

    <!-- 使用注意事项 -->
    <section id="install" class="section">
      <div class="container">
        <div class="head">
          <span class="eyebrow">INSTALLATION</span>
          <h2 class="section-title">使用注意事项</h2>
          <p>阀门可安装在不同方向，但建议优先采用推荐方位；单向密封阀必须按介质流向安装</p>
        </div>

        <div class="cards">
          <div v-for="n in installNotes" :key="n.title" class="card reveal">
            <span class="card__en">{{ n.en }}</span>
            <h3>{{ n.title }}</h3>
            <ul>
              <li v-for="i in n.items" :key="i">{{ i }}</li>
            </ul>
          </div>
        </div>

        <div class="orient">
          <div class="orient__legend">
            <h4>安装方位示意</h4>
            <p>
              阀门推荐竖直安装（阀杆朝上），此时填料与阀座受力最合理；横向安装需考虑执行器自重并设置支架，
              倒装应尽量避免。
            </p>
            <div class="orient__keys">
              <span><i class="k k--ok"></i>推荐使用</span>
              <span><i class="k k--mid"></i>尽量不使用</span>
              <span><i class="k k--no"></i>避免使用</span>
            </div>
          </div>
          <div class="orient__fig">
            <div v-for="o in orientFig" :key="o.label" class="of">
              <div class="of__box">
                <svg viewBox="0 0 100 140" :style="{ transform: `rotate(${o.deg}deg)` }" :class="`of__svg of__svg--${o.tone}`">
                  <ellipse cx="50" cy="24" rx="19" ry="6" />
                  <line x1="50" y1="30" x2="50" y2="74" />
                  <circle cx="50" cy="98" r="22" />
                  <circle cx="50" cy="98" r="9" />
                </svg>
              </div>
              <strong>{{ o.label }}</strong>
              <span>{{ o.tone === 'ok' ? '推荐使用' : o.tone === 'mid' ? '尽量不使用' : '避免使用' }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 预防措施 -->
    <section id="maintenance" class="section section--soft">
      <div class="container">
        <div class="head">
          <span class="eyebrow">MAINTENANCE</span>
          <h2 class="section-title">预防措施</h2>
          <p>出厂时填料压块螺栓为松开状态，安装使用前须按要点处理</p>
        </div>

        <div class="cards cards--2">
          <div v-for="n in maintenanceNotes" :key="n.title" class="card">
            <span class="card__en">{{ n.en }}</span>
            <h3>{{ n.title }}</h3>
            <ul>
              <li v-for="i in n.items" :key="i">{{ i }}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="section">
      <div class="container">
        <div class="head">
          <span class="eyebrow">FAQ</span>
          <h2 class="section-title">常见问题</h2>
          <p>选型与使用中最常被问到的几个问题</p>
        </div>

        <div class="faq">
          <div v-for="(f, i) in techFaqs" :key="f.q" class="faq__item" :class="{ 'is-open': openFaq === i }">
            <button class="faq__q" @click="openFaq = openFaq === i ? -1 : i">
              <span>{{ f.q }}</span>
              <AppIcon name="chevronDown" :size="18" />
            </button>
            <div class="faq__a">
              <p>{{ f.a }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <CtaBand title="还有技术问题需要确认？" desc="把介质、温度、压力与管路标准发给我们，技术人员协助选型" />
  </div>
</template>

<style scoped>
.subnav {
  position: sticky;
  top: var(--header-h);
  z-index: 40;
  background: #fff;
  border-bottom: 1px solid var(--line);
}

.subnav__inner {
  display: flex;
  gap: 30px;
  height: 54px;
  overflow-x: auto;
}

.subnav button {
  border: 0;
  background: none;
  font-size: 14px;
  color: var(--ink-2);
  white-space: nowrap;
  position: relative;
  padding: 0;
}

.subnav button:hover {
  color: var(--blue-600);
}

.subnav button::after {
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

.subnav button:hover::after {
  transform: scaleX(1);
}

.head {
  margin-bottom: 40px;
  max-width: 720px;
}

.head h2 {
  margin: 10px 0 12px;
}

.head p {
  font-size: 14px;
  line-height: 1.95;
  color: var(--muted);
}

/* seats */
.seats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.seat {
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  padding: 26px 24px;
  transition: all 0.3s var(--ease);
}

.seat:hover {
  border-color: rgba(30, 111, 191, 0.32);
  box-shadow: var(--shadow-md);
}

.seat__en {
  font-size: 10px;
  letter-spacing: 0.14em;
  color: var(--blue-500);
  font-weight: 600;
}

.seat h3 {
  font-size: 16px;
  margin: 7px 0 10px;
}

.seat p {
  font-size: 13px;
  line-height: 1.9;
  color: var(--muted);
  margin-bottom: 16px;
}

.seat__parts {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  padding-top: 14px;
  border-top: 1px dashed var(--line);
}

.seat__parts span {
  font-size: 11.5px;
  color: var(--ink-2);
  background: var(--bg-soft);
  padding: 3px 9px;
  border-radius: 2px;
}

/* tabs */
.tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 22px;
}

.tabs__btn {
  height: 38px;
  padding: 0 18px;
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 2px;
  font-size: 13.5px;
  color: var(--ink-2);
  transition: all 0.22s var(--ease);
}

.tabs__btn:hover {
  border-color: var(--blue-400);
  color: var(--blue-600);
}

.tabs__btn.is-on {
  background: var(--navy-800);
  border-color: var(--navy-800);
  color: #fff;
}

.notelist {
  margin-top: 22px;
}

.notelist li {
  position: relative;
  padding-left: 16px;
  font-size: 12.5px;
  line-height: 1.95;
  color: var(--muted);
}

.notelist li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 11px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--blue-400);
}

/* cards */
.cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.cards--2 {
  grid-template-columns: repeat(2, 1fr);
}

.card {
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  padding: 26px 24px;
}

.card__en {
  font-size: 10px;
  letter-spacing: 0.13em;
  color: var(--blue-500);
  font-weight: 600;
}

.card h3 {
  font-size: 15.5px;
  margin: 8px 0 12px;
}

.card ul li {
  position: relative;
  padding-left: 14px;
  font-size: 13px;
  line-height: 1.9;
  color: var(--muted);
  margin-bottom: 6px;
}

.card ul li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 11px;
  width: 4px;
  height: 4px;
  background: var(--blue-400);
  border-radius: 50%;
}

/* orientation figure */
.orient {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 44px;
  align-items: center;
  margin-top: 30px;
  padding: 32px 34px;
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
}

.orient__legend h4 {
  font-size: 15.5px;
  margin-bottom: 10px;
}

.orient__legend p {
  font-size: 13px;
  line-height: 1.95;
  color: var(--muted);
}

.orient__keys {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-top: 18px;
  font-size: 12.5px;
  color: var(--ink-2);
}

.orient__keys span {
  display: inline-flex;
  align-items: center;
  gap: 7px;
}

.k {
  width: 10px;
  height: 10px;
  border-radius: 2px;
  display: inline-block;
}

.k--ok {
  background: #1a5fa8;
}

.k--mid {
  background: #e8c33c;
}

.k--no {
  background: #d97706;
}

.orient__fig {
  display: flex;
  justify-content: center;
  gap: 26px;
}

.of {
  text-align: center;
}

.of__box {
  width: 104px;
  height: 104px;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 2px;
  background: var(--bg-soft);
  margin-bottom: 10px;
}

.of__svg {
  width: 74px;
  height: 74px;
  fill: none;
  stroke-width: 2.4;
  stroke-linecap: round;
  transition: transform 0.3s var(--ease);
}

.of__svg ellipse,
.of__svg line,
.of__svg circle {
  stroke: currentColor;
}

.of__svg--ok {
  color: #1a5fa8;
}

.of__svg--mid {
  color: #c99a16;
}

.of__svg--no {
  color: #c2410c;
}

.of strong {
  display: block;
  font-size: 13px;
  color: var(--ink);
}

.of span {
  font-size: 11.5px;
  color: var(--muted-2);
}

/* faq */
.faq {
  border-top: 1px solid var(--line);
}

.faq__item {
  border-bottom: 1px solid var(--line);
}

.faq__q {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 20px 4px;
  border: 0;
  background: none;
  text-align: left;
  font-size: 15px;
  font-weight: 600;
  color: var(--ink);
}

.faq__q :deep(svg) {
  flex: none;
  color: var(--muted-2);
  transition: transform 0.3s var(--ease);
}

.faq__item.is-open .faq__q {
  color: var(--blue-700);
}

.faq__item.is-open .faq__q :deep(svg) {
  transform: rotate(180deg);
  color: var(--blue-600);
}

.faq__a {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s var(--ease);
}

.faq__item.is-open .faq__a {
  max-height: 320px;
}

.faq__a p {
  padding: 0 4px 22px;
  font-size: 13.5px;
  line-height: 2;
  color: var(--muted);
  max-width: 860px;
}

@media (max-width: 1024px) {
  .seats {
    grid-template-columns: 1fr 1fr;
  }
  .cards {
    grid-template-columns: 1fr 1fr;
  }
  .orient {
    grid-template-columns: 1fr;
    gap: 26px;
  }
}

@media (max-width: 640px) {
  .seats,
  .cards,
  .cards--2 {
    grid-template-columns: 1fr;
  }
  .subnav__inner {
    gap: 20px;
    height: 50px;
  }
  .tabs__btn {
    height: 34px;
    padding: 0 13px;
    font-size: 12.5px;
  }
  .orient {
    padding: 24px 20px;
  }
  .orient__fig {
    gap: 12px;
  }
  .of__box {
    width: 80px;
    height: 80px;
  }
  .of__svg {
    width: 58px;
    height: 58px;
  }
  .faq__q {
    font-size: 14px;
  }
}
</style>
