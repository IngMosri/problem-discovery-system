#!/usr/bin/env python3
"""
consolidate-with-ollama.py
Lee raw-data.json, lo procesa con Ollama local
Output: structured-data.json listo para Claude agentes
"""

import json
import os
import subprocess
import sys
from datetime import datetime

OLLAMA_MODEL = "llama3.1:8b"
RAW_DATA_FILE = "outputs/raw-data.json"
OUTPUT_FILE = "outputs/structured-data.json"

def load_json(filepath):
    if not os.path.exists(filepath):
        print(f"❌ No encontrado: {filepath}")
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def call_ollama(prompt):
    print(f"🤖 Procesando con {OLLAMA_MODEL}...")
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("⏱️ Timeout")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("=" * 60)
    print("CONSOLIDACIÓN CON OLLAMA")
    print("=" * 60)

    raw_data = load_json(RAW_DATA_FILE)
    if not raw_data:
        print("❌ No hay data. Corre primero los scripts de recolección.")
        sys.exit(1)

    print(f"✅ Data cargada: {len(raw_data.get('problems_identified', []))} pain points")

    prompt = f"""
Eres un experto en análisis de mercado LATAM.

Analiza estos datos de investigación de mercado y genera un JSON estructurado.

DATA:
{json.dumps(raw_data, indent=2, ensure_ascii=False)}

GENERA EXACTAMENTE ESTE JSON (solo JSON, sin texto extra):

{{
  "problematicas_analizadas": [
    {{
      "problema": "nombre del problema",
      "demanda": {{
        "score": 8,
        "evidencia": "por qué tiene demanda",
        "fuentes": "Google/Reddit/Twitter"
      }},
      "mercado": {{
        "score": 7,
        "clientes_potenciales": "5000+",
        "poder_adquisitivo": "$50-200/mes"
      }},
      "viabilidad_ia": {{
        "score": 9,
        "por_que": "por qué es viable con IA"
      }},
      "modelo_monetizacion": "SaaS",
      "score_final": 8,
      "notas": "observaciones"
    }}
  ],
  "top_3": ["problema1", "problema2", "problema3"],
  "fecha_analisis": "{datetime.now().isoformat()}"
}}
"""

    response = call_ollama(prompt)

    if not response:
        print("❌ Ollama no respondió")
        sys.exit(1)

    try:
        import re
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            structured_data = json.loads(json_match.group())
        else:
            structured_data = {"raw_output": response}
    except:
        structured_data = {"raw_output": response}

    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2, ensure_ascii=False)

    print(f"💾 Guardado en: {OUTPUT_FILE}")
    print("=" * 60)
    print("✅ LISTO PARA CLAUDE AGENTES")
    print("=" * 60)

if __name__ == "__main__":
    main()
