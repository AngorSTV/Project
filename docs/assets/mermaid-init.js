(function(){
  function render(){
    if(!window.mermaid) return;
    window.mermaid.initialize({ startOnLoad:false, securityLevel:'strict' });
    try{ window.mermaid.run({ querySelector: '.mermaid' }); }catch(e){ console.warn('Mermaid render failed', e); }
  }

  if(window.document$ && typeof window.document$.subscribe === 'function'){
    window.document$.subscribe(function(){ render(); });
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', render);
  } else {
    render();
  }
})();
