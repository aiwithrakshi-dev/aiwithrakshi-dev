"""Shared building blocks for the profile SVGs: theme tokens, fonts, icons, cards."""
import base64, io, re, html
from fontTools import subset as ftsubset
from fontTools.ttLib import TTFont

import os
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, 'fonts')
INPUT = os.path.join(HERE, 'input')
OUT_DIR = os.path.join(HERE, '..', 'assets', 'profile')
FONT_FILES = {
    'ID600': ('ID', 600, 'normal', os.path.join(FONTS, 'InterDisplay-SemiBold.woff2')),
    'ID700': ('ID', 700, 'normal', os.path.join(FONTS, 'InterDisplay-Bold.woff2')),
    'IN400': ('IN', 400, 'normal', os.path.join(FONTS, 'inter-latin-400-normal.woff2')),
    'IN500': ('IN', 500, 'normal', os.path.join(FONTS, 'inter-latin-500-normal.woff2')),
    'IN600': ('IN', 600, 'normal', os.path.join(FONTS, 'inter-latin-600-normal.woff2')),
    'AN400': ('AN', 400, 'normal', os.path.join(FONTS, 'anton-latin-400-normal.woff2')),
    'SE400': ('SE', 400, 'italic', os.path.join(FONTS, 'instrument-serif-latin-400-italic.woff2')),
    'JB400': ('JB', 400, 'normal', os.path.join(FONTS, 'jetbrains-mono-latin-400-normal.woff2')),
    'JB500': ('JB', 500, 'normal', os.path.join(FONTS, 'jetbrains-mono-latin-500-normal.woff2')),
}

# Theme tokens, taken from the Framer project (aiwithrakshith.tech)
INK = '#0B0B12'; MUTED = '#5C6070'; SOFT = '#F4F5F9'
BLUE = '#007AFF'; INDIGO = '#5E5CE6'; PINK = '#FF375F'; ORANGE = '#FF9F0A'
GREEN = '#30D158'; PURPLE = '#BF5AF2'; TEAL = '#00B3A4'; CYAN = '#00C7BE'; YELLOW = '#FFD60A'
GRADS = {
    'violet': ('#5E5CE6', '#BF5AF2'), 'green': ('#30D158', '#00B3A4'), 'blue': ('#007AFF', '#5E5CE6'),
    'cyan': ('#00C7BE', '#007AFF'), 'sunset': ('#FF375F', '#FF9F0A'), 'gold': ('#FFD60A', '#FF9F0A'),
    'amber': ('#FFB340', '#FF6A00'), 'sky': ('#007AFF', '#00C7BE'), 'insta': ('#FFB340', '#FF375F', '#BF5AF2'),
    'ink': ('#3A3A44', '#0B0B12'), 'coral': ('#FF9F0A', '#FF375F'), 'indigo': ('#5E5CE6', '#007AFF'),
}

ICONS = {
    'cpu': ['M7 4h10a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3z', 'M10.5 9.5h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1z',
            'M9.5 2v2', 'M14.5 2v2', 'M20 9.5h2', 'M20 14.5h2', 'M14.5 20v2', 'M9.5 20v2', 'M2 14.5h2', 'M2 9.5h2'],
    'flow': ['M5.5 14a2.5 2.5 0 1 0 0 5a2.5 2.5 0 1 0 0-5z', 'M7.8 15.4C10.6 13.6 12.4 10 18.8 7.2', 'M15 5.5L19 7.1L17.4 11.1'],
    'finger': ['M2 12a10 10 0 0 1 18-6', 'M5 19.5C5.5 18 6 15 6 12a6 6 0 0 1 .34-2', 'M9 6.8a6 6 0 0 1 9 5.2v2', 'M12 10a2 2 0 0 0-2 2c0 1.02-.1 2.51-.26 4',
               'M14 13.12c0 2.38 0 6.38-1 8.88', 'M8.65 22c.21-.66.45-1.32.57-2', 'M17.29 21.02c.12-.6.43-2.3.5-3.02', 'M21.8 16c.2-2 .131-5.354 0-6', 'M2 16h.01'],
    'bell': ['M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9', 'M10.3 21a1.94 1.94 0 0 0 3.4 0'],
    'briefcase': ['M4 7h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z', 'M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16'],
    'building': ['M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18z', 'M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2', 'M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2', 'M10 6h4', 'M10 10h4', 'M10 14h4', 'M10 18h4'],
    'cap': ['M22 10L12 5 2 10l10 5 10-5z', 'M6 12v5c3 3 9 3 12 0v-5', 'M22 10v6'],
    'spark': ['M12 3l2.1 5.9L20 11l-5.9 2.1L12 19l-2.1-5.9L4 11l5.9-2.1z', 'M19 3v4', 'M21 5h-4'],
    'globe': ['M12 2a10 10 0 1 0 0 20a10 10 0 1 0 0-20z', 'M2 12h20', 'M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z'],
    'playc': ['M12 2a10 10 0 1 0 0 20a10 10 0 1 0 0-20z', 'M10 8.5l5.5 3.5-5.5 3.5z'],
    'lang': ['M5 8l6 6', 'M4 14l6-6 2-3', 'M2 5h12', 'M7 2h1', 'M22 22l-5-10-5 10', 'M14 18h6'],
    'phone': ['M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z'],
    'window': ['M5 4h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z', 'M3 9h18', 'M7 6.5h.01', 'M10 6.5h.01'],
    'code': ['M16 18l6-6-6-6', 'M8 6l-6 6 6 6'],
    'film': ['M4 6h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z', 'M16 10.5l6-3.5v10l-6-3.5'],
    'book': ['M4 19.5A2.5 2.5 0 0 1 6.5 17H20', 'M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z'],
    'pen': ['M12 19l7-7 3 3-7 7-3-3z', 'M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z', 'M2 2l7.6 7.6', 'M11 9a2 2 0 1 0 0 4a2 2 0 1 0 0-4z'],
    'insta': ['M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5z', 'M12 8a4 4 0 1 0 0 8a4 4 0 1 0 0-8z', 'M17.5 6.5h.01'],
    'github': ['M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4', 'M9 18c-4.51 2-5-2-7-2'],
    'calendar': ['M6 4.5h12a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3v-10a3 3 0 0 1 3-3z', 'M3 9.5h18', 'M8 2.5v4', 'M16 2.5v4', 'M8.5 14.5l2.2 2.2 4.8-4.8'],
    'mic': ['M12 2.5a3 3 0 0 1 3 3v5a3 3 0 0 1-6 0v-5a3 3 0 0 1 3-3z', 'M5.5 10.5a6.5 6.5 0 0 0 13 0', 'M12 17v4', 'M8.5 21h7'],
    'arrow': ['M7 17L17 7', 'M8 7h9v9'],
    'arrowr': ['M5 12h14', 'M13 6l6 6-6 6'],
    'pin': ['M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z', 'M12 7a3 3 0 1 0 0 6a3 3 0 1 0 0-6z'],
    'layers': ['M12 2L2 7l10 5 10-5-10-5z', 'M2 17l10 5 10-5', 'M2 12l10 5 10-5'],
    'cursor': ['M4 4l7 16 2.5-6.5L20 11z'],
    'check': ['M5 12.5l4.2 4.2L19 7'],
    'terminal': ['M4 17l6-6-6-6', 'M12 19h8'],
}


def esc(s):
    return html.escape(s, quote=True)


def icon(name, x, y, size=24, color='#fff', sw=1.9, cls='', extra=''):
    k = size / 24
    paths = ''.join(f'<path d="{d}"/>' for d in ICONS[name])
    c = f' class="{cls}"' if cls else ''
    return (f'<g{c} transform="translate({x:.2f} {y:.2f}) scale({k:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw / k:.2f}" stroke-linecap="round" stroke-linejoin="round" {extra}>{paths}</g>')


class Doc:
    """Collects defs (gradients, filters) and body markup for one SVG."""

    def __init__(self, w, h, label):
        self.w, self.h, self.label = w, h, label
        self.defs, self.body, self.css = [], [], []
        self.grad_ids = set()
        self.uid = 0

    def nid(self, p='i'):
        self.uid += 1
        return f'{p}{self.uid}'

    def grad(self, key, angle='135'):
        gid = f'g_{key}_{angle}'
        if gid not in self.grad_ids:
            self.grad_ids.add(gid)
            stops = GRADS[key]
            n = len(stops)
            st = ''.join(f'<stop offset="{i / (n - 1):.2f}" stop-color="{c}"/>' for i, c in enumerate(stops))
            x2, y2 = ('1', '1') if angle == '135' else ('1', '0') if angle == '90' else ('0', '1')
            self.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">{st}</linearGradient>')
        return f'url(#{gid})'

    def add(self, *parts):
        self.body.extend(parts)

    def badge(self, x, y, size, grad, ic, r=None, cls=''):
        r = r if r is not None else size * 0.3
        isz = size * 0.52
        return (f'<g class="{cls}"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{r}" fill="{self.grad(grad)}"/>'
                f'<rect x="{x + .5}" y="{y + .5}" width="{size - 1}" height="{size - 1}" rx="{r - .5}" fill="none" stroke="#fff" stroke-opacity=".28"/>'
                f'{icon(ic, x + (size - isz) / 2, y + (size - isz) / 2, isz, "#fff", 2.0)}</g>')

    def glass(self, x, y, w, h, r=28, op=.72, shadow=True, stroke=.9):
        f = ' filter="url(#sh)"' if shadow else ''
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#fff" fill-opacity="{op}" stroke="#fff" stroke-opacity="{stroke}"{f}/>'
                f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="{r - .5}" fill="none" stroke="{INK}" stroke-opacity=".05"/>')

    def render(self, fonts_css):
        base = ('<filter id="sh" x="-20%" y="-20%" width="140%" height="170%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#0F172A" flood-opacity=".09"/>'
                '<feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#0F172A" flood-opacity=".06"/></filter>'
                '<filter id="blur" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="64"/></filter>'
                '<filter id="blur2" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="34"/></filter>')
        css = (fonts_css +
               ".d{font-family:ID,'Inter Display',Inter,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:600}"
               ".b{font-family:IN,Inter,'Segoe UI',Helvetica,Arial,sans-serif}"
               ".a{font-family:AN,Anton,Impact,'Arial Narrow Bold',sans-serif;font-weight:400}"
               ".s{font-family:SE,'Instrument Serif',Georgia,'Times New Roman',serif;font-style:italic;font-weight:400}"
               ".m{font-family:JB,'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}"
               ".up{animation:up .9s cubic-bezier(.2,.8,.2,1) both}"
               "@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
               ".fade{animation:fade 1.2s ease-out both}@keyframes fade{from{opacity:0}}"
               ".pulse{animation:pulse 2.2s ease-in-out infinite}@keyframes pulse{50%{opacity:.25}}"
               ".ring{animation:ring 2.2s ease-out infinite;transform-box:fill-box;transform-origin:center}"
               "@keyframes ring{0%{transform:scale(.6);opacity:.55}100%{transform:scale(2.6);opacity:0}}"
               ".drift1{animation:drift1 16s ease-in-out infinite}.drift2{animation:drift2 19s ease-in-out infinite}.drift3{animation:drift3 22s ease-in-out infinite}"
               "@keyframes drift1{50%{transform:translate(60px,30px)}}@keyframes drift2{50%{transform:translate(-70px,40px)}}@keyframes drift3{50%{transform:translate(40px,-50px)}}"
               ".nudge{animation:nudge 3.2s ease-in-out infinite}@keyframes nudge{0%,70%,100%{transform:none}80%{transform:translate(2px,-2px)}}"
               + ''.join(self.css) +
               "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
        return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{esc(self.label)}">'
                f'<title>{esc(self.label)}</title><defs>{base}{"".join(self.defs)}<style>{css}</style></defs>'
                f'{"".join(self.body)}</svg>')


def page(doc, blobs, r=28, bg='#FFFFFF'):
    """Rounded white page with soft, drifting colour blobs (the site's background glow)."""
    cid = doc.nid('pg')
    doc.defs.append(f'<clipPath id="{cid}"><rect width="{doc.w}" height="{doc.h}" rx="{r}"/></clipPath>')
    b = ''.join(f'<g class="drift{i % 3 + 1}"><circle cx="{x}" cy="{y}" r="{rad}" fill="{c}" fill-opacity="{op}" filter="url(#blur)"/></g>'
                for i, (x, y, rad, c, op) in enumerate(blobs))
    doc.add(f'<g clip-path="url(#{cid})"><rect width="{doc.w}" height="{doc.h}" fill="{bg}"/>{b}</g>',
            f'<rect x=".5" y=".5" width="{doc.w - 1}" height="{doc.h - 1}" rx="{r - .5}" fill="none" stroke="{INK}" stroke-opacity=".07"/>')
    return cid


def eyebrow(x, y, text, color=MUTED, anchor='start', size=12):
    return (f'<text x="{x}" y="{y}" class="b" font-weight="600" font-size="{size}" letter-spacing="1.7" fill="{color}" '
            f'text-anchor="{anchor}">{esc(text.upper())}</text>')


def heading(x, y, plain, serif, size=48, anchor='start', serif_color=BLUE):
    """Inter Display heading with an Instrument Serif italic accent, like the site."""
    return (f'<text x="{x}" y="{y}" class="d" font-size="{size}" letter-spacing="{-0.04 * size:.2f}" fill="{INK}" text-anchor="{anchor}">'
            f'{esc(plain)}<tspan class="s" font-size="{size * 1.04:.1f}" letter-spacing="{-0.01 * size:.2f}" fill="{serif_color}">{esc(serif)}</tspan></text>')


def fonts_css(chars, needed):
    out = []
    for key in needed:
        fam, w, style, path = FONT_FILES[key]
        f = TTFont(path)
        opts = ftsubset.Options()
        opts.flavor = 'woff2'
        opts.layout_features = ['kern', 'liga', 'calt', 'tnum'] if fam in ('IN', 'ID') else ['kern', 'liga']
        opts.name_IDs = []
        opts.notdef_outline = True
        sub = ftsubset.Subsetter(options=opts)
        sub.populate(text=chars)
        sub.subset(f)
        buf = io.BytesIO()
        f.flavor = 'woff2'
        f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        out.append(f"@font-face{{font-family:{fam};src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:{w};font-style:{style}}}")
    return ''.join(out)


def text_chars(svg):
    return html.unescape(''.join(re.findall(r'>([^<>]+)<', svg)))


def finish(doc, path, extra_chars=''):
    raw = doc.render('')
    used = []
    weights = {'d': ['ID600', 'ID700'], 'b': ['IN400', 'IN500', 'IN600'], 'a': ['AN400'], 's': ['SE400'], 'm': ['JB400', 'JB500']}
    for cls, ws in weights.items():
        if re.search(r'class="' + cls + r'[" ]', raw):
            if cls == 'd' and 'font-weight="700"' not in raw:
                ws = ['ID600']
            used.extend(ws)
    chars = ''.join(sorted(set(text_chars(raw) + extra_chars + ' ')))
    svg = doc.render(fonts_css(chars, used))
    open(path, 'w').write(svg)
    return len(svg)
