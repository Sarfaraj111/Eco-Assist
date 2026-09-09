import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import type { Message } from '../types'
import SDGBadge from './SDGBadge'

interface ChatBubbleProps {
  message: Message
}

function TypingDots() {
  return (
    <div className="flex items-center gap-1 py-1">
      <span className="w-2 h-2 rounded-full bg-eco-400 animate-bounce [animation-delay:-0.3s]" />
      <span className="w-2 h-2 rounded-full bg-eco-400 animate-bounce [animation-delay:-0.15s]" />
      <span className="w-2 h-2 rounded-full bg-eco-400 animate-bounce" />
    </div>
  )
}

export default function ChatBubble({ message }: ChatBubbleProps) {
  const isUser = message.role === 'user'

  return (
    <div className={`flex gap-3 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
      {/* Avatar */}
      <div
        className={`flex-shrink-0 w-9 h-9 rounded-full flex items-center justify-center text-lg shadow-sm
          ${isUser ? 'bg-eco-600 text-white' : 'bg-white border-2 border-eco-200 text-eco-700'}`}
      >
        {isUser ? '👤' : '🌿'}
      </div>

      {/* Bubble */}
      <div
        className={`max-w-[80%] rounded-2xl px-4 py-3 shadow-sm
          ${isUser
            ? 'bg-eco-600 text-white rounded-tr-sm'
            : 'bg-white border border-gray-100 rounded-tl-sm text-gray-800'
          }`}
      >
        {message.isLoading ? (
          <TypingDots />
        ) : isUser ? (
          <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
        ) : (
          <>
            <div className="prose-eco text-sm leading-relaxed">
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {message.content}
              </ReactMarkdown>
            </div>

            {/* Sources */}
            {message.sources && message.sources.length > 0 && (
              <div className="mt-3 pt-3 border-t border-gray-100">
                <p className="text-xs font-semibold text-gray-400 uppercase tracking-wide mb-2">
                  📚 Sources
                </p>
                <div className="flex flex-wrap gap-1.5">
                  {message.sources.map((src, i) => (
                    <div
                      key={i}
                      className="bg-gray-50 border border-gray-200 rounded-lg px-2 py-1"
                    >
                      <p className="text-xs font-medium text-gray-700">{src.title}</p>
                      <SDGBadge sdg={src.sdg} />
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Timestamp */}
            <p className="text-xs text-gray-400 mt-2 text-right">
              {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </p>
          </>
        )}
      </div>
    </div>
  )
}
