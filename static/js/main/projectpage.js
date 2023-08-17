
$(document).ready(function(){
    const colorList = ["#8fe025","#d3c226","#d028fa"]
    var cardTags = $(".tags > p")
    for(let i = 0;i<= cardTags.length;i++){
    const randomIndex = Math.floor(Math.random() * colorList.length);
    cardTags[i].style.backgroundColor= colorList[randomIndex];
}
});