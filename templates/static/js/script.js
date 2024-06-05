
$(document).ready(function () {
    let addingButton = $('.button')
    let closerButton = $('.closer');
    let forms = $(".adding-content");
    let blur = $(".blur");
    let cancel = $(".adding-content form .buttons #cancel")
    addingButton.click(function () {
        forms.show("fast");
        blur.show();
        addingButton.hide();
    });

    closerButton.click(() =>{
        forms.hide("fast");
        blur.hide();
        addingButton.show("fast");
    }); 
    cancel.click(() =>{
        forms.hide("fast");
        blur.hide();
        addingButton.show("fast");
    });
});
    