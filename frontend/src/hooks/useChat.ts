import { useState, useCallback } from 'react'
import { v4 as uuidv4 } from 'uuid'
import type { Message } from '../types'
import { sendMessage, resetConversation } from '../api/chat'

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([])
  const [sessionId, setSessionId] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(false)

  const send = useCallback(async (question: string) => {
    if (isLoading) return

    const userMsg: Message = {
      id: uuidv4(),
      role: 'user',
      content: question,
      timestamp: new Date(),
    }

    const loadingMsg: Message = {
      id: uuidv4(),
      role: 'assistant',
      content: '',
      timestamp: new Date(),
      isLoading: true,
    }

    setMessages(prev => [...prev, userMsg, loadingMsg])
    setIsLoading(true)

    try {
      const response = await sendMessage(question, sessionId)

      if (!sessionId) {
        setSessionId(response.session_id)
      }

      setMessages(prev =>
        prev.map(m =>
          m.id === loadingMsg.id
            ? {
                ...m,
                content: response.answer,
                sources: response.sources,
                isLoading: false,
                timestamp: new Date(),
              }
            : m
        )
      )
    } catch (err: unknown) {
      const errorText =
        err instanceof Error
          ? err.message
          : 'Something went wrong. Please check that the backend server is running.'

      setMessages(prev =>
        prev.map(m =>
          m.id === loadingMsg.id
            ? {
                ...m,
                content: `❌ **Error:** ${errorText}\n\nMake sure the Python backend is running on port 8000.`,
                isLoading: false,
                timestamp: new Date(),
              }
            : m
        )
      )
    } finally {
      setIsLoading(false)
    }
  }, [isLoading, sessionId])

  const reset = useCallback(async () => {
    try {
      await resetConversation(sessionId)
    } catch {
      // ignore
    }
    setMessages([])
    setSessionId(null)
  }, [sessionId])

  return { messages, isLoading, send, reset }
}
