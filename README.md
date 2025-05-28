# 📦 Warehouse Utilization Forecasting
> **🔒 Disclaimer**
> This is just a sample of my work does not reflect the full functionality or scale of the internal version deployed at Loeb Electric.

This project forecasts **daily warehouse location utilization** for the next 30 days by analyzing committed inbound/outbound orders, historical inventory movements, and order behavior patterns such as lead times and the likelihood of new orders. The output includes the predicted number of **full storage locations**, segmented by location type:

- **Small** (Carton)  
- **Medium** (2X Carton)  
- **Large** (Pallet)  
- **Oversized** (Yard)

This enables proactive planning of warehouse space, slotting, and labor allocation.

---

## 🧠 What It Does

- Simulates inventory flow by product-location type across time.
- Predicts the number of **full locations** per category for the next 30 days.
- Implements warehouse slotting and replenishment rules:
  - Inbound products go to the **primary location** first, then nearest available.
  - Outbound picks are fulfilled from **primary locations** and replenished from overflow.
- Integrates directly with **Power BI Dataflows**:
  - **Reads** historical and forecast inputs.
  - **Writes** daily utilization forecasts back to Power BI for reporting.

---

## 🛠️ How It Works

1. **Historical Analysis**: Processes 5 years of inventory and order history per product.
2. **Forecasting**: Estimates daily location occupancy per category based on projected order activity and restocking logic.
3. **Data Integration**: Exports forecast data into a **Power BI Dataflow**, enabling dynamic reporting alongside other warehouse KPIs (e.g., product turnover, slot utilization, travel minimization opportunities).

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


