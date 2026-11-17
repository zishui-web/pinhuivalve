// 数据自检：列数一致性 + 法兰尺寸与样本册法兰表交叉核对
import { products, categories } from '../src/data/products.js'
import { flangeTables } from '../src/data/support.js'

let errors = 0
let warnings = 0
const fail = (msg) => {
  errors++
  console.log('  ✗ ' + msg)
}
const warn = (msg) => {
  warnings++
  console.log('  ! ' + msg)
}

console.log('产品数：', products.length)

for (const p of products) {
  const cat = categories.find((c) => c.id === p.category)
  if (!cat) fail(`${p.slug} 分类不存在: ${p.category}`)
  if (!p.image) fail(`${p.slug} 缺少主图`)
  for (const d of p.dimensions || []) {
    if (!d.rows.length) continue
    const bad = d.rows.filter((r) => r.length !== d.columns.length)
    if (bad.length) fail(`${p.slug} 「${d.title}」有 ${bad.length} 行列数 ≠ 列数 ${d.columns.length}`)
  }
  if (!p.specs?.length) fail(`${p.slug} 缺少技术参数`)
  if (!p.features?.length) fail(`${p.slug} 缺少特点`)
}

const flangeMap = {}
for (const t of flangeTables) {
  if (t.id === 'class150') continue
  const pn = t.id === 'pn10' ? 1.0 : t.id === 'pn16' ? 1.6 : 0.6
  flangeMap[pn] = Object.fromEntries(t.rows.map((r) => [r[0], { D1: r[2], D2: r[3], NM: r[4] }]))
}

// 样本册内部已知差异（产品尺寸表与法兰附录表印刷不一致），订单以产品尺寸表为准
const KNOWN_DIFF = new Set([
  'pz73-pz43|1.6|50|D2',
  'pz73-pz43|1.6|250|D2',
  'pz73-pz43|1.6|500|D2',
  'pz73-pz43|1.6|600|D2',
  'pz73-pz43|1.6|900|D2',
  'pz73-pz43|1|800|D2',
  'pz73-pz43|1|900|D2',
  'dmz73|1.6|50|D2',
  'dmz73|1.6|250|D2',
  'dmz73|1.6|500|D2',
  'dmz73|1.6|600|D2',
  'dmz73|1.6|900|D2',
  'dmz73|1|800|D2',
  'pz73-pz43|1.6|250|n-m',
  'pz73-pz43|1.6|300|n-m',
  'pz73-pz43|1.6|350|n-m',
  'pz73-pz43|1.6|600|n-m',
  'pz73-pz43|1.6|700|n-m',
  'dmz73|1.6|250|n-m',
  'dmz73|1.6|300|n-m',
  'dmz73|1.6|350|n-m',
  'dmz73|1.6|600|n-m',
  'dmz73|1.6|700|n-m',
  'dmz73|1|900|D2'
])

const check = (slug, pn, dimIdx) => {
  const p = products.find((x) => x.slug === slug)
  const t = p.dimensions[dimIdx]
  const ref = flangeMap[pn]
  const key = (name) => t.columns.findIndex((c) => c.replace(/\s/g, '').toLowerCase() === name)
  const iDN = key('dn')
  const iD1 = key('d1')
  const iD2 = key('d2')
  const iNM = t.columns.findIndex((c) => /^n-?m$/i.test(c.replace(/\s/g, '')))
  let n = 0
  for (const r of t.rows) {
    const dn = r[iDN]
    const refRow = ref[dn]
    if (!refRow) continue
    n++
    for (const [label, idx, refVal] of [
      ['D1', iD1, refRow.D1],
      ['D2', iD2, refRow.D2],
      ['n-m', iNM, refRow.NM]
    ]) {
      if (idx < 0) continue
      if (r[idx] !== refVal) {
        const k = `${slug}|${pn}|${dn}|${label}`
        if (KNOWN_DIFF.has(k)) warn(`${slug} PN${pn} DN${dn} ${label}=${r[idx]}（法兰表 ${refVal}，样本册内部差异，按产品表）`)
        else fail(`${slug} PN${pn} DN${dn} ${label}=${r[idx]} 与法兰表 ${refVal} 不符`)
      }
    }
  }
  console.log(`  ${slug} PN${pn}: 核对 ${n} 行`)
}

console.log('\n法兰交叉核对：')
check('pz73-pz43', 1.0, 0)
check('pz73-pz43', 1.6, 1)
check('dmz73', 1.0, 0)
check('dmz73', 1.6, 1)
check('ggg40-slurry', 1.0, 0)

console.log(
  errors === 0
    ? `\n✓ 检查通过（${warnings} 处样本册内部差异，已在页面注明）`
    : `\n✗ 共 ${errors} 处问题`
)
process.exit(errors ? 1 : 0)
