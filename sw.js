// fotn service worker — offline app shell + asset cache
const CACHE = 'fotn-v1';
const CORE = [
  './', './index.html', './manifest.webmanifest',
  './generic.jpg?v=2',
  './icon.svg?v=8', './icon-192.png?v=8', './icon-512.png?v=8', './apple-touch-icon.png?v=8',
  './luts/portra400.png', './luts/pro400h.png', './luts/gold200.png', './luts/colorplus200.png',
  './luts/kodacolor100.png', './luts/ultramax400.png', './luts/velvia100.png', './luts/hp5.png',
  './luts/signature1.png',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.all(CORE.map(u => c.add(u).catch(() => {})))) // tolerate any 404
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Page loads: network-first (fresh when online), fall back to the cached shell offline.
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put('./index.html', copy));
        return res;
      }).catch(() => caches.match('./index.html').then(r => r || caches.match('./')))
    );
    return;
  }

  // Same-origin assets + Google Fonts: cache-first, then network (and cache it).
  const isFont = url.host.includes('fonts.googleapis.com') || url.host.includes('fonts.gstatic.com');
  if (url.origin === self.location.origin || isFont) {
    e.respondWith(
      caches.match(req).then(hit => hit || fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy));
        return res;
      }).catch(() => hit))
    );
  }
});
