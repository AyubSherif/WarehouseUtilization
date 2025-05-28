# 📦 Warehouse Location Utilization Forecasting (LSTM-Based)

> **🔒 Disclaimer**
> This is just a sample of my work does not reflect the full functionality or scale of the internal version deployed at Loeb Electric.

This project implements a **sequence-based LSTM model** to forecast the **daily warehouse location utilization** over the next 30 days. Specifically, it predicts the number of **full locations per product and location type** (e.g., small, medium, large, oversized) using historical inventory movements and order activity.

---

## 🧠 What It Does

- Models inventory dynamics per product-location category pair.
- Predicts 30-day outlook for **location fullness**, enabling forward planning.
- Encodes the slotting and replenishment logic used in warehouse operations:
  - Inbound material is slotted into primary locations first, then closest empty.
  - Picking is done from primary locations first, and replenished from overflow.
- Feeds results into a Power BI dataflow.

---

## 🛠️ How It Works

1. **LSTM sequence model** trained on 3 years of history per product.
2. Forecasts **next 30 days** of full locations per category.
3. Results are exported to a **Power BI Dataflow** and joined with other warehouse KPIs.

---

## 📈 Power BI Integration

The model output is loaded into a **Power BI Dataflow**, where it's enriched and visualized within a comprehensive **Warehouse Utiliatation Report**. (Although, it has turned into warehouse Everything report). This report includes:

- **Utilization Forecast**
  - Percentage of location types are full/empty
  - 30 Days forecast

- **Location Analysis**:  
  - Which locations are most touched (high-frequency pick/putaway)
  - Forecast of locations opening up or reaching full capacity
  - Suggests **replenishment schedules**
  - Recommends **reslotting** to minimize picker travel distance

- **Product Analysis**:
  - SKU velocity

- **Operational Insights**:
  - Forecast-driven labor planning
  - Heatmaps of congestion zones

---
## 🖼️ Power BI Report

![alt text](https://github.com/AyubSherif/WarehouseUtilization/blob/main/img/WarehouseUtilizationReport.png)

![alt text](https://github.com/AyubSherif/WarehouseUtilization/blob/main/img/AisleView.png)

---

## 🧪 Model Architecture

- **Model**: LSTM (PyTorch)
- **Input**: 3 years sequences of `[on_hand_qty, incoming_qty, outgoing_qty]`
- **Output**: 30-day sequence of `location_full` count  

---

## 🧭 Future Work

- Due to some Power BI limitations, I am currently working on another interactive too powered by plotly library (Python package)
- See [WarehouseManagementAppDemo](https://github.com/AyubSherif/WarehouseManagementAppDemo/) repository

---

## 📌 Requirements

- Python 3.8+
- PyTorch
- Pandas, NumPy, Matplotlib

Install with:

```bash
pip install torch pandas numpy matplotlib


