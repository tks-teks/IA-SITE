import { useState } from 'react'
import Sidebar from '../components/Sidebar'
import { adminApi } from '../services/api'

const Admin = () => {
  const [stats, setStats] = useState(null)
  const [message, setMessage] = useState('')
  const token = localStorage.getItem('access_token')

  const handleLoad = async () => {
    setMessage('')
    try {
      const data = await adminApi.stats(token)
      setStats(data)
    } catch (error) {
      setMessage(error.message)
    }
  }

  return (
    <div className="flex min-h-[70vh]">
      <Sidebar />
      <div className="flex-1 px-8 py-10">
        <h2 className="text-2xl font-semibold">Admin</h2>
        <button className="btn mt-6" onClick={handleLoad}>Charger les stats</button>
        {message && <p className="mt-3 text-sm text-slate-400">{message}</p>}
        {stats && (
          <div className="mt-6 grid gap-6 md:grid-cols-2">
            <div className="card">
              <p className="text-sm text-slate-400">Utilisateurs</p>
              <h3 className="mt-2 text-3xl font-bold">{stats.users}</h3>
            </div>
            <div className="card">
              <p className="text-sm text-slate-400">Projets</p>
              <h3 className="mt-2 text-3xl font-bold">{stats.projects}</h3>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Admin
