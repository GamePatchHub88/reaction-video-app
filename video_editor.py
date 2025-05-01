import moviepy.editor as mp
import os

def process_video(video_path, avatar_name, output_path):
    clip = mp.VideoFileClip(video_path)

    clip = clip.fx(mp.vfx.speedx, 1.1)
    clip = clip.fx(mp.vfx.mirror_x)
    clip = clip.fx(mp.vfx.colorx, 1.2)
    clip = clip.crop(x_center=clip.w/2, y_center=clip.h/2, width=clip.w*0.9, height=clip.h*0.9)

    border_color = (255, 0, 0)
    clip = clip.margin(10, color=border_color)

    if clip.audio:
        clip = clip.set_audio(clip.audio.fx(mp.vfx.speedx, 1.1))

    avatar_path = os.path.join('static/avatars', avatar_name)
    avatar_clip = mp.VideoFileClip(avatar_path).resize(height=150)

    final = mp.CompositeVideoClip([
        clip,
        avatar_clip.set_position(("right", "top")).set_start(0).set_duration(clip.duration)
    ])

    final.write_videofile(output_path, codec="libx264", audio_codec="aac")