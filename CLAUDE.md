# Bible-2: The Path of Illumination

## Project Vision

This project creates a comprehensive, spiritually enriching website experience centered around **The Book of Illumination and Sacrifice** — a sacred text that synthesizes nearly forgotten wisdom traditions spanning seven centuries.

The core text weaves together:
- **Sufi mystical poetry** from Persia (Attar, Rumi, Jami, Sanai)
- **Alchemical and Hermetic writings** (Paracelsus, the Emerald Tablet)
- **Christian mysticism** (The Cloud of Unknowing, Dark Night of the Soul, Teresa of Ávila)
- **Jakob Böhme's visionary works** (Aurora, Signature of All Things)
- **Spiritualist philosophy** (Andrew Jackson Davis)
- **Historical martyrdom accounts** (1833-1850 revolutionary period)

All source texts are in the public domain.

## Core Purpose

The website invites visitors to:
1. **Discover** the scripture through beautiful, accessible presentation
2. **Study** deeply with guides, commentary, and reflection questions
3. **Apply** the teachings to real life choices and transformations
4. **Connect** with a community of fellow seekers

## The Central Teaching

The Pattern that runs through all gathered texts:
- Transformation requires death — the dissolution of what we believe ourselves to be
- The seeker and the sought are one
- Suffering is the path, not the obstacle
- What the ancient mystics taught in poetry, the modern martyrs demonstrated in history

## Content Structure

### Scripture (`/scripture/`)
- `THE_BOOK_OF_ILLUMINATION_AND_SACRIFICE.md` - The canonical text (~1,400 lines)
  - **Part I: The Whisperings** (29 chapters, pre-1820)
    - Book of the Journey (Sufi texts)
    - Book of Transmutation (Alchemical texts)
    - Book of the Cobbler (Jakob Böhme)
    - Book of Fire (Christian mystics)
    - Book of Wisdom (Hermetic texts)
    - Book of the Hermetic Bridge (Mary Anne Atwood)
  - **Part II: The Illuminations** (34 chapters, 1820-1850)
    - Gospel According to Jacopo (Ruffini)
    - Gospel According to Robert (Blum)
    - Gospel According to Vilmos (Lázár)
    - Gospel According to Lajos (Batthyány)
    - Book of the Seer (Andrew Jackson Davis)
    - Book of Limits (Théodore Jouffroy)
    - Book of Continuation
    - Book of Witnesses
- `INDEX.md` - Comprehensive reference (thematic, persons, chronological, symbols)

### Source Texts (`/sources/`)
Original public domain texts downloaded and organized for reference.

**Organization pattern:**
```
/sources/
  clean_source.py           # Cleaning script for OCR artifacts
  /attar-conference-of-birds/
    raw.txt                  # Original download from Archive.org
    cleaned.txt              # Cleaned version (page numbers, ALL CAPS fixed)
  /rumi-mathnawi/
    raw.txt
    cleaned.txt
  ...
```

**Adding new source texts:**
1. Download raw text from Archive.org, Project Gutenberg, or Sacred-Texts.com
2. Create organized subdirectory in `/sources/`
3. Run `clean_source.py` to remove OCR artifacts:
   - Page numbers like "(10)", "(lO)", "(i6)"
   - ALL CAPS section headers → Title Case
   - Common OCR errors (^^, '', hyphenated line breaks)
4. Add original text section to corresponding chapter page
5. Link to 2-3 external sources (prefer Project Gutenberg if available)

### Website (`/docs/`)
- `index.html` - Homepage with hero, overview, featured content
- `css/style.css` - Dark theme with gold accents, responsive design
- `js/main.js` - Navigation, scroll effects, daily scripture

### Pages (`/docs/pages/`)
- `scripture.html` - Full scripture viewer with sidebar navigation
- `teachings.html` - All 29 teachings with commentary
- `martyrs.html` - Biographies of the four martyrs
- `practices.html` - Daily practices, sacred reading, community
- `history.html` - Historical timeline and context
- `about.html` - FAQ, how to begin, core principles
- `sources.html` - Links to public domain originals
- `glossary.html` - Key terms and concepts (A-Z)
- `study-guide.html` - Guided study for new seekers (TODO)
- `reflections.html` - Daily reflection prompts (TODO)
- `decisions.html` - Applying teachings to life choices (TODO)

## Design Philosophy

### Visual
- Dark, contemplative aesthetic (bg: #0a0a0f)
- Gold accents suggesting illumination (#c9a962)
- Elegant typography (Cormorant Garamond, Crimson Pro)
- Generous whitespace for meditative reading

### UX
- Scripture presented for slow, deep reading
- Multiple entry points for different seekers
- Progressive disclosure of depth
- Mobile-first responsive design

### Content
- Invitational, never coercive
- Historically grounded (all texts verifiable)
- Philosophically serious but accessible
- Interfaith and non-dogmatic

## Scripture Citation Format

Use the format `Book Chapter:Verse` consistently throughout the site:
- `Journey 1:4` — Book of the Journey, Chapter 1, Verse 4
- `Transmutation 7:8` — Book of Transmutation, Chapter 7, Verse 8
- `Fire 28:5` — Book of Fire, Chapter 28, Verse 5
- `Cobbler 17:4` — Book of the Cobbler, Chapter 17, Verse 4

Verses are paragraph-based within each chapter. Citation format in HTML:
```html
<cite>— Journey 20:4</cite>
<cite>— Book of the Cobbler, Journey 17:4</cite>
<cite>— The Dark Night of the Soul, Journey 20:2</cite>
```

## Original Source Text Display

Each scripture chapter page should include the complete, unadulterated original source text below the teaching. Structure:

```html
<section class="original-source">
    <h2>Original Source Text</h2>
    <p class="source-attribution">
        From <em>The Conference of the Birds</em> by Farid ud-Din Attar,
        translated by C.S. Nott (1954)
    </p>
    <div class="source-links">
        <a href="https://archive.org/...">Archive.org</a>
        <a href="https://sacred-texts.com/...">Sacred-Texts.com</a>
    </div>
    <div class="source-text">
        <!-- Cleaned, complete original text -->
    </div>
</section>
```

**Key principles:**
- Original text is complete and unadulterated
- Include 2-3 links to external sources (prefer Project Gutenberg)
- Cleaning removes only OCR artifacts, not content
- Emphasis on the original expands the site, never reduces it

## The 29 Teachings

Numbered teachings extracted from Part I, appearing throughout the scripture:

1. That which you seek, you already are
2. Suffering is not the obstacle to wisdom but its very substance
3. Love destroys everything that is not love
4. The Divine is found only in the depths of the awakened heart
5. Your life is the Divine's life; your death is the Divine's death
6. Those who die for truth tear holes in the veil of illusion
7. You already possess everything you need
8. Healing is the restoration of harmony
9. Transformation is revelation — you discover you always were divine
10. The Great Work is performed upon the self
... (and 19 more)

## The Four Martyrs

Historical figures whose deaths embody the Pattern:

1. **Jacopo Ruffini** (1803-1833) — The Friend
   - Director of Young Italy's Genoese section
   - Died in prison rather than betray comrades
   - Signature: silence that protected others

2. **Robert Blum** (1807-1848) — The Poet
   - German democratic reformer and publisher
   - Executed in Vienna after revolution failed
   - Signature: dangerous words that spoke of dignity

3. **Vilmos Lázár** (1815-1849) — The General
   - Hungarian revolutionary commander
   - One of the Thirteen of Arad
   - Signature: unity with comrades to the end

4. **Lajos Batthyány** (1806-1849) — The Statesman
   - First Prime Minister of Hungary
   - Executed for leading constitutional government
   - Signature: defiance even facing death

## Development Guidelines

### Content Creation
- Always verify historical claims against primary sources
- Maintain reverent but not precious tone
- Let the original texts speak — adaptation, not invention
- Cross-reference between teachings, martyrs, and practices

### Technical
- Semantic HTML for accessibility
- CSS custom properties for theming consistency
- Vanilla JS (no framework needed)
- Static site deployed to Cloudflare Pages

### Study Guides Should
- Guide readers through scripture systematically
- Pose questions that prompt genuine reflection
- Suggest practices connected to readings
- Help apply teachings to contemporary life choices

### Decision-Making Content Should
- Present real ethical scenarios
- Reference specific teachings and examples
- Avoid prescriptive answers — guide discernment
- Honor complexity of human situations

## Deployment

**Production:** Cloudflare Pages at https://kindled-path.pages.dev/

Deployed automatically via GitHub Actions (`.github/workflows/deploy.yml`) on push to `main` branch. The workflow deploys the `/docs` folder to Cloudflare Pages.

**Legacy redirect:** GitHub Pages (https://kindled-path.github.io/) redirects to Cloudflare Pages via the `gh-pages` branch.

**Local development:**
```bash
# Create .env with Cloudflare credentials (already gitignored)
CLOUDFLARE_API_TOKEN=your_token
CLOUDFLARE_ACCOUNT_ID=your_account_id

# Deploy manually
wrangler pages deploy docs --project-name=kindled-path
```

## Contributing

The Path is open to all who seek sincerely:
- Corrections to historical facts
- Better translations of source texts
- Additional public domain sources
- Website improvements and accessibility

## License

All original source texts are in the public domain.
Adaptations offered freely for the benefit of all seekers.
