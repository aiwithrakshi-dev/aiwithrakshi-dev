import { useEffect, useMemo, useRef, useState } from 'react'
import { profile, areas, products, process } from './data/profile'
type Tool = { n: string; d: string; c: string; l?: string; b?: string }
const BASE = import.meta.env.BASE_URL

/* Icons from Magnific stock, drawn as a mask so they take the text colour */
function MIcon({ name, size = 22, label }: { name: string; size?: number; label?: string }) {
  const url = `url(${BASE}icons/${name}.svg)`
  return (
    <span
      className="micon"
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={label ? undefined : true}
      style={{ width: size, height: size, WebkitMaskImage: url, maskImage: url }}
    />
  )
}

/* Reveal sections as they scroll into view */
function useReveal() {
  useEffect(() => {
    const els = document.querySelectorAll('.reveal')
    if (!('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('in')); return }
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target) } })
    }, { threshold: 0.15 })
    els.forEach(e => io.observe(e))
    return () => io.disconnect()
  }, [])
}

function useClock() {
  const [now, setNow] = useState(() => new Date())
  useEffect(() => { const t = setInterval(() => setNow(new Date()), 30_000); return () => clearInterval(t) }, [])
  const fmt = new Intl.DateTimeFormat('en-IN', { hour: '2-digit', minute: '2-digit', hour12: true, timeZone: 'Asia/Kolkata' })
  const hour = Number(new Intl.DateTimeFormat('en-IN', { hour: 'numeric', hour12: false, timeZone: 'Asia/Kolkata' }).format(now))
  return { time: fmt.format(now), hour }
}

function CountUp({ to, suffix = '', decimals = 0 }: { to: number; suffix?: string; decimals?: number }) {
  const [v, setV] = useState(0)
  const ref = useRef<HTMLSpanElement>(null)
  useEffect(() => {
    const el = ref.current
    if (!el) return
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduce) { setV(to); return }
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return
      io.disconnect()
      const start = performance.now()
      const tick = (t: number) => {
        const p = Math.min(1, (t - start) / 1300)
        setV(to * (1 - Math.pow(1 - p, 3)))
        if (p < 1) requestAnimationFrame(tick)
      }
      requestAnimationFrame(tick)
    }, { threshold: 0.6 })
    io.observe(el)
    return () => io.disconnect()
  }, [to])
  return <span ref={ref}>{v.toFixed(decimals)}{suffix}</span>
}

const NAV = [
  { id: 'home', label: 'Home' },
  { id: 'about', label: 'About' },
  { id: 'work', label: 'Work' },
  { id: 'process', label: 'Process' },
  { id: 'stack', label: 'AI Stack' },
  { id: 'contact', label: 'Contact' },
]

function Nav() {
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState('home')
  useEffect(() => {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) setActive(e.target.id) })
    }, { rootMargin: '-45% 0px -50% 0px' })
    NAV.forEach(n => { const el = document.getElementById(n.id); if (el) io.observe(el) })
    return () => io.disconnect()
  }, [])
  return (
    <header className="nav-wrap">
      <nav className="nav glass" aria-label="Main">
        <button className="burger" aria-label={open ? 'Close menu' : 'Open menu'} aria-expanded={open} onClick={() => setOpen(o => !o)}>
          <span /><span /><span />
        </button>
        <a href="#home" className="brand">R<span>.</span></a>
        <ul className={open ? 'open' : ''}>
          {NAV.map(n => (
            <li key={n.id}>
              <a href={`#${n.id}`} className={active === n.id ? 'on' : ''} onClick={() => setOpen(false)}>{n.label}</a>
            </li>
          ))}
        </ul>
        <a className="nav-cta" href="#contact">Let's talk</a>
      </nav>
      <div className="tab-plate" aria-hidden="true">PORTFOLIO</div>
    </header>
  )
}

function ControlCenter() {
  const [state, setState] = useState({ agents: true, auto: true, online: true, secure: true })
  const items: { key: keyof typeof state; icon: string; label: string; on: string; off: string; tone: string }[] = [
    { key: 'agents', icon: 'ai', label: 'AI agents', on: 'Running', off: 'Paused', tone: '#7c3aed' },
    { key: 'auto', icon: 'bot', label: 'Automations', on: 'On', off: 'Off', tone: '#16a34a' },
    { key: 'online', icon: 'wifi', label: 'Availability', on: 'Open to work', off: 'Busy', tone: '#2563eb' },
    { key: 'secure', icon: 'fingerprint', label: 'Secure build', on: 'Enabled', off: 'Off', tone: '#0891b2' },
  ]
  return (
    <div className="widget cc glass" aria-label="Control center">
      {items.map(it => (
        <button
          key={it.key}
          className={`toggle ${state[it.key] ? 'on' : ''}`}
          style={{ ['--tone' as string]: it.tone }}
          aria-pressed={state[it.key]}
          onClick={() => setState(s => ({ ...s, [it.key]: !s[it.key] }))}
        >
          <span className="dot"><MIcon name={it.icon} size={20} /></span>
          <span className="tl"><b>{it.label}</b><small>{state[it.key] ? it.on : it.off}</small></span>
        </button>
      ))}
    </div>
  )
}

function Hero() {
  const { time, hour } = useClock()
  const greet = hour < 12 ? 'Good morning' : hour < 17 ? 'Good afternoon' : 'Good evening'
  return (
    <section id="home" className="hero">
      <aside className="rail glass" aria-label="Quick links">
        <a href="#about" className="rail-aa" aria-label="About">Aa</a>
        <a href="#stack" aria-label="AI stack"><MIcon name="ai" size={24} /></a>
        <a href="#work" aria-label="Work"><MIcon name="bot" size={24} /></a>
        <a href="#process" aria-label="Process"><MIcon name="fingerprint" size={24} /></a>
        <a href="#contact" aria-label="Contact"><MIcon name="bell" size={22} /></a>
        <span className="rail-line" />
      </aside>

      <div className="stage glass">
        <div className="stage-top">
          <div className="mini-profile">
            <img src={`${BASE}img/avatar-square.webp`} alt="" width="64" height="64" />
            <div>
              <b>{profile.name}</b>
              <span><i className="pulse" /> New post · @AIwithRakshith</span>
            </div>
          </div>
          <div className="dots" aria-hidden="true"><i /><i /><i /></div>
        </div>

        <div className="portfolio-word" aria-hidden="true">Portfolio</div>

        <div className="disciplines" aria-label="Disciplines">
          {profile.disciplines.map(d => <span key={d}>{d}</span>)}
        </div>

        <img className="avatar" src={`${BASE}img/avatar-cutout.webp`} alt="Illustrated avatar of Rakshith" width="812" height="1200" />

        <div className="title-block">
          <h1 className="chrome">RAKSHITH</h1>
          <p className="hello">{profile.role}</p>
          <p className="lede">{profile.tagline}</p>
          <p className="loc"><span aria-hidden="true">📍</span> {profile.location}</p>
          <div className="hero-ctas">
            <a className="btn primary" href="#work">See my work</a>
            <a className="btn ghost" href="#stack">My AI stack</a>
          </div>
        </div>

        <div className="select-pop" aria-hidden="true">
          <div className="sp-menu"><span>Select</span><span>Select All</span><span>Paste</span></div>
          <div className="sp-word">FOUNDER<i className="h l" /><i className="h r" /></div>
        </div>
      </div>

      <div className="side">
        <div className="widget status glass" aria-label="Status">
          <span className="sig" aria-hidden="true"><i /><i /><i /><i /></span>
          <MIcon name="wifi" size={18} />
          <span className="clock">{time} IST</span>
          <span className="batt" aria-label="Battery full"><i /></span>
        </div>
        <div className="widget weather glass">
          <MIcon name="night" size={54} label="Night sky" />
          <div><b>{greet}</b><small>Hassan &amp; Bengaluru</small></div>
        </div>
        <ControlCenter />
        <a className="widget now glass" href="#work" aria-label="Now building ContentBrisk">
          <span className="now-top"><span>NOW BUILDING</span><span className="live"><i className="pulse" /> Launching soon</span></span>
          <b>CONTENTBRISK</b>
          <span className="bar" aria-hidden="true"><i /></span>
          <small>Content management for creators and brands</small>
        </a>
      </div>

      <div className="hero-band glass" aria-hidden="true">
        <div className="marquee"><span>BUILD · AUTOMATE · DESIGN · TEACH · REPEAT · </span><span>BUILD · AUTOMATE · DESIGN · TEACH · REPEAT · </span></div>
      </div>
    </section>
  )
}

function About() {
  return (
    <section id="about" className="section about">
      <div className="about-card glass reveal">
        <div className="tag">About me</div>
        <h2 className="serif">AI Generalist.<br /><em>Founder.</em></h2>
        <ul className="facts">{profile.about.map((p, i) => <li key={i}>{p}</li>)}</ul>
      </div>
      <div className="intro-card glass reveal">
        <div className="intro-head"><span className="pill">FOUNDER</span><h3>Introduce<br />my self</h3></div>
        <div className="intro-body">
          <div className="photo-frame">
            <img src={`${BASE}img/avatar.webp`} alt="Illustrated portrait of Rakshith" width="600" height="800" loading="lazy" />
            <div className="cam-modes" aria-hidden="true"><span>SLO-MO</span><span>VIDEO</span><b>PHOTO</b><span>PORTRAIT</span></div>
          </div>
          <div className="stat-grid">
            {profile.stats.map(st => (
              <div className="stat" key={st.label}><b><CountUp to={st.value} decimals={st.decimals} suffix={st.suffix} /></b><span>{st.label}</span></div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}

function Work() {
  return (
    <section id="work" className="section">
      <header className="sec-head reveal">
        <span className="tag">What I work on</span>
        <h2 className="display">What I <em className="serif">do</em></h2>
      </header>
      <div className="area-grid">
        {areas.map((a, i) => (
          <article key={a.title} className="area glass reveal" style={{ ['--accent' as string]: a.accent, transitionDelay: `${i * 60}ms` }}>
            <span className="area-icon"><MIcon name={a.icon} size={24} /></span>
            <h3>{a.title}</h3>
            <p>{a.text}</p>
            <span className="wc-glow" aria-hidden="true" />
          </article>
        ))}
      </div>

      <header className="sec-head reveal products-head">
        <span className="tag">My products</span>
        <h2 className="display">Built <em className="serif">by me</em></h2>
      </header>
      <div className="work-grid two">
        {products.map((p, i) => (
          <article key={p.name} className="work-card glass reveal" style={{ ['--accent' as string]: p.accent, transitionDelay: `${i * 80}ms` }}>
            <div className="wc-top">
              <span className="wc-kind">{p.kind}</span>
              <span className="wc-status"><i style={{ background: '#facc15' }} />{p.status}</span>
            </div>
            <h3>{p.name}</h3>
            <p>{p.blurb}</p>
            <span className="wc-glow" aria-hidden="true" />
          </article>
        ))}
      </div>
    </section>
  )
}

function Process() {
  return (
    <section id="process" className="section">
      <header className="sec-head reveal">
        <span className="tag">How I work</span>
        <h2 className="display">Stages of <em className="serif">work</em></h2>
      </header>
      <ol className="process">
        {process.map(s => (
          <li key={s.n} className="glass reveal">
            <span className="pn">{s.n}</span>
            <div><h3>{s.title}</h3><p>{s.text}</p></div>
          </li>
        ))}
      </ol>
    </section>
  )
}

function useTools() {
  const [tools, setTools] = useState<Tool[]>([])
  useEffect(() => {
    let alive = true
    fetch(`${BASE}data/tools.json`).then(r => r.json()).then((d: Tool[]) => { if (alive) setTools(d) }).catch(() => {})
    return () => { alive = false }
  }, [])
  return tools
}

function Stack() {
  const tools = useTools()
  const [q, setQ] = useState('')
  const [cat, setCat] = useState('All')
  const cats = useMemo(() => ['All', ...Array.from(new Set(tools.map(t => t.c)))], [tools])
  const shown = tools.filter(t => (cat === 'All' || t.c === cat) && t.n.toLowerCase().includes(q.trim().toLowerCase()))
  return (
    <section id="stack" className="section">
      <header className="sec-head reveal">
        <span className="tag">My AI stack</span>
        <h2 className="display"><CountUp to={91} /> premium tools I <em className="serif">use</em></h2>
      </header>
      <div className="stack-controls glass">
        <label className="search">
          <span className="sr">Search tools</span>
          <input type="search" placeholder="Search tools…" value={q} onChange={e => setQ(e.target.value)} />
        </label>
        <div className="cats" role="tablist" aria-label="Categories">
          {cats.map(c => (
            <button key={c} role="tab" aria-selected={cat === c} className={cat === c ? 'on' : ''} onClick={() => setCat(c)}>
              {c} <small>{c === 'All' ? tools.length : tools.filter(t => t.c === c).length}</small>
            </button>
          ))}
        </div>
      </div>
      <ul className="tool-grid">
        {shown.map(t => (
          <li key={t.n}>
            <a href={`https://${t.d}`} target="_blank" rel="noopener noreferrer" className="tool glass">
              <span className="tool-logo" style={t.b ? { background: t.b } : undefined}>
                {t.l ? <img src={t.l} alt="" loading="lazy" width="36" height="36" /> : <b>{t.n[0]}</b>}
              </span>
              <span className="tool-name">{t.n}</span>
              <span className="tool-cat">{t.c}</span>
            </a>
          </li>
        ))}
      </ul>
      {tools.length === 0 && <p className="empty">Loading tools…</p>}
      {tools.length > 0 && shown.length === 0 && <p className="empty">No tools match “{q}”.</p>}
      <p className="fine">All logos and names are trademarks of their respective owners.</p>
    </section>
  )
}

function Contact() {
  const links = [
    ...profile.socials,
    { label: 'GitHub', url: profile.github },
    ...(profile.email ? [{ label: profile.email, url: `mailto:${profile.email}` }] : []),
  ]
  return (
    <section id="contact" className="section">
      <div className="collab glass reveal">
        <div>
          <span className="tag">Collaboration</span>
          <h2 className="serif big">Let's build<br /><em>together.</em></h2>
          <p>Need an AI automation, a calling agent, an app or AI content for your business? Tell me what you're working on.</p>
          <ul className="links">
            {links.map(l => <li key={l.label}><a href={l.url} target="_blank" rel="noopener noreferrer">{l.label} ↗</a></li>)}
          </ul>
        </div>
        <img className="collab-avatar" src={`${BASE}img/avatar-square.webp`} alt="" width="320" height="320" loading="lazy" />
      </div>
      <footer className="foot glass">
        <span className="fp"><MIcon name="fingerprint" size={26} /></span>
        <p>{profile.motto.toUpperCase()}</p>
        <span className="copy">© {new Date().getFullYear()} {profile.name} · MyDesignNexus</span>
      </footer>
    </section>
  )
}

/* Jump to #section links (e.g. from the README) once the page has rendered */
function useHashJump() {
  useEffect(() => {
    const id = decodeURIComponent(window.location.hash.slice(1))
    if (!id) return
    const t = window.setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: 'auto', block: 'start' }), 60)
    return () => window.clearTimeout(t)
  }, [])
}

export default function App() {
  useReveal()
  useHashJump()
  return (
    <>
      <div className="bg" aria-hidden="true" />
      <Nav />
      <main>
        <Hero />
        <About />
        <Work />
        <Process />
        <Stack />
        <Contact />
      </main>
    </>
  )
}
