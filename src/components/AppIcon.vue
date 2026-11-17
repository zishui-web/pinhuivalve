<script setup>
defineProps({
  name: { type: String, required: true },
  size: { type: [Number, String], default: 24 },
  stroke: { type: [Number, String], default: 1.5 }
})

const paths = {
  phone: 'M6.6 3.5h2.2l1.6 4-2 1.3a11.5 11.5 0 0 0 5.3 5.3l1.3-2 4 1.6v2.2a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.6 5.7a2 2 0 0 1 2-2.2Z',
  mail: 'M3.5 6h17v12h-17zM3.5 6l8.5 6.5L20.5 6',
  pin: 'M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z M12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z',
  arrow: 'M4 12h15M13 6l6 6-6 6',
  chevron: 'M9 5l7 7-7 7',
  chevronDown: 'M5 9l7 7 7-7',
  menu: 'M4 7h16M4 12h16M4 17h16',
  close: 'M6 6l12 12M18 6L6 18',
  shield: 'M12 3l7.5 3v6c0 4.6-3.1 8-7.5 9.4C7.6 20 4.5 16.6 4.5 12V6L12 3Z M8.6 12.2l2.4 2.4 4.4-4.6',
  valve: 'M4 8h16v3H4zM4 13h16v3H4z M9 8V5.5A2.5 2.5 0 0 1 14 6 M12 3v3',
  box: 'M12 3l8 4.2v9.6L12 21l-8-4.2V7.2L12 3Z M4 7.2l8 4.3 8-4.3M12 11.5V21',
  headset: 'M4 13v-2a8 8 0 0 1 16 0v2 M4 13h3v6H5.5A1.5 1.5 0 0 1 4 17.5V13Z M20 13h-3v6h1.5a1.5 1.5 0 0 0 1.5-1.5V13Z M17 19v1a2 2 0 0 1-2 2h-3',
  factory: 'M3 20V10l5 3V10l5 3V6l5 3v11H3Z M7 20v-3M11 20v-3M15 20v-3',
  drop: 'M12 3.5S6 10 6 14a6 6 0 0 0 12 0c0-4-6-10.5-6-10.5Z',
  flask: 'M9 3h6 M10 3v6L5 19a1.6 1.6 0 0 0 1.4 2.3h11.2A1.6 1.6 0 0 0 19 19l-5-10V3',
  bolt: 'M13.5 3 6 13.5h4.5L10 21l7.5-10.5H13L13.5 3Z',
  gear: 'M12 15.2a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4Z M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-2.9 1.2 2 2 0 1 1-4 0 1.7 1.7 0 0 0-2.9-1.2l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1A1.7 1.7 0 0 0 3 15a2 2 0 1 1 0-4 1.7 1.7 0 0 0 1.4-2.9l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1A1.7 1.7 0 0 0 10 4a2 2 0 1 1 4 0 1.7 1.7 0 0 0 2.9 1.4l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1A1.7 1.7 0 0 0 21 11a2 2 0 1 1 0 4Z',
  layers: 'M12 3 3 8l9 5 9-5-9-5Z M3 13l9 5 9-5 M3 17.5l9 5 9-5',
  check: 'M5 12.5l4.5 4.5L19 7',
  ruler: 'M3 9h18v6H3z M7 9v3M11 9v3M15 9v3M19 9v3',
  book: 'M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5V5.5Z M20 18v3H6.5A2.5 2.5 0 0 1 4 18.5',
  wrench: 'M14.5 6a4 4 0 1 0 5 5L21 9l-3-3-1 1-2-2 1-1-1.5-1.5L14.5 6Z M13 9 4 18a2 2 0 0 0 3 3l9-9',
  search: 'M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14Z M16.2 16.2 21 21',
  wechat: 'M9.5 4C5.4 4 2 6.7 2 10c0 1.9 1.1 3.6 2.8 4.7L4 17.5l3-1.6c.8.2 1.6.3 2.5.3 M15.5 9c-3.6 0-6.5 2.3-6.5 5.2 0 2.9 2.9 5.2 6.5 5.2.8 0 1.6-.1 2.3-.3l2.7 1.4-.6-2.4c1.4-.9 2.3-2.4 2.3-3.9C21.7 11.3 18.9 9 15.5 9Z'
}
</script>

<template>
  <svg
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    :stroke-width="stroke"
    stroke="currentColor"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
  >
    <path :d="paths[name] || paths.check" />
  </svg>
</template>
