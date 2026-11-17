<script setup>
import { ref, reactive, computed } from 'vue'
import { company } from '../data/company'
import { products } from '../data/products'
import PageHero from '../components/PageHero.vue'
import AppIcon from '../components/AppIcon.vue'
import CtaBand from '../components/CtaBand.vue'

const form = reactive({ name: '', phone: '', company: '', product: '', message: '' })
const sent = ref(false)
const error = ref('')
const qrIndex = ref(0)

const mapUrl = computed(
  () => `https://uri.amap.com/search?keyword=${encodeURIComponent('浙江品汇阀门有限公司')}&view=map`
)

const submit = () => {
  error.value = ''
  if (!form.name.trim()) {
    error.value = '请填写您的称呼'
    return
  }
  if (!/^[\d\-+() ]{7,20}$/.test(form.phone.trim())) {
    error.value = '请填写正确的联系电话'
    return
  }
  sent.value = true
}
</script>

<template>
  <div>
    <PageHero
      eyebrow="CONTACT US"
      title="联系我们"
      desc="产品选型、报价、图纸与非标定制，欢迎直接联系销售经理，或留下需求由我们回复。"
      :crumbs="[{ label: '联系我们' }]"
    />

    <section class="section">
      <div class="container contact">
        <!-- 左：联系方式 -->
        <div class="contact__info">
          <span class="eyebrow">GET IN TOUCH</span>
          <h2 class="section-title">销售咨询</h2>
          <p class="contact__lead">
            浙江省温州市永嘉县瓯北街道马岙村，地处“中国泵阀之乡”，欢迎来厂参观考察、洽谈业务。
          </p>

          <div class="phones">
            <a v-for="c in company.contacts" :key="c.phone" class="phones__item" :href="`tel:${c.phone}`">
              <span class="phones__icon"><AppIcon name="phone" :size="20" /></span>
              <span>
                <em>{{ c.title }}</em>
                <strong>{{ c.name }}</strong>
                <b>{{ c.phone }}</b>
              </span>
            </a>
          </div>

          <div class="addr">
            <div class="addr__row">
              <AppIcon name="pin" :size="18" />
              <div>
                <strong>公司地址</strong>
                <p>{{ company.addressFull }}</p>
              </div>
            </div>
            <a class="addr__map" :href="mapUrl" target="_blank" rel="noopener">
              在地图中打开
              <AppIcon name="arrow" :size="15" />
            </a>
          </div>

          <div class="qr">
            <div class="qr__tabs">
              <button
                v-for="(w, i) in company.wechats"
                :key="w.image"
                :class="{ 'is-on': qrIndex === i }"
                @click="qrIndex = i"
              >
                {{ w.label }}
              </button>
            </div>
            <div class="qr__img">
              <img :src="company.wechats[qrIndex].image" :alt="company.wechats[qrIndex].label" />
              <p>微信扫码，发送产品型号或工况参数</p>
            </div>
          </div>
        </div>

        <!-- 右：留言 -->
        <div class="contact__form">
          <div class="formcard">
            <h3>在线询价</h3>
            <p class="formcard__sub">填写后请同时致电销售经理确认，以便及时响应。</p>

            <div v-if="sent" class="formcard__ok">
              <AppIcon name="check" :size="26" />
              <div>
                <strong>信息已记录</strong>
                <p>
                  请致电 {{ company.contacts[0].name }}
                  <a :href="`tel:${company.contacts[0].phone}`">{{ company.contacts[0].phone }}</a>
                  或 {{ company.contacts[1].name }}
                  <a :href="`tel:${company.contacts[1].phone}`">{{ company.contacts[1].phone }}</a>
                  确认需求。
                </p>
                <button class="link-arrow" @click="sent = false">再填一条 <span>→</span></button>
              </div>
            </div>

            <form v-else @submit.prevent="submit">
              <div class="field-row">
                <label class="field">
                  <span>称呼 <i>*</i></span>
                  <input v-model="form.name" type="text" placeholder="请输入您的称呼" />
                </label>
                <label class="field">
                  <span>联系电话 <i>*</i></span>
                  <input v-model="form.phone" type="tel" placeholder="便于回电的号码" />
                </label>
              </div>
              <label class="field">
                <span>公司名称</span>
                <input v-model="form.company" type="text" placeholder="选填" />
              </label>
              <label class="field">
                <span>意向产品</span>
                <select v-model="form.product">
                  <option value="">请选择（选填）</option>
                  <option v-for="p in products" :key="p.slug" :value="p.name">{{ p.name }}</option>
                  <option value="非标定制">非标定制 / 其他</option>
                </select>
              </label>
              <label class="field">
                <span>需求说明</span>
                <textarea
                  v-model="form.message"
                  rows="4"
                  placeholder="通径、压力、温度、介质、驱动方式、管路法兰标准等"
                ></textarea>
              </label>

              <p v-if="error" class="formcard__err">{{ error }}</p>

              <button type="submit" class="btn btn--primary formcard__btn">
                提交需求
                <AppIcon name="arrow" :size="17" />
              </button>
              <p class="formcard__tip">
                本站为静态展示站，表单不会上传服务器；提交后请电话或微信与销售确认。
              </p>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- 来厂 -->
    <section class="section section--soft">
      <div class="container visit">
        <div class="visit__text">
          <span class="eyebrow">VISIT US</span>
          <h2 class="section-title">来厂路线</h2>
          <p>
            公司位于浙江省温州市永嘉县瓯北街道马岙村（马岙工业区），毗邻瓯江，交通便利。
            自驾来访请导航搜索“浙江品汇阀门有限公司”；抵达瓯北后可电话联系，我们安排接待。
          </p>
          <ul>
            <li><strong>地址</strong>{{ company.addressFull }}</li>
            <li><strong>导航</strong>高德 / 百度地图搜索公司全称</li>
            <li><strong>接待</strong>{{ company.contacts[0].name }} {{ company.contacts[0].phone }}</li>
          </ul>
        </div>
        <div class="visit__card">
          <div class="visit__badge">
            <AppIcon name="factory" :size="30" />
            <strong>{{ company.brand }}</strong>
            <span>{{ company.brandEn }}</span>
          </div>
          <div class="visit__addr">
            <AppIcon name="pin" :size="16" />
            {{ company.addressFull }}
          </div>
          <a :href="mapUrl" target="_blank" rel="noopener" class="btn btn--outline btn--sm">
            打开地图导航
            <AppIcon name="arrow" :size="15" />
          </a>
        </div>
      </div>
    </section>

    <CtaBand title="需要报价单或产品图纸？" desc="告诉我们型号与数量，销售经理会尽快回复" />
  </div>
</template>

<style scoped>
.contact {
  display: grid;
  grid-template-columns: 1fr 460px;
  gap: 62px;
  align-items: start;
}

.contact__info h2 {
  margin: 10px 0 14px;
}

.contact__lead {
  font-size: 14px;
  line-height: 2;
  color: var(--muted);
  max-width: 520px;
}

.phones {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin: 30px 0;
}

.phones__item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 20px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
  transition: all 0.28s var(--ease);
}

.phones__item:hover {
  border-color: var(--blue-500);
  box-shadow: var(--shadow-sm);
  transform: translateY(-2px);
}

.phones__icon {
  width: 44px;
  height: 44px;
  flex: none;
  display: grid;
  place-items: center;
  background: var(--blue-100);
  color: var(--blue-600);
  border-radius: 2px;
}

.phones__item em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: var(--muted-2);
  letter-spacing: 0.06em;
}

.phones__item strong {
  font-size: 14px;
  margin-right: 8px;
}

.phones__item b {
  font-size: 16px;
  color: var(--navy-800);
  letter-spacing: 0.02em;
}

.addr {
  padding: 22px 24px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
}

.addr__row {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.addr__row :deep(svg) {
  color: var(--blue-600);
  margin-top: 3px;
}

.addr__row strong {
  display: block;
  font-size: 13.5px;
  margin-bottom: 3px;
}

.addr__row p {
  font-size: 13px;
  color: var(--muted);
}

.addr__map {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: var(--blue-600);
}

.qr {
  margin-top: 18px;
  padding: 20px 22px;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  background: #fff;
  display: inline-flex;
  gap: 22px;
  align-items: flex-start;
}

.qr__tabs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.qr__tabs button {
  padding: 8px 14px;
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 2px;
  font-size: 12.5px;
  color: var(--ink-2);
  white-space: nowrap;
}

.qr__tabs button.is-on {
  background: var(--navy-800);
  border-color: var(--navy-800);
  color: #fff;
}

.qr__img {
  text-align: center;
}

.qr__img img {
  width: 176px;
  height: 235px;
  object-fit: contain;
  display: block;
  border: 1px solid var(--line-2);
  padding: 6px;
  background: #fff;
}

.qr__img p {
  font-size: 11.5px;
  color: var(--muted-2);
  margin-top: 8px;
  width: 176px;
  line-height: 1.7;
}

/* form */
.formcard {
  padding: 34px 32px;
  background: #fff;
  border: 1px solid var(--line-2);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}

.formcard h3 {
  font-size: 20px;
  margin-bottom: 6px;
}

.formcard__sub {
  font-size: 12.5px;
  color: var(--muted);
  margin-bottom: 24px;
}

.field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.field {
  display: block;
  margin-bottom: 14px;
}

.field > span {
  display: block;
  font-size: 12.5px;
  color: var(--ink-2);
  margin-bottom: 7px;
}

.field > span i {
  color: var(--brand-red);
  font-style: normal;
}

.field input,
.field select,
.field textarea {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 2px;
  padding: 11px 13px;
  font-size: 13.5px;
  font-family: inherit;
  color: var(--ink);
  background: #fff;
  outline: none;
  transition: border-color 0.2s var(--ease);
}

.field textarea {
  resize: vertical;
  line-height: 1.8;
}

.field input:focus,
.field select:focus,
.field textarea:focus {
  border-color: var(--blue-500);
  box-shadow: 0 0 0 3px rgba(30, 111, 191, 0.1);
}

.formcard__btn {
  width: 100%;
  margin-top: 6px;
}

.formcard__err {
  font-size: 12.5px;
  color: var(--brand-red);
  margin-bottom: 10px;
}

.formcard__tip {
  margin-top: 12px;
  font-size: 11.5px;
  line-height: 1.8;
  color: var(--muted-2);
}

.formcard__ok {
  display: flex;
  gap: 14px;
  padding: 24px;
  background: var(--blue-100);
  border-radius: var(--radius);
}

.formcard__ok :deep(svg) {
  color: var(--blue-600);
  flex: none;
  margin-top: 2px;
}

.formcard__ok strong {
  display: block;
  font-size: 16px;
  margin-bottom: 6px;
}

.formcard__ok p {
  font-size: 13px;
  line-height: 1.9;
  color: var(--ink-2);
}

.formcard__ok a {
  color: var(--blue-700);
  font-weight: 600;
}

.formcard__ok button {
  margin-top: 14px;
  border: 0;
  background: none;
  padding: 0;
}

/* visit */
.visit {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 56px;
  align-items: center;
}

.visit__text h2 {
  margin: 10px 0 16px;
}

.visit__text > p {
  font-size: 14px;
  line-height: 2;
  color: var(--muted);
}

.visit__text ul {
  margin-top: 22px;
  border-top: 1px solid var(--line);
}

.visit__text li {
  display: grid;
  grid-template-columns: 60px 1fr;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--line-2);
  font-size: 13.5px;
  color: var(--ink-2);
}

.visit__text li strong {
  color: var(--muted);
  font-weight: 400;
}

.visit__card {
  background: var(--navy-800);
  color: #fff;
  border-radius: var(--radius);
  padding: 34px 30px;
  background-image: radial-gradient(circle at 80% 10%, rgba(60, 138, 214, 0.35), transparent 60%);
}

.visit__badge {
  color: #fff;
  margin-bottom: 22px;
}

.visit__badge :deep(svg) {
  color: #6fa8dc;
  margin-bottom: 10px;
}

.visit__badge strong {
  display: block;
  font-size: 20px;
  letter-spacing: 0.12em;
}

.visit__badge span {
  font-size: 10.5px;
  letter-spacing: 0.2em;
  color: rgba(255, 255, 255, 0.55);
}

.visit__addr {
  display: flex;
  gap: 9px;
  align-items: flex-start;
  font-size: 13px;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.72);
  padding: 16px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.14);
  margin-bottom: 18px;
}

.visit__addr :deep(svg) {
  color: #6fa8dc;
  flex: none;
  margin-top: 3px;
}

@media (max-width: 1080px) {
  .contact {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .visit {
    grid-template-columns: 1fr;
    gap: 32px;
  }
  .qr {
    flex-wrap: wrap;
  }
}

@media (max-width: 640px) {
  .phones {
    grid-template-columns: 1fr;
  }
  .formcard {
    padding: 26px 20px;
  }
  .field-row {
    grid-template-columns: 1fr;
  }
  .qr {
    gap: 16px;
  }
  .qr__img img {
    width: 148px;
    height: 197px;
  }
  .visit__card {
    padding: 26px 22px;
  }
}
</style>
