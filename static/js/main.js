const mainBody = document.getElementById("mainBody");

function removeAllClassInPath(e) {
  const arrays = document.getElementsByClassName("get-path");
  // remove backslash from the parameter value
  const Filter_Value = e.split("/").filter((e) => e != "")[0];

  for (let i = 0; i < arrays.length; i++) {
    // remove all class
    arrays[i].classList.remove("active");
    // add active in class
    if (arrays[i].id == Filter_Value || Filter_Value == "")
      arrays[i].classList.add("active");
  }
}

function stopAnimation() {
  mainBody.classList.add("loaded");
  const isPath = [
    "/",
    "/about/",
    "/contact/",
    "/video/",
    "/photo/",
    "/photo/product/",
  ];
  path = window.location.pathname;

  if (isPath.includes(path)) {
    isPath.map((e) => {
      if (e == path) {
        if (path != "/") removeAllClassInPath(e);
      }
    });
  }
}
