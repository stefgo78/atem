const { Atem } = require('atem-connection');
const express = require('express');
const path = require('path');

const app = express();
app.use(express.json());

const atem = new Atem();

// 🔧 WPISZ IP SWOJEGO ATEM MINI PRO
const ATEM_IP = "192.168.1.50";

atem.connect(ATEM_IP);

atem.on('connected', () => {
  console.log("Połączono z ATEM Mini Pro");
});

const PRESETS = {
  youtube: {
    url: "rtmp://a.rtmp.youtube.com/live2",
    key: "WPISZ-SWOJ-KLUCZ"
  },
  facebook: {
    url: "rtmp://live-api-s.facebook.com:80/rtmp/",
    key: "WPISZ-SWOJ-KLUCZ"
  },
  rtmp1: {
    url: "rtmp://192.168.1.10/live",
    key: "stream1"
  }
};

app.post('/preset/:name', async (req, res) => {
  const preset = PRESETS[req.params.name];
  if (!preset) return res.status(404).json({ error: "Preset not found" });

  try {
    await atem.setStreamingService(preset.url, preset.key);
    res.json({ status: "OK" });
  } catch (err) {
    res.status(500).json({ error: err.toString() });
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, () => console.log("Panel działa na porcie 3000"));
