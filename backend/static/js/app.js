const csrf_token= document.querySelector("#csrf").value






async function render_home() {



    try{
        const response= await fetch("/auth/me/",{
            method:"GET",
            credentials:"include"
        })
        const data=await response.json()
        document.querySelector(".loginPage").style.display='none'
        document.querySelector(".home").style.display='flex'
        document.querySelector(".me").innerText=data.user_email

    }
    catch(err){
        alert(err || " error")
    }

    


    
}


async function register(){
    const user_email= document.querySelector("#userEmail").value
    const user_password= document.querySelector('#userPassword').value

    try{
        const response= await fetch('/auth/register/',{
            method:'POST',
            credentials:"include",
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrf_token
            },
            body:JSON.stringify({
                "user_email":user_email,
                "user_password":user_password,
            })
        })
        const data= await response.json()
        console.log(data)


        if(!response.ok){
            alert(data.error||"error")
            return
        }


        render_home()

    }
    catch(err ){
        alert(err || "network err")
    }
    
}

async function login(){
    const user_email= document.querySelector("#userEmail").value
    const user_password= document.querySelector('#userPassword').value

    try{
        const response= await fetch('/auth/login/',{
            method:'POST',
            credentials:"include",
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrf_token
            },
            body:JSON.stringify({
                "user_email":user_email,
                "user_password":user_password,
            })
        })
        const data= await response.json()
        console.log(data)


        if(!response.ok){
            alert(data.error||"error")
            return
        }
        render_home()

    }
    catch(err ){
        alert(err || "network err")
    }
    
}
