from fpdf import FPDF
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_pdf_report(flight_data, analysis, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(0, 10, "FPV Flight Analysis Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Flight ID: {flight_data['id']}", ln=True)
    pdf.cell(0, 10, f"Duration: {flight_data['duration']:.1f}s", ln=True)

    # График
    plt.figure(figsize=(10, 5))
    times = [p["time"] / 1e6 for p in flight_data["telemetry"][:200]]
    volts = [p["voltage"] for p in flight_data["telemetry"][:200]]
    plt.plot(times, volts)
    plt.title("Battery Voltage Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close()

    # Временный файл
    temp_img = "/tmp/voltage.png"
    with open(temp_img, "wb") as f:
        f.write(base64.b64decode(img_data))
    
    pdf.image(temp_img, x=10, y=60, w=180)
    pdf.set_y(150)
    pdf.cell(0, 10, f"AI Analysis: {analysis['advice']}", ln=True)

    pdf.output(output_path)