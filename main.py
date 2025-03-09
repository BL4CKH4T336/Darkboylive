from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    quality = request.args.get('quality', '1080p')
    
    # Define video URLs based on quality
    video_urls = {
        '1080p': "https://v18tataplaysyndication.akamaized.net/bpk-tv/Sports18_1_HD_voot_MOB/output03/index.m3u8?hdnea=exp=1741520182~acl=/*~hmac=1a03b1cce9e170f94589ef43002f4ca93183df5ba52f1fb9319f3d2151846076",
        '720p': "https://cdnt20.t20hd.cfd/live/m3-index.m3u8",
        '480p': "ae6ff841ccbb41d820a46f0a255ad02a678707e7c6ad9a63bd546d3ee24d/JC_Sports18_1HD-audio_108038_eng=108000-video=2297600.m3u8",
        '360p': "https://v18tataplaysyndication.akamaized.net/bpk-tv/Sports18_1_HD_voot_MOB/output03/hdntl=exp=1741149777~acl=%2f*~data=hdntl~hmac=76411f198e0ce7850ded22c05da3f9239a037d38338204abb41f4a6d6a0a7f56/Sports18_1_HD_voot_MOB-audio_108038_eng=108000-video=2297600.m3u8",
        '240p': "https://jcevents.jiocinema.com/bpk-tv/JC_Sports18_1HD/JCHLS/hdntl=exp=1740378932~acl=%2F*~id=aaf549ec51984c86b32dd7de3e1334c7~data=hdntl~hmac=6029ae6ff841ccbb41d820a46f0a255ad02a678707e7c6ad9a63bd546d3ee24d/JC_Sports18_1HD-audio_108038_eng=108000-video=305200.m3u8",
        '144p': "https://jcevents.jiocinema.com/bpk-tv/JC_Sports18_1HD/JCHLS/hdntl=exp=1740378932~acl=%2F*~id=aaf549ec51984c86b32dd7de3e1334c7~data=hdntl~hmac=6029ae6ff841ccbb41d820a46f0a255ad02a678707e7c6ad9a63bd546d3ee24d/JC_Sports18_1HD-audio_42842_eng=42800-video=151600.m3u8"
    }
    
    video_url = video_urls.get(quality, video_urls['1080p'])  # Default to 1080p if quality is not found
    
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
                .quality-select {
                    margin-top: 20px;
                }
                .quality-select select {
                    background-color: #00ff00;
                    border: none;
                    padding: 10px;
                    font-size: 1rem;
                    cursor: pointer;
                    text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00;
                }
                .quality-select select option {
                    background-color: #0a0a0a;
                    color: #00ff00;
                }
            </style>
            <script>
                function changeQuality() {
                    var quality = document.getElementById('quality-select').value;
                    window.location.href = '/?quality=' + quality;
                }
            </script>
        </head>
        <body>
            <div class="header">Darkboy's Live Cricket Stream</div>
            <div class="container">
                <div class="neon">Enjoy the Match!</div>
                <div class="video-container">
                    <video controls autoplay>
                        <source src="{{ video_url }}" type="application/x-mpegURL">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="quality-select">
                    <select id="quality-select" onchange="changeQuality()">
                        <option value="1080p" {% if quality == '1080p' %}selected{% endif %}>1080p</option>
                        <option value="720p" {% if quality == '720p' %}selected{% endif %}>720p</option>
                        <option value="480p" {% if quality == '480p' %}selected{% endif %}>480p</option>
                        <option value="360p" {% if quality == '360p' %}selected{% endif %}>360p</option>
                        <option value="240p" {% if quality == '240p' %}selected{% endif %}>240p</option>
                        <option value="144p" {% if quality == '144p' %}selected{% endif %}>144p</option>
                    </select>
                </div>
            </div>
        </body>
        </html>
    ''', video_url=video_url, quality=quality)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
