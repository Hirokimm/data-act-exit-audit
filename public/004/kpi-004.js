(()=>{
  const sink='https://ai-search-audit-dun.vercel.app/api/kpi';
  const params=new URLSearchParams(location.search);
  const synthetic=params.get('avf_synthetic')==='1';
  const emit=(event)=>{
    if(synthetic)return;
    try{
      fetch(sink,{
        method:'POST',
        headers:{'content-type':'application/json'},
        body:JSON.stringify({event}),
        keepalive:true,
        mode:'cors',
        credentials:'omit'
      }).catch(()=>{});
    }catch(_){ }
  };
  emit('article4_page_view');
  const generate=document.getElementById('generate');
  if(generate){
    generate.addEventListener('click',()=>setTimeout(()=>{
      const preview=document.getElementById('packPreview')?.textContent||'';
      if(preview && preview!=='未生成' && !preview.startsWith('未入力があります:')) emit('article4_pack_generated');
    },0));
  }
  const cta=document.getElementById('cta');
  if(cta)cta.addEventListener('click',()=>emit('article4_paid_pilot_interest'));
})();
