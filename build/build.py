# -*- coding: utf-8 -*-
"""
AP Statistics course site builder.

    python build/build.py

Reads build/manifest.json, converts every source into a page that shares
build/assets/course.css and course.js, wires prev/next and the contents
sidebar, and writes the result to site/.

Sources may be:
  kind "md"            a markdown file in the project root (authoring format,
                       see STANDARDS.md for the directive set)
  kind "html"/"tool"   an existing body fragment in the scratchpad (legacy
                       hand-written pages, wrapped unchanged)
  kind "index"         the generated course home page

Everything is relative-path, so the site works opened from disk (file://)
and on any static host without configuration.
"""
import json, os, re, shutil, html as H, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
SITE = os.path.join(ROOT, "site")
FIGS_IN = os.path.join(ROOT, "figures")
FRAGMENTS = [
    os.path.join(ROOT, "build", "fragments"),
    r"C:\Users\vrlabacademy\AppData\Local\Temp\claude\C--10-AP-Statistics\c4beae93-3502-45f0-90c2-bb24e78dd325\scratchpad",
]
MAN = json.load(open(os.path.join(BUILD, "manifest.json"), encoding="utf-8"))

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=IBM+Plex+Mono:wght@400;500;600&"
         "family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&"
         "family=Spectral:ital,wght@0,600;0,700;1,600&display=swap")


# ------------------------------------------------------------------ markdown
def inline_md(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"!\[(.*?)\]\((.+?)\)", "", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*([^\*]+?)\*(?!\*)", r"<em>\1</em>", t)
    return t


def read_svg(name):
    for d in (FIGS_IN,):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return open(p, encoding="utf-8").read()
    return None


def render_md(md, depth):
    """Markdown + the course directive set -> HTML body."""
    out, i = [], 0
    lines = md.split("\n")
    n = len(lines)
    while i < n:
        s = lines[i].strip()

        # ---- directives -------------------------------------------------
        m = re.match(r"^:::(\w+)\s*(.*)$", s)
        if m:
            kind, arg = m.group(1), m.group(2).strip()
            i += 1
            buf = []
            while i < n and lines[i].strip() != ":::":
                buf.append(lines[i]); i += 1
            i += 1
            inner = "\n".join(buf)
            if kind in ("note", "teal", "amber", "red"):
                tone = arg.split()[0] if (kind == "note" and arg) else (kind if kind != "note" else "teal")
                lbl = arg[len(tone):].strip() if kind == "note" else arg
                out.append('<div class="note %s">%s%s</div>' % (
                    tone,
                    ('<span class="lbl">%s</span>' % inline_md(lbl)) if lbl else "",
                    render_md(inner, depth)))
            elif kind == "script":
                rows = ""
                for ln in inner.split("\n"):
                    mm = re.match(r"^\s*(ask|listen|ifsay|intro)\s*\|\s*(.*?)\s*\|\s*(.*)$", ln, re.I)
                    if mm:
                        rows += '<div class="line %s"><span class="lbl">%s</span><span class="txt">%s</span></div>' % (
                            mm.group(1).lower(), inline_md(mm.group(2)), inline_md(mm.group(3)))
                out.append('<div class="script">%s</div>' % rows)
            elif kind == "yourturn":
                out.append('<div class="yourturn">%s</div>' % render_md(inner, depth))
            elif kind == "reveal":
                out.append("<details><summary><strong>%s</strong></summary>%s</details>" % (
                    inline_md(arg or "Reveal"), render_md(inner, depth)))
            elif kind == "formula":
                out.append('<div class="formula">%s</div>' % inline_md(inner.strip()))
            elif kind == "checks":
                out.append('<div class="checks">%s</div>' % "".join(
                    '<span class="chk">%s</span>' % inline_md(x.strip())
                    for x in inner.split("\n") if x.strip()))
            elif kind == "sim":
                parts = [p.strip() for p in arg.split("|")]
                sid = parts[0]
                ttl = parts[1] if len(parts) > 1 else sid
                hgt = parts[2] if len(parts) > 2 else "720"
                up = "../" * depth
                out.append(
                    '<div class="sim"><div class="sim-head"><span class="lbl">Interactive</span>'
                    '<span class="ttl">%s</span>'
                    '<a href="%stools/%s.html" target="_blank" rel="noopener">Open full screen &#8599;</a></div>'
                    '<div class="sim-body"><iframe src="%stools/%s.html" height="%s" loading="lazy" '
                    'title="%s"></iframe></div>%s</div>' % (
                        H.escape(ttl), up, sid, up, sid, hgt, H.escape(ttl),
                        ('<div class="sim-why">%s</div>' % render_md(inner, depth)) if inner.strip() else ""))
            else:
                out.append(render_md(inner, depth))
            continue

        # ---- raw html passthrough --------------------------------------
        if s.startswith("<details") or s.startswith("</details") or s.startswith("<summary"):
            out.append(s); i += 1; continue
        if not s:
            i += 1; continue
        if s == "---":
            out.append("<hr>"); i += 1; continue

        # ---- figure -----------------------------------------------------
        m = re.match(r"^!\[(.*?)\]\(figures/(.+?)\.svg\)$", s)
        if m:
            svg = read_svg(m.group(2) + ".svg")
            cap = ""
            if i + 2 < n and lines[i + 2].strip().startswith("*") and lines[i + 2].strip().endswith("*"):
                cap = inline_md(lines[i + 2].strip()[1:-1]); i += 2
            if svg:
                out.append('<figure><div class="figscroll">%s</div>%s</figure>' % (
                    svg, ('<figcaption>%s</figcaption>' % cap) if cap else ""))
            i += 1; continue

        # ---- fenced code -------------------------------------------------
        if s.startswith("```"):
            i += 1; buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre class="data">%s</pre>' % H.escape("\n".join(buf)))
            continue

        # ---- heading -----------------------------------------------------
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lv = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lv, inline_md(m.group(2)), lv))
            i += 1; continue

        # ---- table -------------------------------------------------------
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-\|]+\|$", lines[i + 1].strip()):
            hdr = [c.strip() for c in s.strip("|").split("|")]
            i += 2; rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            th = "".join("<th>%s</th>" % inline_md(c) for c in hdr)
            tb = ""
            for r in rows:
                cls = ' class="tot"' if r and r[0].startswith("**") else ""
                tb += "<tr%s>%s</tr>" % (cls, "".join("<td>%s</td>" % inline_md(c) for c in r))
            out.append('<div class="tbl"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                       % (th, tb))
            continue

        # ---- blockquote --------------------------------------------------
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("<blockquote>%s</blockquote>" %
                       "<br>".join(inline_md(b) for b in buf if b))
            continue

        # ---- lists -------------------------------------------------------
        if re.match(r"^- \[ \]", s):
            items = []
            while i < n and re.match(r"^- \[ \]", lines[i].strip()):
                items.append(inline_md(lines[i].strip()[6:])); i += 1
            out.append('<ul class="checklist">%s</ul>' % "".join("<li>%s</li>" % t for t in items))
            continue
        if s.startswith("- "):
            items = []
            while i < n and lines[i].strip().startswith("- "):
                items.append(inline_md(lines[i].strip()[2:])); i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % t for t in items))
            continue
        if re.match(r"^\d+\.\s", s):
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(inline_md(re.sub(r"^\d+\.\s", "", lines[i].strip()))); i += 1
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % t for t in items))
            continue

        # ---- paragraph ----------------------------------------------------
        buf = []
        stop = r"^(#{1,4}\s|\||>|- |\d+\.\s|```|!\[|---$|:::|<details|</details|<summary)"
        while i < n and lines[i].strip() and not re.match(stop, lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        p = inline_md(" ".join(buf))
        cls = ' class="yourturn"' if p.startswith("<strong>Your turn.") else ""
        out.append("<p%s>%s</p>" % (cls, p))
    return "\n".join(out)


# ------------------------------------------------------------------ nav data
FLAT = []
for g in MAN["groups"]:
    for it in g["items"]:
        it["_group"] = g["label"]
        FLAT.append(it)


def depth_of(out):
    return out.count("/")


def nav_for(idx):
    it = FLAT[idx]
    d = depth_of(it["out"])
    up = "../" * d

    def href(o):
        return up + o

    nav = {
        "kicker": (it.get("topics") or MAN["kicker"]),
        "title": it.get("title") or it["label"],
        "map": [],
    }
    if idx > 0:
        nav["prev"] = {"href": href(FLAT[idx - 1]["out"]), "label": FLAT[idx - 1]["label"]}
    if idx < len(FLAT) - 1:
        nav["next"] = {"href": href(FLAT[idx + 1]["out"]), "label": FLAT[idx + 1]["label"]}
    # tutor <-> student switch
    if it.get("session"):
        sibs = [o for o in FLAT if o.get("session") == it["session"]]
        if len(sibs) > 1:
            nav["variants"] = [{"href": href(s["out"]),
                                "label": (s.get("variant") or "").capitalize(),
                                "current": s["id"] == it["id"]} for s in sibs]
    for g in MAN["groups"]:
        nav["map"].append({"label": g["label"],
                           "items": [{"href": href(o["out"]), "label": o["label"],
                                      "current": o["id"] == it["id"]} for o in g["items"]]})
    return nav


# ------------------------------------------------------------------ page shell
def page(body, nav, title, depth, extra_head="", main_cls=""):
    up = "../" * depth
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>%s</title>\n"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
        "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n"
        "<link rel=\"stylesheet\" href=\"%s\">\n"
        "<link rel=\"stylesheet\" href=\"%sassets/course.css\">\n%s</head>\n<body>\n"
        "<main class=\"%s\">\n%s\n</main>\n"
        "<script>window.COURSE_NAV=%s;</script>\n"
        "<script src=\"%sassets/course.js\"></script>\n</body>\n</html>\n"
        % (H.escape(title), FONTS, up, extra_head, main_cls, body,
           json.dumps(nav, ensure_ascii=False), up))



COMPAT = ("<style>"
          "/* legacy fragment: .page already supplies the column */"
          ".page > .wrap, .page section > .wrap, .page .wrap{max-width:none;padding-inline:0}"
          ".page > section, .page > header.mast{padding-block:26px}"
          ".page > header.mast{background:none;border:0}"
          "</style>")
COMPAT_TOOL = ("<style>.page{max-width:none;padding-inline:0}"
               ".page .wrap{max-width:62rem}</style>")


def find_fragment(name):
    for d in FRAGMENTS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return open(p, encoding="utf-8").read()
    return None


# ------------------------------------------------------------------ home page
def build_home(nav):
    rows = ""
    for g in MAN["groups"]:
        if g["label"] == "Course":
            continue
        cards = ""
        for it in g["items"]:
            tone = " live" if it["kind"] == "tool" else ""
            cards += ('<a class="card%s" href="%s"><span class="tag">%s</span>'
                      '<span class="name">%s</span><span class="desc">%s</span></a>'
                      % (tone, it["out"], H.escape(it.get("topics") or ""),
                         H.escape(it.get("title") or it["label"]),
                         H.escape(it.get("blurb") or it["label"])))
        rows += '<h2>%s</h2><div class="cardgrid">%s</div>' % (H.escape(g["label"]), cards)
    css = ("<style>.cardgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));"
           "gap:13px;margin-bottom:26px}a.card{display:flex;flex-direction:column;gap:7px;text-decoration:none;"
           "color:inherit;background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--accent);"
           "border-radius:3px;padding:17px 19px}a.card:hover{border-color:var(--accent);background:var(--accent-soft)}"
           "a.card .tag{font-family:var(--f-mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;"
           "color:var(--accent);font-weight:600}a.card .name{font-family:var(--f-display);font-size:1.1rem;"
           "font-weight:600}a.card .desc{font-size:.88rem;color:var(--ink-2)}a.card.live{border-left-color:var(--amber)}"
           "a.card.live .tag{color:var(--amber)}</style>")
    body = ('<h1>%s</h1><p class="standfirst">%s &middot; built for one-to-one tuition, '
            'usable live on a shared screen and afterwards for revision.</p>%s%s'
            % (H.escape(MAN["course"]), H.escape(MAN["ced"]), css, rows))
    return body


# ------------------------------------------------------------------ main
def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    shutil.copytree(os.path.join(BUILD, "assets"), os.path.join(SITE, "assets"))
    if os.path.isdir(FIGS_IN):
        shutil.copytree(FIGS_IN, os.path.join(SITE, "assets", "figures"), dirs_exist_ok=True)

    built, missing = 0, []
    for idx, it in enumerate(FLAT):
        nav = nav_for(idx)
        d = depth_of(it["out"])
        outp = os.path.join(SITE, it["out"].replace("/", os.sep))
        os.makedirs(os.path.dirname(outp), exist_ok=True)

        if it["kind"] == "index":
            body = build_home(nav)
        elif it["kind"] == "md":
            src = os.path.join(ROOT, it["src"])
            if not os.path.exists(src):
                missing.append(it["src"]); continue
            body = render_md(open(src, encoding="utf-8").read(), d)
            body = body.replace("</strong> <strong>CED Topics", "</strong><br><strong>CED Topics", 1)
            body = body.replace("<p><strong>AP Statistics", '<p class="standfirst"><strong>AP Statistics', 1)
        else:
            name = it["src"].split(":", 1)[1]
            frag = find_fragment(name)
            if frag is None:
                missing.append(name); continue
            frag = re.sub(r"<title>.*?</title>\s*", "", frag, count=1, flags=re.S)
            frag = re.sub(r'<link rel="preconnect".*?>\s*', "", frag, flags=re.S)
            frag = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis[^>]*>\s*', "", frag)
            body = (COMPAT_TOOL if it["kind"] == "tool" else COMPAT) + frag

        open(outp, "w", encoding="utf-8").write(
            page(body, nav, (it.get("title") or it["label"]) + " · " + MAN["course"], d,
                 main_cls="page" + (" page--wide" if it["kind"] == "tool" else "")))
        built += 1
        print("  built %-34s <- %s" % (it["out"], it["src"] or "(generated)"))

    print("\n%d pages -> %s" % (built, SITE))
    if missing:
        print("MISSING SOURCES:", missing); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
