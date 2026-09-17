# AP Statistics in Twenty Hours

A twenty-hour AP Statistics course built for one-to-one tuition: usable live on a
shared screen during a session, and afterwards for revision. Aligned to the
Course and Exam Description effective Fall 2026.

**Live site:** https://sevketgunduz.github.io/ap-statistics-20-hours/

## What is here

| Path | What it is |
| --- | --- |
| `site/` | The published static site (no server, no build step at deploy time) |
| `build/build.py` | Generates `site/` from the Markdown documents in the project root |
| `build/assets/` | Source stylesheet and script, copied into `site/assets/` |
| `Session-*.md` | Course documents: tutor notes, student workbooks, tests |
| `STANDARDS.md` | House style and authoring conventions |

## Rebuilding after an edit

Edit the Markdown, then:

```
python build/build.py
git add -A
git commit -m "Update session material"
git push
```

`build.py` deletes and regenerates `site/` on each run, so nothing should be
edited inside `site/` by hand. Pushing to `main` redeploys automatically via
`.github/workflows/pages.yml`.

## Note on sources

The reference PDFs used while writing this course (Barron's, Princeton Review,
5 Steps to a 5, and the College Board CED) are deliberately excluded from this
repository by `.gitignore`. They are copyrighted and are not redistributed here.
