import csv, re, json

rows=list(csv.DictReader(open('fuji.csv')))

def num(s):
    s=s.strip().replace('+','')
    m=re.search(r'-?\d+(?:\.\d+)?', s)
    return float(m.group()) if m else None

def find(settings, *keys):
    """Return the value text after the first matching key line."""
    low=settings.lower()
    for line in settings.split('\n'):
        if ':' not in line: 
            # also handle "Acros Red Filter" style without colon -> skip here
            continue
        k,v=line.split(':',1)
        k=k.strip().lower()
        for key in keys:
            if k==key:
                return v.strip()
    return None

def level(v):
    """Off/Weak/Strong/Medium normalization."""
    if v is None: return None
    v=v.lower()
    if 'off' in v or 'none' in v: return 'Off'
    if 'strong' in v: return 'Strong'
    if 'weak' in v: return 'Weak'
    if 'medium' in v or 'std' in v: return 'Medium'
    return v.strip().title()

def dr(v):
    if v is None: return None
    v=v.lower()
    if 'auto' in v: return 'Auto'
    m=re.search(r'(100|200|400)',v)
    return 'DR'+m.group() if m else v.strip()

out=[]
for r in rows:
    s=r['Settings'] or ''
    grain_raw = find(s,'grain effect','grain')
    grain_size = find(s,'grain size')
    rec={
        'creator': r['Creator'].strip(),
        'name': r['Name'].strip(),
        'mono': (r['Color /BW'].strip().lower().startswith('b')),
        'camera': r['Camera'].strip(),
        'sensor': r['Sensor'].strip(),
        'base': r['Base'].strip(),
        'url': r['URL'].strip(),
        'dynamicRange': dr(find(s,'dynamic range','dr','d-range')),
        'grain': level(grain_raw.split(',')[0]) if grain_raw else None,
        'grainSize': ('Large' if grain_raw and 'large' in grain_raw.lower() else ('Small' if grain_raw and 'small' in grain_raw.lower() else (level(grain_size) if grain_size else None))),
        'colorChrome': level(find(s,'color chrome effect','colour chrome effect','color chrome','color chrome fx')),
        'colorChromeBlue': level(find(s,'color chrome effect blue','colour chrome blue','color chrome fx blue','color chrome blue','colour chrome effect blue')),
        'whiteBalance': find(s,'white balance','wb'),
        'highlights': num(find(s,'highlights','highlight','highlight tone') or ''),
        'shadows': num(find(s,'shadows','shadow','shadow tone') or ''),
        'color': num(find(s,'color','colour') or ''),
        'sharpness': num(find(s,'sharpness','sharpening') or ''),
        'noiseReduction': num(find(s,'noise reduction','iso noise reduction','high iso nr','nr') or ''),
        'clarity': num(find(s,'clarity') or ''),
        'toning': find(s,'toning','mono shift'),
        'raw': s,
    }
    # WB shift
    wbs=find(s,'wb shift','wb color shift','shift','wb colour shift')
    rec['wbRed']=None; rec['wbBlue']=None
    if wbs:
        rm=re.search(r'(-?\d+)\s*(?:red|r\b)', wbs, re.I) or re.search(r'r[:\s]*(-?\d+)', wbs, re.I)
        bm=re.search(r'(-?\d+)\s*(?:blue|b\b)', wbs, re.I) or re.search(r'b[:\s]*(-?\d+)', wbs, re.I)
        if rm: rec['wbRed']=int(rm.group(1))
        if bm: rec['wbBlue']=int(bm.group(1))
    out.append(rec)

json.dump(out, open('recipes.json','w'), ensure_ascii=False)
print('wrote', len(out))
# sample
import random
for rec in out[:3]:
    print(json.dumps({k:v for k,v in rec.items() if k!='raw'}, ensure_ascii=False))
# coverage
def cov(f): return sum(1 for r in out if r[f] is not None)
for f in ['dynamicRange','grain','colorChrome','colorChromeBlue','whiteBalance','highlights','shadows','color','sharpness','noiseReduction','clarity','wbRed']:
    print(f, cov(f))
