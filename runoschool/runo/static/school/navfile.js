document.addEventListener('DOMContentLoaded', () =>{
    //alert('Hello world')
    document.querySelector('.nav-links').style.width = '0px';
    //overflow-x: hidden

    
      var x = window.matchMedia("(max-width: 800px)")
      myFunction(x) // Call listener function at run time
      x.addListener(myFunction) // Attach listener function on state changes
    
      function myFunction(x) {
        if (x.matches) { // If media query matches
    // This controls the menu display.
    burgerClicks = 0
   document.querySelector('.burger').onclick = function(){
       burgerClicks += 1
       if((burgerClicks % 2) == 1){
       
       document.querySelector('.nav-links').style.animationName = 'expand';
       document.querySelector('.nav-links').style.animationDuration = '1s';
       document.querySelector('.nav-links').style.animationFillMode = 'forwards';
       document.querySelector('.nav-links').addEventListener('animationend', ()=>{
           
                document.querySelector('.nav-links').style.right = '0';
                 
                document.querySelector('.nav-links').style.width = '50%';  
                        })
       
       document.querySelector('.nav-links').style.right = '0';
       

        }
        else{
            document.querySelector('.nav-links').style.animationName = 'contract';
            document.querySelector('.nav-links').style.animationDuration = '1s';
            document.querySelector('.nav-links').addEventListener('animationend', ()=>{
                document.querySelector('.nav-links').style.width = '0px';
                document.querySelector('.nav-links').style.right = '-100%';   
                        })
            
            
        }
        }
        //document.body.style.backgroundColor = "yellow";
    } 
    else{
      //document.querySelector('.nav-links').style.display = 'block'
     
        document.querySelector('.nav-links').style.display = 'flex';
        
        document.querySelector('.nav-links').style.width = '40%';
        
    

      //document.body.style.backgroundColor = "pink";
    }
  }
        
           
  

    
})