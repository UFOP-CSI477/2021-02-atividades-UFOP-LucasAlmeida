$(document).ready(function(){
    $.getJSON('https://brasilapi.com.br/api/banks/v1', function(data) {
        var jsonData = data;//where json is the JSON data.
        var selectHTML = '';
        for(i=0;i<jsonData.length;i++){
            selectHTML+= '<option value="' + jsonData[i].fullName + '">' + jsonData[i].fullName + '</option>';
            }
        $("#banco").append(selectHTML);
    });

    


});


form.addEventListener('submit', function(e) {
    var form = document.getElementById('form');
    var chave = $("#chave").val()
    var valor = parseInt($("#valor").val())
    var data = $("#data").val()
    var banco = $("#banco").val()
    var tipo = $("input[name='tipo']:checked").val()
    var total = parseInt($("#total").text())
    var html = `
    <li class="list-group-item d-flex justify-content-between lh-condensed">
    <div>
      <h6 class="my-0">`+chave+`</h6>
      <small class="text-muted">`+data+`</small>
      <small class="text-muted">`+banco+`</small>
      <small class="text-muted">`+tipo+`</small>
    </div>
    <span class="text-muted">R$`+valor+`</span>
  </li>
    
    `
    $("#lista").before(html);
    $("#total").text(total+valor)
    // impede o envio do form
    console.log(total)
    e.preventDefault();
});
