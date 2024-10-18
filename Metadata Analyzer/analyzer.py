import json
from collections import defaultdict
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def analyze_metadata(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    description_fields = defaultdict(lambda: {"null": 0, "non_null": 0})
    relaxed_permissions = []
    non_null_descriptions = []
    relationships = defaultdict(lambda: {"source": 0, "target": 0})

    def traverse(obj, path=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{path}.{key}" if path else key
                if key == "description":
                    if value:
                        description_fields[current_path]["non_null"] += 1
                        non_null_descriptions.append({"path": current_path, "value": value})
                    else:
                        description_fields[current_path]["null"] += 1
                
                if key == "kind" and value == "ModelPermissions":
                    analyze_permissions(obj)
                
                if key == "kind" and value == "Relationship":
                    analyze_relationship(obj)
                
                traverse(value, current_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path = f"{path}[{i}]"
                traverse(item, current_path)

    def analyze_permissions(obj):
        if "definition" in obj and "permissions" in obj["definition"]:
            for perm in obj["definition"]["permissions"]:
                if "select" in perm and perm["select"].get("filter") is None:
                    relaxed_permissions.append(obj["definition"]["modelName"])

    def analyze_relationship(obj):
        if "definition" in obj:
            source = obj["definition"].get("sourceType", "")
            target = obj["definition"].get("target", {}).get("model", {}).get("name", "")
            relationships[source]["source"] += 1
            relationships[target]["target"] += 1

    traverse(data)

    total_description_fields = sum(field["null"] + field["non_null"] for field in description_fields.values())
    null_description_percentage = sum(field["null"] for field in description_fields.values()) / total_description_fields * 100 if total_description_fields > 0 else 0

    return {
        "description_fields": len(description_fields),
        "null_description_percentage": null_description_percentage,
        "relaxed_permissions": relaxed_permissions,
        "non_null_descriptions": non_null_descriptions,
        "relationships": relationships
    }

def create_charts(results):
    st.title("Metadata Analysis")

    st.header("1. Description Fields Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Number of 'description' fields", results["description_fields"])
    with col2:
        st.metric("Percentage of null 'description' fields", f"{results['null_description_percentage']:.2f}%")

    st.header("2. Entities with Relaxed Permission Rules")
    if results["relaxed_permissions"]:
        st.write("Models with no filter on all rows:")
        st.write(", ".join(results["relaxed_permissions"]))
    else:
        st.write("No models found with relaxed permission rules.")

    st.header("3. Models with Most Relationships")
    relationships_df = pd.DataFrame(results["relationships"]).T.reset_index()
    relationships_df.columns = ['Model', 'Source', 'Target']
    relationships_df['Total'] = relationships_df['Source'] + relationships_df['Target']
    relationships_df = relationships_df.sort_values('Total', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    relationships_df.plot(x='Model', y=['Source', 'Target'], kind='bar', stacked=True, ax=ax)
    ax.set_title("Top 10 Models with Most Relationships")
    ax.set_xlabel("Model")
    ax.set_ylabel("Number of Relationships")
    plt.legend(title="Relationship Type")
    st.pyplot(fig)

    st.header("4. Non-null Description Fields")
    if results["non_null_descriptions"]:
        df = pd.DataFrame(results["non_null_descriptions"])
        st.dataframe(df)
    else:
        st.write("No non-null description fields found.")

def main():
    st.set_page_config(page_title="Metadata Analyzer", layout="wide")
    st.sidebar.title("Metadata Analyzer")
    uploaded_file = st.sidebar.file_uploader("Choose a JSON file", type="json")
    
    if uploaded_file is not None:
        with open("temp.json", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        results = analyze_metadata("temp.json")
        create_charts(results)
    else:
        st.write("Please upload a JSON file to analyze.")

if __name__ == "__main__":
    main()