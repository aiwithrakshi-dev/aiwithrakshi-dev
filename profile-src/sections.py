import sys, os, json, base64
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

OUT = OUT_DIR + os.sep
X0, CONTENT = 64, 1072


def wrap(text, max_px, size, k=0.53):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if len(t) * size * k > max_px and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur: lines.append(cur)
    return lines


def tw(text, size, k=0.55):
    return len(text) * size * k


def stag(i, base=.1, step=.08):
    return f'style="animation-delay:{base + i * step:.2f}s"'


# ---------------- About ----------------
def about():
    H = 730
    d = Doc(1200, H, 'About me — AI Generalist. Founder. 300+ AI tools hands-on, 91 premium tools, 20+ projects delivered, 3.2M+ Reel plays.')
    page(d, [(80, 120, 230, INDIGO, .22), (1150, 360, 230, ORANGE, .26), (600, 760, 220, BLUE, .10)])
    d.css.append('.bar{animation:bar 1.2s cubic-bezier(.2,.8,.2,1) both;transform-box:fill-box;transform-origin:left}@keyframes bar{from{transform:scaleX(0)}}')
    d.add(f'<g class="up">{eyebrow(X0, 74, "About me")}{heading(X0, 130, "AI Generalist. ", "Founder.", 50)}</g>')
    stats = [('300+', 'AI tools, hands-on', BLUE), ('91', 'Premium tools', INDIGO), ('20+', 'Projects delivered', GREEN), ('3.2M+', 'Reel plays · top Reel 1.6M', PINK)]
    sw = (CONTENT - 3 * 16) / 4
    for i, (v, l, c) in enumerate(stats):
        x, y = X0 + i * (sw + 16), 164
        d.add(f'<g class="up" {stag(i, .15)}>', d.glass(x, y, sw, 118, r=24, op=.8),
              f'<rect class="bar" style="animation-delay:{.5 + i * .1:.2f}s" x="{x + 24}" y="{y + 22}" width="30" height="4" rx="2" fill="{c}"/>',
              f'<text x="{x + 22}" y="{y + 78}" class="d" font-size="46" letter-spacing="-2" fill="{INK}">{esc(v)}</text>',
              f'<text x="{x + 24}" y="{y + 101}" class="b" font-weight="500" font-size="13" fill="{MUTED}">{esc(l)}</text></g>')
    facts = [('blue', 'building', 'Founder & CEO', 'Founder & CEO of MyDesignNexus, an MSME-registered AI solutions company.'),
             ('violet', 'cap', 'CSE graduate, 2025', 'Computer Science Engineering graduate (2025); went straight into entrepreneurship.'),
             ('amber', 'spark', '300+ AI tools', 'Hands-on with 300+ AI tools (91 premium), with 20+ projects delivered.'),
             ('green', 'globe', 'Learned globally', 'Learned AI and tech through US-based communities, then freelanced.'),
             ('sunset', 'playc', '3.2M+ Reel plays', '3.2M+ Reel plays on @aiwithrakshi.global, with a top Reel at 1.6M.'),
             ('gold', 'lang', 'AI in Kannada', 'Teaching AI in Kannada for Karnataka creators, SME owners and students.')]
    fw = (CONTENT - 2 * 16) / 3
    for i, (g, ic, t, body) in enumerate(facts):
        x, y = X0 + (i % 3) * (fw + 16), 298 + (i // 3) * 200
        d.add(f'<g class="up" {stag(i, .35)}>', d.glass(x, y, fw, 184, r=24, op=.8), d.badge(x + 24, y + 24, 44, g, ic, r=13),
              f'<text x="{x + 24}" y="{y + 100}" class="d" font-size="20" letter-spacing="-.4" fill="{INK}">{esc(t)}</text>')
        for j, line in enumerate(wrap(body, fw - 48, 14.5)):
            d.add(f'<text x="{x + 24}" y="{y + 126 + j * 21}" class="b" font-size="14.5" fill="{MUTED}">{esc(line)}</text>')
        d.add('</g>')
    return d, 'about.svg'


# ---------------- Skills ----------------
def skills():
    H = 356
    d = Doc(1200, H, 'Skills — UI, UX and development, end to end: visual design, design systems, Figma, Framer, user flows, prototyping, React & TypeScript, Supabase, n8n automation, AI agents & voice.')
    page(d, [(1100, 80, 200, BLUE, .16), (120, 330, 200, PINK, .14)])
    d.add(f'<g class="up">{eyebrow(X0, 70, "Skills")}<text x="{X0}" y="{108}" class="d" font-size="28" letter-spacing="-.8" fill="{INK}">UI, UX and development, end to end.</text></g>')
    cards = [('sunset', 'pen', 'UI Design', ['Visual design', 'Design systems', 'Figma', 'Framer', 'Motion & micro-interactions', 'Responsive layouts']),
             ('violet', 'cursor', 'UX Design', ['User flows', 'Wireframes', 'Prototyping', 'Information architecture', 'UX research', 'Usability reviews']),
             ('sky', 'code', 'Development', ['React & TypeScript', 'PWAs & mobile apps', 'Supabase', 'n8n automation', 'AI agents & voice', 'APIs & integrations'])]
    fw = (CONTENT - 2 * 16) / 3
    for i, (g, ic, t, chips) in enumerate(cards):
        x, y = X0 + i * (fw + 16), 136
        d.add(f'<g class="up" {stag(i, .15, .1)}>', d.glass(x, y, fw, 188, r=24, op=.82), d.badge(x + 22, y + 22, 40, g, ic, r=12),
              f'<text x="{x + 74}" y="{y + 48}" class="d" font-size="20" letter-spacing="-.4" fill="{INK}">{t}</text>')
        cx, cy = x + 22, y + 82
        for c in chips:
            w = tw(c, 12.5, .54) + 24
            if cx + w > x + fw - 20:
                cx, cy = x + 22, cy + 36
            d.add(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="28" rx="14" fill="#fff" fill-opacity=".9" stroke="{INK}" stroke-opacity=".08"/>',
                  f'<text x="{cx + w / 2:.1f}" y="{cy + 18.5}" text-anchor="middle" class="b" font-weight="500" font-size="12.5" fill="{INK}">{esc(c)}</text>')
            cx += w + 8
        d.add('</g>')
    return d, 'skills.svg'


# ---------------- Code + terminal ----------------
def code():
    H = 560
    d = Doc(1200, H, 'rakshith.ts — the short version, in code: Founder & CEO of MyDesignNexus; AI automation, AI calling agents and custom software; Hassan & Bengaluru; 300+ AI tools (91 premium); 20+ projects; available for work.')
    page(d, [(160, 80, 220, BLUE, .16), (1080, 480, 240, PINK, .16), (700, 40, 180, INDIGO, .12)])
    d.add(f'<g class="up">{eyebrow(X0, 70, "Under the hood")}{heading(X0, 120, "The short version, ", "in code.", 42)}</g>')
    EX, EY, EW, EH = X0, 150, 668, 370
    # editor
    d.add('<g class="up" style="animation-delay:.12s">', d.glass(EX, EY, EW, EH, r=22, op=1),
          f'<path d="M{EX} {EY + 44}h{EW}" stroke="{INK}" stroke-opacity=".07"/>')
    for i, c in enumerate([PINK, ORANGE, GREEN]):
        d.add(f'<circle cx="{EX + 24 + i * 18}" cy="{EY + 22}" r="5.5" fill="{c}"/>')
    d.add(f'<rect x="{EX + 86}" y="{EY + 9}" width="116" height="26" rx="8" fill="{SOFT}"/>',
          icon('code', EX + 96, EY + 15, 14, BLUE, 2.2),
          f'<text x="{EX + 116}" y="{EY + 26.5}" class="m" font-weight="500" font-size="12" fill="{INK}">rakshith.ts</text>',
          f'<text x="{EX + 220}" y="{EY + 26.5}" class="m" font-size="12" fill="{MUTED}">now.md</text>',
          f'<text x="{EX + EW - 20}" y="{EY + 26.5}" text-anchor="end" class="m" font-size="11.5" fill="{MUTED}">TypeScript</text>')
    K, S, N, C, P, B, T = INDIGO, BLUE, '#E07A00', '#8A90A2', '#7A7F92', PINK, INK
    lines = [
        [('// rakshith.ts — the short version', C)],
        [('export ', K), ('const ', K), ('rakshith', T), (' = {', P)],
        [('  role', T), (': ', P), ('"Founder & CEO, MyDesignNexus"', S), (',', P)],
        [('  craft', T), (': [', P), ('"AI automation"', S), (', ', P), ('"AI calling agents"', S), (', ', P), ('"custom software"', S), ('],', P)],
        [('  based', T), (': ', P), ('"Hassan & Bengaluru, India"', S), (',', P)],
        [('  tools', T), (': { ', P), ('handsOn', T), (': ', P), ('300', N), (', ', P), ('premium', T), (': ', P), ('91', N), (' },', P)],
        [('  shipped', T), (': ', P), ('"20+ projects"', S), (',', P)],
        [('  reach', T), (': ', P), ('"3.2M+ reel plays"', S), (',', P)],
        [('  teaches', T), (': ', P), ('"AI in Kannada"', S), (',', P)],
        [('  available', T), (': ', P), ('true', B), (',', P)],
        [('} ', P), ('as ', K), ('const', K), (';', P)],
        [],
        [('book', '#0A7A6E'), ('(rakshith, { ', P), ('slot', T), (': ', P), ('"Mon–Fri · 9–4 IST"', S), (', ', P), ('fee', T), (': ', P), ('0', N), (' });', P)],
    ]
    lh, top = 22, EY + 74
    for i, toks in enumerate(lines):
        y = top + i * lh
        d.add(f'<text x="{EX + 42}" y="{y}" text-anchor="end" class="m" font-size="12" fill="{INK}" fill-opacity=".25">{i + 1}</text>')
        if not toks:
            continue
        spans = ''.join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in toks)
        style = ' font-style="italic"' if toks[0][1] == C else ''
        d.add(f'<text x="{EX + 58}" y="{y}" class="m" font-size="13" xml:space="preserve"{style}>{spans}</text>')
        # typing reveal: a white cover slides away, line by line
        d.add(f'<rect class="type" style="animation-delay:{.8 + i * .32:.2f}s" x="{EX + 54}" y="{y - 15}" width="{EW - 70}" height="20" fill="#fff"/>')
    last_y = top + (len(lines) - 1) * lh
    d.add(f'<rect class="caret" x="{EX + 58 + 54 * 7.8:.1f}" y="{last_y - 13}" width="7.5" height="16" fill="{BLUE}"/>')
    d.add(f'<path d="M{EX} {EY + EH - 30}h{EW}" stroke="{INK}" stroke-opacity=".07"/>',
          f'<circle cx="{EX + 22}" cy="{EY + EH - 15}" r="3.5" fill="{GREEN}"/>',
          f'<text x="{EX + 32}" y="{EY + EH - 11}" class="m" font-size="11" fill="{MUTED}">main  ✓ 0 problems</text>',
          f'<text x="{EX + EW - 20}" y="{EY + EH - 11}" text-anchor="end" class="m" font-size="11" fill="{MUTED}">TypeScript · UTF-8 · Ln 13, Col 54</text>', '</g>')
    d.css.append('.type{animation:type .45s steps(18,end) both;transform-box:fill-box;transform-origin:right}'
                 '@keyframes type{from{transform:scaleX(1)}to{transform:scaleX(0)}}'
                 '.caret{animation:caret 1s steps(1) infinite}@keyframes caret{50%{opacity:0}}'
                 '.tl{animation:tl .4s ease-out both}@keyframes tl{from{opacity:0;transform:translateX(-6px)}}')
    # terminal
    TX, TW = EX + EW + 20, CONTENT - EW - 20
    d.add('<g class="up" style="animation-delay:.2s">',
          f'<rect x="{TX}" y="{EY}" width="{TW}" height="{EH}" rx="22" fill="{INK}" filter="url(#sh)"/>',
          f'<path d="M{TX} {EY + 44}h{TW}" stroke="#fff" stroke-opacity=".08"/>')
    for i, c in enumerate([PINK, ORANGE, GREEN]):
        d.add(f'<circle cx="{TX + 24 + i * 18}" cy="{EY + 22}" r="5.5" fill="{c}"/>')
    d.add(f'<text x="{TX + TW / 2 + 20}" y="{EY + 26.5}" text-anchor="middle" class="m" font-size="11.5" fill="#fff" fill-opacity=".5">zsh — rakshith@mdn</text>')
    G2, BL, OR, WH, DIM = '#4ADE80', '#6CB6FF', '#FFB340', '#F2F3F7', '#8B90A3'
    term = [
        [('$ ', G2), ('whoami', WH)],
        [('rakshith · founder @ MyDesignNexus', DIM)],
        [('$ ', G2), ('cat milestones.log', WH)],
        [('✓ ', G2), ('aiwithrakshith.tech live on Framer', WH)],
        [('✓ ', G2), ('free 1:1 booking · n8n + Sheets', WH)],
        [('✓ ', G2), ('ElevenLabs voice + chat assistant', WH)],
        [('✓ ', G2), ('AI calling agents for SMEs', WH)],
        [('✓ ', G2), ('3.2M+ reel plays · AI in Kannada', WH)],
        [('$ ', G2), ('book --free --slot "Mon–Fri 9–4"', WH)],
        [('→ ', BL), ('confirmed instantly', OR)],
        [('$ ', G2)],
    ]
    for i, toks in enumerate(term):
        y = EY + 76 + i * 26
        spans = ''.join(f'<tspan fill="{c}">{esc(t)}</tspan>' for t, c in toks)
        d.add(f'<text class="m tl" style="animation-delay:{5.2 + i * .28:.2f}s" x="{TX + 24}" y="{y}" font-size="12.5" xml:space="preserve">{spans}</text>')
    d.add(f'<rect class="caret" x="{TX + 24 + 2 * 7.5}" y="{EY + 76 + 10 * 26 - 12}" width="7.5" height="15" fill="{G2}"/>', '</g>')
    return d, 'code.svg'


# ---------------- Work ----------------
def work():
    H = 610
    d = Doc(1200, H, 'What I work on — six ways I help businesses: AI Automation, AI Calling Agents, Web & App Development, Custom Software, AI Content Production and AI Education.')
    page(d, [(1120, 120, 230, BLUE, .24), (60, 460, 220, PINK, .18), (620, 600, 180, GREEN, .12)])
    d.css.append('.lsw{animation:lsw 7s ease-in-out infinite}@keyframes lsw{0%,60%{transform:translateX(-400px)}100%{transform:translateX(1400px)}}')
    d.add(f'<g class="up">{eyebrow(X0, 70, "What I work on")}{heading(X0, 126, "Six ways I ", "help businesses.", 50)}',
          f'<text x="{X0}" y="{164}" class="b" font-size="16.5" fill="{MUTED}">From the first automation to a full product, I build the AI and software that small</text>',
          f'<text x="{X0}" y="{188}" class="b" font-size="16.5" fill="{MUTED}">and growing businesses actually use.</text></g>')
    items = [('violet', 'cpu', 'AI Automation', 'Workflow automation and business systems for SMEs.'),
             ('green', 'phone', 'AI Calling Agents', 'Voice agents for sales, support and lead handling.'),
             ('blue', 'window', 'Web & App Development', 'Websites, PWAs and mobile apps.'),
             ('cyan', 'code', 'Custom Software', 'Tailored tools for real business problems.'),
             ('sunset', 'film', 'AI Content Production', 'AI video, UGC ads and visual content.'),
             ('gold', 'book', 'AI Education', 'Kannada-first AI learning content.')]
    fw = (CONTENT - 2 * 16) / 3
    for i, (g, ic, t, body) in enumerate(items):
        x, y = X0 + (i % 3) * (fw + 16), 224 + (i // 3) * 176
        cid = d.nid('wc')
        d.defs.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{fw}" height="160" rx="24"/></clipPath>')
        d.add(f'<g class="up" {stag(i, .15)}>', d.glass(x, y, fw, 160, r=24, op=.8),
              f'<g clip-path="url(#{cid})"><g transform="skewX(-20)"><rect class="lsw" style="animation-delay:{1 + i * .35:.2f}s" x="{x - 200}" y="{y}" width="90" height="160" fill="#fff" fill-opacity=".55"/></g></g>',
              d.badge(x + 22, y + 22, 44, g, ic, r=13),
              f'<text x="{x + fw - 24}" y="{y + 40}" text-anchor="end" class="b" font-weight="500" font-size="12" fill="{INK}" fill-opacity=".3">0{i + 1}</text>',
              f'<text x="{x + 22}" y="{y + 98}" class="d" font-size="19" letter-spacing="-.4" fill="{INK}">{esc(t)}</text>')
        for j, line in enumerate(wrap(body, fw - 44, 14.5)):
            d.add(f'<text x="{x + 22}" y="{y + 123 + j * 20}" class="b" font-size="14.5" fill="{MUTED}">{esc(line)}</text>')
        d.add('</g>')
    return d, 'work.svg'


# ---------------- Products ----------------
def products():
    H = 480
    d = Doc(1200, H, 'Our products — built by me: ContentBrisk, a content management system for creators and brands (launching soon), and Adsynthra, an AI-powered ad platform (coming soon).')
    page(d, [(1100, 60, 180, INDIGO, .12)])
    d.add(f'<g class="up">{eyebrow(X0, 70, "Our products")}{heading(X0, 126, "Built by ", "me.", 50)}</g>')
    cards = [('ContentBrisk', 'Content management', 'A content management system for creators and brands.', 'Launching soon', 'layers', [(INDIGO, .9), (PINK, .85), (BLUE, .8)]),
             ('Adsynthra', 'AI ad platform', 'An AI-powered ad platform.', 'Coming soon', 'cursor', [(ORANGE, .9), (GREEN, .8), (BLUE, .75)])]
    cw = (CONTENT - 24) / 2
    for i, (name, kind, body, status, ic, fields) in enumerate(cards):
        x, y, h = X0 + i * (cw + 24), 160, 280
        cid = d.nid('pc')
        d.defs.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{cw}" height="{h}" rx="28"/></clipPath>')
        pos = [(x + cw * .12, y + h * .35, 200), (x + cw * .55, y + h * 1.0, 210), (x + cw * .95, y + h * .15, 200)]
        blobs = ''.join(f'<g class="drift{k + 1}"><circle cx="{px:.0f}" cy="{py:.0f}" r="{r}" fill="{c}" fill-opacity="{op}" filter="url(#blur2)"/></g>'
                        for k, ((px, py, r), (c, op)) in enumerate(zip(pos, fields)))
        d.add(f'<g class="up" {stag(i, .15, .12)}>', f'<rect x="{x}" y="{y}" width="{cw}" height="{h}" rx="28" fill="#fff" filter="url(#sh)"/>',
              f'<g clip-path="url(#{cid})">{blobs}</g>',
              f'<rect x="{x + .5}" y="{y + .5}" width="{cw - 1}" height="{h - 1}" rx="27.5" fill="none" stroke="{INK}" stroke-opacity=".06"/>',
              d.glass(x + 20, y + 20, tw(status, 12, .56) + 40, 30, r=15, op=.88, shadow=False),
              f'<circle class="pulse" cx="{x + 36}" cy="{y + 35}" r="3.6" fill="{ORANGE}"/>',
              f'<text x="{x + 46}" y="{y + 39.5}" class="b" font-weight="600" font-size="12" fill="{INK}">{status}</text>',
              d.glass(x + cw - 56, y + 18, 36, 36, r=11, op=.75, shadow=False), icon(ic, x + cw - 47, y + 27, 18, INK, 1.9),
              d.glass(x + 20, y + h - 132, cw - 40, 112, r=20, op=.66, shadow=False),
              eyebrow(x + 42, y + h - 100, kind, MUTED, size=10.5),
              f'<text x="{x + 40}" y="{y + h - 58}" class="d" font-weight="700" font-size="36" letter-spacing="-1.4" fill="{INK}">{name}</text>',
              f'<text x="{x + 42}" y="{y + h - 34}" class="b" font-size="14" fill="{MUTED}">{esc(body)}</text>', '</g>')
    return d, 'products.svg'


# ---------------- AI stack ----------------
def stack():
    H = 516
    logos = json.load(open(os.path.join(INPUT, 'logos.json')))
    d = Doc(1200, H, 'My AI stack — 91 premium AI tools, used daily, sorted by what they do. Hands-on with 300+ AI tools in total.')
    page(d, [(80, 100, 220, ORANGE, .20), (1150, 420, 240, BLUE, .20)])
    d.add(f'<g class="up">{eyebrow(X0, 70, "My AI stack")}{heading(X0, 126, "91 premium AI tools, ", "used daily.", 50)}',
          f'<text x="{X0}" y="{164}" class="b" font-size="16.5" fill="{MUTED}">Every premium tool I pay for and use, sorted by what it does. Hands-on with 300+ AI tools in total.</text></g>')
    cats = [('AI Chat', BLUE), ('Build & Code', INDIGO), ('Design', PURPLE), ('Image', PINK), ('Video', ORANGE), ('Audio & Voice', GREEN),
            ('Automation', CYAN), ('Backend & Deploy', '#0A84FF'), ('Productivity', '#FFB340'), ('3D', '#AF52DE'), ('Payments', '#34C759')]
    counts = {}
    for l in logos: counts[l['c']] = counts.get(l['c'], 0) + 1
    cmap = dict(cats)
    x, y = X0, 194
    d.add('<g class="up" style="animation-delay:.15s">')
    for c, col in cats:
        label = f'{c} · {counts.get(c, 0)}'
        w = tw(label, 12, .56) + 34
        if x + w > X0 + CONTENT:
            x, y = X0, y + 38
        d.add(d.glass(x, y, w, 30, r=15, op=.85, shadow=False), f'<circle cx="{x + 15}" cy="{y + 15}" r="3.5" fill="{col}"/>',
              f'<text x="{x + 24}" y="{y + 19.5}" class="b" font-weight="500" font-size="12" fill="{INK}">{esc(label)}</text>')
        x += w + 8
    d.add('</g>')
    for i, l in enumerate(logos):
        d.defs.append(f'<image id="L{i}" href="data:image/webp;base64,{l["w"]}" width="22" height="22"/>')
    rows = [logos[0::3], logos[1::3], logos[2::3]]
    CW_, CH, GAP = 188, 54, 12
    top = y + 58
    mid = d.nid('mk')
    d.defs.append(f'<linearGradient id="{mid}g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
                  f'<mask id="{mid}"><rect x="0" y="{top - 10}" width="1200" height="{3 * (CH + 14) + 20}" fill="url(#{mid}g)"/></mask>')
    d.add(f'<g mask="url(#{mid})" class="fade" style="animation-delay:.3s">')
    for r, row in enumerate(rows):
        ry = top + r * (CH + 14)
        span = len(row) * (CW_ + GAP)
        dur = 70 + r * 12
        d.css.append(f'.mq{r}{{animation:mq{r} {dur}s linear infinite}}@keyframes mq{r}{{from{{transform:translateX({0 if r % 2 == 0 else -span}px)}}to{{transform:translateX({-span if r % 2 == 0 else 0}px)}}}}')
        chips = []
        for rep in range(2):
            for k, l in enumerate(row):
                cx = X0 + (rep * len(row) + k) * (CW_ + GAP)
                idx = logos.index(l)
                dark = l.get('b') == '#000000'
                chips.append(f'<rect x="{cx}" y="{ry}" width="{CW_}" height="{CH}" rx="16" fill="#fff" fill-opacity=".9" stroke="{INK}" stroke-opacity=".07"/>'
                             f'<rect x="{cx + 10}" y="{ry + 10}" width="34" height="34" rx="10" fill="{"#000" if dark else "#fff"}" stroke="{INK}" stroke-opacity=".08"/>'
                             f'<use href="#L{idx}" x="{cx + 16}" y="{ry + 16}"/>'
                             f'<text x="{cx + 54}" y="{ry + 25}" class="b" font-weight="600" font-size="13" fill="{INK}">{esc(l["n"])}</text>'
                             f'<text x="{cx + 54}" y="{ry + 41}" class="b" font-weight="500" font-size="11" fill="{cmap.get(l["c"], BLUE)}">{esc(l["c"])}</text>')
        d.add(f'<g class="mq{r}">{"".join(chips)}</g>')
    d.add('</g>')
    return d, 'stack.svg'


# ---------------- Contact ----------------
def contact():
    H = 440
    d = Doc(1200, H, 'Let’s build together — Building AI for India, from Karnataka. Automation, AI calling agents, apps or AI content: tell me what you’re building. Book a free 1:1 call or start a project.')
    page(d, [(160, 120, 230, PINK, .22), (1060, 120, 230, INDIGO, .22), (600, 470, 230, ORANGE, .20)])
    d.add('<g class="up">', d.glass(120, 36, 960, H - 72, r=32, op=.55),
          eyebrow(600, 104, 'Let’s build together', MUTED, 'middle'),
          f'<text x="600" y="162" text-anchor="middle" class="d" font-size="54" letter-spacing="-2.2" fill="{INK}">Building AI for India,</text>',
          f'<text x="600" y="228" text-anchor="middle" class="s" font-size="60" letter-spacing="-.6" fill="{BLUE}">from Karnataka.</text>',
          f'<text x="600" y="270" text-anchor="middle" class="b" font-size="16.5" fill="{MUTED}">Automation, AI calling agents, apps or AI content: tell me what you’re building and let’s make it work.</text>')
    bw1, bw2 = 230, 176
    bx = 600 - (bw1 + 14 + bw2) / 2
    d.add(f'<rect x="{bx}" y="298" width="{bw1}" height="54" rx="27" fill="{INK}"/>',
          icon('calendar', bx + 24, 315, 19, '#fff', 2), f'<text x="{bx + 52}" y="330.5" class="b" font-weight="600" font-size="15" fill="#fff">Book a free 1:1 call</text>',
          d.glass(bx + bw1 + 14, 298, bw2, 54, r=27, op=.95),
          f'<text x="{bx + bw1 + 14 + bw2 / 2 - 10}" y="330.5" text-anchor="middle" class="b" font-weight="600" font-size="15" fill="{INK}">Start a project</text>',
          f'<g class="nudge">{icon("arrowr", bx + bw1 + 14 + bw2 - 40, 318, 15, INK, 2.2)}</g>',
          f'<text x="600" y="{H - 52}" text-anchor="middle" class="b" font-weight="500" font-size="13" fill="{MUTED}">I reply within 24 hours · Mon–Fri, 9 AM–4 PM IST</text>', '</g>')
    return d, 'contact.svg'


# ---------------- Find-me cards ----------------
def card(name, g, ic, label, value, cta='Open'):
    W, H = 400, 132
    d = Doc(W, H, f'{label}: {value}')
    page(d, [(360, 20, 110, GRADS[g][0], .16)], r=24)
    d.add('<g class="up">', d.badge(22, 22, 48, g, ic, r=14),
          f'<text x="86" y="44" class="b" font-weight="500" font-size="12.5" fill="{MUTED}">{esc(label)}</text>',
          f'<text x="86" y="70" class="d" font-size="19" letter-spacing="-.4" fill="{INK}">{esc(value)}</text>',
          f'<path d="M22 {H - 32}h{W - 44}" stroke="{INK}" stroke-opacity=".06"/>',
          f'<text x="22" y="{H - 12}" class="b" font-weight="600" font-size="12" fill="{BLUE}">{esc(cta)}</text>',
          f'<circle cx="{W - 36}" cy="36" r="16" fill="#fff" stroke="{INK}" stroke-opacity=".08"/>',
          f'<g class="nudge">{icon("arrow", W - 43, 29, 14, INK, 2.2)}</g>', '</g>')
    return d, f'find-{name}.svg'


# ---------------- Showcase ----------------
def showcase():
    H = 798
    d = Doc(1200, H, 'Showcase — featured productions crafted with AI: AI films and ad creatives in 16:9, and AI avatar videos in 9:16 for Reels and Shorts, from MDN Creatives.')
    page(d, [(120, 90, 220, BLUE, .14), (1120, 640, 240, PINK, .16)])
    d.add(f'<g class="up">{eyebrow(X0, 70, "Showcase")}{heading(X0, 126, "Featured productions, ", "crafted with AI.", 50)}',
          f'<text x="{X0}" y="{164}" class="b" font-size="16.5" fill="{MUTED}">AI films, ad creatives and CGI from MDN Creatives.</text></g>')
    sdir = os.path.join(INPUT, 'showcase')
    for kind, n in (('film', 5), ('avatar', 5)):
        for i in range(1, n + 1):
            b = base64.b64encode(open(os.path.join(sdir, f'{kind}{i}.webp'), 'rb').read()).decode()
            w, h = (320, 180) if kind == 'film' else (150, 266)
            d.defs.append(f'<image id="{kind}{i}" href="data:image/webp;base64,{b}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"/>')
    d.defs.append('<linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".62"/></linearGradient>')
    mid = d.nid('sm')
    d.defs.append(f'<linearGradient id="{mid}g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".07" stop-color="#fff"/><stop offset=".93" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
                  f'<mask id="{mid}"><rect x="0" y="0" width="1200" height="{H}" fill="url(#{mid}g)"/></mask>')
    rows = [('film', 'AI films & ad creatives', 'Cinematic AI storytelling and ad creatives in 16:9.', 'Project', 236, 320, 180, 18, 64),
            ('avatar', 'AI avatar videos', 'Vertical 9:16 AI presenter videos for brands, ready for Reels and Shorts.', 'Avatar', 478, 150, 266, 18, 52)]
    for r, (kind, title, sub, label, y, w, h, gap, dur) in enumerate(rows):
        d.add(f'<g class="up" style="animation-delay:{.15 + r * .12:.2f}s"><text x="{X0}" y="{y - 20 if r == 0 else y - 20}" class="d" font-size="19" letter-spacing="-.4" fill="{INK}">{esc(title)}</text>',
              f'<text x="{X0 + (tw(title, 19, .5) + 14)}" y="{y - 20}" class="b" font-size="13.5" fill="{MUTED}">{esc(sub)}</text></g>')
        span = 5 * (w + gap)
        d.css.append(f'.sh{r}{{animation:sh{r} {dur}s linear infinite}}@keyframes sh{r}{{from{{transform:translateX({0 if r == 0 else -span}px)}}to{{transform:translateX({-span if r == 0 else 0}px)}}}}')
        cards = []
        copies = -(-1200 // span) + 1
        for k in range(5 * copies):
            i = k % 5 + 1
            x = X0 + k * (w + gap)
            cid = f'c{kind}{k}'
            d.defs.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18"/></clipPath>')
            cards.append(f'<g clip-path="url(#{cid})"><use href="#{kind}{i}" x="{x}" y="{y}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#shade)"/></g>'
                         f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="17.5" fill="none" stroke="#fff" stroke-opacity=".25"/>'
                         f'<circle cx="{x + w / 2}" cy="{y + h / 2}" r="20" fill="#fff" fill-opacity=".28" stroke="#fff" stroke-opacity=".55"/>'
                         f'<path d="M{x + w / 2 - 5} {y + h / 2 - 8}l13 8-13 8z" fill="#fff"/>'
                         f'<text x="{x + 14}" y="{y + h - 14}" class="b" font-weight="600" font-size="13" fill="#fff">{label} 0{i}</text>')
        d.add(f'<g mask="url(#{mid})" class="fade" style="animation-delay:.3s"><g class="sh{r}">{"".join(cards)}</g></g>')
    d.add(f'<text x="{X0}" y="{H - 24}" class="b" font-weight="600" font-size="13" fill="{BLUE}">Watch them with sound on aiwithrakshith.tech  →</text>')
    return d, 'showcase.svg'


if __name__ == '__main__':
    import os
    os.makedirs(OUT, exist_ok=True)
    which = sys.argv[1:] or ['about', 'skills', 'code', 'work', 'showcase', 'products', 'stack', 'contact', 'cards']
    for w in which:
        if w == 'cards':
            for args in [('website', 'indigo', 'globe', 'Website', 'aiwithrakshith.tech', 'Visit the website'),
                         ('booking', 'green', 'calendar', 'Free 1:1 session · Mon–Fri', 'Book a call', 'Book now · confirmed instantly'),
                         ('assistant', 'violet', 'mic', 'AI assistant · voice + chat', 'Ask Rakshith’s AI', 'Start a chat'),
                         ('instagram-kannada', 'insta', 'insta', 'Instagram · Kannada', '@AIwithRakshith', 'Follow'),
                         ('instagram-global', 'insta', 'insta', 'Instagram · Global', '@aiwithrakshi.global', 'Follow'),
                         ('company', 'cyan', 'building', 'Company', '@mydesignnexus.in', 'Follow MyDesignNexus')]:
                d, f = card(*args)
                print(f, finish(d, OUT + f) // 1024, 'KB')
        else:
            d, f = globals()[w]()
            print(f, finish(d, OUT + f) // 1024, 'KB')
