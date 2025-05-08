# Toyota Virtual Dealer CLI 🚗

A terminal-based Python application that simulates a Toyota car dealership experience. Users can select, customize, and purchase vehicles through a structured, interactive menu system.

## 📌 Features

- **State-driven flow** using Enums (`Select`, `Customize`, `Quantity`, `Calculate`, `Update`, `Receipt`)
- **Class-based models** for customers and vehicles
- **Inventory system** with validation and quantity updates
- **Customization options**: color, transmission type, seat material, and wheel color
- **Real-time cost calculation** and payment validation
- **Fully interactive CLI** experience in Spanish
- **No external libraries required**

## 🧠 How It Works

The program starts in the `Select` state, allowing a customer to choose a vehicle model. From there, it guides the user through:
1. **Customization** – choose vehicle options
2. **Quantity** – how many vehicles to buy
3. **Cost Calculation** – total pricing and user payment
4. **Inventory Update** – subtract purchased units
5. **Receipt and Loop** – return to main menu for a new transaction

All logic is handled with enums and conditionals, making it a great example of **state machines and control flow in Python**.

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Running the Program

Clone the repository and run the script:

```bash
python toyota_virtual_dealer.py
