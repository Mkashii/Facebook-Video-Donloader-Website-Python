from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp
import os
import hashlib

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Define the directory to store downloaded videos temporarily
DOWNLOAD_DIR = "downloads"

# Ensure the download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def get_unique_filename(url):
    """Generate a unique filename based on the video URL"""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return f"{url_hash}.mp4"

@app.route('/')
def home():
    return render_template('en.html')

@app.route('/download', methods=['POST'])
def download_video():
    # Get the video URL from the form
    video_url = request.form.get('url')

    if not video_url:
        return jsonify({"error": "No URL provided!"}), 400

    # Generate a unique filename based on the URL
    output_filename = get_unique_filename(video_url)

    # Check if the video already exists in the download folder
    video_file_path = os.path.join(DOWNLOAD_DIR, output_filename)
    if os.path.exists(video_file_path):
        return send_file(video_file_path, as_attachment=True, download_name=output_filename)

    # Set download options for yt-dlp
    ydl_opts = {
        'outtmpl': video_file_path,
        'quiet': True,  # Suppress yt-dlp output to keep it clean
    }

    try:
        # Download the video using yt-dlp (only for Facebook)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Send the video file to the user for download
        return send_file(video_file_path, as_attachment=True, download_name=output_filename)

    except Exception as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500

@app.route("/aboutus")
def about_us():
    return render_template("aboutus.html")  # Ensure the file is in the templates folder

@app.route("/termsandcondition")
def termsandcondition():
    return render_template("termsandcondition.html")  # Ensure the file is in the templates folder

# Ensure the file is in the templates folder
@app.route('/sitemap.xml')
def sitemap():
    return send_file(os.path.join(app.static_folder, 'sitemap.xml'), mimetype='application/xml')
    
    
@app.route('/robots.txt')
def robots():
    return send_file(os.path.join(app.static_folder, 'robots.txt'), mimetype='text/plain')


@app.route("/privacypolicy")
def privacypolicy():
    return render_template("privacypolicy.html")  # Ensure the file is in the templates folder
@app.route("/privacypolicy/ar")
def privacypolicyar():
    return render_template("privacypolicy/index_ar.html")

@app.route("/privacypolicy/pt")
def privacypolicypt():
    return render_template("privacypolicy/index_pt.html")

@app.route("/privacypolicy/ru")
def privacypolicyru():
    return render_template("privacypolicy/index_ru.html")

@app.route("/privacypolicy/de")
def privacypolicyde():
    return render_template("privacypolicy/index_de.html")

@app.route("/privacypolicy/el")
def privacypolicyel():
    return render_template("privacypolicy/index_el.html")

@app.route("/privacypolicy/es")
def privacypolicyes():
    return render_template("privacypolicy/index_es.html")

@app.route("/privacypolicy/fr")
def privacypolicyfr():
    return render_template("privacypolicy/index_fr.html")

@app.route("/privacypolicy/he")
def privacypolicyhe():
    return render_template("privacypolicy/index_he.html")

@app.route("/privacypolicy/hi")
def privacypolicyhi():
    return render_template("privacypolicy/index_hi.html")

@app.route("/privacypolicy/it")
def privacypolicyit():
    return render_template("privacypolicy/index_it.html")

@app.route("/privacypolicy/js")
def privacypolicyjs():
    return render_template("privacypolicy/index_js.html")

@app.route("/privacypolicy/ko")
def privacypolicyko():
    return render_template("privacypolicy/index_ko.html")

@app.route("/privacypolicy/nl")
def privacypolicynl():
    return render_template("privacypolicy/index_nl.html")

@app.route("/privacypolicy/pl")
def privacypolicypl():
    return render_template("privacypolicy/index_pl.html")

@app.route("/privacypolicy/nu")
def privacypolicynu():
    return render_template("privacypolicy/index_nu.html")

@app.route("/privacypolicy/sv")
def privacypolicysv():
    return render_template("privacypolicy/index_sv.html")

@app.route("/privacypolicy/th")
def privacypolicyth():
    return render_template("privacypolicy/index_th.html")

@app.route("/privacypolicy/tr")
def privacypolicytr():
    return render_template("privacypolicy/index_tr.html")

@app.route("/privacypolicy/uk")
def privacypolicyuk():   
    return render_template("privacypolicy/index_uk.html")

@app.route("/privacypolicy/vi")
def privacypolicyvi():
    return render_template("privacypolicy/index_vi.html")

@app.route("/contactus")
def contact_us():
    return render_template("contactus.html")
@app.route("/home/ar")
def home_ar():
    return render_template("en/index_ar.html")  # Arabic home page


@app.route("/home/de")
def home_de():
    return render_template("en/index_de.html")  # German home page


@app.route("/home/el")
def home_el():
    return render_template("en/index_el.html")  # Greek home page


@app.route("/home/es")
def home_es():
    return render_template("en/index_es.html")  # Spanish home page


@app.route("/home/fr")
def home_fr():
    return render_template("en/index_fr.html")  # French home page


@app.route("/home/he")
def home_he():
    return render_template("en/index_he.html")  # Hebrew home page


@app.route("/home/hi")
def home_hi():
    return render_template("en/index_hi.html")  # Hindi home page


@app.route("/home/it")
def home_it():
    return render_template("en/index_it.html")  # Italian home page


@app.route("/home/ja")
def home_ja():
    return render_template("en/index_ja.html")  # Japanese home page


@app.route("/home/ko")
def home_ko():
    return render_template("en/index_ko.html")  # Korean home page


@app.route("/home/nl")
def home_nl():
    return render_template("en/index_nl.html")  # Dutch home page


@app.route("/home/sv")
def home_sv():
    return render_template("en/index_sv.html")  # Swedish home page


@app.route("/home/th")
def home_th():
    return render_template("en/index_th.html")  # Thai home page


@app.route("/home/tr")
def home_tr():
    return render_template("en/index_tr.html")  # Turkish home page


@app.route("/home/uk")
def home_uk():
    return render_template("en/index_uk.html")  # Ukrainian home page


@app.route("/home/vi")
def home_vi():
    return render_template("en/index_vi.html")  # Vietnamese home page


@app.route("/home/zncn")
def home_zncn():
    return render_template("en/index_zh-cn.html")  # Simplified Chinese home page
  # Chinese home page@app.route("/home/ru")
def home_ru():
    return render_template("en/index_ru.html")  # Russian home page


@app.route("/aboutus/zhcn")
def aboutus_znch():
    return render_template("aboutus/index_zhcn.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/en")
def aboutus_en():
    return render_template("aboutus/index_en.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/ar")
def aboutus_ar():
    return render_template("aboutus/index_ar.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/de")
def aboutus_de():
    return render_template("aboutus/index_de.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/el")
def aboutus_el():
    return render_template("aboutus/index_el.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/es")
def aboutus_es():
    return render_template("aboutus/index_es.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/fr")
def aboutus_fr():
    return render_template("aboutus/index_fr.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/he")
def aboutus_he():
    return render_template("aboutus/index_he.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/hi")
def aboutus_hi():
    return render_template("aboutus/index_hi.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/it")
def aboutus_it():
    return render_template("aboutus/index_it.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/js")
def aboutus_js():
    return render_template("aboutus/index_js.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/ko")
def aboutus_ko():
    return render_template("aboutus/index_ko.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/nl")
def aboutus_nl():
    return render_template("aboutus/index_nl.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/nu")
def aboutus_nu():
    return render_template("aboutus/index_nu.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/sv")
def aboutus_sv():
    return render_template("aboutus/index_sv.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/th")
def aboutus_th():
    return render_template("aboutus/index_th.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/tr")
def aboutus_tr():
    return render_template("aboutus/index_tr.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/uk")
def aboutus_uk():
    return render_template("aboutus/index_uk.html")  # Ensure the file is in the templates folder


@app.route("/aboutus/vi")
def aboutus_vi():
    return render_template("aboutus/index_vi.html")  # Ensure the file is in the templates folder
@app.route("/contactus/en")
def contactus_en():
    return render_template("/contactus/index_en.html")  # Ensure the file is in the templates folder


@app.route("/contactus/ar")
def contactus_ar():
    return render_template("/contactus/index_ar.html")  # Ensure the file is in the templates folder


@app.route("/contactus/de")
def contactus_de():
    return render_template("/contactus/index_de.html")  # Ensure the file is in the templates folder


@app.route("/contactus/el")
def contactus_el():
    return render_template("/contactus/index_el.html")  # Ensure the file is in the templates folder


@app.route("/contactus/es")
def contactus_es():
    return render_template("/contactus/index_es.html")  # Ensure the file is in the templates folder


@app.route("/contactus/fr")
def contactus_fr():
    return render_template("/contactus/index_fr.html")  # Ensure the file is in the templates folder


@app.route("/contactus/he")
def contactus_he():
    return render_template("/contactus/index_he.html")  # Ensure the file is in the templates folder


@app.route("/contactus/hi")
def contactus_hi():
    return render_template("/contactus/index_hi.html")  # Ensure the file is in the templates folder


@app.route("/contactus/it")
def contactus_it():
    return render_template("/contactus/index_it.html")  # Ensure the file is in the templates folder


@app.route("/contactus/js")
def contactus_js():
    return render_template("/contactus/index_js.html")  # Ensure the file is in the templates folder


@app.route("/contactus/ko")
def contactus_ko():
    return render_template("/contactus/index_ko.html")  # Ensure the file is in the templates folder


@app.route("/contactus/nl")
def contactus_nl():
    return render_template("/contactus/index_nl.html")  # Ensure the file is in the templates folder


@app.route("/contactus/nu")
def contactus_nu():
    return render_template("/contactus/index_nu.html")  # Ensure the file is in the templates folder


@app.route("/contactus/sv")
def contactus_sv():
    return render_template("/contactus/index_sv.html")  # Ensure the file is in the templates folder


@app.route("/contactus/th")
def contactus_th():
    return render_template("/contactus/index_th.html")  # Ensure the file is in the templates folder


@app.route("/contactus/tr")
def contactus_tr():
    return render_template("/contactus/index_tr.html")  # Ensure the file is in the templates folder


@app.route("/contactus/uk")
def contactus_uk():
    return render_template("/contactus/index_uk.html")  # Ensure the file is in the templates folder


@app.route("/contactus/vi")
def contactus_vi():
    return render_template("/contactus/index_vi.html")  # Ensure the file is in the templates folder
@app.route("/termsandcondition/en")
def termsandcondition_en():
    return render_template("/termsandcondition/index_en.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/ar")
def termsandcondition_ar():
    return render_template("/termsandcondition/index_ar.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/de")
def termsandcondition_de():
    return render_template("/termsandcondition/index_de.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/el")
def termsandcondition_el():
    return render_template("/termsandcondition/index_el.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/es")
def termsandcondition_es():
    return render_template("/termsandcondition/index_es.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/fr")
def termsandcondition_fr():
    return render_template("/termsandcondition/index_fr.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/he")
def termsandcondition_he():
    return render_template("/termsandcondition/index_he.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/hi")
def termsandcondition_hi():
    return render_template("/termsandcondition/index_hi.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/it")
def termsandcondition_it():
    return render_template("/termsandcondition/index_it.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/js")
def termsandcondition_js():
    return render_template("/termsandcondition/index_js.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/ko")
def termsandcondition_ko():
    return render_template("/termsandcondition/index_ko.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/nl")
def termsandcondition_nl():
    return render_template("/termsandcondition/index_nl.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/nu")
def termsandcondition_nu():
    return render_template("/termsandcondition/index_nu.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/sv")
def termsandcondition_sv():
    return render_template("/termsandcondition/index_sv.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/th")
def termsandcondition_th():
    return render_template("/termsandcondition/index_th.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/tr")
def termsandcondition_tr():
    return render_template("/termsandcondition/index_tr.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/uk")
def termsandcondition_uk():
    return render_template("/termsandcondition/index_uk.html")  # Ensure the file is in the templates folder


@app.route("/termsandcondition/vi")
def termsandcondition_vi():
    return render_template("/termsandcondition/index_vi.html")  # Ensure the file is in the templates folder

if __name__ == '__main__':
    app.run(debug=True)
