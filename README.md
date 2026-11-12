# 🌟 Advanced Light Polarization & Nicol Prism Analysis Simulation

An interactive 3D physics simulation built using **Python** and **VPython** that models complex polarization states, Quarter-Wave Plate ($\lambda/4$) transformations, and analyzer interactions using a **Nicol Prism**.

This project provides a comprehensive visual demonstration of how different states of light behave when passing through optical elements and a continuously rotating analyzer.

---

## 🔍 How the Simulation Differentiates Between Light States

In classical optics, distinguishing between unpolarized, circularly, elliptically, and partially polarized light can be tricky because some states (like unpolarized vs. circular) both show constant intensity when viewed through a simple analyzer alone. This simulation makes the distinction crystal clear by demonstrating the combined effect of a **Quarter-Wave Plate ($\lambda/4$)** and a **rotating Nicol Prism**:

1. **Unpolarized Light:**
   * **Behavior:** Completely unaffected by the quarter-wave plate (retaining random multi-planar oscillations). When it passes through the rotating Nicol prism, the transmitted intensity remains **strictly constant**, as all orientations are equally represented.
2. **Circularly Polarized Light:**
   * **Behavior:** The $\lambda/4$ plate successfully converts circular polarization into clean **plane-polarized (linear)** light. As the Nicol prism rotates, the intensity **drops to zero twice per rotation** ($\cos^2\theta$), visually proving its coherent single-plane nature after phase retardation.
3. **Elliptically Polarized Light:**
   * **Behavior:** Similar to circular light, the $\lambda/4$ plate transforms the elliptical state into linear polarization. When analyzed by the rotating Nicol prism, the intensity also **extinguishes to zero twice per rotation**, distinguishing it clearly from partial polarization.
4. **Partially Polarized Light:**
   * **Behavior:** Represents a statistical mixture of unpolarized and polarized light. When analyzed, its intensity **fluctuates between a maximum and a non-zero minimum ($I_{\min} > 0$)**. It **never drops to zero** because of the persistent unpolarized background fraction, giving you a visual telemetry readout of fluctuating contrast rather than full extinction.

---

## ✨ Features

* **Four Interactive Light States:** Easily toggle between different input states using the on-screen dashboard buttons.
* **Rotating Nicol Prism Analyzer:** A 3D crystal block featuring a visible **Transmission Axis** that continuously rotates at angular velocity $\omega$.
* **Live Telemetry & Dynamic Title:** Real-time on-screen tracking of the current input mode, analyzer angle ($\theta$), and normalized transmitted intensity ($I / I_0$).

---

## 🛠️ Prerequisites & Dependencies

To run this simulation, ensure you have Python installed along with the required libraries:

```bash
pip install vpython numpy
```

---

## 🚀 How to Run

1. Save the simulation script as `Detection.py`.
2. Run the script from your terminal or IDE:
   ```bash
   python Detection.py
   ```
3. A browser window will automatically launch displaying the interactive 3D simulation. Use the top buttons to switch between light states and observe the real-time wave behaviors!