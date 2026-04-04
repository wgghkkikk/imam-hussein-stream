import os
import subprocess
import time

# إعدادات البث - عدلها إذا تغيرت القناة أو السيرفر
VIDEO_URL = "https://www.youtube.com/watch?v=9cauMvs6aYQ"
STREAM_KEY = "q12g-s6wc-0y03-0ua5-6e6p"
RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

def start_stream():
    print("جاري تشغيل البث لقناة عين كربلاء...")
    
    # أمر الحصول على رابط الفيديو المباشر وتشغيل ffmpeg
    # تم ضبط الإعدادات لتناسب سيرفرات Zeet المستقرة
    cmd = (
        f'url=$(yt-dlp -f "best[height<=360]" -g "{VIDEO_URL}") && '
        f'ffmpeg -re -i "$url" -c:v libx264 -preset ultrafast -tune zerolatency '
        f'-b:v 600k -maxrate 600k -bufsize 1200k -pix_fmt yuv420p -g 60 '
        f'-c:a aac -b:a 128k -ar 44100 -f flv "{RTMP_URL}"'
    )
    
    try:
        # تشغيل الأمر وانتظار النتائج
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        print(f"حدث خطأ: {e}")
        print("إعادة المحاولة بعد 10 ثواني...")
        time.sleep(10)

if __name__ == "__main__":
    while True:
        start_stream()
