import sys, re, base64
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

W, H = 1200, 676
d = Doc(W, H, "Rakshith — Founder & CEO, MyDesignNexus · AI Generalist. I help businesses put AI to work: automation, AI calling agents, custom software and AI-produced content. Hassan & Bengaluru, Karnataka, India. Book a free 1:1 call.")
page(d, [(250, 150, 230, INDIGO, .26), (640, 40, 210, BLUE, .28), (1130, 430, 230, PINK, .20), (40, 470, 210, ORANGE, .30), (900, 620, 160, BLUE, .14)])

avatar = base64.b64encode(open(os.path.join(INPUT, 'avatar_2x.webp'), 'rb').read()).decode()
pfp = base64.b64encode(open(os.path.join(INPUT, 'pfp_2x.webp'), 'rb').read()).decode()
logo_d = re.search(r' d="([^"]+)"', open(os.path.join(INPUT, 'logo.svg')).read()).group(1)

d.css.append(
    # rail icons: draw in, then a gentle wave of icon "actions" every 8 s
    ".dr{stroke-dasharray:1 1;animation:draw 1s cubic-bezier(.65,0,.35,1) both}"
    "@keyframes draw{0%{stroke-dashoffset:1;opacity:0}12%{opacity:1}100%{stroke-dashoffset:0;opacity:1}}"
    ".hop{animation:hop 8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}"
    "@keyframes hop{0%,8%,100%{transform:none}3%{transform:translateY(-3px)}5.5%{transform:translateY(.6px)}}"
    ".core{animation:core 8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}"
    f"@keyframes core{{0%,11%,100%{{transform:none;fill:transparent}}4%{{transform:scale(.7);fill:{BLUE};stroke:{BLUE}}}8%{{transform:scale(1.1);fill:{BLUE};stroke:{BLUE}}}}}"
    ".comet{stroke-dasharray:.24 1.3;animation:comet 8s ease-in-out infinite}"
    "@keyframes comet{0%{stroke-dashoffset:.24;opacity:1}10%{stroke-dashoffset:-1.06;opacity:1}10.5%,100%{opacity:0}}"
    ".scan{animation:scan 8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}"
    "@keyframes scan{0%{transform:translateY(-9px);opacity:0}2%{opacity:.85}11%{opacity:.85}13%,100%{transform:translateY(9px);opacity:0}}"
    ".ringb{animation:ringb 8s ease-in-out infinite;transform-box:view-box;transform-origin:12px 2.5px}"
    "@keyframes ringb{0%,13%,100%{transform:none}2%{transform:rotate(14deg)}4%{transform:rotate(-11deg)}6%{transform:rotate(8deg)}8%{transform:rotate(-5deg)}10%{transform:rotate(2deg)}}"
    ".prog{animation:prog 6s ease-in-out infinite;transform-box:fill-box;transform-origin:top}"
    "@keyframes prog{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}"
    # hero content
    ".bob{animation:bob 7s ease-in-out infinite}@keyframes bob{50%{transform:translateY(-6px)}}"
    ".ghost{animation:ghost 14s ease-in-out infinite}@keyframes ghost{50%{transform:translateX(-18px)}}"
    ".sweep{animation:sweep 5.5s ease-in-out infinite}@keyframes sweep{0%,55%{transform:translateX(-460px)}100%{transform:translateX(520px)}}"
    ".hand{animation:spin 60s linear infinite;transform-box:view-box}@keyframes spin{to{transform:rotate(360deg)}}"
    ".sel{animation:sel 10s steps(1) infinite}@keyframes sel{0%{opacity:1}20%,100%{opacity:0}}"
    ".selt{animation:selt 14s steps(1) infinite}@keyframes selt{0%{opacity:1}14.2857%,100%{opacity:0}}"
    ".shine{animation:shine 4.5s ease-in-out infinite}@keyframes shine{0%,60%{transform:translateX(-300px)}100%{transform:translateX(300px)}}"
)

# ---------- Navigation ----------
nav_items = [('HOME', 58), ('ABOUT', 64), ('WORK', 58), ('PRODUCTS', 88), ('AI STACK', 80), ('CONTACT', 78)]
pad, gap = 8, 6
total = sum(w for _, w in nav_items) + gap * (len(nav_items) - 1) + pad * 2
nx = (W - total) / 2
d.add('<g class="up">',
      d.glass(24, 18, W - 48, 58, r=29, op=.66),
      f'<svg x="44" y="30" width="38" height="33" viewBox="0 0 1061 922"><path d="{logo_d}" fill="{INK}" fill-rule="evenodd"/></svg>',
      f'<circle cx="86" cy="60" r="3.6" fill="{BLUE}"/>',
      d.glass(nx, 26, total, 42, r=21, op=.55, shadow=False))
x = nx + pad
d.defs.append(f'<linearGradient id="navact" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3AA0FF"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>')
for i, (label, w) in enumerate(nav_items):
    if i == 0:
        d.add(f'<rect x="{x}" y="32" width="{w}" height="30" rx="15" fill="url(#navact)"/>',
              f'<rect x="{x + 6}" y="33.5" width="{w - 12}" height="5" rx="2.5" fill="#fff" fill-opacity=".45"/>')
    d.add(f'<text x="{x + w / 2}" y="51.5" text-anchor="middle" class="b" font-weight="600" font-size="12.5" letter-spacing=".6" fill="{"#fff" if i == 0 else MUTED}">{label}</text>')
    x += w + gap
d.add(f'<rect x="{W - 168}" y="26" width="132" height="42" rx="21" fill="{INK}"/>',
      f'<text x="{W - 112}" y="52" text-anchor="middle" class="b" font-weight="600" font-size="14" fill="#fff">Let’s talk</text>',
      f'<g class="nudge">{icon("arrow", W - 74, 40.5, 13, "#fff", 2.2)}</g>',
      d.glass(W / 2 - 52, 74, 104, 24, r=12, op=.7, shadow=False),
      f'<text x="{W / 2}" y="90" text-anchor="middle" class="b" font-weight="600" font-size="10" letter-spacing="1.6" fill="{INK}">PORTFOLIO</text>',
      '</g>')

# ---------- Rail ----------
RX, RY, RW, RH = 28, 108, 56, H - 132
d.add(f'<g class="up" style="animation-delay:.08s">', d.glass(RX, RY, RW, RH, r=28, op=.7))
cx = RX + RW / 2
d.add(f'<text x="{cx}" y="{RY + 46}" text-anchor="middle" class="d hop" font-size="19" letter-spacing="-.5" fill="{INK}">Aa</text>')
def rail_icon(name, y, delay, extra=''):
    k = 22 / 24
    paths = ''.join(f'<path pathLength="1" class="dr" style="animation-delay:{delay + .07 * i:.2f}s" d="{p}"/>' for i, p in enumerate(ICONS[name]))
    return f'<g transform="translate({cx - 11} {y}) scale({k:.4f})" fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{paths}{extra}</g>'
# cpu: pulsing core
d.add(rail_icon('cpu', RY + 92, .5, f'<path class="core" style="animation-delay:2.6s" d="{ICONS["cpu"][1]}" stroke="{INK}"/>'))
d.add(rail_icon('flow', RY + 156, .7, f'<path class="comet" style="animation-delay:3.2s" pathLength="1" d="{ICONS["flow"][1]}" stroke="{BLUE}" stroke-width="2.5"/>'))
cid = d.nid('fp')
d.defs.append(f'<clipPath id="{cid}"><circle cx="12" cy="12" r="10.5"/></clipPath>')
d.add(rail_icon('finger', RY + 220, .9, f'<g clip-path="url(#{cid})"><path class="scan" style="animation-delay:3.8s" d="M1 12h22" stroke="{BLUE}" stroke-width="1.4" opacity="0"/></g>'))
k = 22 / 24
d.add(f'<g transform="translate({cx - 11} {RY + 284}) scale({k:.4f})" fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">'
      f'<g class="ringb" style="animation-delay:4.4s">' + ''.join(f'<path pathLength="1" class="dr" style="animation-delay:{1.1 + .07 * i:.2f}s" d="{p}"/>' for i, p in enumerate(ICONS['bell'])) + '</g></g>')
d.defs.append(f'<linearGradient id="railp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{INDIGO}"/><stop offset=".6" stop-color="{BLUE}"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></linearGradient>')
d.add(f'<rect x="{cx - 1.5}" y="{RY + 350}" width="3" height="150" rx="1.5" fill="{INK}" fill-opacity=".06"/>',
      f'<rect class="prog" x="{cx - 1.5}" y="{RY + 350}" width="3" height="150" rx="1.5" fill="url(#railp)"/>', '</g>')

# ---------- Hero card ----------
HX, HY, HW, HH = 96, 108, 756, H - 132
hc = d.nid('hc')
d.defs.append(f'<clipPath id="{hc}"><rect x="{HX}" y="{HY}" width="{HW}" height="{HH}" rx="32"/></clipPath>')
d.defs.append(f'<radialGradient id="cardglow" cx=".38" cy=".52" r=".6"><stop offset="0" stop-color="{INDIGO}" stop-opacity=".26"/><stop offset=".45" stop-color="{BLUE}" stop-opacity=".11"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>')
d.add('<g class="up" style="animation-delay:.14s">', d.glass(HX, HY, HW, HH, r=32, op=.55),
      f'<g clip-path="url(#{hc})">',
      f'<rect x="{HX}" y="{HY}" width="{HW}" height="{HH}" fill="url(#cardglow)"/>',
      f'<g class="ghost"><text x="{HX + 150}" y="{HY + 300}" class="s" font-size="228" letter-spacing="-6" fill="{INDIGO}" fill-opacity=".09">Portfolio</text></g>',
      f'<g class="bob"><image href="data:image/webp;base64,{avatar}" x="{HX + 26}" y="{HY + 120}" width="300" height="443" preserveAspectRatio="xMidYMax meet"/></g>',
      '</g>')
# profile chip
d.add(d.glass(HX + 22, HY + 22, 246, 54, r=27, op=.8, shadow=False),
      f'<clipPath id="pf"><circle cx="{HX + 49}" cy="{HY + 49}" r="20"/></clipPath>',
      f'<circle cx="{HX + 49}" cy="{HY + 49}" r="22" fill="#fff" stroke="{INDIGO}" stroke-opacity=".35" stroke-width="1.5"/>',
      f'<image href="data:image/webp;base64,{pfp}" x="{HX + 29}" y="{HY + 29}" width="40" height="40" clip-path="url(#pf)"/>',
      f'<text x="{HX + 80}" y="{HY + 45}" class="b" font-weight="600" font-size="14" fill="{INK}">Rakshith</text>',
      f'<circle class="ring" cx="{HX + 85}" cy="{HY + 59}" r="3.6" fill="{GREEN}"/><circle cx="{HX + 85}" cy="{HY + 59}" r="3.6" fill="{GREEN}"/>',
      f'<text x="{HX + 94}" y="{HY + 63}" class="b" font-weight="500" font-size="12" fill="{MUTED}">Available for new projects</text>')
# window dots
for i, c in enumerate([PINK, ORANGE, GREEN]):
    d.add(f'<circle cx="{HX + HW - 72 + i * 22}" cy="{HY + 46}" r="6.5" fill="{c}"/>')
# name + copy
tx = HX + 340
nm = d.nid('nm')
name_text = f'<text x="{tx}" y="{HY + 222}" class="a" font-size="112" letter-spacing=".5" textLength="388" lengthAdjust="spacingAndGlyphs">RAKSHITH</text>'
d.defs.append(f'<clipPath id="{nm}">{name_text}</clipPath>')
d.defs.append('<linearGradient id="shineg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')
d.add(name_text.replace('class="a"', f'class="a" fill="{INK}"'),
      f'<g clip-path="url(#{nm})"><g transform="skewX(-18)"><rect class="sweep" x="{tx + 60}" y="{HY + 100}" width="110" height="140" fill="url(#shineg)"/></g></g>',
      f'<text x="{tx + 2}" y="{HY + 256}" class="b" font-weight="600" font-size="14.5" fill="{INK}">Founder &amp; CEO, MyDesignNexus · AI Generalist</text>')
for i, line in enumerate(['I help businesses put AI to work:', 'automation, AI calling agents, custom', 'software and AI-produced content.']):
    d.add(f'<text x="{tx + 2}" y="{HY + 296 + i * 28}" class="b" font-size="19.5" letter-spacing="-.25" fill="{MUTED}">{esc(line)}</text>')
d.add(icon('pin', tx + 1, HY + 368, 17, PINK, 2.1),
      f'<text x="{tx + 26}" y="{HY + 382}" class="b" font-weight="600" font-size="13" letter-spacing="1" fill="{MUTED}">HASSAN &amp; BENGALURU, KARNATAKA, INDIA</text>')
by = HY + 408
d.add(f'<rect x="{tx + 2}" y="{by}" width="178" height="52" rx="26" fill="{INK}"/>',
      f'<text x="{tx + 76}" y="{by + 31.5}" text-anchor="middle" class="b" font-weight="600" font-size="15" fill="#fff">Start a project</text>',
      f'<g class="nudge">{icon("arrowr", tx + 142, by + 19, 15, "#fff", 2.2)}</g>',
      d.glass(tx + 194, by, 146, 52, r=26, op=.95, shadow=True),
      icon('playc', tx + 214, by + 16, 20, BLUE, 1.9),
      f'<text x="{tx + 244}" y="{by + 31.5}" class="b" font-weight="600" font-size="15" fill="{INK}">View work</text>',
      '</g>')

# ---------- Right column ----------
CX, CW = 864, 308
d.add('<g class="up" style="animation-delay:.22s">', d.glass(CX, 108, CW, 54, r=27, op=.72),
      f'<text x="{CX + 24}" y="{108 + 33}" class="b" font-weight="500" font-size="13" fill="{MUTED}">Local time</text>',
      f'<circle cx="{CX + 146}" cy="135" r="8.5" fill="none" stroke="{INK}" stroke-width="1.6"/>',
      f'<path d="M{CX + 146} 135v-5" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"/>',
      f'<g class="hand" style="transform-origin:{CX + 146}px 135px"><path d="M{CX + 146} 135l4 2.5" stroke="{BLUE}" stroke-width="1.6" stroke-linecap="round"/></g>',
      f'<text x="{CX + CW - 24}" y="{108 + 34}" text-anchor="end" class="d" font-size="15.5" letter-spacing="-.2" fill="{INK}">IST · UTC+5:30</text>', '</g>')

TY = 174
d.add('<g class="up" style="animation-delay:.3s">', d.glass(CX, TY, CW, 206, r=28, op=.42))
tiles = [('violet', 'cpu', 'Automation', 'For SMEs'), ('green', 'flow', 'Voice Agents', 'Sales & support'),
         ('blue', 'briefcase', 'Availability', 'Open to projects'), ('cyan', 'finger', 'Company', 'MSME registered')]
for i, (g, ic, t1, t2) in enumerate(tiles):
    x = CX + 10 + (i % 2) * 148
    y = TY + 10 + (i // 2) * 96
    d.add(d.glass(x, y, 140, 88, r=20, op=.78, shadow=False), d.badge(x + 12, y + 12, 34, g, ic, r=11),
          f'<text x="{x + 12}" y="{y + 64}" class="b" font-weight="600" font-size="13" fill="{INK}">{esc(t1)}</text>',
          f'<circle cx="{x + 15.5}" cy="{y + 75.5}" r="2.6" fill="{GREEN}"/>',
          f'<text x="{x + 22}" y="{y + 79.5}" class="b" font-weight="500" font-size="11" fill="{MUTED}">{esc(t2)}</text>')
d.add('</g>')

# booking card
BY = 392
bc = d.nid('bk')
d.defs.append(f'<clipPath id="{bc}"><rect x="{CX}" y="{BY}" width="{CW}" height="{H - 24 - BY}" rx="28"/></clipPath>')
d.add('<g class="up" style="animation-delay:.38s">', d.glass(CX, BY, CW, H - 24 - BY, r=28, op=.66),
      f'<g clip-path="url(#{bc})"><circle cx="{CX + CW}" cy="{BY + 10}" r="120" fill="{PINK}" fill-opacity=".16" filter="url(#blur2)"/><circle cx="{CX}" cy="{H - 30}" r="110" fill="{BLUE}" fill-opacity=".10" filter="url(#blur2)"/></g>',
      eyebrow(CX + 22, BY + 30, '1:1 Session', MUTED, size=11),
      f'<circle class="pulse" cx="{CX + CW - 104}" cy="{BY + 26}" r="3.6" fill="{GREEN}"/>',
      f'<text x="{CX + CW - 22}" y="{BY + 30}" text-anchor="end" class="b" font-weight="600" font-size="11.5" fill="#20A447">Mon–Fri · IST</text>',
      f'<text x="{CX + 22}" y="{BY + 64}" class="a" font-size="32" letter-spacing=".3" fill="{INK}">BOOK A 1:1 CALL</text>',
      f'<text x="{CX + 22}" y="{BY + 84}" class="b" font-weight="500" font-size="12" fill="{MUTED}">Free 1:1 session · confirmed instantly</text>')
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
cw_, cg = 48.8, 6
for i, dd in enumerate(days):
    x = CX + 22 + i * (cw_ + cg)
    y = BY + 100
    d.add(f'<rect x="{x:.1f}" y="{y}" width="{cw_}" height="38" rx="12" fill="#fff" fill-opacity=".85" stroke="{INK}" stroke-opacity=".08"/>',
          f'<text x="{x + cw_ / 2:.1f}" y="{y + 24}" text-anchor="middle" class="b" font-weight="600" font-size="12.5" fill="{INK}">{dd}</text>',
          f'<g class="sel" style="animation-delay:{-((10 - i * 2) % 10)}s"><rect x="{x:.1f}" y="{y}" width="{cw_}" height="38" rx="12" fill="{INK}"/>'
          f'<text x="{x + cw_ / 2:.1f}" y="{y + 24}" text-anchor="middle" class="b" font-weight="600" font-size="12.5" fill="#fff">{dd}</text></g>')
times = ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM']
tw = (CW - 44 - 3 * 6) / 4
for i, t in enumerate(times):
    x = CX + 22 + (i % 4) * (tw + 6)
    y = BY + 148 + (i // 4) * 34
    d.add(f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="28" rx="9" fill="#fff" fill-opacity=".85" stroke="{INK}" stroke-opacity=".08"/>',
          f'<text x="{x + tw / 2:.1f}" y="{y + 18.5}" text-anchor="middle" class="b" font-weight="500" font-size="11.5" fill="{INK}">{t}</text>',
          f'<g class="selt" style="animation-delay:{-((14 - i * 2) % 14)}s"><rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="28" rx="9" fill="{BLUE}" fill-opacity=".12" stroke="{BLUE}" stroke-opacity=".55"/>'
          f'<text x="{x + tw / 2:.1f}" y="{y + 18.5}" text-anchor="middle" class="b" font-weight="600" font-size="11.5" fill="{BLUE}">{t}</text></g>')
bb = BY + 222
sb = d.nid('sb')
d.defs.append(f'<clipPath id="{sb}"><rect x="{CX + 22}" y="{bb}" width="{CW - 44}" height="40" rx="20"/></clipPath>')
d.add(f'<rect x="{CX + 22}" y="{bb}" width="{CW - 44}" height="40" rx="20" fill="{INK}"/>',
      f'<g clip-path="url(#{sb})"><g transform="skewX(-20)"><rect class="shine" x="{CX + 150}" y="{bb}" width="60" height="40" fill="url(#shineg)" opacity=".5"/></g></g>',
      f'<text x="{CX + CW / 2 - 10}" y="{bb + 25.5}" text-anchor="middle" class="b" font-weight="600" font-size="14" fill="#fff">Book free session</text>',
      f'<g class="nudge">{icon("arrowr", CX + CW / 2 + 60, bb + 13, 14, "#fff", 2.2)}</g>', '</g>')

import os
os.makedirs(OUT_DIR, exist_ok=True)
n = finish(d, os.path.join(OUT_DIR, 'hero.svg'))
print('hero', n // 1024, 'KB')
