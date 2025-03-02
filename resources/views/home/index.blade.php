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
            align-items: center;
            display: flex;
            flex-direction: column;
        }

        .logo {
            width: 250px;
            margin-top: 5rem;
        }

        .name {
            font-size: 36px;
            margin-top: 1rem;
        }

        .fucking-dd-container {
            width: 45%;
            margin-top: 2rem;
        }

        .article {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            padding: 12px 14px;
            box-sizing: border-box;
            border-bottom: 1px solid #000;
        }

        .article:hover {
            background-color: #eee;
            transition: all 0.2s;
        }


        .title {
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 5px;
            width: 100%;
        }

        i {
            font-size: 48px;
        }

        .deets {
            width: 100%;
        }
        

        .bottom-chaos {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }

        .tickers {
            text-decoration: wavy !important;
            color: #000;
        }
    </style>
</head>
<body>
    <a href="/">
        <img src="/images/transparent.png" alt="Logo" class="logo">
    </a>
    <div class="name">
        <h1>Briac Industries</h1>
    </div>
    <div class="fucking-dd-container">
        <a href="/article/auto-lenders" style="color: #000; text-decoration: none;">
            <div class="article">
                <div class="deets">
                    <div class="title">
                        Why Auto Lenders are about to eat 💩.
                    </div>
                    <div class="bottom-chaos">
                        <div class="shitdongle-date">
                            March 1st, 2025
                        </div>
                        <div class="targetted-tickers">
                           <a href="https://finance.yahoo.com/quote/ALLY/" class="tickers">ALLY</a>, <a href="https://finance.yahoo.com/quote/CVNA/" class="tickers">CVNA</a>, <a href="https://finance.yahoo.com/quote/^VIX/" class="tickers"><sup>^</sup>VIX</a>
                        </div>
                    </div>
                </div>
            </div>
        </a>
    </div>
    
</body>
</html>
