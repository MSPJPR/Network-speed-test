from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

# Function to perform the speed test
def get_speedtest_results():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    isp = st.results.client['isp']
    return {
        "download_speed": round(download_speed, 2),
        "upload_speed": round(upload_speed, 2),
        "ping": ping,
        "isp": isp
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/speedtest')
def speedtest_api():
    results = get_speedtest_results()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
