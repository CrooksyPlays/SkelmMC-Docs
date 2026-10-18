(() => {
  'use strict';
  const root = document.body.dataset.root || './';
  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => [...document.querySelectorAll(selector)];
  const themeToggle = $('#theme-toggle');
  themeToggle?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('skelm-theme', next); } catch (_) {}
  });

  const side = $('#sidebar');
  const sideButton = $('#mobile-menu');
  const backdrop = $('#mobile-backdrop');
  const setSideOpen = (open) => {
    side?.classList.toggle('open', open);
    backdrop?.classList.toggle('open', open);
    sideButton?.setAttribute('aria-expanded', String(open));
    sideButton?.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  };
  sideButton?.addEventListener('click', () => setSideOpen(!side?.classList.contains('open')));
  backdrop?.addEventListener('click', () => setSideOpen(false));
  $$('.side-link').forEach((el) => el.addEventListener('click', () => setSideOpen(false)));

  // Code-copy buttons are rendered by the static site builder.
  $$('.copy-code').forEach((button) => button.addEventListener('click', async () => {
    const code = button.closest('.code-frame')?.querySelector('pre code, pre');
    if (!code) return;
    try {
      await navigator.clipboard.writeText(code.textContent);
      button.textContent = 'Copied!';
      setTimeout(() => { button.textContent = 'Copy'; }, 1600);
    } catch (_) {
      button.textContent = 'Select to copy';
      const range = document.createRange(); range.selectNodeContents(code);
      window.getSelection()?.removeAllRanges(); window.getSelection()?.addRange(range);
    }
  }));

  const headings = $$('.markdown-body h2[id], .markdown-body h3[id]');
  const tocLinks = $$('.toc a[href^="#"]');
  if (headings.length && 'IntersectionObserver' in window) {
    let activeId = null;
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) activeId = entry.target.id;
      });
      if (activeId) tocLinks.forEach(el => el.classList.toggle('active', el.getAttribute('href') === '#' + activeId));
    }, {rootMargin:'-110px 0px -68% 0px', threshold:0});
    headings.forEach(h => obs.observe(h));
  }

  // Local, dependency-free, full-content search with keyboard support.
  const overlay = $('#search-overlay');
  const input = $('#search-input');
  const results = $('#search-results');
  const closeButton = $('#close-search');
  let docs = null;
  let chosen = 0;
  let matching = [];
  const siteBase = new URL(root, window.location.href);
  async function loadIndex() {
    if (docs !== null) return docs;
    try {
      const resp = await fetch(new URL('search-index.json', siteBase));
      if (!resp.ok) throw new Error('Cannot load search index');
      docs = await resp.json();
    } catch (_) {
      docs = [];
      if (results) results.textContent = 'Search unavailable in file preview. Use the included local server to enable it.';
    }
    return docs;
  }
  function score(item, query) {
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    const title = item.title.toLowerCase(), section = item.section.toLowerCase();
    const slug = item.slug.toLowerCase(), head = item.headings.join(' ').toLowerCase();
    const body = item.text.toLowerCase();
    let total = 0;
    for (const term of terms) {
      if (title === term) total += 200;
      else if (title.includes(term)) total += 55;
      if (section.includes(term)) total += 13;
      if (slug.includes(term)) total += 16;
      if (head.includes(term)) total += 18;
      if (body.includes(term)) total += 5;
      if (!title.includes(term) && !section.includes(term) && !slug.includes(term) && !head.includes(term) && !body.includes(term)) return 0;
    }
    return total;
  }
  function drawResults(query) {
    if (!results) return;
    results.replaceChildren();
    if (!query.trim()) {
      const helper = document.createElement('div'); helper.className='search-hint';
      helper.textContent='Start typing to search all documentation.'; results.append(helper); matching = []; return;
    }
    if (!docs?.length) { const helper=document.createElement('div');helper.className='search-empty';helper.textContent='No index available. Run the included local server to search.';results.append(helper);return; }
    matching = docs.map(item => ({item,rank:score(item,query.trim())})).filter(x=>x.rank>0).sort((a,b)=>b.rank-a.rank).slice(0,9).map(x=>x.item);
    chosen = 0;
    if (!matching.length) { const empty=document.createElement('div');empty.className='search-empty';empty.textContent=`No results for “${query}”. Try another term.`;results.append(empty);return; }
    matching.forEach((item,i)=>{
      const a=document.createElement('a');a.className='search-result'+(i===chosen?' selected':'');a.href=new URL(item.path,siteBase).href;
      const ico=document.createElement('span');ico.className='search-result-icon';ico.innerHTML='<svg class="icon"><use href="#i-book"/></svg>';
      const body=document.createElement('span');body.className='search-result-body';
      const head=document.createElement('div');const title=document.createElement('span');title.className='search-result-title';title.textContent=item.title;
      const label=document.createElement('span');label.className='search-result-label';label.textContent=item.section;
      const summary=document.createElement('div');summary.className='search-result-summary';summary.textContent=item.description;
      head.append(title,label);body.append(head,summary);a.append(ico,body);a.addEventListener('mouseenter',()=>{chosen=i;updateChoice();});results.append(a);
    });
  }
  function updateChoice(){ $$('.search-result').forEach((el,i)=>el.classList.toggle('selected',i===chosen)); const active=$$('.search-result')[chosen];active?.scrollIntoView({block:'nearest'}); }
  async function openSearch() {
    setSideOpen(false);
    if (!overlay) return;
    overlay.classList.add('open');overlay.setAttribute('aria-hidden','false');
    document.body.style.overflow='hidden';
    input?.focus();
    await loadIndex();
    if (overlay.classList.contains('open')) drawResults(input.value);
  }
  function closeSearch() { if (!overlay)return;overlay.classList.remove('open');overlay.setAttribute('aria-hidden','true');document.body.style.overflow='';input.value=''; }
  $$('[data-open-search]').forEach(btn => btn.addEventListener('click',openSearch));
  closeButton?.addEventListener('click',closeSearch);
  overlay?.addEventListener('mousedown',(e)=>{if(e.target===overlay)closeSearch();});
  input?.addEventListener('input',()=>drawResults(input.value));
  input?.addEventListener('keydown',e=>{
    if(e.key==='ArrowDown'){e.preventDefault();chosen=Math.min(matching.length-1,chosen+1);updateChoice();}
    else if(e.key==='ArrowUp'){e.preventDefault();chosen=Math.max(0,chosen-1);updateChoice();}
    else if(e.key==='Enter'&&matching.length){e.preventDefault();window.location.href=new URL(matching[chosen].path,siteBase).href;}
  });
  document.addEventListener('keydown',e=>{
    if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();overlay?.classList.contains('open')?closeSearch():openSearch();}
    if(e.key==='Escape'){closeSearch();setSideOpen(false);}
  });
})();
