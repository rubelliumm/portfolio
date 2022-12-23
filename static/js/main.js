const card = document.getElementsByClassName("card");
const class_list = ["top", "right", "bottom", "left"];

for (let c of card) {
  if (c.childElementCount == 0) {
    class_list.forEach((element) => {
      var elem = document.createElement("span");
      elem.className = element;
      c.appendChild(elem);
    });
  } else {
    var cl_l = [];
    for (let el of c.children) {
      if (el.tagName == "SPAN") {
        cl_l.push(el.className);
      }
    }
    cl_l.forEach((elm) => {
      if (class_list.includes(elm)) {
      } else {
        var elem = document.createElement("span");
        elem.className = elm;
        c.appendChild(elem);
      }
    });
  }
}
