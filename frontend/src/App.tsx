import { useEffect, useRef } from 'react'
import { useChat } from './hooks/useChat'
import Header from './components/Header'
import ChatBubble from './components/ChatBubble'
import ChatInput from './components/ChatInput'
import WelcomeScreen from './components/WelcomeScreen'

export default function App() {
  const { messages, isLoading, send, reset } = useChat()
  const bottomRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to latest message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  return (
    <div className="h-screen flex flex-col bg-gray-50 overflow-hidden">
      <Header onReset={reset} messageCount={messages.length} />

      {/* Chat area */}
      <main className="flex-1 overflow-hidden flex flex-col">
        {messages.length === 0 ? (
          <WelcomeScreen onSelectQuestion={send} />
        ) : (
          <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4 max-w-3xl mx-auto w-full">
            {messages.map(msg => (
              <ChatBubble key={msg.id} message={msg} />
            ))}
            <div ref={bottomRef} />
          </div>
        )}
      </main>

      {/* Input bar */}
      <footer className="flex-shrink-0 border-t border-gray-100 bg-white px-4 py-4">
        <div className="max-w-3xl mx-auto">
          <ChatInput onSend={send} disabled={isLoading} />
          <p className="text-xs text-gray-400 text-center mt-2">
            EcoAssist covers SDG 3 · SDG 11 · SDG 12 · SDG 13 &nbsp;·&nbsp;
            Press <kbd className="px-1 py-0.5 bg-gray-100 rounded text-xs">Enter</kbd> to send,{' '}
            <kbd className="px-1 py-0.5 bg-gray-100 rounded text-xs">Shift+Enter</kbd> for new line
          </p>
        </div>
      </footer>
    </div>
  )
}
