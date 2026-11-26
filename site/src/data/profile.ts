// Everything the site says about you lives here. Edit this file to update the site.

export const profile = {
  name: 'Rakshith',
  handle: 'aiwithrakshi-dev',
  role: 'AI Generalist & Founder, MyDesignNexus',
  tagline: 'I build AI systems, automations and AI content, and teach AI in Kannada.',
  location: 'Hassan & Bengaluru, Karnataka, India',
  disciplines: ['AI', 'APPS', 'CONTENT'],
  about: [
    'Founder & CEO of MyDesignNexus, an MSME-registered AI solutions company.',
    'Computer Science Engineering graduate (2025); went straight into entrepreneurship.',
    'Hands-on with 300+ AI tools (70+ premium), with 20+ projects delivered.',
    'Learned AI and tech through US-based communities, then freelanced.',
    '3.2M+ Reel plays on @aiwithrakshith.global, with a top Reel at 1.6M.',
    'Teaching AI in Kannada for Karnataka creators, SME owners and students.',
  ],
  stats: [
    { value: 300, decimals: 0, suffix: '+', label: 'AI tools, hands-on' },
    { value: 20, decimals: 0, suffix: '+', label: 'Projects delivered' },
    { value: 3.2, decimals: 1, suffix: 'M+', label: 'Reel plays' },
    { value: 1.6, decimals: 1, suffix: 'M', label: 'Top Reel' },
  ],
  github: 'https://github.com/aiwithrakshi-dev',
  socials: [
    { label: 'Instagram (Kannada) · @AIwithRakshith', url: 'https://instagram.com/aiwithrakshi' },
    { label: 'Company · @mydesignnexus.in', url: 'https://instagram.com/mydesignnexus.in' },
  ] as { label: string; url: string }[],
  email: '', // e.g. 'hello@yourdomain.com'
  motto: 'Building AI for India, from Karnataka.',
}

export const areas = [
  { icon: 'bot', title: 'AI Automation', text: 'Workflow automation and business systems for SMEs', accent: '#c084fc' },
  { icon: 'bell', title: 'AI Calling Agents', text: 'Voice agents for sales, support and lead handling', accent: '#34d399' },
  { icon: 'wifi', title: 'Web & App Development', text: 'Websites, PWAs and mobile apps', accent: '#22d3ee' },
  { icon: 'fingerprint', title: 'Custom Software', text: 'Tailored tools for real business problems', accent: '#60a5fa' },
  { icon: 'night', title: 'AI Content Production', text: 'AI video, UGC ads and visual content', accent: '#f472b6' },
  { icon: 'ai', title: 'AI Education', text: 'Kannada-first AI learning content', accent: '#facc15' },
]

export const products: {
  name: string
  kind: string
  blurb: string
  status: string
  accent: string
}[] = [
  { name: 'ContentBrisk', kind: 'Content management', blurb: 'A content management system for creators and brands.', status: 'Launching soon', accent: '#c084fc' },
  { name: 'Adsynthra', kind: 'AI ad platform', blurb: 'An AI-powered ad platform.', status: 'Coming soon', accent: '#22d3ee' },
]

export const process = [
  { n: '01', title: 'Discovery', text: 'A first call to understand the business, the users and what success looks like.' },
  { n: '02', title: 'Brief', text: 'Goals, scope and constraints written down, so we agree before anything is built.' },
  { n: '03', title: 'Proposal', text: 'Approach, timeline and cost, with the stack chosen for the job.' },
  { n: '04', title: 'Design', text: 'Research, flows and a design system, then hi-fi screens you can click through.' },
  { n: '05', title: 'Build & automate', text: 'The app, the agents and the automations, tested against the brief.' },
  { n: '06', title: 'Launch', text: 'Handover, training and support, then we measure and improve.' },
]
