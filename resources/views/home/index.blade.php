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
                font-size: 15px;
            }

            .values {
                width: 90% !important;
            }
        }

        .values {
            width: 45%;
            margin-top: 3rem;
            gap: 1rem;
            display: flex;
            flex-direction: column;
            margin-bottom: 150px;
        }

        .value-title {
            font-size: 24px;
            font-weight: 600;
        }

        .value-description {
            font-size: 16px;
            font-weight: 400;
            margin-top: .5rem;
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
    
    <div class="values">
        <h2>Values</h2>
        <div class="value">
            <div class="value-title">
                1. Money ≠ Necessity
            </div>
            <div class="value-description">
                I don’t chase money. It’s not a necessity. If I make it, great. If I don’t, I'll still move forward. Freedom matters more than digits.
            </div>
        </div>
        <div class="value">
            <div class="value-title">
                2. YOLO is the Only Strategy
            </div>
            <div class="value-description">
                There’s one life, one shot. I don’t play small. I go in with conviction, not caution, because there’s no reward without risk.
            </div>
        </div>
        <div class="value">
            <div class="value-title">
                3. No Credit. No Debt.
            </div>
            <div class="value-description">
            I don’t borrow. I don’t owe. If I can’t afford it, I don’t buy it. Loans are proof you’re stretching beyond your means. I don’t stretch for things I don’t need.
            </div>
        </div>
        <div class="value">
            <div class="value-title">
                4. Materialism ≠ Value
            </div>
            <div class="value-description">
            A car is a tool. A house is shelter. I don’t need expensive things to feel accomplished. The road doesn’t care what you drive, but if I earn it, and I love it, I’ll drive what I want. Just never on borrowed time.
            </div>
        </div>
        <div class="value">
            <div class="value-title">
                5. Massive Gains = Massive Conviction
            </div>
            <div class="value-description">
            I don’t diversify out of fear. If I believe in something, I go all in. People want 10x returns but only risk 5%. That’s not how I play.
            </div>
        </div>
    </div>

</body>

<script>
document.addEventListener("copy", function(e) {
    e.preventDefault();
    const fakeText = "Nice try, retard.";
    e.clipboardData.setData("text/plain", fakeText);
});
</script>
</html>
