import { useEffect, useState } from 'react'
import Sidebar from '../components/Sidebar'
import { projectApi } from '../services/api'

const Projects = () => {
  const [projects, setProjects] = useState([])
  const [query, setQuery] = useState('')
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')
  const token = localStorage.getItem('access_token')

  const loadProjects = async () => {
    if (!token) return
    try {
      const data = await projectApi.list(token, query)
      setProjects(data)
    } catch (error) {
      setMessage(error.message)
    }
  }

  useEffect(() => {
    loadProjects()
  }, [])

  const handleCreate = async (event) => {
    event.preventDefault()
    setMessage('')
    try {
      await projectApi.create(token, { name, description: 'Nouveau projet' })
      setName('')
      loadProjects()
    } catch (error) {
      setMessage(error.message)
    }
  }

  return (
    <div className="flex min-h-[70vh]">
      <Sidebar />
      <div className="flex-1 px-8 py-10">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <h2 className="text-2xl font-semibold">Projets</h2>
          <form className="flex gap-2" onSubmit={(e) => { e.preventDefault(); loadProjects() }}>
            <input className="input" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Rechercher" />
            <button className="btn" type="submit">Search</button>
          </form>
        </div>

        <div className="mt-6 grid gap-6 md:grid-cols-2">
          <div className="card">
            <h3 className="text-lg font-semibold">Créer un projet</h3>
            <form className="mt-4 space-y-3" onSubmit={handleCreate}>
              <input className="input" value={name} onChange={(e) => setName(e.target.value)} placeholder="Nom" required />
              <button className="btn" type="submit">Créer</button>
            </form>
            {message && <p className="mt-3 text-sm text-slate-400">{message}</p>}
          </div>
          <div className="card">
            <h3 className="text-lg font-semibold">Liste</h3>
            <ul className="mt-4 space-y-3 text-slate-300">
              {projects.length === 0 && <li>Aucun projet pour le moment.</li>}
              {projects.map((project) => (
                <li key={project.id} className="rounded-md border border-slate-800 p-3">
                  <p className="font-semibold">{project.name}</p>
                  <p className="text-xs text-slate-400">{project.status}</p>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Projects
