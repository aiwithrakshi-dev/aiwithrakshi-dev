// Everything the site says about you lives here. Edit this file to update the site.

export const profile = {
  name: 'Rakshith',
  handle: 'aiwithrakshi-dev',
  role: 'Founder · MyDesignNexus',
  tagline: 'I build AI products, automations and apps for businesses.',
  disciplines: ['AI', 'UI/UX', 'APPS'],
  about: [
    'I started in design, and that is still how I think: research first, then systems, then screens.',
    'Today I run MyDesignNexus, an agency building websites, apps and AI systems for businesses in India, and I teach AI for business on my AI with Rakshith channels in Kannada and English.',
    'Most of my work now is AI that does real jobs: voice agents that make calls, research that runs itself, and internal tools that automate a whole team.',
  ],
  services: ['AI agents & voice agents', 'Workflow automation (n8n, MCP)', 'UI/UX research & design', 'Web apps, PWAs & React Native apps', 'Brand identity'],
  github: 'https://github.com/aiwithrakshi-dev',
  // Add your links here, e.g. { label: 'Instagram', url: 'https://instagram.com/…' }
  socials: [] as { label: string; url: string }[],
  email: '', // e.g. 'hello@yourdomain.com'
}

export type Status = 'Live' | 'Active' | 'Prototype' | 'Pre-launch' | 'Publishing' | 'In design'

export const projects: {
  name: string
  kind: string
  blurb: string
  status: Status
  stack: string[]
  accent: string
  link?: string
}[] = [
  { name: 'ContentBrisk', kind: 'AI content studio', blurb: 'Research, scripts, voice, video, approvals and publishing for creators and agencies, planned week by week.', status: 'Pre-launch', stack: ['Lovable', 'Apify', 'Firecrawl', 'ElevenLabs', 'OpenRouter'], accent: '#c084fc' },
  { name: 'AdSynthra', kind: 'Ad intelligence', blurb: 'AI advertising intelligence and creative strategy across Meta, Google and more.', status: 'Prototype', stack: ['React', 'Vite', 'Supabase'], accent: '#22d3ee' },
  { name: 'Nexa voice agent', kind: 'AI calling', blurb: 'An ElevenLabs voice agent on a Twilio number that runs batch calls for the team.', status: 'Live', stack: ['ElevenLabs', 'Twilio'], accent: '#34d399' },
  { name: 'PowerdTask', kind: 'Productivity app', blurb: 'A to-do and productivity app on its way to iOS and Android, with refer-and-earn and an admin panel.', status: 'Publishing', stack: ['React Native', 'Next.js'], accent: '#f472b6' },
  { name: 'ScanNeya', kind: 'QR menus', blurb: 'QR digital menus and catalogs for Indian businesses.', status: 'Active', stack: ['PWA'], accent: '#fb923c' },
  { name: 'Pikorbit', kind: 'Local commerce', blurb: 'Order from your local kirana store at home; the store packs it and you pick it up.', status: 'In design', stack: ['Mobile app'], accent: '#facc15' },
  { name: 'My AI Stack', kind: 'Showcase', blurb: 'The 91 AI tools I use every day, with official logos, search and categories.', status: 'Live', stack: ['React'], accent: '#a78bfa', link: '#stack' },
]

export const process = [
  { n: '01', title: 'Discovery', text: 'A first call to understand the business, the users and what success looks like.' },
  { n: '02', title: 'Brief', text: 'Goals, scope and constraints written down, so we agree before anything is built.' },
  { n: '03', title: 'Proposal', text: 'Approach, timeline and cost, with the stack chosen for the job.' },
  { n: '04', title: 'Design', text: 'Research, flows and a design system, then hi-fi screens you can click through.' },
  { n: '05', title: 'Build & automate', text: 'The app, the agents and the automations, tested against the brief.' },
  { n: '06', title: 'Launch', text: 'Handover, training and support, then we measure and improve.' },
]
