import { Link } from 'react-router-dom'

const Sidebar = () => (
  <aside className="w-64 border-r border-slate-800 bg-slate-950 p-6">
    <h2 className="mb-6 text-lg font-semibold">Dashboard</h2>
    <nav className="space-y-3 text-sm">
      <Link to="/dashboard" className="block text-slate-300 hover:text-white">Overview</Link>
      <Link to="/dashboard/projects" className="block text-slate-300 hover:text-white">Projects</Link>
      <Link to="/admin" className="block text-slate-300 hover:text-white">Admin</Link>
    </nav>
  </aside>
)

export default Sidebar
