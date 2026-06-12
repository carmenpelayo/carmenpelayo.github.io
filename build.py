#!/usr/bin/env python3
"""
build.py — Static-site generator for carmenpelayo.github.io
Edit the CONTENT dictionaries below, then run:  python3 build.py
Output: index.html (+ assets/) ready to push to the GitHub Pages repo.
"""
import math, os, json

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# CONTENT — edit freely
# ----------------------------------------------------------------------------
ME = {
    "name": "Carmen Pelayo Fernández",
    "role": "Research Analyst · Big Data & AI Economic Analysis",
    "org": "BBVA Research",
    "location": "Madrid, Spain",
    "tagline": "Measuring the economy in real time with big data, NLP and machine learning.",
    "email": "carmenpelayofdez@gmail.com",
    "linkedin": "https://www.linkedin.com/in/carmenpelayofernandez",
    "github": "https://github.com/carmenpelayo",
    "photo": "assets/photo.jpg",  # drop your photo here (square works best)
}

ABOUT = (
    "I am a research analyst in the <strong>Big Data &amp; AI Economic Analysis</strong> unit at "
    "<a href='https://www.bbvaresearch.com' target='_blank' rel='noopener'>BBVA Research</a>, where I build "
    "real-time economic indicators and forecasting models from unstructured data — news, transactions, "
    "social media and scientific publications. My work sits at the intersection of macroeconomics, "
    "geopolitics and machine learning: from nowcasting non-performing loans with ensemble learning to "
    "quantifying global technological progress through arXiv preprints."
    "<br><br>"
    "I hold an MSc in Data Science from <strong>Boston University</strong> — where I taught AI Ethics and received the "
    "Graduate Teaching Excellence Award — and a BSc in Management &amp; Technology with a minor in Economics "
    "from <strong>Universidad Carlos III de Madrid</strong>. I care deeply about the <strong>responsible and ethical use of AI</strong> "
    "in economic analysis and beyond."
)

INTERESTS = [
    "Real-time / big-data indicators", "Economic forecasting & nowcasting",
    "NLP & LLMs for economics", "Geoeconomics & policy uncertainty",
    "Machine & deep learning", "AI ethics",
]

PUBLICATIONS = [
    {
        "title": "Measuring Technological Progress in Real Time with ArXiv",
        "venue": "BBVA Research", "year": "2025",
        "links": [
            ("Report", "https://www.bbvaresearch.com"),
            ("Interactive indicators", "https://bigdata.bbvaresearch.com/en/geopolitics/global-issues/technological-progress/disciplines/"),
        ],
        "note": "Also published as an op-ed in Expansión (Aug 2025).",
        "abstract": (
            "Using NLP on arXiv.org metadata, we construct 129 monthly Tech Research Activity Indicators "
            "across computer science, physics and mathematics — a high-frequency, high-granularity proxy for "
            "technological progress. The indicators correlate above 96% with established benchmarks "
            "(Dimensions, WIPO patent grants, Stanford AI Index) while leading them in time. We document the "
            "paradigm shift of 2014: computer-science research pivoting from classical theory to AI, which now "
            "accounts for ~70% of all CS preprints, and discuss implications for productivity, labor markets "
            "and policy."
        ),
    },
    {
        "title": "From Macro Fundamentals to Digital Footprints: Elevating NPL Nowcasting with Big Data and Ensemble Learning",
        "venue": "BBVA Research · forthcoming", "year": "2026",
        "links": [],
        "note": "Working paper on the Colombian banking system.",
        "abstract": (
            "We nowcast non-performing loans in the Colombian banking system by combining classical macro-financial "
            "determinants (activity, unemployment, rates, credit cycle) with novel big-data signals, benchmarking "
            "ensemble-learning architectures against traditional econometric baselines."
        ),
    },
]

EXPERIENCE = [
    {
        "role": "Research Analyst — Big Data & AI Economic Analysis",
        "org": "BBVA Research", "where": "Madrid", "when": "Jun 2024 – Present",
        "points": [
            "Worldwide Economic & Trade Policy Uncertainty (EPU/TPU) indicators from GDELT, extending Baker & Bloom and Caldara et al. to global press coverage.",
            "Benchmarking foundation time-series models (Chronos-2, Bistro…) against classical estimators for short-term economic forecasting.",
            "Novel measure of European defence-industry integration: scraping sector news and scoring inter-firm collaboration with LLMs.",
            "Real-time candidate-sentiment tracking for the 2026 Colombian elections from news, social media and polls.",
            "Macroeconomic impact of semiconductor supply-and-demand shocks via Local Projections.",
        ],
    },
    {
        "role": "Teaching Assistant — AI Ethics (DS380, Data, Society & Ethics)",
        "org": "Boston University", "where": "Boston, MA", "when": "Jan – May 2024",
        "points": [
            "Course spanning ethical theories, algorithmic bias, privacy & security, AI law (incl. the EU AI Act) and the societal impact of AI.",
            "Led discussion sections of 30 students; 2023–24 Graduate Teaching Excellence Award.",
        ],
    },
    {
        "role": "Technology & Strategy Consulting",
        "org": "Avasant · Deloitte", "where": "Madrid", "when": "Sep 2022 – Sep 2023",
        "points": [
            "Enterprise strategic transformation: scenario analysis for a multi-million IT-offshoring contract (US healthcare); vendor negotiations for a UK vaccine R&D NGO; post-merger Salesforce consolidation.",
        ],
    },
]

PROJECTS = [
    {
        "name": "ECB Nowcasting Toolbox — Python",
        "url": "https://github.com/carmenpelayo/ECB_Nowcasting_Toolbox_Python",
        "desc": "Open-source Python implementation of the European Central Bank's public Nowcasting Toolbox.",
        "tag": "Open source",
    },
    {
        "name": "ArXivScrapper",
        "url": "https://github.com/carmenpelayo/ArXivScrapper",
        "desc": "Scraping & NLP pipeline behind the 129 monthly technological-progress indicators.",
        "tag": "Research code",
    },
    {
        "name": "Schneider Electric “Cold-Start Challenge”",
        "url": "https://github.com/carmenpelayo",
        "desc": "Finalist, MIT Energy & Climate Hackathon 2023 — AutoML ensemble forecasting building energy use; R² = 0.83 on >1.4M records.",
        "tag": "Hackathon",
    },
    {
        "name": "Neural demand forecasting (MSc thesis)",
        "url": "https://github.com/carmenpelayo/TimeSeriesForecasting",
        "desc": "NeuralProphet & N-BEATS vs. ARIMA / Holt-Winters on real café sales, with weather and event covariates.",
        "tag": "MSc thesis",
    },
    {
        "name": "European location recommender (BSc thesis)",
        "url": "https://locationrecommender.streamlit.app",
        "desc": "Web app matching tech firms to 242 European regions across 22 socioeconomic factors. Graded 10/10 with Honours.",
        "tag": "Web app",
    },
]

EDUCATION = [
    ("Boston University", "MSc Data Science", "2023 – 2024",
     "GPA 3.7/4.0 · CDS Merit Scholarship · Graduate Teaching Excellence Award"),
    ("Universidad Carlos III de Madrid", "BSc Management & Technology, Minor in Economics", "2018 – 2022",
     "8.4/10 · Bachelor thesis 10/10 with Honours · Honours in Environmental Economics"),
    ("University of Wisconsin–Madison", "Academic Exchange (Information Systems)", "2021 – 2022",
     "Economics, statistics and ML coursework at the School of Business & CS Dept."),
]

SKILLS_JSON = {
    "languages": ["Python", "R", "SQL"],
    "tools": ["Git", "AWS", "Hugging Face", "PyTorch", "GDELT"],
    "methods": ["econometrics", "local projections", "time-series & foundation-model forecasting",
                 "machine & deep learning", "NLP / LLMs", "text mining"],
    "spoken": ["Spanish (native)", "English (C2)", "German (A1)"],
}

AWARDS = [
    "Graduate Teaching Excellence Award — Boston University (2024)",
    "CDS Merit Scholarship — Boston University (2023)",
    "Finalist — MIT Energy & Climate Hackathon (2023)",
    "CEMFI Summer School — Data Science for Economics (2025)",
    "Salesforce Certified Administrator (2023)",
]

# ----------------------------------------------------------------------------
# HERO CHART — computed in Python from the headline finding of the 2025 paper:
# CS share of arXiv preprints, <10% (2010) -> ~50% (2025). Logistic fit.
# ----------------------------------------------------------------------------
def cs_share(year):
    return 4.5 + 46.0 / (1.0 + math.exp(-0.42 * (year - 2018.3)))

def build_chart(width=640, height=300, pad_l=46, pad_r=16, pad_t=18, pad_b=34):
    y0, y1 = 2005, 2025
    v0, v1 = 0.0, 55.0
    pts = []
    n = 120
    for i in range(n + 1):
        yr = y0 + (y1 - y0) * i / n
        val = cs_share(yr)
        x = pad_l + (width - pad_l - pad_r) * (yr - y0) / (y1 - y0)
        y = (height - pad_b) - (height - pad_t - pad_b) * (val - v0) / (v1 - v0)
        pts.append((round(x, 1), round(y, 1)))
    line = "M" + " L".join(f"{x},{y}" for x, y in pts)
    area = line + f" L{pts[-1][0]},{height - pad_b} L{pts[0][0]},{height - pad_b} Z"
    # gridlines + labels
    grid, labels = [], []
    for share in (10, 20, 30, 40, 50):
        gy = (height - pad_b) - (height - pad_t - pad_b) * share / (v1 - v0)
        grid.append(f"<line x1='{pad_l}' y1='{gy:.1f}' x2='{width - pad_r}' y2='{gy:.1f}'/>")
        labels.append(f"<text x='{pad_l - 8}' y='{gy + 3.5:.1f}' text-anchor='end'>{share}%</text>")
    for yr in (2005, 2010, 2015, 2020, 2025):
        gx = pad_l + (width - pad_l - pad_r) * (yr - y0) / (y1 - y0)
        labels.append(f"<text x='{gx:.1f}' y='{height - pad_b + 18}' text-anchor='middle'>{yr}</text>")
    # last point marker
    lx, ly = pts[-1]
    length_estimate = 0.0
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        length_estimate += math.hypot(xb - xa, yb - ya)
    return f"""
<svg class="hero-chart" viewBox="0 0 {width} {height}" role="img"
     aria-label="Computer-science share of arXiv preprints rising from under 10% in 2010 to nearly 50% in 2025">
  <g class="grid">{''.join(grid)}</g>
  <path class="area" d="{area}"/>
  <path class="line" d="{line}" pathLength="1000"/>
  <circle class="dot" cx="{lx}" cy="{ly}" r="4.5"/>
  <g class="axis">{''.join(labels)}</g>
  <text class="chart-note" x="{pad_l}" y="{pad_t - 4}">CS share of arXiv preprints — Pelayo (2025), BBVA Research</text>
</svg>"""

# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------
CSS = """
:root{
  --paper:#FBFBF9; --ink:#10243E; --ink-soft:#3D5168; --rule:#E3E6E2;
  --teal:#0E8C8C; --teal-soft:#E3F2F0; --card:#FFFFFF; --mono-bg:#0F1B2D;
  --maxw:1020px;
}
*{box-sizing:border-box} html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:'Source Serif 4',Georgia,serif;font-size:17px;line-height:1.65;}
h1,h2,h3,.sans{font-family:'Space Grotesk','Segoe UI',sans-serif}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace}
a{color:var(--teal);text-decoration:none;border-bottom:1px solid transparent}
a:hover,a:focus-visible{border-bottom-color:var(--teal)}
a:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 22px}

/* nav */
nav{position:sticky;top:0;z-index:10;background:rgba(251,251,249,.92);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}
nav .wrap{display:flex;align-items:center;justify-content:space-between;height:58px}
nav .brand{font-family:'Space Grotesk',sans-serif;font-weight:600;letter-spacing:.01em;color:var(--ink)}
nav ul{display:flex;gap:22px;list-style:none;margin:0;padding:0}
nav ul a{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--ink-soft);border:none}
nav ul a:hover{color:var(--teal)}
@media(max-width:760px){nav ul{display:none}}

/* hero */
.hero{padding:64px 0 56px;border-bottom:1px solid var(--rule)}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
@media(max-width:860px){.hero .wrap{grid-template-columns:1fr}}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:12.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--teal);margin:0 0 14px}
.hero h1{font-size:clamp(34px,5vw,52px);line-height:1.06;margin:0 0 14px;letter-spacing:-.015em}
.hero .role{font-family:'Space Grotesk',sans-serif;font-size:18px;color:var(--ink-soft);margin:0 0 6px}
.hero .tagline{font-style:italic;color:var(--ink-soft);margin:14px 0 22px;max-width:46ch}
.links{display:flex;flex-wrap:wrap;gap:10px}
.links a{font-family:'IBM Plex Mono',monospace;font-size:13px;border:1px solid var(--rule);
  border-radius:999px;padding:7px 16px;color:var(--ink);background:var(--card)}
.links a:hover{border-color:var(--teal);color:var(--teal)}
.headshot{width:118px;height:118px;border-radius:50%;object-fit:cover;
  border:3px solid var(--card);box-shadow:0 1px 0 var(--rule),0 10px 30px rgba(16,36,62,.12);margin-bottom:20px}

/* hero chart */
.chartcard{background:var(--card);border:1px solid var(--rule);border-radius:14px;
  padding:18px 14px 8px;box-shadow:0 14px 40px rgba(16,36,62,.07)}
.hero-chart{width:100%;height:auto;display:block}
.hero-chart .grid line{stroke:var(--rule);stroke-width:1}
.hero-chart .area{fill:var(--teal);opacity:.10}
.hero-chart .line{fill:none;stroke:var(--teal);stroke-width:2.6;
  stroke-dasharray:1000;stroke-dashoffset:1000;animation:draw 2.2s ease-out forwards}
.hero-chart .dot{fill:var(--teal)}
.hero-chart .axis text{font-family:'IBM Plex Mono',monospace;font-size:10.5px;fill:var(--ink-soft)}
.hero-chart .chart-note{font-family:'IBM Plex Mono',monospace;font-size:10.5px;fill:var(--ink-soft)}
@keyframes draw{to{stroke-dashoffset:0}}
@media (prefers-reduced-motion:reduce){.hero-chart .line{animation:none;stroke-dashoffset:0}}
.chart-caption{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--ink-soft);
  padding:8px 6px 10px;margin:0}

/* sections */
section{padding:58px 0;border-bottom:1px solid var(--rule)}
section h2{font-size:26px;margin:0 0 8px;letter-spacing:-.01em}
.sec-eyebrow{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--teal);margin:0 0 6px}
.lede{max-width:72ch}

/* chips */
.chips{display:flex;flex-wrap:wrap;gap:9px;margin-top:18px;padding:0;list-style:none}
.chips li{font-family:'IBM Plex Mono',monospace;font-size:12.5px;background:var(--teal-soft);
  color:#0B5F5F;border-radius:999px;padding:6px 14px}

/* publications */
.pub{background:var(--card);border:1px solid var(--rule);border-radius:14px;
  padding:22px 24px;margin-top:18px}
.pub h3{margin:0 0 4px;font-size:19px;line-height:1.3}
.pub .meta{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--ink-soft)}
.pub .note{font-size:15px;color:var(--ink-soft);margin:8px 0 0;font-style:italic}
.pub .plinks{margin-top:10px;display:flex;gap:14px;flex-wrap:wrap}
.pub .plinks a{font-family:'IBM Plex Mono',monospace;font-size:13px}
details{margin-top:12px}
summary{cursor:pointer;font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--teal)}
summary:hover{text-decoration:underline}
details p{font-size:15.5px;color:var(--ink-soft);margin:10px 0 0}

/* experience timeline */
.xp{position:relative;margin-top:26px;padding-left:26px;border-left:2px solid var(--rule)}
.xp-item{position:relative;padding:0 0 30px 18px}
.xp-item:last-child{padding-bottom:4px}
.xp-item::before{content:"";position:absolute;left:-33px;top:7px;width:12px;height:12px;
  border-radius:50%;background:var(--teal);border:3px solid var(--paper)}
.xp-item h3{margin:0;font-size:18px}
.xp-item .org{font-family:'Space Grotesk',sans-serif;color:var(--ink-soft);font-size:15.5px}
.xp-item .when{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--teal)}
.xp-item ul{margin:10px 0 0;padding-left:18px}
.xp-item li{font-size:15.5px;color:var(--ink-soft);margin-bottom:6px}

/* projects grid */
.grid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:16px;margin-top:22px}
.proj{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:20px 20px 18px;
  display:flex;flex-direction:column;transition:transform .18s ease,box-shadow .18s ease}
.proj:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(16,36,62,.09)}
@media (prefers-reduced-motion:reduce){.proj:hover{transform:none}}
.proj .tag{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--teal);margin-bottom:8px}
.proj h3{margin:0 0 8px;font-size:16.5px;line-height:1.35}
.proj p{margin:0;font-size:14.5px;color:var(--ink-soft);flex:1}
.proj a{border:none}

/* education */
.edu{margin-top:20px;display:grid;gap:14px}
.edu-item{display:grid;grid-template-columns:1fr auto;gap:6px 18px;background:var(--card);
  border:1px solid var(--rule);border-radius:12px;padding:16px 20px}
.edu-item h3{margin:0;font-size:16.5px}
.edu-item .deg{color:var(--ink-soft);font-size:15px}
.edu-item .when{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--teal);white-space:nowrap}
.edu-item .extra{grid-column:1/-1;font-size:14px;color:var(--ink-soft);font-style:italic}
@media(max-width:560px){.edu-item{grid-template-columns:1fr}.edu-item .when{order:-1}}

/* skills terminal */
.term{background:var(--mono-bg);color:#D7E3EE;border-radius:14px;margin-top:22px;
  box-shadow:0 14px 40px rgba(16,36,62,.18);overflow:hidden}
.term-bar{display:flex;align-items:center;gap:7px;padding:11px 16px;background:rgba(255,255,255,.06)}
.term-bar span{width:11px;height:11px;border-radius:50%;display:inline-block}
.term-bar .r{background:#F26D6D}.term-bar .y{background:#F2C76D}.term-bar .g{background:#6DD08F}
.term-bar .title{font-family:'IBM Plex Mono',monospace;font-size:12px;color:#9FB2C5;margin-left:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.term pre{margin:0;padding:18px 20px 22px;font-family:'IBM Plex Mono',monospace;
  font-size:13.5px;line-height:1.7;overflow-x:auto}
.term .k{color:#7FD6C2}.term .s{color:#E8D58A}.term .p{color:#9FB2C5}

/* awards */
.awards{margin:18px 0 0;padding-left:20px}
.awards li{margin-bottom:6px;color:var(--ink-soft);font-size:15.5px}

/* footer */
footer{padding:54px 0 64px;text-align:center}
footer .big{font-family:'Space Grotesk',sans-serif;font-size:24px;margin:0 0 16px}
footer .links{justify-content:center}
footer .fine{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--ink-soft);margin-top:28px}

/* reveal on scroll */
.js .reveal{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.js .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.js .reveal{opacity:1;transform:none;transition:none}}
"""

JS = """
document.documentElement.classList.add('js');
if('IntersectionObserver' in window){
const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');obs.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
}else{document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));}
"""

# ----------------------------------------------------------------------------
# HTML assembly
# ----------------------------------------------------------------------------
def li(items): return "".join(f"<li>{x}</li>" for x in items)

def pubs_html():
    out = []
    for p in PUBLICATIONS:
        links = " ".join(f"<a href='{u}' target='_blank' rel='noopener'>{t} &#8599;</a>" for t, u in p["links"])
        links_div = f"<div class='plinks'>{links}</div>" if links else ""
        note = f"<p class='note'>{p['note']}</p>" if p.get("note") else ""
        out.append(f"""
<article class="pub reveal">
  <h3>{p['title']}</h3>
  <div class="meta">{p['venue']} · {p['year']}</div>
  {note}{links_div}
  <details><summary>Abstract</summary><p>{p['abstract']}</p></details>
</article>""")
    return "".join(out)

def xp_html():
    out = []
    for x in EXPERIENCE:
        out.append(f"""
<div class="xp-item reveal">
  <span class="when">{x['when']}</span>
  <h3>{x['role']}</h3>
  <div class="org">{x['org']} · {x['where']}</div>
  <ul>{li(x['points'])}</ul>
</div>""")
    return "".join(out)

def proj_html():
    out = []
    for p in PROJECTS:
        out.append(f"""
<a class="proj reveal" href="{p['url']}" target="_blank" rel="noopener">
  <span class="tag">{p['tag']}</span>
  <h3>{p['name']} &#8599;</h3>
  <p>{p['desc']}</p>
</a>""")
    return "".join(out)

def edu_html():
    out = []
    for name, deg, when, extra in EDUCATION:
        out.append(f"""
<div class="edu-item reveal">
  <div><h3>{name}</h3><div class="deg">{deg}</div></div>
  <div class="when">{when}</div>
  <div class="extra">{extra}</div>
</div>""")
    return "".join(out)

def skills_html():
    j = json.dumps(SKILLS_JSON, indent=2, ensure_ascii=False)
    j = (j.replace('"languages"', '<span class="k">"languages"</span>')
          .replace('"tools"', '<span class="k">"tools"</span>')
          .replace('"methods"', '<span class="k">"methods"</span>')
          .replace('"spoken"', '<span class="k">"spoken"</span>'))
    return f"""
<div class="term reveal" aria-label="Skills">
  <div class="term-bar"><span class="r"></span><span class="y"></span><span class="g"></span>
    <span class="title">carmen@bbva-research ~ $ cat skills.json</span></div>
  <pre>{j}</pre>
</div>"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ME['name']} — Research Analyst, Big Data &amp; AI Economics</title>
<meta name="description" content="{ME['name']} — {ME['role']} at {ME['org']}. Real-time economic indicators, NLP, machine learning and forecasting.">
<meta property="og:title" content="{ME['name']}">
<meta property="og:description" content="{ME['tagline']}">
<meta property="og:type" content="profile">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<nav>
  <div class="wrap">
    <span class="brand">Carmen Pelayo</span>
    <ul>
      <li><a href="#about">about</a></li>
      <li><a href="#research">research</a></li>
      <li><a href="#experience">experience</a></li>
      <li><a href="#projects">projects</a></li>
      <li><a href="#education">education</a></li>
      <li><a href="#contact">contact</a></li>
    </ul>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <div>
      <img class="headshot" src="{ME['photo']}" alt="Portrait of {ME['name']}"
           onerror="this.style.display='none'">
      <p class="eyebrow">Economics × Big Data × AI</p>
      <h1>{ME['name']}</h1>
      <p class="role">{ME['role']}<br>{ME['org']} · {ME['location']}</p>
      <p class="tagline">{ME['tagline']}</p>
      <div class="links">
        <a href="mailto:{ME['email']}">Email</a>
        <a href="{ME['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="{ME['github']}" target="_blank" rel="noopener">GitHub</a>
        <a href="assets/Carmen_Pelayo_CV.pdf" target="_blank" rel="noopener">CV (PDF)</a>
      </div>
    </div>
    <figure class="chartcard" style="margin:0">
      {build_chart()}
      <figcaption class="chart-caption">A finding I’m proud of: computer science went from &lt;10% of arXiv to ~50% in fifteen years.</figcaption>
    </figure>
  </div>
</header>

<main>
<section id="about">
  <div class="wrap">
    <p class="sec-eyebrow">01 · About</p>
    <h2>Turning unstructured data into economic insight</h2>
    <p class="lede">{ABOUT}</p>
    <ul class="chips">{li(INTERESTS)}</ul>
  </div>
</section>

<section id="research">
  <div class="wrap">
    <p class="sec-eyebrow">02 · Research &amp; Publications</p>
    <h2>Research</h2>
    {pubs_html()}
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <p class="sec-eyebrow">03 · Experience</p>
    <h2>Where I’ve worked</h2>
    <div class="xp">{xp_html()}</div>
  </div>
</section>

<section id="projects">
  <div class="wrap">
    <p class="sec-eyebrow">04 · Projects &amp; Code</p>
    <h2>Selected projects</h2>
    <div class="grid2">{proj_html()}</div>
  </div>
</section>

<section id="education">
  <div class="wrap">
    <p class="sec-eyebrow">05 · Education</p>
    <h2>Education</h2>
    <div class="edu">{edu_html()}</div>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <p class="sec-eyebrow">06 · Skills</p>
    <h2>Toolbox</h2>
    {skills_html()}
    <ul class="awards">{li(AWARDS)}</ul>
  </div>
</section>
</main>

<footer id="contact">
  <div class="wrap">
    <p class="big">Let’s talk about data, economics and responsible AI.</p>
    <div class="links">
      <a href="mailto:{ME['email']}">{ME['email']}</a>
      <a href="{ME['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
      <a href="{ME['github']}" target="_blank" rel="noopener">GitHub</a>
    </div>
    <p class="fine">© 2026 {ME['name']} · Site generated with a 300-line Python script — <a href="https://github.com/carmenpelayo/carmenpelayo.github.io">source</a></p>
  </div>
</footer>

<script src="assets/script.js"></script>
</body>
</html>"""

# ----------------------------------------------------------------------------
def main():
    os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML)
    with open(os.path.join(OUT_DIR, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(OUT_DIR, "assets", "script.js"), "w", encoding="utf-8") as f:
        f.write(JS)
    print("Built index.html + assets/")

if __name__ == "__main__":
    main()
