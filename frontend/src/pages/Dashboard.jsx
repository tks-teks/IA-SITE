import Sidebar from '../components/Sidebar'

const Dashboard = () => (
  <div className="flex min-h-[70vh]">
    <Sidebar />
    <div className="flex-1 px-8 py-10">
      <h2 className="text-2xl font-semibold">Vue d'ensemble</h2>
      <div className="mt-6 grid gap-6 md:grid-cols-2">
        <div className="card">
          <p className="text-sm text-slate-400">Projets actifs</p>
          <h3 className="mt-2 text-3xl font-bold">12</h3>
        </div>
        <div className="card">
          <p className="text-sm text-slate-400">Utilisateurs</p>
          <h3 className="mt-2 text-3xl font-bold">3</h3>
        </div>
      </div>
    </div>
  </div>
)

export default Dashboard
