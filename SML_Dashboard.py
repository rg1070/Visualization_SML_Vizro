import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
import pandas as pd
import os

# Load and preprocess data
Energy_2022 = pd.read_csv("Energy_2022.csv")
Energy_2022["Date"] = pd.to_datetime(Energy_2022["Date"], format="%m/%d/%y %H:%M")
Energy_2022["timestamp"] = Energy_2022["Date"].astype("int64") // 10**6  # milliseconds

Water_2022 = pd.read_csv("Water_2022.csv")
Input_2022 = pd.read_csv("Input_2022.csv")

# Summary of generation and demand
sums = {
    "PV": round(Energy_2022["PV (kW) [ECB+Dorms]"].sum() / 60),
    "Wind": round(Energy_2022["Wind (kW)"].sum() / 60),
    "Diesel": round(Energy_2022["Diesel (kW)"].sum() / 60),
    "Energy Demand": round(Input_2022["Demand (W)"].sum() / 60000),
}
df_summary = pd.DataFrame(list(sums.items()), columns=["Source", "Energy (kWh)"])

df_pie = df_summary[df_summary["Source"].isin(["PV", "Wind", "Diesel"])]


## Figures
fig1 = px.line(Energy_2022, x="Date", y="PV (kW) [ECB+Dorms]",title="Renewable Energy Generation Trend - 6/1/2022 0:00 to 8/31/2022 23:59", color_discrete_sequence=["green"],
    labels={
        "PV (kW) [ECB+Dorms]": "PV Generation (kW)",
        "Wind (kW)": "Wind Generation (kW)",
        "Diesel (kW)": "Diesel Generation (kW)"
    })

fig2 = px.line(Energy_2022, x="Date", y="SOC (%)",title="Battery State of Charge Trend - 6/1/2022 0:00 to 8/31/2022 23:59", color_discrete_sequence=["blue"],
    labels={
        "SOC (%)": "Battery State of Charge (%)"
    })


color_order = ["PV", "Wind", "Diesel"]
color_map = {
    "PV": "green",
    "Wind": "blue",
    "Diesel": "orange"
}

fig3 = px.bar(
    df_summary,
    x="Source",
    y="Energy (kWh)",
    title="Total 92 days Energy Generation and Demand (kWh)",
    color="Source",
    color_discrete_map=color_map,
    text="Energy (kWh)"
)

fig3.update_traces(
    texttemplate='%{text}',
    cliponaxis=False,
    showlegend=False  # 👈 Force hide on each trace
)


# Optional: adjust layout so text isn't clipped
fig3.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    margin=dict(t=50, b=50)
)




fig4 = px.pie(
    df_pie,
    values="Energy (kWh)",
    names="Source",
    title="Share of Energy Generation by Source",
    hole=0.4,
    color_discrete_map=color_map,
    category_orders={"Source": color_order}
)

fig4.update_traces(textposition="inside", textinfo="percent+label")





# Build page
page1 = vm.Page(
    title="SML Energy Generation Historical Data",
    components=[
        vm.Graph(id="EnergyGraph", figure=fig1),
        vm.Graph(id="SOC", figure=fig2)
    ],
    controls=[
        # Dropdown to select variable
        vm.Parameter(
            selector=vm.Dropdown(
                options=["PV (kW) [ECB+Dorms]", "Wind (kW)","Diesel (kW)"],
                multi=False,
                value="PV (kW) [ECB+Dorms]",
                title="Select Energy Generation Source"
            ),
            targets=["EnergyGraph.y"]
        ),
        # RangeSlider for timestamp (x-axis)
        vm.Parameter(
            selector=vm.RangeSlider(
                min=Energy_2022["timestamp"].min(),
                max=Energy_2022["timestamp"].max(),
                value=[Energy_2022["timestamp"].min(), Energy_2022["timestamp"].max()],
                step = 60 * 60 * 1000,  # 1 minute = 60 seconds = 60,000 milliseconds
                title="Date Range"
            ),
            targets=["EnergyGraph.range_x","SOC.range_x"]
        )
    ]
)

page2 = vm.Page(
    title="Energy Summary",
    components=[
        vm.Graph(id="EnergyPie", figure=fig4),
        vm.Graph(id="EnergySummary", figure=fig3)
        
    ]
)
dashboard = vm.Dashboard(pages=[page1,page2])

port = int(os.environ.get("PORT", 10000))
Vizro().build(dashboard).run(host="0.0.0.0", port=port)
