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
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            background-color: #000;
        }
        .navbar {
            display: flex;
            box-sizing: border-box;
            height: 90px;
            width: 100%;
            flex-direction: row;
            position: fixed;
            justify-content: center;
            align-items: center;
            padding: .3rem;
            box-sizing: border-box;
            background-color: #fff;
            padding-bottom: 1rem;
            padding-top: 1rem;
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
            margin-left: 2rem;
            margin-right: 2rem;
            gap: 1.5rem;
        }
        .nav-grp {
            gap: 1.5rem;
            width: 100%;
            align-items: center;
            justify-content: center;
            display: flex;
            flex-direction: row;
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
                <a href="">Imagine</a>
                <a href="">Ventures</a>
                <a href="">Administration</a>
                <a href="">Careers</a>
                <a href="">News</a>
                <a href="">About</a>
            </div>
            
        </div>
        <div class="other-links">
            <div class="more-links">
                <a href=""><i class="bi bi-plus-lg"></i></a>
            </div>
            <div class="nav-btn">
                <a href="">Contact</a>
            </div>
        </div>
    </div>
</body>
</html>
