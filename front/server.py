from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import re
import os
import subprocess
import tempfile

app = Flask(__name__)
CORS(app)


def parse_srt(text):
    blocks = re.split(r'\n\s*\n', text.strip())
    entries = []
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 3:
            continue
        try:
            index = int(lines[0])
            times = lines[1].split(' --> ')
            start = times[0].strip()
            end = times[1].strip()
            original = ' '.join(lines[2:]).strip()
            entries.append({'index': index, 'start': start, 'end': end, 'original': original})
        except:
            continue
    return entries


def normalizar(texto):
    ruidos = r'\b(hmm|hm|ux|chou|hein|né|ah|oh|uh|ai)\b'
    texto = re.sub(ruidos, '', texto, flags=re.IGNORECASE)
    texto = re.sub(r'[^\w\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto


@app.route('/processar', methods=['POST'])
def processar():
    try:
        text = request.data.decode('utf-8')
        entries = parse_srt(text)
        for e in entries:
            limpo = normalizar(e['original'])
            e['glossa'] = limpo
        return jsonify(entries)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@app.route('/converter', methods=['POST'])
def converter():
    if 'video' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    webm_file = request.files['video']

    # verifica se ffmpeg está disponível
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return jsonify({'error': 'ffmpeg não instalado'}), 500

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'input.webm')
        output_path = os.path.join(tmpdir, 'output.mp4')

        webm_file.save(input_path)

        result = subprocess.run([
            'ffmpeg', '-i', input_path,
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '23',
            '-c:a', 'aac',
            '-y', output_path
        ], capture_output=True)

        if result.returncode != 0:
            return jsonify({'error': result.stderr.decode()}), 500

        return send_file(output_path, mimetype='video/mp4', as_attachment=True, download_name='libras.mp4')


if __name__ == '__main__':
    app.run(port=5000)