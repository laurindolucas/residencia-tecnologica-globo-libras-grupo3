from flask import Flask, request, jsonify
from flask_cors import CORS
import re

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
    # Remove interjeições
    ruidos = r'\b(hmm|hm|ux|chou|hein|né|ah|oh|uh|ai)\b'
    texto = re.sub(ruidos, '', texto, flags=re.IGNORECASE)
    # Remove pontuação
    texto = re.sub(r'[^\w\s]', ' ', texto)
    # Remove espaços duplos
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

if __name__ == '__main__':
    app.run(port=5000)