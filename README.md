# 📊 Shoals Marine Laboratory (SML) Energy Dashboard

This project demonstrates the development and deployment of an interactive data dashboard for Shoals Marine Laboratory (SML), based on historical data. The dashboard was created as part of a Ph.D. research project at the University of New Hampshire and is intended to visualize renewable energy generation, battery storage behavior, and demand dynamics within an off-grid microgrid environment.

📍 **Live demo**: [Deployed on Render](https://sml-vizro-dashboard.onrender.com)  
🕒 *Note*: Due to Render’s free-tier limitations, the dashboard may take up to **one minute** to load when first accessed after a period of inactivity.

---

## 📚 Research Context

The dashboard is developed using data and methods presented in peer-reviewed publications associated with the doctoral research conducted at the University of New Hampshire. The full details of data preparation, modeling framework, and analysis are documented in the published literature. A complete list of scholarly contributions can be found via the author's Google Scholar profile:

🔗 **Author Profile**: [Roozbeh Ghasemi – Google Scholar](https://scholar.google.com/citations?user=4X92o5gAAAAJ&hl=en)

---

## 🗃️ Data Source

All data visualized within this dashboard are sourced from the publicly available archives of the Shoals Marine Laboratory (SML):

🌐 [https://sustainablesml.org](https://sustainablesml.org)

The data include:
- Photovoltaic (PV) generation
- Wind generation
- Diesel generator output
- Battery state of charge (SOC)
- Energy demand and water use metrics

---

## 🛠️ Technologies Used

- **[Vizro](https://github.com/plotly/vizro)** (built on Plotly Dash)
- **Python**, **Pandas**, **Plotly Express**
- **Deployed via [Render.com](https://render.com)** (free tier hosting)

---

## 📦 Installation

To run this dashboard locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sml-dashboard.git
   cd sml-dashboard
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python SML_Dashboard.py
   ```

The dashboard will be served at `http://127.0.0.1:8050/` by default.

---

## 📌 Acknowledgments

- This project builds upon the research supported by the University of New Hampshire and Shoals Marine Laboratory.
- Data used in this dashboard were collected and published under the SML sustainability initiative.
- Deployment is made possible through [Render.com](https://render.com), utilizing their free-tier services.

---

## 📝 License

This project is shared for educational and research purposes. For data usage, please refer to the source repository at [https://sustainablesml.org](https://sustainablesml.org) and citation requirements in associated publications.
