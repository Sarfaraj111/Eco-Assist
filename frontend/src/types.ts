export interface Source {
  title: string
  sdg: string
  tags?: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  sources?: Source[]
  timestamp: Date
  isLoading?: boolean
}

export interface ChatResponse {
  answer: string
  sources: Source[]
  session_id: string
}

export const SDG_CONFIG = {
  'SDG 13': {
    label: 'Climate Action',
    emoji: '🌍',
    color: 'sdg-13',
    bg: 'bg-green-50',
    border: 'border-green-200',
    icon: '🌡️',
  },
  'SDG 11': {
    label: 'Sustainable Cities',
    emoji: '🏙️',
    color: 'sdg-11',
    bg: 'bg-amber-50',
    border: 'border-amber-200',
    icon: '🏗️',
  },
  'SDG 12': {
    label: 'Responsible Consumption',
    emoji: '♻️',
    color: 'sdg-12',
    bg: 'bg-yellow-50',
    border: 'border-yellow-200',
    icon: '🛍️',
  },
  'SDG 3': {
    label: 'Good Health',
    emoji: '💚',
    color: 'sdg-3',
    bg: 'bg-teal-50',
    border: 'border-teal-200',
    icon: '🏥',
  },
} as const

export type SDGKey = keyof typeof SDG_CONFIG

export const SUGGESTED_QUESTIONS = [
  { text: 'What are the main causes of air pollution in cities?', sdg: 'SDG 11' as SDGKey },
  { text: 'How does plastic pollution affect marine ecosystems?', sdg: 'SDG 12' as SDGKey },
  { text: 'What individual actions reduce carbon emissions the most?', sdg: 'SDG 13' as SDGKey },
  { text: 'How does air pollution affect human health?', sdg: 'SDG 3' as SDGKey },
  { text: 'What is the circular economy and why does it matter?', sdg: 'SDG 12' as SDGKey },
  { text: 'What is the Paris Agreement and its targets?', sdg: 'SDG 13' as SDGKey },
  { text: 'How can cities reduce the urban heat island effect?', sdg: 'SDG 11' as SDGKey },
  { text: 'What are PFAS chemicals and why are they dangerous?', sdg: 'SDG 3' as SDGKey },
]
