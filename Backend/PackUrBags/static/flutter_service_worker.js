'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "assets/AssetManifest.json": "3b5f44133a7cc0e679f07ce2e5e2055b",
"assets/assets/flightLoading.gif": "8d5a92a831c83f3b780c670253298a89",
"assets/assets/img/air.png": "2afac2010336582413444f3fb6b3d125",
"assets/assets/img/CardImageDelhi.jpg": "5829756d527b7759fb6b3dde6e54ab40",
"assets/assets/img/CardImageMumbai.jpg": "595ee935f881c599184efd09f0f06ca3",
"assets/assets/img/CardImageSriCity.jpg": "658f64c6d439a6a79004815e4d7d0433",
"assets/assets/img/CardImageVadodara.jpg": "31e48802f62bb362a85b5df138b77b67",
"assets/assets/img/CardImageVizag.jpg": "e7244a981249951bb6ad17a2c5debc49",
"assets/assets/img/ImageDelhi.jpg": "4a6a61a47d2161ead6eefcb932a72d8f",
"assets/assets/img/ImageMumbai.jpg": "18343be3a12458dd34ad0affccf6a77c",
"assets/assets/img/ImageSriCity.jpg": "67177e3c3ab88da312f604b3a5d113b1",
"assets/assets/img/ImageVadodara.jpg": "8a37ecc043af9f459184b9ab80f74e61",
"assets/assets/img/ImageVizag.jpg": "cf83afaf4d3c21600576a4c77b1d2774",
"assets/assets/img/scooter.png": "9a2bdd1b86c410c9b255a81856c899dc",
"assets/assets/loading.gif": "c7a857eb3b2650e73e70aaf392e47d80",
"assets/assets/monumentLoading.gif": "0788b6ee10dbdc3a726bb2a6f37a37d0",
"assets/assets/pageLoading.gif": "433b6c5336c72a21bcfd9db8d831562a",
"assets/flightLoading.gif": "8d5a92a831c83f3b780c670253298a89",
"assets/FontManifest.json": "5a32d4310a6f5d9a6b651e75ba0d7372",
"assets/fonts/MaterialIcons-Regular.otf": "1288c9e28052e028aba623321f7826ac",
"assets/img/air.png": "2afac2010336582413444f3fb6b3d125",
"assets/img/CardImageDelhi.jpg": "5829756d527b7759fb6b3dde6e54ab40",
"assets/img/CardImageMumbai.jpg": "595ee935f881c599184efd09f0f06ca3",
"assets/img/CardImageSriCity.jpg": "658f64c6d439a6a79004815e4d7d0433",
"assets/img/CardImageVadodara.jpg": "31e48802f62bb362a85b5df138b77b67",
"assets/img/CardImageVizag.jpg": "e7244a981249951bb6ad17a2c5debc49",
"assets/img/ImageDelhi.jpg": "4a6a61a47d2161ead6eefcb932a72d8f",
"assets/img/ImageMumbai.jpg": "18343be3a12458dd34ad0affccf6a77c",
"assets/img/ImageSriCity.jpg": "67177e3c3ab88da312f604b3a5d113b1",
"assets/img/ImageVadodara.jpg": "8a37ecc043af9f459184b9ab80f74e61",
"assets/img/ImageVizag.jpg": "cf83afaf4d3c21600576a4c77b1d2774",
"assets/img/scooter.png": "9a2bdd1b86c410c9b255a81856c899dc",
"assets/loading.gif": "c7a857eb3b2650e73e70aaf392e47d80",
"assets/monumentLoading.gif": "0788b6ee10dbdc3a726bb2a6f37a37d0",
"assets/NOTICES": "ef3e156c08dd4f944c88cf8769b33150",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "115e937bb829a890521f72d2e664b632",
"assets/packages/font_awesome_flutter/lib/fonts/fa-brands-400.ttf": "831eb40a2d76095849ba4aecd4340f19",
"assets/packages/font_awesome_flutter/lib/fonts/fa-regular-400.ttf": "a126c025bab9a1b4d8ac5534af76a208",
"assets/packages/font_awesome_flutter/lib/fonts/fa-solid-900.ttf": "d80ca32233940ebadc5ae5372ccd67f9",
"assets/pageLoading.gif": "433b6c5336c72a21bcfd9db8d831562a",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"index.html": "76d5d7cfc6e0ccfbc3513b14d9736115",
"/": "76d5d7cfc6e0ccfbc3513b14d9736115",
"main.dart.js": "f82343baa461480c8130ef5a243e46ba",
"manifest.json": "2951f10deb3dfe4a7a29bc37f9282f6e",
"version.json": "7c196c092c5a8ae92c94177c47f7d9ba"
};

// The application shell files that are downloaded before a service worker can
// start.
const CORE = [
  "/static/",
"main.dart.js",
"index.html",
"assets/NOTICES",
"assets/AssetManifest.json",
"assets/FontManifest.json"];
// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request("/static/"+value + '?revision=' + RESOURCES[value], {'cache': 'reload'})));
    })
  );
});

// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});

// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache.
        return response || fetch(event.request).then((response) => {
          cache.put(event.request, response.clone());
          return response;
        });
      })
    })
  );
});

self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});

// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey in Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}

// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
