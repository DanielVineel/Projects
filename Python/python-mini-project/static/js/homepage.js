
    //created by G Daniel Vineel

document.addEventListener("DOMContentLoaded", function() {
   const infix=document.getElementById("infix-postfix")
   const postfix=document.getElementById("postfix-infix")
   
   if(infix!=null){
        infix.onclick=(e)=>{
            window.open("/infix-postfix", "_blank");
        }
   }
   if(postfix!=null){
       postfix.onclick=(e)=>{
           window.open("/postfix-infix", "_blank");
          
       }

   }

    const PostFixToInfix=document.getElementById('PostfixToInfix')
    const InfixToPostFix=document.getElementById('InfixToPostfix')

    if(InfixToPostFix!=null){
        InfixToPostFix.addEventListener('submit',async(e)=>{
            e.preventDefault()
            let formData=new FormData(InfixToPostFix)
            data={}
            formData.forEach((value,key)=> data[key]=value);
            console.log(data)
            try {
                const response = await fetch("/InToPost", {
                    method: "POST",
                    headers: {
                    "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                });
       
                const result = await response.text();
                let tmp=document.createElement("div")
                tmp.innerText=result
                document.getElementById("result").appendChild(tmp)
                console.log("Server says:", result);

            } catch (error) {
                console.error("Error:", error);
            }


        })
    }
    //created by G Daniel Vineel
    
    if(PostFixToInfix!=null){
    PostFixToInfix.addEventListener('submit',async(e)=>{
        e.preventDefault()
        let formData=new FormData(PostFixToInfix)
        data={}
        formData.forEach((value,key)=> data[key]=value);

        try {
            const response = await fetch("/PostToIn", {
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            });

            const result = await response.text();
            let tmp=document.createElement("div")
                tmp.innerText=result
                document.getElementById("result").appendChild(tmp)

            console.log("Server says:", result);

        } catch (error) {
            console.error("MY Error:", error);
        }

    })
    }

    //created by G Daniel Vineel

});

