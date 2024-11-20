<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Briac Industries</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
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
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-sizing: border-box;
            height: 110px;
            padding-right: 1rem;
            border-bottom: 1px solid #000;
            flex-direction: row;
            position: relative;
        }
        .logo {
            width: 110px;
        }
        .logo a img {
            width: 85px;
            padding-left: 1rem;
        }
        .links {
            width: 100%;
            height: 110px;
            align-items: center;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            margin-left: 1rem;
            padding-left: 2rem;
            margin-right: 1rem;
            padding-right: 2rem;
            border-left: 1px solid #000;
            border-right: 1px solid #000;
        }
        .nav-grp {
            gap: 1.5rem;
            width: 100%;
            height: 110px;
            align-items: center;
            display: flex;
            flex-direction: row;
            margin-right: 1rem;
        }
        .links a {
            font-family: 'Montserrat', sans-serif;
            text-decoration: none;
            font-size: 1.2rem;
            color: #000;
            font-weight: 500;
        }
        .nav-btn {
            width: 110px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .nav-btn a {
            font-family: 'Montserrat', sans-serif;
            text-decoration: none;
            font-size: 1.2rem;
            color: #000;
            font-weight: 500;
        }


    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo">
            <a href="/">
                <img src="/images/logo.png" alt="Logo">
            </a>
        </div>
        <div class="links">
            <div class="nav-grp">
                <a href="">About</a>
                <a href="">Imagine</a>
                <a href="">Ventures</a>
                <a href="">Divisions</a>
                <a href="">Future</a>
                <a href="">Careers</a>
                <a href="">News</a>
            </div>
            <a href="">More</a>
        </div>
        <div class="nav-btn">
            <a href="">Contact</a>
        </div>
    </div>
</body>
</html>