import type { SDGKey } from '../types'
import { SDG_CONFIG } from '../types'

interface SDGBadgeProps {
  sdg: string
  size?: 'sm' | 'md'
}

function parsePrimarySDG(sdgString: string): SDGKey | null {
  const keys = Object.keys(SDG_CONFIG) as SDGKey[]
  for (const key of keys) {
    if (sdgString.includes(key)) return key
  }
  return null
}

export default function SDGBadge({ sdg, size = 'sm' }: SDGBadgeProps) {
  const key = parsePrimarySDG(sdg)
  if (!key) return null

  const config = SDG_CONFIG[key]
  const sizeClass = size === 'md' ? 'px-3 py-1 text-sm' : 'px-2 py-0.5 text-xs'

  return (
    <span className={`sdg-badge ${config.color} ${sizeClass}`}>
      <span>{config.emoji}</span>
      <span>{key}</span>
      <span className="opacity-70">– {config.label}</span>
    </span>
  )
}
