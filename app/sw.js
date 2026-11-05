// Cache para o app abrir rápido e funcionar mesmo com internet fraca.
const CACHE = 'minha-colecao-v2';
const BASE = ['./', './index.html', './manifest.webmanifest', './icone-192.png',
  './fontes/Fraunces_600SemiBold.woff2', './fontes/Fraunces_800ExtraBold.woff2', './fontes/Fraunces_700Bold_Italic.woff2',
  './fontes/NunitoSans_400Regular.woff2', './fontes/NunitoSans_600SemiBold.woff2', './fontes/NunitoSans_700Bold.woff2', './fontes/NunitoSans_800ExtraBold.woff2'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(BASE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  e.respondWith(
    fetch(r).then(res => { if (res.ok) { const cp = res.clone(); caches.open(CACHE).then(c => c.put(r, cp)); } return res; })
      .catch(() => caches.match(r, { ignoreSearch: true }))
  );
});
