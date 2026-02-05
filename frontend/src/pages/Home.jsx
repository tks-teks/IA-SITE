const Home = () => (
  <section className="mx-auto max-w-6xl px-6 py-16">
    <div className="grid gap-10 lg:grid-cols-2">
      <div>
        <p className="text-sm uppercase tracking-widest text-slate-400">Plateforme IA</p>
        <h1 className="mt-4 text-4xl font-bold text-white">
          Concevez des projets web complets avec une IA architecte.
        </h1>
        <p className="mt-6 text-slate-300">
          IA Site fournit une stack full-stack, une API sécurisée, une base de données et un tableau de bord
          pour piloter vos projets rapidement.
        </p>
        <div className="mt-8 flex gap-4">
          <button className="btn">Lancer un projet</button>
          <button className="rounded-md border border-slate-700 px-4 py-2 text-slate-200">Voir la démo</button>
        </div>
      </div>
      <div className="card">
        <h2 className="text-xl font-semibold">Fonctionnalités clés</h2>
        <ul className="mt-4 space-y-3 text-slate-300">
          <li>• Authentification sécurisée avec JWT</li>
          <li>• Dashboard admin avec statistiques</li>
          <li>• Gestion de projets avec recherche et pagination</li>
          <li>• UI responsive et moderne</li>
        </ul>
      </div>
    </div>
  </section>
)

export default Home
