/* ============================================================
   AP Statistics — twenty-hour course
   Shell behaviour: contents sidebar (resizable, collapsible),
   prev/next navigation, theme, keyboard shortcuts.
   Reads window.COURSE_NAV, injected per page by the build.
   ============================================================ */
(function () {
  "use strict";

  var LS = {
    theme: "apstats-theme",
    sbWidth: "apstats-sidebar-width",
    sbClosed: "apstats-sidebar-closed"
  };
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var root = document.documentElement;
  var body = document.body;
  var NAV = window.COURSE_NAV || {};

  /* ---------------- theme ---------------- */
  var saved = get(LS.theme);
  if (saved) root.setAttribute("data-theme", saved);
  function isDark() {
    var t = root.getAttribute("data-theme");
    return t === "dark" || (!t && window.matchMedia("(prefers-color-scheme: dark)").matches);
  }

  /* ---------------- build the shell ---------------- */
  var main = document.querySelector("main");
  if (!main) return;

  // wrap main in .shell/.page if the page did not already
  var shell = document.createElement("div");
  shell.className = "shell";
  main.parentNode.insertBefore(shell, main);
  shell.appendChild(main);
  if(!main.classList.contains("page")) main.classList.add("page");

  /* ---- topbar ---- */
  var bar = document.createElement("div");
  bar.className = "topbar";
  bar.innerHTML =
    '<button class="tb-btn" id="sbToggle" type="button" aria-label="Toggle contents" title="Contents (c)">' +
      '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true">' +
      '<rect x="0" y="1.5" width="14" height="1.6" fill="currentColor"/>' +
      '<rect x="0" y="6.2" width="14" height="1.6" fill="currentColor"/>' +
      '<rect x="0" y="10.9" width="14" height="1.6" fill="currentColor"/></svg>' +
      '<span class="tb-hide-sm">Contents</span></button>' +
    '<div class="tb-title"><small>' + (NAV.kicker || "AP Statistics") + '</small>' +
      (NAV.title || document.title) + '</div>' +
    (NAV.variants && NAV.variants.length > 1
      ? '<div class="tb-seg tb-hide-sm">' + NAV.variants.map(function (v) {
          return '<a href="' + v.href + '"' + (v.current ? ' aria-current="page"' : "") + '>' + v.label + "</a>";
        }).join("") + "</div>"
      : "") +
    '<button class="tb-btn" id="navPrev" type="button" title="Previous (←)">←<span class="tb-hide-sm">Back</span></button>' +
    '<button class="tb-btn" id="navNext" type="button" title="Next (→)"><span class="tb-hide-sm">Next</span>→</button>' +
    '<button class="tb-btn" id="themeBtn" type="button" title="Toggle theme (d)"></button>';
  body.insertBefore(bar, body.firstChild);

  var scrim = document.createElement("div");
  scrim.className = "scrim";
  body.appendChild(scrim);

  /* ---- sidebar ---- */
  var sb = document.createElement("nav");
  sb.className = "sidebar";
  sb.setAttribute("aria-label", "Contents");
  sb.innerHTML =
    '<div class="sb-head"><span class="eyebrow">Contents</span>' +
      '<button class="tb-btn" id="sbClose" type="button" aria-label="Hide contents" ' +
      'style="padding:3px 8px;font-size:.7rem">Hide</button></div>' +
    '<div class="sb-scroll" id="sbScroll"></div>' +
    '<div class="sb-grip" id="sbGrip" role="separator" aria-orientation="vertical" ' +
    'aria-label="Resize contents" tabindex="0"></div>';
  body.insertBefore(sb, shell);

  /* ---- fill the sidebar: this page's headings, then the course map ---- */
  var scroll = document.getElementById("sbScroll");
  var heads = [].slice.call(main.querySelectorAll("h2, h3"));
  if (heads.length) {
    var sec = document.createElement("div");
    sec.className = "sb-sec";
    sec.innerHTML = '<span class="lbl">On this page</span>';
    heads.forEach(function (h, i) {
      if (!h.id) {
        h.id = "s-" + i + "-" + (h.textContent || "").toLowerCase()
          .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40);
      }
      var a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent;
      if (h.tagName === "H3") a.className = "lv3";
      a.dataset.target = h.id;
      sec.appendChild(a);
    });
    scroll.appendChild(sec);
  }
  if (NAV.map && NAV.map.length) {
    NAV.map.forEach(function (group) {
      var sec = document.createElement("div");
      sec.className = "sb-sec";
      sec.innerHTML = '<span class="lbl">' + group.label + "</span>";
      group.items.forEach(function (it) {
        var a = document.createElement("a");
        a.href = it.href;
        a.textContent = it.label;
        if (it.current) a.className = "active";
        sec.appendChild(a);
      });
      scroll.appendChild(sec);
    });
  }

  /* ---- scroll spy ---- */
  var links = [].slice.call(scroll.querySelectorAll("a[data-target]"));
  if (links.length && "IntersectionObserver" in window) {
    var seen = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { seen[e.target.id] = e.isIntersecting ? e.intersectionRatio : 0; });
      var best = null, bestV = 0;
      links.forEach(function (a) {
        var v = seen[a.dataset.target] || 0;
        if (v > bestV) { bestV = v; best = a; }
      });
      if (best) links.forEach(function (a) { a.classList.toggle("active", a === best); });
    }, { rootMargin: "-" + (parseInt(getComputedStyle(root).getPropertyValue("--topbar")) + 10) + "px 0px -60% 0px",
         threshold: [0, .25, .6, 1] });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* ---- sidebar open/close ---- */
  var narrow = function () { return window.matchMedia("(max-width: 640px)").matches; };
  function openSb(on) {
    if (narrow()) { body.classList.toggle("sb-open", on); }
    else { body.classList.toggle("sb-closed", !on); set(LS.sbClosed, on ? "0" : "1"); }
  }
  if (get(LS.sbClosed) === "1" && !narrow()) body.classList.add("sb-closed");
  document.getElementById("sbToggle").addEventListener("click", function () {
    openSb(narrow() ? !body.classList.contains("sb-open") : body.classList.contains("sb-closed"));
  });
  document.getElementById("sbClose").addEventListener("click", function () { openSb(false); });
  scrim.addEventListener("click", function () { openSb(false); });
  scroll.addEventListener("click", function (e) {
    if (e.target.tagName === "A" && narrow()) openSb(false);
  });

  /* ---- sidebar resize ---- */
  var w = parseInt(get(LS.sbWidth) || "", 10);
  if (w >= 190 && w <= 560) root.style.setProperty("--sidebar", w + "px");
  var grip = document.getElementById("sbGrip"), dragging = false;
  function applyW(px) {
    px = Math.max(190, Math.min(560, px));
    root.style.setProperty("--sidebar", px + "px");
    set(LS.sbWidth, String(px));
  }
  grip.addEventListener("pointerdown", function (e) {
    dragging = true; body.classList.add("resizing");
    grip.setPointerCapture(e.pointerId); e.preventDefault();
  });
  grip.addEventListener("pointermove", function (e) { if (dragging) applyW(e.clientX); });
  grip.addEventListener("pointerup", function (e) {
    dragging = false; body.classList.remove("resizing");
    try { grip.releasePointerCapture(e.pointerId); } catch (err) {}
  });
  grip.addEventListener("keydown", function (e) {
    var cur = parseInt(getComputedStyle(root).getPropertyValue("--sidebar"), 10) || 280;
    if (e.key === "ArrowLeft") { applyW(cur - 20); e.preventDefault(); }
    if (e.key === "ArrowRight") { applyW(cur + 20); e.preventDefault(); }
  });

  /* ---- prev / next ---- */
  function go(href) { if (href) window.location.href = href; }
  var prevBtn = document.getElementById("navPrev"), nextBtn = document.getElementById("navNext");
  if (NAV.prev) prevBtn.addEventListener("click", function () { go(NAV.prev.href); });
  else prevBtn.disabled = true;
  if (NAV.next) nextBtn.addEventListener("click", function () { go(NAV.next.href); });
  else nextBtn.disabled = true;

  // big pager at the foot
  var pager = document.createElement("nav");
  pager.className = "pager";
  pager.setAttribute("aria-label", "Previous and next");
  pager.innerHTML =
    (NAV.prev
      ? '<a class="prev" href="' + NAV.prev.href + '"><span class="dir">← Back</span>' +
        '<span class="ttl">' + NAV.prev.label + "</span></a>"
      : '<span class="empty"></span>') +
    (NAV.next
      ? '<a class="next" href="' + NAV.next.href + '"><span class="dir">Next →</span>' +
        '<span class="ttl">' + NAV.next.label + "</span></a>"
      : '<span class="empty"></span>');
  main.appendChild(pager);

  /* ---- theme button ---- */
  var tb = document.getElementById("themeBtn");
  function labelTheme() { tb.textContent = isDark() ? "Light" : "Dark"; }
  tb.addEventListener("click", function () {
    var next = isDark() ? "light" : "dark";
    root.setAttribute("data-theme", next); set(LS.theme, next); labelTheme();
  });
  labelTheme();

  /* ---- keyboard ---- */
  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var t = e.target.tagName;
    if (t === "INPUT" || t === "TEXTAREA" || t === "SELECT" || e.target.isContentEditable) return;
    if (e.key === "ArrowLeft" && NAV.prev) go(NAV.prev.href);
    else if (e.key === "ArrowRight" && NAV.next) go(NAV.next.href);
    else if (e.key === "c") openSb(narrow() ? !body.classList.contains("sb-open") : body.classList.contains("sb-closed"));
    else if (e.key === "d") tb.click();
    else if (e.key === "e") {           // expand/collapse every reveal on the page
      var ds = [].slice.call(main.querySelectorAll("details"));
      var anyClosed = ds.some(function (d) { return !d.open; });
      ds.forEach(function (d) { d.open = anyClosed; });
    }
  });
})();
