import { useState } from 'react'
import { authApi } from '../services/api'

const Register = () => {
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [message, setMessage] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    setMessage('')
    try {
      await authApi.register({ email, password, full_name: fullName })
      setMessage('Compte créé. Vous pouvez vous connecter.')
    } catch (error) {
      setMessage(error.message)
    }
  }

  return (
    <section className="mx-auto max-w-md px-6 py-16">
      <div className="card">
        <h2 className="text-2xl font-semibold">Créer un compte</h2>
        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="text-sm text-slate-300">Nom complet</label>
            <input className="input" type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
          </div>
          <div>
            <label className="text-sm text-slate-300">Email</label>
            <input className="input" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div>
            <label className="text-sm text-slate-300">Mot de passe</label>
            <input className="input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button className="btn" type="submit">Créer</button>
          {message && <p className="text-sm text-slate-300">{message}</p>}
        </form>
      </div>
    </section>
  )
}

export default Register
