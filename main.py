from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Darkboy's Live Cricket Stream</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0a0a0a;
                    color: #f8f9fa;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    background: linear-gradient(135deg, #0a0a0a 25%, #1a1a1a 25%, #1a1a1a 50%, #0a0a0a 50%, #0a0a0a 75%, #1a1a1a 75%, #1a1a1a 100%);
                    background-size: 56.57px 56.57px;
                }
                .header {
                    font-family: 'Roboto', sans-serif;
                    background-color: #0a0a0a;
                    padding: 20px;
                    color: #00ff00;
                    font-size: 2.5rem;
                    text-transform: uppercase;
                    text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 20px #00ff00;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                    margin-bottom: 20px;
                }
                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                    background: rgba(0, 0, 0, 0.8);
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                }
                .neon {
                    color: #00ff00;
                    text-shadow:
                        0 0 5px #00ff00,
                        0 0 10px #00ff00,
                        0 0 20px #00ff00,
                        0 0 40px #00ff00;
                    margin-bottom: 20px;
                    font-size: 1.5rem;
                }
                .video-container {
                    width: 100%;
                    max-width: 1200px;
                    background: #000;
                    margin: 20px 0;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                    border-radius: 10px;
                }
                .video-container iframe,
                .video-container video {
                    width: 100%;
                    height: auto;
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <div class="header">Darkboy's Live Cricket Stream</div>
            <div class="container">
                <div class="neon">Enjoy the Match!</div>
                <div class="video-container">
                    <video controls autoplay>
                        <source src="https://jcevents.jiocinema.com/bpk-tv/JC_Sports18_1HD/JCHLS/hdntl=exp=1740378932~acl=%2F*~id=aaf549ec51984c86b32dd7de3e1334c7~data=hdntl~hmac=6029ae6ff841ccbb41d820a46f0a255ad02a678707e7c6ad9a63bd546d3ee24d/JC_Sports18_1HD-audio_108038_eng=108000-video=3728000.m3u8" type="application/x-mpegURL">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
