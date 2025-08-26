⚡ SPATL – Simulation of Power Analysis in Transmission Lines

SPATL (Simulation of Power Analysis in Transmission Lines) is a Python-based project designed to analyze short, medium, and long transmission lines. It provides a complete framework for simulating, calculating, and visualizing the performance of transmission lines using mathematical models and user-friendly tools.


---

📌 Introduction

Transmission lines form the backbone of power systems, and their behavior directly impacts voltage stability, efficiency, and power quality. This project aims to bridge the gap between theoretical models and practical analysis by simulating all three types of lines:

•Short Line

•Medium Line

•Long Line


SPATL allows users to input real-world parameters, run simulations, and obtain numerical as well as graphical outputs, making it an ideal educational and research tool.


---

🚀 Features

Simulation of short, medium, and long transmission lines

Calculation of:

•ABCD Parameters

•Receiving End Voltage

•Voltage Regulation

•Transmission Efficiency


Graphical Outputs – Line charts & bar graphs for better visualization

Extendable to fault analysis and smart grid studies



---

🛠️ Methodology

1. User Input – Line length, resistance (R), inductance (L), capacitance (C), conductance (G), sending end voltage, power factor, etc.


2. Model Selection – Based on line length: Short, Medium, or Long.


3. Calculations – Apply ABCD models (lumped, nominal-π, or distributed).


4. Results – Compute receiving end voltage, efficiency, and regulation.


5. Visualization – Display results in both numerical and graphical formats.




---

📊 Example Inputs

Line Length: 300 km
Sending End Voltage: 220 kV
Power to be Transmitted: 100 MW
Power Factor: 0.9 lagging
R = 0.15 Ω/km
L = 1.2e-3 H/km
C = 0.01e-6 F/km
G = 1e-8 S/km


---

📷 Flowchart


flowchart TD
    A[User Input] --> B[Select Line Model]
    B --> C[Perform Calculations: ABCD, VR, Efficiency]
    C --> D[Numerical Results]
    D --> E[Graphical Visualization]


---

💻 How to Run

1. Clone the repository:

git clone https://github.com/your-username/SPATL.git
cd SPATL


2. Install dependencies:

pip install -r requirements.txt


3. Run the program:

python spatl.py


4. Launch Jupyter Notebook for step-by-step simulation:

jupyter notebook




---

🌍 Applications

•Academic learning for Power System Analysis

•Transmission line design and performance studies

•Research in grid reliability and renewable energy integration

•Can be extended to fault analysis and protection studies



---

📜 Motto

“Simulate, Analyze, and Visualize for Smarter Power Systems.”


---

🧑‍💻 Author

Developed by [Tushar Ranjan Rout]
🔗 Connect with me on LinkedIn



