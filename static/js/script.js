const observer = new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add("show");

}

});

},{
threshold:0.2
});

document.querySelectorAll(

'.feature-card,.stat-card,.mission-card,.workflow-card,.tech-card,.predict-card,.result-card'

).forEach(el=>{

observer.observe(el);

});