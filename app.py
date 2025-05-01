from flask import Flask, render_template, request, send_file
import os
from processing.video_editor import process_video

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
AVATAR_FOLDER = 'static/avatars'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    avatar = request.form.get('avatar')

    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    output_path = os.path.join(UPLOAD_FOLDER, f"processed_{video.filename}")

    process_video(video_path, avatar, output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)