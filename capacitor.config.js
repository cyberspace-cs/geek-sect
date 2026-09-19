const productionUrl = "https://hack.taoxie.vip";
const configuredUrl = process.env.CAPACITOR_SERVER_URL?.trim();
const serverUrl = configuredUrl || productionUrl;

/** @type {import('@capacitor/cli').CapacitorConfig} */
const config = {
  appId: "com.taoxie.geeksect",
  appName: "极客宗",
  webDir: "mobile-shell",
  backgroundColor: "#0a0a12",
  loggingBehavior: "debug",
  server: {
    url: serverUrl,
    cleartext: serverUrl.startsWith("http://"),
    androidScheme: "https",
    errorPath: "geek.html",
  },
  ios: {
    contentInset: "never",
    backgroundColor: "#0a0a12",
    preferredContentMode: "mobile",
    scheme: "GeekSect",
  },
  android: {
    allowMixedContent: false,
    backgroundColor: "#0a0a12",
  },
};

module.exports = config;
