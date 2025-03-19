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
            margin-bottom: 150px;
        }

        .article {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            padding: 12px 14px;
            box-sizing: border-box;
            border: 1px solid #000;
            margin-top: 5px;
        }

        .article:hover {
            background-color: #efefef;
            transition: all 0.2s;
        }

        .article:first-child {
            margin-top: 0;
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
            align-items: center;
        }

        .tickers {
            text-decoration: wavy !important;
            color: #000;
            padding: 0;
            margin: 0;
        }

        .slogan {
            font-weight: 600;
            font-size: 28px;
            margin-top: .5rem;
        }

        a {
            color: #000;
            font-size: 16px;
            font-weight: 500;
            margin-top: 2rem;
        }

        @media screen and (max-width: 768px) {
            .name {
                font-size: 20px;
                text-align: center;
            }

            .logo {
                width: 220px;
            }

            .slogan {
                font-weight: 600;
                font-size: 20px;
            }

            a {
                font-size: 12px;
            }
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
    <h2 class="slogan">Shaping Tomorrow.</h2>
    <a href="mailto:contact@ivleaguecapital.com">contact@ivleaguecapital.com</a>
    <!--<div class="fucking-dd-container">
        <a href="/article/auto-lenders" style="color: #000; text-decoration: none;">
            <div class="article">
                <div class="deets">
                    <div class="title">
                        Why Auto Lenders are about to eat 💩.
                    </div>
                    <div class="bottom-chaos">
                        <div class="shitdongle-date">
                            March 2nd, 2025
                        </div>
                        <div class="targetted-tickers">
                           <a href="https://finance.yahoo.com/quote/ALLY/" class="tickers">ALLY</a>, <a href="https://finance.yahoo.com/quote/CVNA/" class="tickers">CVNA</a>, <a href="https://finance.yahoo.com/quote/^VIX/" class="tickers">VIX</a>
                        </div>
                    </div>
                </div>
            </div>
        </a>

    </div>-->


</body>

<script>
document.addEventListener("copy", function(e) {
    e.preventDefault();
    const fakeText = "Nice try, retard. Read the full DD instead of asking AI for a summary.";
    e.clipboardData.setData("text/plain", fakeText);
});
</script>
</html>
