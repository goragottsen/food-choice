function csrfSafeMethod(method) 
{
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
}

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$('#spicy').on('change', register);
$('#sweet').on('change', register);
$('#sour').on('change', register);

function register(){
    $.ajax({
        
        type: 'POST',
        url: window.location.href,
        data:{
            taste: event.target.id.toString(),
            value: $(event.target).val(),
            el_id: event.target.id.toString()
        },
        success: function(data) {
            console.log("value taken");
            var timeout = null;
            // timeout = window.setTimeout(() => {
            //     location.href = window.location.href;
            // }, 300000)
            //console.log(data);
            return data;
        },
        fail: function(response) {
            console.log("failure in jq")
        }
    });
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});