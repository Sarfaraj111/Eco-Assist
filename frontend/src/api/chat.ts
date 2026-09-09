import axios from 'axios'
import type { ChatResponse } from '../types'

// In production (Vercel), VITE_API_URL is set to the Render backend URL.
// In dev, the Vite proxy forwards /api → http://localhost:8000.
const API_BASE = import.meta.env.VITE_API_URL
  ? `${import.meta.env.VITE_API_URL}/api`
  : '/api'

export async function sendMessage(
  question: string,
  sessionId: string | null
): Promise<ChatResponse> {
  const response = await axios.post<ChatResponse>(`${API_BASE}/chat`, {
    question,
    session_id: sessionId,
  })
  return response.data
}

export async function resetConversation(sessionId: string | null): Promise<void> {
  await axios.post(`${API_BASE}/reset`, { session_id: sessionId })
}
