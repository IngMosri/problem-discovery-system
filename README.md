<div align="center">

# 🔍 Problem Discovery System

**Multi-Agent AI Pipeline for Market Opportunity Discovery in LATAM**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-llama3.1:8b-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

[Qué es](#-qué-es) • [Arquitectura](#-arquitectura) • [Setup](#-setup) • [Uso](#-uso)

</div>

---

## 📌 Qué es

Sistema automatizado que identifica **problemáticas reales en Latinoamérica** atacables con IA/automatización.

Cada semana el pipeline:
1. **Recolecta** señales de Google Trends, Reddit y Twitter
2. **Estructura** la data localmente con Ollama (sin costo de API)
3. **Analiza** con 6 agentes Claude especializados que debaten entre sí
4. **Genera** un reporte con Top 3 oportunidades rankeadas por viabilidad

---

## 🏗 Arquitectura

```
┌─────────────────────────────────────────────────────┐
│                  FASE 1: RECOLECCIÓN                 │
│  Google Trends → Reddit → Twitter → consolidate.py  │
│                          ↓                          │
│                   raw-data.json                      │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│              FASE 2: ESTRUCTURACIÓN LOCAL            │
│           consolidate-with-ollama.py                 │
│              Modelo: llama3.1:8b (GPU)               │
│                          ↓                          │
│                structured-data.json                  │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│                FASE 3: ANÁLISIS CLAUDE               │
│  Search → Social → Manual → Viable ⚔️ Risk → Lead   │
│                          ↓                          │
│            Top 3 oportunidades rankeadas             │
└─────────────────────────────────────────────────────┘
```

---

## ⚡ Tech Stack

| Componente | Tecnología | Razón |
|:---|:---|:---|
| Recolección | Python 3.12+ | Librerías robustas para scraping |
| LLM local | Ollama + llama3.1:8b | Cero costo de API, GPU local |
| Análisis profundo | Claude Agents | Mejor razonamiento complejo |
| Fuentes | Google Trends, Reddit, Twitter | Cobertura multi-canal |
| Storage | JSON | Simple y portable |

---

## 🚀 Setup

### Prerequisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado
- NVIDIA GPU con 8GB+ VRAM (recomendado)

### Instalación

```bash
# 1. Clona el repo
git clone https://github.com/IngMosri/problem-discovery-system.git
cd problem-discovery-system

# 2. Virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Dependencias
pip install -r requirements.txt

# 4. Modelo Ollama
ollama pull llama3.1:8b
```

---

## 📖 Uso

```bash
# Activa el entorno
source venv/bin/activate

# Fase 1: Recolección
python3 scripts/fetch-google-trends.py
python3 scripts/scrape-reddit.py
python3 scripts/search-twitter.py
python3 scripts/consolidate.py

# Fase 2: Estructuración con Ollama
ollama serve &
python3 consolidate-with-ollama.py
```

---

## 📁 Estructura

```
problem-discovery-system/
├── scripts/
│   ├── fetch-google-trends.py
│   ├── scrape-reddit.py
│   ├── search-twitter.py
│   └── consolidate.py
├── outputs/
├── consolidate-with-ollama.py
├── requirements.txt
└── README.md
```

---

## 🤖 Los 6 Agentes

| Agente | Rol | Pregunta que responde |
|:---|:---|:---|
| 🔍 Search | Analiza búsquedas | ¿Qué busca activamente la gente? |
| 📱 Social | Analiza redes | ¿Qué duele en Twitter/Reddit/LinkedIn? |
| 🔧 Manual | Observa procesos | ¿Qué sigue siendo manual en 2026? |
| ✅ Viable | Abogado defensor | ¿Por qué SÍ vale la pena construirlo? |
| ⚠️ Risk | Abogado del diablo | ¿Qué podría salir mal? |
| 🏆 Lead | Orquestador | Síntesis final + ranking |

> El debate entre **Viable** y **Risk** elimina el sesgo de confirmación.

---

## 💡 Decisiones de Diseño

<details>
<summary><b>¿Por qué Ollama local y no API externa?</b></summary>
<br>
Reducción de costos del ~80%. La estructuración de data no requiere el modelo más potente. Claude se reserva para el análisis profundo.
</details>

<details>
<summary><b>¿Por qué múltiples fuentes de data?</b></summary>
<br>
Una sola fuente genera sesgo. Google Trends muestra volumen, Reddit muestra dolor cualitativo, Twitter muestra urgencia en tiempo real.
</details>

<details>
<summary><b>¿Por qué agentes de debate?</b></summary>
<br>
Un solo agente tiende a confirmar lo que ya cree. El debate forzado entre Viable y Risk produce análisis más honesto.
</details>

---

## 📝 License

MIT — úsalo, modifícalo, mejóralo.

---

<div align="center">

Construido por [@IngMosri](https://github.com/IngMosri) · Guadalajara, México · 2026

</div>
