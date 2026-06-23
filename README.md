# 🎙️ Unlimited Voice Cloning by Zaib

**A powerful, self-hosted Text-to-Speech server with unlimited voice cloning, multilingual support, and a modern Web UI — built and maintained by Zaib.**

> 💬 **Join my WhatsApp Channel for updates, keys, and support:**
> 
> [![WhatsApp Channel](https://img.shields.io/badge/WhatsApp-Join%20Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)

---

[![Made by Zaib](https://img.shields.io/badge/Made%20by-Zaib-blueviolet?style=for-the-badge)](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10_(required)-blue.svg?style=for-the-badge)](https://www.python.org/downloads/release/python-31011/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![CUDA Compatible](https://img.shields.io/badge/NVIDIA_CUDA-Compatible-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
[![ROCm Compatible](https://img.shields.io/badge/AMD_ROCm-Compatible-ED1C24?style=for-the-badge&logo=amd&logoColor=white)](https://rocm.docs.amd.com/)
[![MPS Compatible](https://img.shields.io/badge/Apple_MPS-Compatible-000000?style=for-the-badge&logo=apple&logoColor=white)](https://developer.apple.com/metal/)
[![API](https://img.shields.io/badge/OpenAI_Compatible_API-Ready-000000?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/docs/api-reference)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)

---

## 👤 Credits & Contact

| | |
|---|---|
| **Created & Maintained by** | **Zaib** |
| **WhatsApp Channel** | [Join here for updates & keys](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10) |
| **Access Keys** | Obtained via WhatsApp channel or admin |
| **Support** | WhatsApp channel only |

> ⚠️ **All credit for this tool belongs to Zaib.** Redistribution or reselling without permission is not allowed.

---

## 🌟 What Is This?

**Unlimited Voice Cloning by Zaib** is a self-hosted TTS (Text-to-Speech) server that lets you:

- 🎤 **Clone any voice** from a short audio sample
- 🌍 **Speak 23 languages** including Arabic, English, Chinese, French, Urdu-style, and more
- ⚡ **Generate audio fast** using Turbo mode (350M parameter model, 1-step diffusion)
- 📚 **Create full audiobooks** from long text automatically
- 🔑 **Access-key protected** — only authorized users can generate audio
- 🖥️ **Modern Web UI** — no coding needed, works in your browser

---

## 🔑 How to Get Access

1. **Join the WhatsApp channel:** [https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)
2. Request an access key from the admin
3. Enter your key in the tool's login screen
4. Start cloning voices!

---

## 🚀 Features

### 🎙️ Voice Cloning
- Clone any voice from a `.wav` or `.mp3` reference file
- Zero-shot cloning — no training required
- Consistent output using built-in seed control

### 🌍 Multilingual (23 Languages)
Arabic, Chinese, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Italian, Japanese, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Swahili, Turkish

### ⚡ Three TTS Engines
| Engine | Speed | Languages | Special |
|--------|-------|-----------|---------|
| **Original** | Fast | English | Emotion control |
| **Multilingual** | Fast | 23 languages | Voice cloning |
| **Turbo** | Fastest | English | `[laugh]` `[cough]` `[chuckle]` tags |

### 📚 Audiobook Generation
- Paste an entire book — it processes automatically
- Intelligent sentence-based chunking
- Seamless audio stitching

### 🖥️ Web UI
- Modern dark/light mode interface
- Waveform audio player
- Preset management
- Parameter sliders (temperature, exaggeration, speed, etc.)
- Configuration management

### 🔒 Access Key Protection
- All TTS endpoints protected by server-side key validation
- Keys validated against the admin panel in real time
- Expired or revoked keys are blocked instantly

---

## 🛠️ Installation

### Requirements
- Python **3.10** (required — other versions may fail)
- NVIDIA GPU (recommended) or Apple Silicon / AMD / CPU

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/shazoovlog11/Unlimited-voice-cloning-by-Zaib
cd Unlimited-voice-cloning-by-Zaib

# 2. Run the launcher
# Windows:
start.bat

# Linux/Mac:
bash start.sh
```

The launcher will:
- Create a virtual environment
- Install all dependencies automatically
- Download the AI model from Hugging Face
- Start the server and open the Web UI

### GPU Support

| Hardware | Command |
|----------|---------|
| NVIDIA (CUDA 12.1) | `start.bat` / `start.sh` |
| NVIDIA Blackwell (CUDA 12.8) | `start.bat --nvidia-cu128` |
| AMD ROCm | `start.bat --rocm` |
| Apple Silicon (MPS) | `start.sh` |
| CPU only | `start.bat --cpu` |

### Docker

```bash
# NVIDIA GPU
docker compose up -d

# CPU only
docker compose -f docker-compose-cpu.yml up -d
```

---

## ⚙️ Configuration

All settings are in `config.yaml` (auto-created on first run):

```yaml
server:
  host: 0.0.0.0
  port: 8004

model:
  device: auto        # auto, cuda, mps, cpu
  default_engine: original

ui:
  title: "Unlimited Voice Cloning by Zaib"
```

---

## 📡 API Usage

The server is **OpenAI-compatible**. All endpoints require the `X-ZK` access key header.

### Generate Speech
```bash
curl -X POST http://localhost:8004/tts \
  -H "X-ZK: YOUR-ACCESS-KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "voice_mode": "predefined"}' \
  --output speech.wav
```

### OpenAI-Compatible Endpoint
```bash
curl -X POST http://localhost:8004/v1/audio/speech \
  -H "X-ZK: YOUR-ACCESS-KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tts-1", "input": "Hello world", "voice": "alloy"}' \
  --output speech.wav
```

---

## 💬 Support & Updates

All support is provided through the **WhatsApp channel**:

👉 **[https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)**

Join to get:
- 🔑 Access keys
- 🆕 Update announcements
- 🛠️ Setup help
- 💡 Tips & tricks

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

The underlying TTS engine is based on [Resemble AI's Chatterbox](https://github.com/resemble-ai/chatterbox) (open-source).  
This project — the server, UI, key protection system, and all customizations — is the work of **Zaib**.

---

<div align="center">

**Made with ❤️ by Zaib**

[![WhatsApp Channel](https://img.shields.io/badge/WhatsApp-Join%20My%20Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VbBY6cq002T07EkzJc10)

</div>
