import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Set page config
st.set_page_config(page_title="API Platform Dashboard", layout="wide")

# Function to generate random data
def random_metric(min_val, max_val):
    return random.randint(min_val, max_val)

# Function to calculate and format ratio
def calculate_ratio(part, whole):
    ratio = part / whole
    return f"{part} / {whole} ({ratio:.2%})"

# Sidebar for navigation with larger font
st.sidebar.markdown("<h1 style='font-size: 30px;'></h1>", unsafe_allow_html=True)

#Custom CSS to style the radio buttons
st.markdown("""
    <style>
    div.row-widget.stRadio > div{
        flex-direction: column;
        font-size: 35px;  /* Adjust this value to change the font size */
    }
    div.row-widget.stRadio > div > label{
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 5px;
        margin-bottom: 10px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation with custom key
page = st.sidebar.radio("", ["System Performance and Reliability", 
                             "Developer Productivity and Collaboration", 
                             "API Changes and Evolution", 
                             "Security and Governance", 
                             "Schema and Data Management"],
                        key="navigation")

# Dashboard title
st.title("API Platform Dashboard")

# Feedback form
with st.expander("Provide Feedback / Feature Request"):
    feedback = st.text_area("Your feedback:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! We'll review it shortly.")

# Function to display metrics in columns
def display_metrics(metrics_list):
    cols = st.columns(3)
    for i, metric in enumerate(metrics_list):
        with cols[i % 3]:
            st.metric(metric['label'], metric['value'])

# Page content
if page == "System Performance and Reliability":
    st.header("System Performance and Reliability")
    
    uptime = random_metric(99, 100)
    total_requests = random_metric(1000000, 10000000)
    total_data_served = random_metric(100, 1000)
    total_data_ingested = random_metric(50, 500)
    
    metrics = [
        {"label": "Platform Uptime", "value": f"{uptime}%"},
        {"label": "Total Requests Served", "value": f"{total_requests:,}"},
        {"label": "Total Data Served", "value": f"{total_data_served} GB"},
        {"label": "Total Data Ingested", "value": f"{total_data_ingested} GB"},
        {"label": "p50 Response Time", "value": f"{random_metric(50, 100)} ms"},
        {"label": "p95 Response Time", "value": f"{random_metric(100, 200)} ms"},
        {"label": "p99 Response Time", "value": f"{random_metric(200, 500)} ms"},
    ]
    display_metrics(metrics)
    
    st.subheader("Most Common API Errors")
    errors = pd.DataFrame({
        'Error': [f'Error_{i}' for i in range(1, 6)],
        'Frequency': [random_metric(10, 1000) for _ in range(5)]
    })
    fig = px.pie(errors, names='Error', values='Frequency', title='Most Common API Errors')
    st.plotly_chart(fig)
    
    st.subheader("Success Rate per Subgraph")
    subgraphs = pd.DataFrame({
        'Subgraph': [f'Subgraph_{i}' for i in range(1, 6)],
        'Success Rate (%)': [random_metric(95, 100) for _ in range(5)]
    })
    fig = px.bar(subgraphs, x='Subgraph', y='Success Rate (%)', title='Success Rate per Subgraph')
    st.plotly_chart(fig)
    
    st.subheader("Data Source Latency")
    sources = pd.DataFrame({
        'Source': [f'Source_{i}' for i in range(1, 6)],
        'Latency (ms)': [random_metric(10, 500) for _ in range(5)]
    })
    fig = px.bar(sources, x='Source', y='Latency (ms)', title='Data Source Latency')
    st.plotly_chart(fig)

elif page == "Developer Productivity and Collaboration":
    st.header("Developer Productivity and Collaboration")
    
    total_comments = random_metric(500, 2000)
    resolved_comments = random_metric(400, total_comments)
    total_devs = random_metric(50, 200)
    active_devs = random_metric(30, total_devs)
    
    metrics = [
        {"label": "Resolved/Open Comments Ratio", "value": calculate_ratio(resolved_comments, total_comments)},
        {"label": "Developers Engaging on Portal", "value": calculate_ratio(active_devs, total_devs)},
        {"label": "Unique On-Demand Compositions", "value": random_metric(50, 200)},
    ]
    display_metrics(metrics)
    
    st.subheader("Top 5 Metadata Objects with Comments")
    top_objects = pd.DataFrame({
        'Object': [f'Object_{i}' for i in range(1, 6)],
        'Comments': [random_metric(10, 100) for _ in range(5)]
    })
    fig = px.bar(top_objects, x='Object', y='Comments', title='Top 5 Metadata Objects with Comments')
    st.plotly_chart(fig)
    
    st.subheader("Subgraph with Max Comments")
    max_comments_subgraph = f"Subgraph_{random_metric(1, 5)}"
    st.info(f"Subgraph with maximum comments: {max_comments_subgraph}")
    
    st.subheader("Subgraph with Most Builds")
    max_builds_subgraph = f"Subgraph_{random_metric(1, 5)}"
    st.info(f"Subgraph with most builds: {max_builds_subgraph}")
    
    st.subheader("Developers per Subgraph")
    dev_subgraph = pd.DataFrame({
        'Subgraph': [f'Subgraph_{i}' for i in range(1, 6)],
        'Developers': [random_metric(5, 30) for _ in range(5)]
    })
    fig = px.bar(dev_subgraph, x='Subgraph', y='Developers', title='Developers per Subgraph')
    st.plotly_chart(fig)
    
    st.subheader("Top Developer Team")
    top_team = f"Team_{random_metric(1, 5)}"
    st.info(f"Top Developer Team: {top_team}")
    
    st.subheader("Top 3 Developers per Subgraph")
    top_devs = pd.DataFrame({
        'Subgraph': [f'Subgraph_{i}' for _ in range(3) for i in range(1, 6)],
        'Developer': [f'Dev_{random_metric(1, 20)}' for _ in range(15)],
        'Contributions': [random_metric(10, 100) for _ in range(15)]
    })
    fig = px.bar(top_devs, x='Developer', y='Contributions', color='Subgraph', title='Top 3 Developers per Subgraph')
    st.plotly_chart(fig)

elif page == "API Changes and Evolution":
    st.header("API Changes and Evolution")
    
    total_changes = random_metric(50, 200)
    auto_changes = random_metric(10, total_changes)
    
    metrics = [
        {"label": "Automatic Model Changes without API Breaks", "value": calculate_ratio(auto_changes, total_changes)},
        {"label": "Deprecated API Endpoints", "value": random_metric(5, 20)},
        {"label": "New Builds Applied (Last Week)", "value": random_metric(20, 100)},
        {"label": "Build Validations Prompted", "value": random_metric(30, 150)},
    ]
    display_metrics(metrics)
    
    st.subheader("Top 5 Deprecated API Endpoints with Maximum Usage")
    deprecated_endpoints = pd.DataFrame({
        'Endpoint': [f'Endpoint_{i}' for i in range(1, 6)],
        'Usage': [random_metric(100, 1000) for _ in range(5)]
    })
    fig = px.bar(deprecated_endpoints, x='Endpoint', y='Usage', title='Top 5 Deprecated API Endpoints with Maximum Usage')
    st.plotly_chart(fig)

elif page == "Security and Governance":
    st.header("Security and Governance")
    
    total_models = random_metric(500, 1000)
    protected_models = random_metric(300, total_models)
    documented_models = random_metric(200, total_models)
    public_models = random_metric(0, 5)
    
    metrics = [
        {"label": "Models Protected by Authorization Rules", "value": calculate_ratio(protected_models, total_models)},
        {"label": "Well Documented Models", "value": calculate_ratio(documented_models, total_models)},
        {"label": "Number of Roles", "value": random_metric(5, 20)},
    ]
    display_metrics(metrics)
    
    st.subheader("Public Endpoints (No Auth)")
    if public_models > 0:
        st.warning(f"Warning: {public_models} public endpoint(s) available without authentication")
    else:
        st.success("No public endpoints available without authentication")
    
    st.subheader("Role with Maximum Permissions")
    max_perm_role = f"Role_{random_metric(1, 5)}"
    st.info(f"Role with maximum permissions: {max_perm_role}")

else:  # Schema and Data Management
    st.header("Schema and Data Management")
    
    total_entities = random_metric(100, 500)
    total_methods = random_metric(200, 1000)
    total_models = random_metric(500, 1000)
    introspected_models = random_metric(300, total_models)
    models_with_relationships = random_metric(200, total_models)
    
    metrics = [
        {"label": "Entities Delivered", "value": total_entities},
        {"label": "Methods Delivered", "value": total_methods},
        {"label": "Introspected Models", "value": calculate_ratio(introspected_models, total_models)},
        {"label": "Models with Relationships", "value": calculate_ratio(models_with_relationships, total_models)},
        {"label": "Queries Across Subgraphs", "value": random_metric(50, 200)},
    ]
    display_metrics(metrics)
    
    st.subheader("Top 10 Entities and Methods")
    top_10 = pd.DataFrame({
        'Entity/Method': [f'Item_{i}' for i in range(1, 11)],
        'Usage Count': [random_metric(1000, 10000) for _ in range(10)]
    })
    fig = px.bar(top_10, x='Entity/Method', y='Usage Count', title='Top 10 Entities and Methods')
    st.plotly_chart(fig)
    
    st.subheader("Region with Most Requests")
    top_region = f"Region_{random_metric(1, 5)}"
    st.info(f"Region with most requests: {top_region}")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("API Platform Dashboard - v0.0.1")