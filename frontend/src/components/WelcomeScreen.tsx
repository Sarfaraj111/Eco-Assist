import { SDG_CONFIG, SUGGESTED_QUESTIONS } from '../types'
import type { SDGKey } from '../types'

interface WelcomeScreenProps {
  onSelectQuestion: (question: string) => void
}

function SDGPill({ sdgKey }: { sdgKey: SDGKey }) {
  const config = SDG_CONFIG[sdgKey]
  return (
    <div className={`flex items-center gap-2 ${config.bg} border ${config.border} rounded-xl p-3`}>
      <span className="text-2xl">{config.emoji}</span>
      <div>
        <p className="text-xs font-bold text-gray-700">{sdgKey}</p>
        <p className="text-xs text-gray-500">{config.label}</p>
      </div>
    </div>
  )
}

export default function WelcomeScreen({ onSelectQuestion }: WelcomeScreenProps) {
  return (
    <div className="flex-1 overflow-y-auto flex flex-col items-center justify-center px-6 py-10 gap-8">
      {/* Hero */}
      <div className="text-center max-w-xl">
        <div className="text-6xl mb-4">🌿</div>
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Welcome to <span className="text-eco-600">EcoAssist</span>
        </h1>
        <p className="text-gray-500 text-base leading-relaxed">
          Your AI-powered guide to <strong>pollution awareness</strong> and{' '}
          <strong>sustainable development</strong>. Ask me anything about climate change,
          air &amp; water pollution, sustainable cities, health impacts, and more.
        </p>
      </div>

      {/* SDG Grid */}
      <div className="w-full max-w-xl">
        <p className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3 text-center">
          Covering these SDGs
        </p>
        <div className="grid grid-cols-2 gap-3">
          {(Object.keys(SDG_CONFIG) as SDGKey[]).map(key => (
            <SDGPill key={key} sdgKey={key} />
          ))}
        </div>
      </div>

      {/* Suggested Questions */}
      <div className="w-full max-w-xl">
        <p className="text-xs font-semibold text-gray-400 uppercase tracking-widest mb-3 text-center">
          Try asking...
        </p>
        <div className="flex flex-col gap-2">
          {SUGGESTED_QUESTIONS.map((q, i) => {
            const config = SDG_CONFIG[q.sdg]
            return (
              <button
                key={i}
                onClick={() => onSelectQuestion(q.text)}
                className={`text-left px-4 py-3 rounded-xl border text-sm text-gray-700
                  hover:shadow-md transition-all group
                  ${config.bg} ${config.border} hover:border-eco-300`}
              >
                <span className="mr-2 opacity-70">{config.emoji}</span>
                {q.text}
                <span className="ml-2 text-eco-500 opacity-0 group-hover:opacity-100 transition-opacity">→</span>
              </button>
            )
          })}
        </div>
      </div>
    </div>
  )
}
