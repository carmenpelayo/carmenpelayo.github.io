
document.documentElement.classList.add('js');
if('IntersectionObserver' in window){
const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');obs.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
}else{document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));}
