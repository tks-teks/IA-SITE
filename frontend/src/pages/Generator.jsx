import { useState } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const Generator = () => {
  const [projectName, setProjectName] = useState('')
  const [description, setDescription] = useState('')
  const [resource, setResource] = useState('projets')
  const [response, setResponse] = useState(null)
  const [message, setMessage] = useState('')

  const handleGenerate = async (event) => {
    event.preventDefault()
    setMessage('')
    setResponse(null)
    try {
      const res = await fetch(`${API_URL}/ai/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          project_name: projectName,
          description,
          primary_resource: resource
        })
      })
      if (!res.ok) {
        const error = await res.json().catch(() => ({}))
        throw new Error(error.detail || 'Erreur génération')
      }
      const data = await res.json()
      setResponse(data)
    } catch (error) {
      setMessage(error.message)
    }
  }

  return (
    <section className="mx-auto max-w-5xl px-6 py-16">
      <div className="card">
        <h2 className="text-2xl font-semibold">Générateur IA</h2>
        <p className="mt-2 text-slate-300">
          Décrivez votre projet et générez un squelette complet (UI + API + DB + déploiement).
        </p>
        <form className="mt-6 space-y-4" onSubmit={handleGenerate}>
          <div>
            <label className="text-sm text-slate-300">Nom du projet</label>
            <input className="input" value={projectName} onChange={(e) => setProjectName(e.target.value)} required />
          </div>
          <div>
            <label className="text-sm text-slate-300">Description</label>
            <textarea className="input" rows="4" value={description} onChange={(e) => setDescription(e.target.value)} required />
          </div>
          <div>
            <label className="text-sm text-slate-300">Ressource principale</label>
            <input className="input" value={resource} onChange={(e) => setResource(e.target.value)} />
          </div>
          <button className="btn" type="submit">Générer</button>
          {message && <p className="text-sm text-slate-300">{message}</p>}
        </form>
      </div>
      {response && (
        <div className="mt-8 card">
          <h3 className="text-lg font-semibold">Résumé</h3>
          <p className="mt-2 text-slate-300">{response.summary}</p>
          <h4 className="mt-4 text-sm uppercase text-slate-400">Fichiers générés</h4>
          <ul className="mt-3 space-y-2 text-sm text-slate-300">
            {response.files.map((file) => (
              <li key={file.path} className="rounded-md border border-slate-800 p-3">
                <p className="font-semibold">{file.path}</p>
                <pre className="mt-2 whitespace-pre-wrap text-xs text-slate-400">{file.content}</pre>
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  )
}

export default Generator
