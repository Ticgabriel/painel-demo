from pathlib import Path
p=Path(__file__).parent
src=p/'src'
base=(src/'app.js').read_text();pos=base.index('try{let saved=localStorage.getItem(KEY)')
base=base[:pos]+'\n'.join((src/f).read_text() for f in ['revision.js','ux.js'])+'\n'+base[pos:]
base+='\ndocument.querySelector(".topActions").insertAdjacentHTML("afterbegin",\'<a href="../gerencial.html" target="_blank" rel="noopener">Gerencial ↗</a><a href="../comercial.html" target="_blank" rel="noopener">Comercial ↗</a>\');'
css='\n'.join((src/f).read_text() for f in ['style.css','portfolio.css','revision.css','ux.css'])+'\n.grade .top:before{content:"DEMO · DADOS FICTÍCIOS";font-size:9px;color:#8b6412;font-weight:700;max-width:85px}.topActions a{font-size:11px;color:var(--accent)}'
js='const MODE="grade";const SEED='+(src/'seed.json').read_text()+';const MULTI='+(src/'multi.json').read_text()+';\n'+base
(p/'index.html').write_text('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Planejador · demonstração fictícia</title><style>'+css+'</style></head><body><script>'+js.replace('</script','<\\/script')+'</script></body></html>')
(p/'combined.js').write_text(js)
print('Demonstração reconstruída.')
