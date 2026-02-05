import { Link } from 'react-router-dom'

const Navbar = () => (
  <header className="border-b border-slate-800 bg-slate-950">
    <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
      <Link to="/" className="text-xl font-bold text-white">IA Site</Link>
      <div className="flex items-center gap-4 text-sm">
        <Link to="/about" className="text-slate-300 hover:text-white">About</Link>
        <Link to="/contact" className="text-slate-300 hover:text-white">Contact</Link>
        <Link to="/login" className="rounded-md border border-slate-700 px-3 py-2 text-slate-200">Login</Link>
        <Link to="/register" className="btn">Register</Link>
      </div>
    </nav>
  </header>
)

export default Navbar
