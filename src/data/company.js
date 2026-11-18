// 企业基础信息 —— 全部来自 素材/官网介绍 与 样本册（不编造）
export const company = {
  name: '浙江品汇阀门有限公司',
  nameEn: 'ZHEJIANG PINHUI VALVE CO., LTD.',
  brand: '品汇阀门',
  brandEn: 'PINHUI VALVE',
  slogan: '专业 成就品质典范',
  sloganEn: 'PROFESSIONAL · QUALITY · TRUST',
  shortIntro:
    '坐落于“中国泵阀之乡”温州永嘉，专业生产刀型闸阀、浆液阀、矿浆阀、纸浆阀、排渣阀、非标闸门与陶瓷闸阀，集设计、开发、生产、销售、服务于一体。',
  introParagraphs: [
    '浙江品汇阀门有限公司座落于中国“泵阀之乡”——浙江温州永嘉，是一家专业生产刀型闸阀、浆液阀、矿浆阀、纸浆阀、排渣阀、非标闸门、陶瓷闸阀等系列产品的企业，是集设计、开发、生产、销售、服务为一体的阀门专业制造商。公司拥有先进的设计和精良的生产与检测设备，以及成熟的制造工艺技术，为客户提供完美的产品。',
    '公司始终如一致力于科技创新，努力开发新产品，能按照 API、NF、DIN、BS、JIS、GB 等国内外行业标准生产，产品规格从 50mm–2000mm 及 2"~24"，工作压力从 0.6MPa~2.5MPa 及 150Lb~300Lb，工作温度 -80℃~900℃，驱动形式有手动、齿轮传动、电动、气动和液动。产品主体材料采用铸铁、铸钢、不锈钢（316、304、2520）等。多年来产品广泛应用于电力、石油、化工、造纸、城建、污水环保工程、轻工化纤、冶金、水泥厂等行业，并可根据客户特殊需求冶炼和制造非标产品。',
    '本公司以科技为先导，以质量为根本；以诚信服务为宗旨，以合理的价位取向用户的信任，我们将以“不求最好，只求更好”的精神，向广大顾客提供满意的产品和服务。公司不断地推出性能优越、经济实用的高品质阀门，竭诚欢迎国内外用户来我公司参观考察，洽谈业务，互利合作，共创佳绩！'
  ],
  // 均出自样本册「企业简介」与「产品特点」页，可核对
  facts: [
    { value: '50–2000', unit: 'mm', label: '通径范围', sub: '2" ~ 24"' },
    { value: '0.6–2.5', unit: 'MPa', label: '工作压力', sub: '150Lb ~ 300Lb' },
    { value: '−80~900', unit: '℃', label: '工作温度', sub: '按材质与密封组合' },
    { value: '6', unit: '大系列', label: '产品体系', sub: '21+ 型号可选' }
  ],
  standards: ['API', 'NF', 'DIN', 'BS', 'JIS', 'GB'],
  materials: ['铸铁', '铸钢', '不锈钢 304', '不锈钢 316', '不锈钢 2520'],
  drives: ['手动', '齿轮传动', '电动', '气动', '液动'],
  industries: [
    { name: '电力', icon: 'power' },
    { name: '石油', icon: 'oil' },
    { name: '化工', icon: 'chemical' },
    { name: '造纸', icon: 'paper' },
    { name: '城建', icon: 'city' },
    { name: '污水环保', icon: 'water' },
    { name: '轻工化纤', icon: 'fiber' },
    { name: '冶金', icon: 'metallurgy' },
    { name: '水泥', icon: 'cement' },
    { name: '矿山', icon: 'mine' }
  ],
  businessScope: [
    '普通阀门和旋塞制造（不含特种设备制造）；阀门和旋塞销售',
    '工业自动控制系统装置制造、销售',
    '液气密元件及系统制造',
    '泵及真空设备制造、销售；通用设备制造（不含特种设备制造）',
    '智能仪器仪表制造、销售；五金产品制造、零售',
    '许可项目：货物进出口；技术进出口'
  ],
  contacts: [
    { title: '销售咨询', name: '郭经理', phone: '13868399046' },
    { title: '销售咨询', name: '许经理', phone: '15057598392' }
  ],
  address: '浙江省温州市永嘉县瓯北街道马岙村',
  addressFull: '浙江省温州市永嘉县瓯北街道马岙村（马岙工业区）',
  // 样本册封底同样标注该厂区地址
  addressNote: '中国泵阀之乡 · 永嘉瓯北',
  wechats: [
    { image: '/images/wechat-1.png', label: '微信咨询 一' },
    { image: '/images/wechat-2.png', label: '微信咨询 二' }
  ]
}

export const advantages = [
  {
    title: '品质把控',
    en: 'QUALITY CONTROL',
    desc: '从铸件入厂到成品试压，逐台进行壳体与密封试验，出厂前完成启闭动作检验。'
  },
  {
    title: '产品专业',
    en: 'FOCUSED PRODUCTS',
    desc: '专注刀型闸阀、浆液阀、穿透式插板阀、陶瓷阀门与闸门，规格覆盖 DN50–DN2000。'
  },
  {
    title: '稳定供应',
    en: 'STABLE SUPPLY',
    desc: '机加工、装配、库存一体化组织，常规规格现货供应，非标产品可按图定制。'
  },
  {
    title: '贴心服务',
    en: 'TECHNICAL SERVICE',
    desc: '提供选型建议、安装指导与使用维护说明，气动输送与粉料工况可专项对接。'
  }
]

export const supportTopics = [
  {
    title: '阀座结构',
    en: 'SEAT STRUCTURE',
    desc: '金属硬密封、橡胶/四氟软密封、双向密封（X 结构）等多种阀座形式，可视介质与工况选配。',
    to: '/support#seat'
  },
  {
    title: '法兰安装尺寸',
    en: 'FLANGE DIMENSIONS',
    desc: 'GB/T 79 PN0.6 / 1.0 / 1.6MPa 凸面 RF 与美标 Class 150 法兰尺寸表。',
    to: '/support#flange'
  },
  {
    title: '使用注意事项',
    en: 'INSTALLATION',
    desc: '安装方位推荐、螺栓组合、单向密封阀的介质流向与对夹连接要求。',
    to: '/support#install'
  },
  {
    title: '预防措施',
    en: 'MAINTENANCE',
    desc: '填料压块的逐步拧紧、阀杆套管润滑、大口径执行器支架的设置要点。',
    to: '/support#maintenance'
  }
]
