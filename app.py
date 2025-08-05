
from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import os
import datetime

app = Flask(__name__)

@app.route('/')
def generate_poster():
    BACKGROUND_FOLDER = 'backgrounds'
    OUTPUT_FOLDER = 'output'
    FONT_PATH = 'fonts/ShreeDev0714.ttf'

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    festivals = [
        {"name": "Today Festival", "date": datetime.datetime.now().strftime('%Y-%m-%d')}
    ]

    background = Image.open(os.path.join(BACKGROUND_FOLDER, 'khatu_shyam_baba.png')).convert('RGBA')

    for fest in festivals:
        poster = background.copy()
        draw = ImageDraw.Draw(poster)

        font_large = ImageFont.truetype(FONT_PATH, 120)
        font_small = ImageFont.truetype(FONT_PATH, 60)

        text_fest = f"शुभ {fest['name']}"
        w, h = draw.textsize(text_fest, font=font_large)
        draw.text(((poster.width - w) / 2, 100), text_fest, font=font_large, fill="gold")

        shyam_text = "जय श्री श्याम 🙏📿"
        w2, h2 = draw.textsize(shyam_text, font=font_small)
        draw.text(((poster.width - w2) / 2, poster.height - 200), shyam_text, font=font_small, fill="white")

        output_path = os.path.join(OUTPUT_FOLDER, 'daily_poster.png')
        poster.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
