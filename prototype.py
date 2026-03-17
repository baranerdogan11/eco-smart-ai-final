import streamlit as st
import pandas as pd
import time
from logic import (
    get_mock_inventory, 
    recommend_meals, 
    calculate_impact, 
    intelligent_audit, 
    generate_zero_waste_recipe
)

st.set_page_config(page_title="Eco-Smart AI Architect V2", page_icon="🥗", layout="wide")

# Initialize Session States
if "inventory" not in st.session_state:
    with st.spinner("Initializing AI System & Training ML..."):
        inv, acc = get_mock_inventory()
        st.session_state.inventory = inv
        st.session_state.accuracy = acc
        time.sleep(1)
    st.success(f"System Ready! ML Accuracy: {acc:.1%}")

if "current_results" not in st.session_state:
    st.session_state.current_results = None

# UI Layout
st.markdown("# 🥗 Eco-Smart AI Architect: Agentic Edition")
st.caption("Machine Learning Powered Ingredient Planning | Assignment #2")

# Sidebar Configuration
with st.sidebar:
    st.header("🤖 Model Intelligence")
    st.metric("Model Test Accuracy", f"{st.session_state.accuracy:.1%}")
    
    st.divider()
    st.header("🛡️ Safety Filters")
    allergens_list = ["Dairy", "Wheat", "Almonds", "Eggs", "Peanuts", "Soy"]
    selected_allergens = st.multiselect("Exclude Allergens:", allergens_list, key="excluded_allergens")

# Conversational Input
prompt = st.chat_input("Search for an ingredient (e.g., 'creamy chicken')...")

if prompt:
    st.session_state.last_prompt = prompt
    
    # AI AUDIT PHASE
    with st.spinner("🕵️ Auditing intent for hidden risks..."):
        vetted_query = intelligent_audit(prompt, selected_allergens)
        
    if vetted_query.lower() != prompt.lower():
        st.warning(f"Risk Found! Redirected to safe search: **{vetted_query}**")
    else:
        st.success("Query verified as safe.")

    # DATA RETRIEVAL
    st.session_state.current_results = recommend_meals(vetted_query, st.session_state.inventory, selected_allergens)

# Display Results
if st.session_state.current_results is not None:
    st.subheader("Your AI-Curated Eco-Cart")
    
    st.dataframe(
        st.session_state.current_results[["Food Product", "Main Ingredient", "Allergens", "Final_Price", "Days_to_Expiry", "CO2_Impact"]],
        use_container_width=True,
        hide_index=True
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🛒 Checkout & Impact", type="primary", use_container_width=True):
            saved, co2, waste = calculate_impact(st.session_state.current_results)
            st.balloons()
            st.markdown(f"### 🌍 Eco-Savings: €{saved:.2f}")
            st.markdown(f"### ☁️ CO2 Saved: {co2:.1f}kg")

    with c2:
        # EXTREME AI RECIPE SYNTHESIS (JSON to UI)
        if st.button("👨‍🍳 Generate Interactive Recipe", use_container_width=True):
            with st.spinner("Chef AI is compiling structured JSON data..."):
                recipe_data = generate_zero_waste_recipe(st.session_state.current_results)
                st.session_state.recipe_data = recipe_data

    with c3:
        if st.button("🔄 Refresh Ideas", use_container_width=True):
            st.rerun()

    # --- DYNAMIC JSON UI RENDERING ---
    if "recipe_data" in st.session_state:
        recipe = st.session_state.recipe_data
        st.markdown("---")
        
        if "error" in recipe:
            st.error(recipe["error"])
        else:
            # 1. Header Section
            st.markdown(f"## 🍽️ {recipe.get('recipe_name', 'Zero-Waste Special')}")
            st.caption(recipe.get('description', ''))
            
            # 2. Macro-Nutrient Metrics
            macros = recipe.get('macros', {})
            col1, col2, col3 = st.columns(3)
            col1.metric("Prep Time", recipe.get('prep_time', 'N/A'))
            col2.metric("Est. Calories", f"{macros.get('calories', 0)} kcal")
            col3.metric("Est. Protein", f"{macros.get('protein', 0)}g")
            
            st.divider()
            
            # 3. Interactive UI Elements
            ing_col, step_col = st.columns([1, 2])
            
            with ing_col:
                st.subheader("🛒 Required Items")
                for item in recipe.get('ingredients_needed', []):
                    st.checkbox(item, key=item)
                    
            with step_col:
                st.subheader("🍳 Cooking Steps")
                for i, step in enumerate(recipe.get('steps', [])):
                    st.info(f"**Step {i+1}:** {step}")