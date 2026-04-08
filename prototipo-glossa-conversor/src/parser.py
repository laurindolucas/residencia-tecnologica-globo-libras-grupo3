import pysrt

def parse_srt(file_path):
    subs = pysrt.open(file_path)

    data = []
    for sub in subs:
        data.append({
            "index": sub.index,
            "start": str(sub.start),
            "end": str(sub.end),
            "text": sub.text.replace('\n', ' ')
        })

    return data