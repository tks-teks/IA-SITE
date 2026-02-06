import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import Login from './pages/Login'
import Register from './pages/Register'
import Generator from './pages/Generator'
import Dashboard from './pages/Dashboard'
import Projects from './pages/Projects'
import Admin from './pages/Admin'

const App = () => (
  <div className="flex min-h-screen flex-col bg-navy text-white">
    <Navbar />
    <main className="flex-1">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/generator" element={<Generator />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/dashboard/projects" element={<Projects />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </main>
    <Footer />
  </div>
)

export default App
