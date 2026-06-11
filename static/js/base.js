document.addEventListener("DOMContentLoaded", function () {
    const flashMessages = document.querySelectorAll(".flash-message");

    setTimeout(() => {
        flashMessages.forEach(msg => {
            msg.style.opacity = "0";
            msg.style.transform = "translateY(-10px)";
            
            setTimeout(() => {
                msg.remove();
            }, 300);
        });
    }, 3000); 
});