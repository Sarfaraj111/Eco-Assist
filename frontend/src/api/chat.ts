import axios from 'axios'
import type { ChatResponse } from '../types'

const API_BASE = '/api'

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
