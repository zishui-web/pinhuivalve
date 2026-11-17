<script setup>
defineProps({
  table: { type: Object, required: true },
  compact: { type: Boolean, default: false }
})
</script>

<template>
  <div class="table-block">
    <div v-if="table.title" class="table-block__head">
      <h4>{{ table.title }}</h4>
      <span v-if="table.note" class="table-block__note">{{ table.note }}</span>
    </div>
    <div class="data-table-wrap">
      <div class="data-table-scroll">
        <table class="data-table">
          <thead>
            <tr>
              <th v-for="(c, i) in table.columns" :key="i">{{ c }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, ri) in table.rows" :key="ri">
              <td v-for="(cell, ci) in row" :key="ci">{{ cell }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <p class="table-scroll-hint">← 左右滑动查看完整表格 →</p>
  </div>
</template>

<style scoped>
.table-block + .table-block {
  margin-top: 34px;
}

.table-block__head {
  margin-bottom: 14px;
}

.table-block__head h4 {
  font-size: 16px;
  color: var(--ink);
  margin-bottom: 6px;
}

.table-block__note {
  display: block;
  font-size: 12.5px;
  color: var(--muted);
  line-height: 1.8;
}
</style>
