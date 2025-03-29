    window.addEventListener('scroll', function () {
            let scrollPosition = window.scrollY;
            let blurBg = document.getElementById('blur-bg');
            if (blurBg) {
                blurBg.style.opacity = scrollPosition > 100 ? '1' : '0';
            }
        });

        document.addEventListener("DOMContentLoaded", function () {
            let button = document.querySelector(".btn");
            if (button) {
                button.addEventListener("mouseover", function () {
                    button.style.boxShadow = "0px 0px 15px #ffcc00";
                });
                button.addEventListener("mouseleave", function () {
                    button.style.boxShadow = "none";
                });
            }

            document.getElementById('confirm_password').addEventListener('input', function () {
                const password = document.getElementById('password').value;
                const confirmPassword = this.value;
                if (password !== confirmPassword) {
                    this.setCustomValidity("Passwords don't match");
                } else {
                    this.setCustomValidity('');
                }
            });
        });