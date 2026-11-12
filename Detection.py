import numpy as np
import vpython as vp

# Scene setup
scene = vp.canvas(title="", width=1600, height=900, background=vp.color.black)

# --- Dynamic Scene Title (Updates with state) ---
scene_title_label = vp.wtext(text="<h2><b>Simulation:</b> Circularly Polarized Light Analysis</h2>\n")
scene.append_to_caption("<hr>")

# --- State Control Variable ---
current_state = "Circular"  # Options: "Unpolarized", "Circular", "Partial", "Elliptical"

def set_unpolarized(b):
    global current_state
    current_state = "Unpolarized"
    scene_title_label.text = "<h2><b>Simulation:</b> Non-Polarized (Unpolarized) Light Analysis</h2>\n"
    state_label.text = "<b>Current State:</b> Non-Polarized (Unpolarized) Light | Unaffected by QWP | Constant Intensity"

def set_circular(b):
    global current_state
    current_state = "Circular"
    scene_title_label.text = "<h2><b>Simulation:</b> Circularly Polarized Light Analysis</h2>\n"
    state_label.text = "<b>Current State:</b> Circularly Polarized Light | Converted to Linear by QWP | Intensity Drops to 0"

def set_partial(b):
    global current_state
    current_state = "Partial"
    scene_title_label.text = "<h2><b>Simulation:</b> Partially Polarized Light Analysis</h2>\n"
    state_label.text = "<b>Current State:</b> Partially Polarized Light | Fluctuates (Min > 0, Never Zero)"

def set_elliptical(b):
    global current_state
    current_state = "Elliptical"
    scene_title_label.text = "<h2><b>Simulation:</b> Elliptically Polarized Light Analysis</h2>\n"
    state_label.text = "<b>Current State:</b> Elliptically Polarized Light | Converted to Linear by QWP | Intensity Drops to 0"

# --- Dashboard & Buttons ---
scene.append_to_caption("<b>Select Input Light State:</b>\n")
vp.button(text="Unpolarized", bind=set_unpolarized, color=vp.color.orange)
vp.button(text="Circularly Polarized", bind=set_circular, color=vp.color.cyan)
vp.button(text="Partially Polarized", bind=set_partial, color=vp.color.green)
vp.button(text="Elliptically Polarized", bind=set_elliptical, color=vp.color.magenta)

scene.append_to_caption("\n\n")
state_label = vp.wtext(text="<b>Current State:</b> Circularly Polarized Light | Converted to Linear by QWP | Intensity Drops to 0\n")
angle_label = vp.wtext(text="Analyzer Angle (theta): 0.0° | ")
intensity_label = vp.wtext(text="Transmitted Intensity (I/I₀): 1.00\n\n")

# --- Visual Components Setup ---
source = vp.box(pos=vp.vector(-8, 0, 0), size=vp.vector(0.4, 2.0, 2.0), color=vp.color.orange)
vp.label(pos=vp.vector(-8, 1.8, 0), text="Light Source", box=False, height=12)

beam1 = vp.cylinder(pos=vp.vector(-7.8, 0, 0), axis=vp.vector(3.3, 0, 0), radius=0.9, color=vp.color.yellow, opacity=0.15)

qwp = vp.box(pos=vp.vector(-4.3, 0, 0), size=vp.vector(0.15, 2.8, 2.8), color=vp.color.blue, opacity=0.4)
vp.label(pos=vp.vector(-4.3, 1.8, 0), text="Quarter-Wave Plate (λ/4)", box=False, height=12)

beam2 = vp.cylinder(pos=vp.vector(-4.15, 0, 0), axis=vp.vector(4.8, 0, 0), radius=0.8, color=vp.color.cyan, opacity=0.15)

analyzer_center = vp.vector(0.8, 0, 0)
analyzer_box = vp.box(pos=analyzer_center, size=vp.vector(0.3, 2.6, 2.6), color=vp.color.magenta, opacity=0.4)
analyzer_axis_line = vp.arrow(pos=analyzer_center - vp.vector(0, 1.1, 0), axis=vp.vector(0, 2.2, 0), color=vp.color.white, shaftwidth=0.08)

vp.label(pos=vp.vector(0.8, 1.8, 0), text="Nicol Prism (Analyzer)", box=False, height=12)
vp.label(pos=vp.vector(0.8, -1.6, 0), text="Transmission Axis", box=False, height=10, color=vp.color.white)

beam3 = vp.cylinder(pos=vp.vector(0.95, 0, 0), axis=vp.vector(5.0, 0, 0), radius=0.7, color=vp.color.magenta, opacity=0.4)

screen = vp.box(pos=vp.vector(6.2, 0, 0), size=vp.vector(0.2, 3.0, 3.0), color=vp.color.gray(0.3))
vp.label(pos=vp.vector(6.2, 1.8, 0), text="Detector Screen", box=False, height=12)

# --- Wave Particles Setup ---
num_points = 55
x_vals = np.linspace(-7.2, 6.0, num_points)

y_spheres = []
z_spheres = []

for x in x_vals:
    sy = vp.sphere(pos=vp.vector(x, 0, 0), radius=0.07, color=vp.color.green)
    y_spheres.append((x, sy))
    
    sz = vp.sphere(pos=vp.vector(x, 0, 0), radius=0.07, color=vp.color.yellow)
    z_spheres.append((x, sz))

# --- Simulation Loop Parameters ---
theta = 0.0
omega = 0.015
time = 0.0
prev_theta = 0.0

while True:
    vp.rate(60)
    time += 0.12
    
    theta += omega
    theta_deg = np.degrees(theta) % 360
    
    d_theta = theta - prev_theta
    prev_theta = theta
    
    analyzer_box.rotate(angle=d_theta, axis=vp.vector(1,0,0), origin=analyzer_center)
    analyzer_axis_line.rotate(angle=d_theta, axis=vp.vector(1,0,0), origin=analyzer_center)
    
    # Accurate Physics Intensity Calculations:
    if current_state == "Unpolarized":
        intensity = 0.5  # Constant transmission
    elif current_state == "Circular":
        intensity = np.cos(theta)**2  # Converted to linear by QWP -> drops to 0 twice per rotation
    elif current_state == "Elliptical":
        intensity = np.cos(theta)**2  # Converted to linear by QWP -> drops to 0 twice per rotation
    elif current_state == "Partial":
        intensity = 0.55 + 0.45 * np.cos(2 * theta)  # Fluctuates, min > 0 (never zero)
        
    amplitude_out = np.sqrt(intensity)
    beam3.opacity = max(0.05, 0.4 * intensity)
    
    for i, x in enumerate(x_vals):
        phase = time - x * 1.5
        
        if x < -4.3:
            # Region 1: Before QWP (Source characteristics)
            if current_state == "Unpolarized":
                y_spheres[i][1].pos = vp.vector(x, 0.6 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.6 * np.cos(phase * 1.3))
                z_spheres[i][1].visible = True
            elif current_state == "Circular":
                y_spheres[i][1].pos = vp.vector(x, 0.6 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.6 * np.cos(phase))
                z_spheres[i][1].visible = True
            elif current_state == "Partial":
                y_spheres[i][1].pos = vp.vector(x, 0.7 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.3 * np.cos(phase * 1.1))
                z_spheres[i][1].visible = True
            elif current_state == "Elliptical":
                y_spheres[i][1].pos = vp.vector(x, 0.7 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.3 * np.cos(phase + np.pi/4))
                z_spheres[i][1].visible = True
                
        elif -4.3 <= x <= 0.8:
            # Region 2: Between QWP and Nicol Prism
            if current_state == "Unpolarized":
                # Unpolarized light remains completely unaffected by QWP
                y_spheres[i][1].pos = vp.vector(x, 0.6 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.6 * np.cos(phase * 1.3))
                z_spheres[i][1].visible = True
            else:
                # Circular, Elliptical, and Partial polarized components converted to linear by QWP
                y_spheres[i][1].pos = vp.vector(x, 0.6 * np.sin(phase), 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0)
                z_spheres[i][1].visible = False
            
        else:
            # Region 3: After Nicol Prism Analyzer
            if current_state == "Unpolarized":
                y_spheres[i][1].pos = vp.vector(x, 0.6 * np.sin(phase) * amplitude_out, 0)
                z_spheres[i][1].pos = vp.vector(x, 0, 0.6 * np.cos(phase * 1.3) * amplitude_out)
                z_spheres[i][1].visible = True
            else:
                base_y = 0.6 * np.sin(phase) * amplitude_out
                y_val = base_y * np.cos(theta)
                z_val = base_y * np.sin(theta)
                
                y_spheres[i][1].pos = vp.vector(x, y_val, z_val)
                z_spheres[i][1].pos = vp.vector(x, 0, 0)
                z_spheres[i][1].visible = False

    angle_label.text = f"Analyzer Angle (theta): {theta_deg:.1f}° | "
    intensity_label.text = f"Transmitted Intensity (I/I₀): {intensity:.3f}\n\n"