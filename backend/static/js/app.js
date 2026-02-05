const csrf_token = document.querySelector("#csrf").value || null;

async function render_projects() {
  try {
    const response = await fetch("/projects/get_project/");

    const data = await response.json();
    console.log(data);
    if (!response.ok) {
      console.log(data.error || "error in getting projects");

      return;
    }
    let projects = [];
    let project_html = `
    
    `;
    console.log(data);
    data.message.forEach((project, index) => {
      project_html += `
      <div class="card projectCard" data-project-id="${project.id}">
          <div class="card-body">
            <h5 class="card-title">${project.name}</h5>
            <p class="card-text">
              ${project.description}
            </p>
            <button class="btn btn-primary btn-sm" onclick="render_tasks()">Manage</button>
          </div>
        </div>
      
      
      `;
    });
    document.querySelector(".projects").innerHTML = project_html;
  } catch (err) {
    console.log("error in render_projects()" + err);
  }
}

async function create_project() {
  const name = document.querySelector(".projectName").value;
  const description = document.querySelector(".projectDescription").value;

  try {
    const response = await fetch("/projects/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify({
        name: name,
        description: description,
      }),
    });
    const data = await response.json();
    if (!response.ok) {
      alert(data.error || "error in response");
      return;
    }

    render_projects();
  } catch (err) {
    alert(err || "Network Error");
  }
}

async function render_home() {
  try {
    const response = await fetch("/auth/me/", {
      method: "GET",
      credentials: "include",
    });
    const data = await response.json();
    document.querySelector(".loginPage").style.display = "none";
    document.querySelector(".home").style.display = "flex";
    document.querySelector(".me").innerText = data.user_email;
  } catch (err) {
    alert(err || " error");
  }
}

async function register() {
  const user_email = document.querySelector("#userEmail").value;
  const user_password = document.querySelector("#userPassword").value;

  try {
    const response = await fetch("/auth/register/", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify({
        user_email: user_email,
        user_password: user_password,
      }),
    });
    const data = await response.json();
    console.log(data);

    if (!response.ok) {
      alert(data.error || "error");
      return;
    }
    render_projects();
    render_home();
  } catch (err) {
    alert(err || "network err");
  }
}

async function login() {
  const user_email = document.querySelector("#userEmail").value;
  const user_password = document.querySelector("#userPassword").value;

  try {
    const response = await fetch("/auth/login/", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify({
        user_email: user_email,
        user_password: user_password,
      }),
    });
    const data = await response.json();
    console.log(data);

    if (!response.ok) {
      alert(data.error || "error");
      return;
    }
    render_projects();
    render_home();
  } catch (err) {
    alert(err || "network err");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".taskCard").forEach((task) => {
    task.addEventListener("click", () => {
      task.classList.toggle("done");
    });
  });
});
