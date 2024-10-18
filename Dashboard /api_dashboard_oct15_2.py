import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# Set page config
st.set_page_config(page_title="API Platform Dashboard", layout="wide")

# Function to generate random data
def random_metric(min_val, max_val):
    return random.randint(min_val, max_val)

# Dashboard title
st.title("API Platform Dashboard")

# Sidebar navigation
st.sidebar.title("Navigation")
categories = [
    "Security and Governance",
    "System Performance and Reliability",
    "Developer Productivity",
    "API Usage Trends"
]

for category in categories:
    if st.sidebar.button(category):
        st.query_params["section"] = category.lower().replace(" ", "_")

# Get the current section from URL parameters
current_section = st.query_params.get("section", "")

# Security and Governance
st.header("1. Security and Governance", anchor="security_and_governance")
if current_section == "security_and_governance":
    st.query_params.clear()

# Public endpoint alert
st.subheader("1.1 Public endpoint alert")
public_endpoints = random_metric(0, 3)
if public_endpoints > 0:
    st.warning(f"Warning: {public_endpoints} model(s) exposed without auth!")
    st.markdown("""
    **How to fix this security issue:**
    1. Identify the exposed models in your API configuration.
    2. Implement proper authentication mechanisms:
       - Use OAuth 2.0 or JWT for token-based authentication.
       - Set up API keys for simpler use cases.
    3. Update your API gateway or server configuration to require authentication for these endpoints.
    4. Test the endpoints to ensure they now require proper authentication.
    5. Monitor access logs to verify that unauthorized access attempts are blocked.
    6. Regularly audit your API endpoints to prevent future exposure.
    """)
else:
    st.success("No models exposed without auth.")

# System Performance and Reliability
st.header("2. System Performance and Reliability", anchor="system_performance_and_reliability")
if current_section == "system_performance_and_reliability":
    st.query_params.clear()

# Performance per team
st.subheader("2.1 Performance per team (last 30 days)")
teams = ["Team A", "Team B", "Team C"]
performance_data = []
for team in teams:
    performance_data.append({
        "Team": team,
        "Min Latency": random_metric(10, 50),
        "Max Latency": random_metric(100, 500),
        "Median Latency": random_metric(50, 100)
    })
performance_df = pd.DataFrame(performance_data)
fig_performance = px.bar(performance_df, x="Team", y=["Min Latency", "Median Latency", "Max Latency"], 
                         title="Team Performance (Latency in ms)")
st.plotly_chart(fig_performance)

# Reliability per team
st.subheader("2.2 Reliability per team (last 30 days)")
reliability_data = []
for team in teams:
    reliability_data.append({
        "Team": team,
        "Error/Success Ratio": random.uniform(0, 0.1)
    })
reliability_df = pd.DataFrame(reliability_data)
fig_reliability = px.bar(reliability_df, x="Team", y="Error/Success Ratio", 
                         title="Team Reliability (Error/Success Ratio)")
st.plotly_chart(fig_reliability)

# Team Reliability Rating
st.subheader("2.3 Team Reliability Rating")
for team in teams:
    rating = random.choice(["Bronze", "Silver", "Gold"])
    st.text(f"{team}: {rating}")

# Developer Productivity
st.header("3. Developer Productivity", anchor="developer_productivity")
if current_section == "developer_productivity":
    st.query_params.clear()

# Number of developers per team
st.subheader("3.1 Number of developers per team")
dev_count = {team: random_metric(5, 20) for team in teams}
st.bar_chart(dev_count)

# Team with most builds
st.subheader("3.2 Team with most builds (last 30 days)")
most_builds_team = random.choice(teams)
most_builds_count = random_metric(100, 500)
st.info(f"Team with most builds: {most_builds_team} ({most_builds_count} builds)")

# Team pushing most changes to production
st.subheader("3.3 Team pushing most changes to production (last 30 days)")
most_changes_team = random.choice(teams)
most_changes_count = random_metric(50, 200)
st.info(f"Team pushing most changes: {most_changes_team} ({most_changes_count} changes)")

# Top 3 developers per team
st.subheader("3.4 Top 3 developers per team")
top_devs_data = []
for team in teams:
    for rank in range(1, 4):
        top_devs_data.append({
            "Team": team,
            "Rank": rank,
            "Developer": f"Dev_{random_metric(1, 100)}",
            "Commits": random_metric(50, 200)
        })
top_devs_df = pd.DataFrame(top_devs_data)
fig_top_devs = px.bar(top_devs_df, x="Developer", y="Commits", color="Team", facet_col="Team",
                      labels={"Developer": "Developer", "Commits": "Number of Commits"},
                      title="Top 3 Developers per Team")
st.plotly_chart(fig_top_devs)

# API Usage Trends
st.header("4. API Usage Trends", anchor="api_usage_trends")
if current_section == "api_usage_trends":
    st.query_params.clear()

# Subgraph with most traffic
st.subheader("4.1 Subgraph with most traffic (last 30 days)")
subgraphs = ["Subgraph A", "Subgraph B", "Subgraph C"]
most_traffic_subgraph = random.choice(subgraphs)
most_traffic_requests = random_metric(1000000, 10000000)
st.info(f"Subgraph with most traffic: {most_traffic_subgraph} ({most_traffic_requests:,} requests)")

# Top 3 Models per Subgraph
st.subheader("4.2 Top 3 Models per Subgraph")
top_models_data = []
for subgraph in subgraphs:
    for rank in range(1, 4):
        top_models_data.append({
            "Subgraph": subgraph,
            "Rank": rank,
            "Model": f"Model_{random_metric(1, 100)}",
            "Requests": random_metric(10000, 1000000)
        })
top_models_df = pd.DataFrame(top_models_data)
fig_top_models = px.bar(top_models_df, x="Model", y="Requests", color="Subgraph", facet_col="Subgraph",
                        labels={"Model": "Model", "Requests": "Number of Requests"},
                        title="Top 3 Models per Subgraph")
st.plotly_chart(fig_top_models)

# Top 3 Fields per Subgraph
st.subheader("4.3 Top 3 Fields per Subgraph")
top_fields_data = []
for subgraph in subgraphs:
    for rank in range(1, 4):
        top_fields_data.append({
            "Subgraph": subgraph,
            "Rank": rank,
            "Field": f"Field_{random_metric(1, 100)}",
            "Model": f"Model_{random_metric(1, 100)}",
            "Requests": random_metric(5000, 500000)
        })
top_fields_df = pd.DataFrame(top_fields_data)
fig_top_fields = px.bar(top_fields_df, x="Field", y="Requests", color="Subgraph", facet_col="Subgraph",
                        labels={"Field": "Field", "Requests": "Number of Requests"},
                        title="Top 3 Fields per Subgraph",
                        hover_data=["Model"])
st.plotly_chart(fig_top_fields)

# Unused API percentage
st.subheader("4.4 Unused API percentage")
unused_api_data = []
for subgraph in subgraphs:
    unused_api_data.append({
        "Subgraph": subgraph,
        "Unused Models (%)": random.uniform(0, 30)
    })
unused_api_df = pd.DataFrame(unused_api_data)
fig_unused_api = px.bar(unused_api_df, x="Subgraph", y="Unused Models (%)", 
                        title="Percentage of Unused Models per Subgraph")
st.plotly_chart(fig_unused_api)

# Deprecated features
st.subheader("4.5 Deprecated features")
for subgraph in subgraphs:
    deprecated_objects = random_metric(0, 10)
    st.text(f"{subgraph}: {deprecated_objects} deprecated object(s)")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("API Platform Dashboard - v0.0.5")
