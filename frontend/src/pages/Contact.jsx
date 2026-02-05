const Contact = () => (
  <section className="mx-auto max-w-5xl px-6 py-16">
    <div className="card">
      <h2 className="text-2xl font-semibold">Contact</h2>
      <form className="mt-6 space-y-4">
        <div>
          <label className="text-sm text-slate-300">Email</label>
          <input className="input" type="email" placeholder="you@example.com" />
        </div>
        <div>
          <label className="text-sm text-slate-300">Message</label>
          <textarea className="input" rows="4" placeholder="Votre message" />
        </div>
        <button className="btn" type="button">Envoyer</button>
      </form>
    </div>
  </section>
)

export default Contact
