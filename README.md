# 🥗 Eco-Smart AI Architect (Agentic Edition)
**Prototyping Products with Data & AI | Assignment #2** **Student:** Baran Erdogan – Master in Business Analytics, ESADE

---

## 🚀 Project Overview
The **Eco-Smart AI Architect** is an intelligent grocery assistant designed to bridge the gap between vague user cravings and strict dietary safety. While Assignment #1 focused on a static ML model, this version introduces an **Agentic Layer** that uses Generative AI to audit user intent and synthesize structured kitchen solutions.

### Key Features:
* **🤖 Intelligent Auditor:** Uses an LLM to "reason" through implicit allergen risks (e.g., identifying that "creamy" implies a Dairy risk).
* **⚖️ ML Safety Engine:** A Logistic Regression model (92.5% accuracy) that verifies ingredient safety profiles.
* **♻️ Zero-Waste JSON Synthesizer:** An "Extreme" implementation where the LLM generates raw JSON data to build a dynamic, interactive recipe dashboard.
* **🌍 Eco-Impact Tracking:** Real-time calculation of CO2 savings and financial discounts based on product shelf-life.

---

## 🛠️ Technical Architecture (Non-Straightforward AI)
This project avoids "straightforward" AI implementation by using a **Multi-Model Pipeline**:

1.  **Intent Classification (Logic Gate):** The LLM acts as a pre-processor. It reformulates natural language queries into safe search terms before the database is ever touched.
2.  **Structured Output (Data Engineering):** Instead of generating text, the LLM is constrained to output a strict JSON schema. 
3.  **Python Post-Processing:** The application uses the `json` library to parse AI output into Python dictionaries, which are then used to dynamically render interactive Streamlit widgets (metrics, checkboxes, and info-blocks).

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/baranerdogan11/prototyping-assignment-2.git](https://github.com/baranerdogan11/prototyping-assignment-2.git)
cd prototyping-assignment-2