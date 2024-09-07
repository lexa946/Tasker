
document.addEventListener("DOMContentLoaded", function(){


let buttons = document.querySelectorAll('#delete');


buttons.forEach(button => {
    button.addEventListener('click', event => {
        fetch(location.protocol + '//' + location.host+'/tasks/'+ button.value, {
            method: 'DELETE'
        }).then();
        let row = document.querySelector('#task-id-'+button.value);
        row.remove();
    });
})

});
