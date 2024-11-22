<!DOCTYPE html>
<html lang="en">
<head>
    @include('head', [
        'title' => 'Briac Industries'
    ])
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        @import url('https://fonts.cdnfonts.com/css/cooper-hewitt');
        * {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            overscroll-behavior: none;
        }
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            background-color: #fff;
        }
        .navbar {
            display: flex;
            box-sizing: border-box;
            height: 90px;
            flex-direction: row;
            border-left: 1px solid #0b1d6f;
            border-right: 1px solid #0b1d6f;
            border-bottom: 1px solid #0b1d6f;
            position: fixed;
            background-color: #fff;
            justify-content: center;
            align-items: center;
            width: 80%;
            padding-bottom: 1rem;
            padding-top: 1rem;
        }

        .rotate {
        transform: rotate(180deg);
        transition: transform 0.3s ease-in-out;
    }

        .logo {
            display: flex;
            align-items: center;
            background-color: #fff;
            border-radius: 50px;
            height: 65px;
            width: 65px;
            justify-content: center;
        }
        .logo a img {
            width: 70px;
            margin-top: 4px;
        }
        .links {
            align-items: center;
            display: flex;
            flex-direction: row;
            justify-content: center;
            margin-left: 1rem;
        }
        .nav-grp {
            width: 100%;
            gap: 1.5rem;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
        }

        .nav-grp h1 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2rem;
            color: #000;
            font-weight: 600;
        }

        .nav-grp i {
            transition: transform 0.3s ease-in-out;
        }

        .nav-grp a:hover {
            text-decoration: underline;
            transition: all 0.3s;
        }
        .links a {
            font-family: 'Montserrat', sans-serif;
            text-decoration: none;
            font-size: 1.2rem;
            color: #000;
            font-weight: 500;
        }

        .nav-btn {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #0b1d6f;
            height: 40px;
            padding-left: .7rem;
            padding-right: .7rem;
        }
        .nav-btn a {
            font-family: 'Montserrat', sans-serif;
            text-decoration: none;
            font-size: 1.3rem;
            color: #fff;
            font-weight: 500;
        }

        .other-links {
            display: flex;
            flex-direction: row;
        }

        .more-links {
            width: 43px;
            border: 1px solid #000;
            display: flex;
            height: 40px;
            font-size: 1.5rem;
            justify-content: center;
            align-items: center;
            border-right: none;
        }

        .more-links a i  {
            color: #000;
        }

        .content {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 80%;
            border-left: 1px solid #0b1d6f;
            border-right: 1px solid #0b1d6f;
        }

        .top-container {
            height: 100vh;
            margin-top: 90px;
        }

        .container {
            height: 100vh;
        }
.covernav {
    width: 80%;
    z-index: 100;
    max-height: 0; /* Initial collapsed state */
    overflow: hidden; /* Prevent content from spilling out */
    position: fixed;
    padding: 0; /* Remove padding to make the transition smoother */
    margin-top: 90px;
    display: flex;
    flex-direction: row;
    background-color: #0b1d6f;
    transform: translateY(0);
    transition: max-height .6s ease-in-out; /* Smooth height and padding */
}

.covernav.show {
    max-height: calc(75vh - 90px); /* Expand to the desired height */
}

.covernav-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 2rem;
    width: 40%;
}

.covernav-list a {
    color: #fff;
    font-size: 1.5rem;
    text-decoration: none;
}

.covernav-list a:hover {
    transition: all 0.2s;
    color: #ddd;
}

.cover-sublinks {
    width: 60%;
    padding: 2rem;
    box-sizing: border-box;
}

.sublink-container {
    border-left: 1px solid #fff;
    height: 100%;
    padding-left: 1rem;
    padding-right: 2rem;
    color: #fff;
    font-size: 1.3rem;
}
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo">
            <a href="/">
                <img src="/images/transparent.png" alt="Logo">
            </a>
        </div>
        <div class="links">
            <div class="nav-grp">
                <h1>Briac Industries</h1>
                <i class="bi bi-chevron-down" style="font-size: 2rem;"></i>
            </div>
            
        </div>
    </div>
    <div class="covernav">
        <div class="covernav-list">
            <a href="">Imagine</a>
            <a href="">Ventures</a>
            <a href="">Administration</a>
            <a href="">Careers</a>
            <a href="">News</a>
            <a href="">About</a>
        </div>
        <div class="cover-sublinks">
            <div class="sublink-container">
                hi
            </div>
        </div>
    </div>
    <div class="content">
        <div class="top-container">
            <div class="row">
                <div class="col-md-12">
                    <h1 class="text-center text-white">Welcome to Briac Industries</h1>
                </div>
            </div>
        </div>
        <div class="container">
            hi
        </div>
    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const navbar = document.querySelector('.navbar');
        const covernav = document.querySelector('.covernav');
        const chevronIcon = document.querySelector('.nav-grp i');

        navbar.addEventListener('mouseenter', function() {
            covernav.classList.add('show');
            chevronIcon.classList.add('rotate');
        });

        covernav.addEventListener('mouseenter', function() {
            covernav.classList.add('show');
            chevronIcon.classList.add('rotate');
        });

        covernav.addEventListener('mouseleave', function() {
            covernav.classList.remove('show');
            chevronIcon.classList.remove('rotate');
        });

        document.addEventListener('click', function(event) {
            if (!navbar.contains(event.target) && !covernav.contains(event.target)) {
                covernav.classList.remove('show');
                chevronIcon.classList.remove('rotate');
            }
        });
    });
</script>
</body>
</html>