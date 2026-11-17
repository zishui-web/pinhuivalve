<script setup>
import PageHero from '../components/PageHero.vue'
import SectionHead from '../components/SectionHead.vue'
import CtaBand from '../components/CtaBand.vue'
import AppIcon from '../components/AppIcon.vue'

const steps = [
  { no: '01', title: '铸件与原材料入厂', desc: '按材质要求核对铸铁、铸钢、不锈钢毛坯，确认化学成分与外观质量。' },
  { no: '02', title: '机加工', desc: '阀体、阀盖、闸板、阀杆在加工中心完成车、铣、钻工序，保证密封面与法兰尺寸精度。' },
  { no: '03', title: '装配', desc: '按图纸装配阀座、填料、阀杆与执行机构，调整闸板行程与压紧量。' },
  { no: '04', title: '试压检验', desc: '逐台进行壳体强度试验（1.5×PN）与密封试验（1.1×PN），并做启闭动作检验。' },
  { no: '05', title: '涂装与包装', desc: '表面处理后按客户要求涂装，配套法兰保护与出口包装。' }
]

const gallery = [
  { img: '/images/strength-cnc.jpg', title: '机加工中心', desc: '立式加工中心完成阀体法兰与密封面加工，型号 VM1103S。' },
  { img: '/images/gallery-1.jpg', title: '装配与调试', desc: '成排阀门在装配区完成执行机构安装与启闭调试。' },
  { img: '/images/gallery-2.jpg', title: '成品待发区', desc: '按订单配套、检验合格后进入成品库存区等待发货。' },
  { img: '/images/strength-qc.jpg', title: '现场加工', desc: '大规格阀体在机床上加工，工人同步进行尺寸复核。' }
]

const qc = [
  { t: '壳体强度试验', v: '1.5 × PN', d: '检验阀体与阀盖的承压强度与铸造质量' },
  { t: '密封试验', v: '1.1 × PN', d: '检验阀座与闸板配合的密封性能' },
  { t: '启闭动作检验', v: '全行程', d: '手动 / 电动 / 气动执行机构全行程启闭，确认无卡阻' },
  { t: '外观与涂装', v: '逐台', d: '铸件表面、法兰密封面保护与涂装外观检查' }
]
</script>

<template>
  <div>
    <PageHero
      eyebrow="MANUFACTURING"
      title="生产实力"
      desc="拥有先进的设计和精良的生产与检测设备，以及成熟的制造工艺技术——从铸件入厂到成品试压，每一道工序都可追溯。"
      :crumbs="[{ label: '生产实力' }]"
    />

    <section class="section">
      <div class="container">
        <div class="lead">
          <div class="lead__text">
            <span class="eyebrow">WORKSHOP</span>
            <h2 class="section-title">机加工 · 装配 · 试压一体化</h2>
            <p>
              公司具备从阀体加工、零部件装配到整机试压的完整生产条件，常规规格可按库存组织供货，
              非标结构与特殊材质可按图定制。加工与装配过程按工序流转，关键尺寸逐件复核。
            </p>
            <ul class="lead__list">
              <li><AppIcon name="check" :size="16" />阀体、阀盖、闸板自主加工，密封面精度可控</li>
              <li><AppIcon name="check" :size="16" />执行机构（手动 / 电动 / 气动 / 液动）配套安装与调试</li>
              <li><AppIcon name="check" :size="16" />整机试压后入库，常规规格现货供应</li>
            </ul>
          </div>
          <div class="lead__media">
            <img src="/images/strength-cnc.jpg" alt="机加工车间" loading="lazy" />
          </div>
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container">
        <SectionHead eyebrow="PROCESS" title="制造流程" desc="五道主要工序，关键节点设置检验" />
        <div class="steps">
          <div v-for="(s, i) in steps" :key="s.no" class="step reveal">
            <span class="step__no">{{ s.no }}</span>
            <h3>{{ s.title }}</h3>
            <p>{{ s.desc }}</p>
            <i v-if="i < steps.length - 1" class="step__line"></i>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <SectionHead eyebrow="EQUIPMENT" title="设备与现场" desc="加工中心、装配区与成品库存区实景" />
        <div class="gal">
          <figure v-for="g in gallery" :key="g.img" class="gal__item reveal">
            <img :src="g.img" :alt="g.title" loading="lazy" />
            <figcaption>
              <strong>{{ g.title }}</strong>
              <span>{{ g.desc }}</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section section--soft">
      <div class="container">
        <SectionHead
          eyebrow="QUALITY CONTROL"
          title="检验标准"
          desc="按样本册技术参数执行壳体与密封试验，试验压力随公称压力等级对应"
        />
        <div class="qc">
          <div v-for="q in qc" :key="q.t" class="qc__item reveal">
            <span class="qc__v">{{ q.v }}</span>
            <h4>{{ q.t }}</h4>
            <p>{{ q.d }}</p>
          </div>
        </div>
        <p class="qc__note">
          注：1.0MPa 产品壳体试验 1.5MPa、密封试验 1.1MPa；1.6MPa 产品壳体试验 2.4MPa、密封试验 1.8MPa；
          穿透式插板阀按 1.5×PN / 1.1×PN 执行。具体以各产品页「主要性能规范」为准。
        </p>
      </div>
    </section>

    <CtaBand title="需要现场考察或样品确认？" desc="欢迎来厂参观，我们可提供样品与检测记录" />
  </div>
</template>

<style scoped>
.lead {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  align-items: center;
}

.lead__text h2 {
  margin: 10px 0 18px;
}

.lead__text p {
  font-size: 14.5px;
  line-height: 2.05;
  color: var(--muted);
}

.lead__list {
  margin-top: 24px;
}

.lead__list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 9px 0;
  font-size: 13.5px;
  color: var(--ink-2);
  border-top: 1px dashed var(--line);
}

.lead__list li :deep(svg) {
  flex: none;
  margin-top: 5px;
  color: var(--blue-600);
}

.lead__media img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
}

/* steps */
.steps {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 18px;
}

.step {
  position: relative;
  padding: 26px 22px;
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
}

.step__no {
  font-family: 'SF Mono', Menlo, monospace;
  font-size: 12px;
  color: var(--blue-500);
  letter-spacing: 0.08em;
}

.step h3 {
  font-size: 15px;
  margin: 10px 0 8px;
}

.step p {
  font-size: 12.5px;
  line-height: 1.85;
  color: var(--muted);
}

.step__line {
  position: absolute;
  right: -13px;
  top: 42px;
  width: 8px;
  height: 8px;
  border-top: 1px solid var(--line);
  border-right: 1px solid var(--line);
  transform: rotate(45deg);
}

/* gallery */
.gal {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 22px;
}

.gal__item {
  margin: 0;
  overflow: hidden;
  border-radius: var(--radius);
  border: 1px solid var(--line-2);
  background: #fff;
}

.gal__item img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  transition: transform 0.6s var(--ease);
}

.gal__item:hover img {
  transform: scale(1.03);
}

.gal__item figcaption {
  padding: 18px 22px 20px;
}

.gal__item strong {
  display: block;
  font-size: 15px;
  margin-bottom: 4px;
}

.gal__item span {
  font-size: 12.5px;
  color: var(--muted);
  line-height: 1.8;
}

/* qc */
.qc {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.qc__item {
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  padding: 26px 22px;
}

.qc__v {
  display: inline-block;
  font-size: 20px;
  font-weight: 700;
  color: var(--blue-600);
  letter-spacing: 0.02em;
}

.qc__item h4 {
  font-size: 14.5px;
  margin: 10px 0 6px;
}

.qc__item p {
  font-size: 12.5px;
  line-height: 1.8;
  color: var(--muted);
}

.qc__note {
  margin-top: 24px;
  font-size: 12.5px;
  color: var(--muted-2);
  line-height: 1.9;
}

@media (max-width: 1024px) {
  .lead {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .lead__media img {
    height: 300px;
  }
  .steps {
    grid-template-columns: repeat(2, 1fr);
  }
  .step__line {
    display: none;
  }
  .qc {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .gal {
    grid-template-columns: 1fr;
  }
  .gal__item img {
    height: 220px;
  }
  .steps {
    grid-template-columns: 1fr;
  }
  .qc {
    grid-template-columns: 1fr;
  }
}
</style>
