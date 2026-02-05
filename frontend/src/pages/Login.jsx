import { useState } from 'react'
import { authApi } from '../services/api'

const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    setMessage('')
    try {
      const data = await authApi.login({ email, password })
      localStorage.setItem('access_token', data.access_token)
      localStorage.setItem('refresh_token', data.refresh_token)
      setMessage('Connexion réussie.')
    } catch (error) {
      setMessage(error.message)
    }
  }

  return (
    <section className="mx-auto max-w-md px-6 py-16">
      <div className="card">
        <h2 className="text-2xl font-semibold">Connexion</h2>
        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="text-sm text-slate-300">Email</label>
            <input className="input" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div>
            <label className="text-sm text-slate-300">Mot de passe</label>
            <input className="input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button className="btn" type="submit">Se connecter</button>
          {message && <p className="text-sm text-slate-300">{message}</p>}
        </form>
      </div>
    </section>
  )
}

export default Login
