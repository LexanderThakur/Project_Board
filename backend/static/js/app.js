const csrf_token= document.querySelector("#csrf").value



async function register(){
    const user_email= document.querySelector("#userEmail").value
    const user_password= document.querySelector('#userPassword').value

    try{
        const response= await fetch('auth/register/',{
            method:'POST',
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

    }
    catch(err ){
        alert(err || "network err")
    }
}