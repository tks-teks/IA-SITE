const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const request = async (path, options = {}) => {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    },
    ...options
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({}))
    throw new Error(error.detail || 'Une erreur est survenue')
  }
  return response.json()
}

export const authApi = {
  register: (payload) => request('/auth/register', { method: 'POST', body: JSON.stringify(payload) }),
  login: (payload) =>
    request('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ username: payload.email, password: payload.password })
    }),
  refresh: (token) => request(`/auth/refresh?token=${token}`, { method: 'POST' })
}

export const projectApi = {
  list: (token, query = '') =>
    request(`/projects/?query=${encodeURIComponent(query)}`, {
      headers: { Authorization: `Bearer ${token}` }
    }),
  create: (token, payload) =>
    request('/projects', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      body: JSON.stringify(payload)
    })
}

export const adminApi = {
  stats: (token) =>
    request('/admin/stats', {
      headers: { Authorization: `Bearer ${token}` }
    })
}
